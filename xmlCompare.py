import xml.etree.ElementTree as ET
import sys
import time
import logging
from typing import Generator, Tuple

"""
Ce programme fonctionne avec 2 arguments supplémentaires (donc 3 au total), et fonctionne comme suit :
Argument 1 : nom du programme. Exemple : xml-Parser.py
Argument 2 : nom du fichier le plus récent. Exemple ; fichier_recent.xml
Argument 3 : nom du fichier ancien. Exemple : fichier_ancien.xml
Un exemple d'utilisation serait le suivant :
python Argument 1 Argument 2 Argument 3
Soit :
python xml-Parser.py fichier_recent.xml fichier_ancien.xml
Il faut inclure les 3 arguments, dans le cas contraire le programme ne fonctionnera pas.
"""

def compareElement(element_new, element_old, attrib) -> Tuple[str, str, str, bool, bool]:
    result = '?'
    texte = "--------"
    if element_new is not None and element_old is not None:
        # on a obtenu 1 element dans new et dans old
        attribValue_new = element_new.get(attrib)
        attribValue_old = element_old.get(attrib)
        # print(f"{attribValue_new} <--> {attribValue_old}")
        if attribValue_new == attribValue_old:
            result = '='
            texte = f""
            compareLevel(element_new, element_old, path=attribValue_new, attrib='nom')
            attribValue = attribValue_new
            get_new = True
            get_old = True
        elif attribValue_new > attribValue_old:
            result = 's'
            texte = "--> supprimé"
            attribValue = attribValue_old
            get_new = False
            get_old = True
        elif attribValue_new < attribValue_old:
            result = 'a'
            texte = "--> ajouté"
            attribValue = attribValue_new
            get_new = True
            get_old = False
    elif element_new is not None:
        result = 'a'
        attribValue_new = element_new.get(attrib)
        texte = "--> ajouté"
        attribValue = attribValue_new
        get_new = True
        get_old = False
    elif element_old is not None:
        result = 's'
        attribValue_old = element_old.get(attrib)
        texte = "--> supprimé"
        attribValue = attribValue_old
        get_new = False
        get_old = True
    else:
        result = '?'
        return '?', None, None, None, None
    logging.info(f"compareElement() : result={result}, texte={texte}, attribValue={attribValue}, get_new={get_new}, get_old={get_old}")
    return result, texte, attribValue, get_new, get_old

def iterOneLevelXml(tree: ET.Element) -> Generator[ET.Element, None, None]:
    # doc = ET.parse(file)
    # root = doc.getroot()
    # objectmodel = root[0][0]

    for element in tree:
        # print(f"iterOneLevelXml() tag={element.tag} classname={element.get('class-name')} nom={element.get('nom')}")
        yield element

def compareLevel(tree_new, tree_old, path, attrib):
    generator_new = iterOneLevelXml(tree_new)
    generator_old = iterOneLevelXml(tree_old)
    get_new = True
    get_old = True
    while True:
        if get_new:
            try:
                element_new = next(generator_new)
                # print(f"NEW --> tag={element_new.tag} class-name={element_new.get(attrib)}")
            except StopIteration:
                # print("FIN_new")
                element_new = None
        if get_old:
            try:
                element_old = next(generator_old)
                # print(f"OLD --> tag={element_old.tag} class-name={element_old.get(attrib)}")
            except StopIteration:
                # print("FIN_old")
                element_old = None
        result, texte, attribValue, get_new, get_old = compareElement(element_new, element_old, attrib)
        logging.info(f"result={result}, texte={texte}, attribValue={attribValue}, get_new={get_new}, get_old={get_old}")
        if not attribValue and not texte:
            break
        if element_new is not None:
            if element_old is not None:
                logging.info(f"{result}    {attrib} = {attribValue} {element_new.get(attrib)} <-> {element_old.get(attrib)}")
            else:
                logging.info(f"{result}    {attrib} = {attribValue} {element_new.get(attrib)} <-> None")
        else:
            if element_old is not None:
                logging.info(f"{result}    {attrib} = {attribValue} None <-> {element_old.get(attrib)}")
            else:
                logging.info(f"{result}    {attrib} = {attribValue} None <-> None")
        # 
        if attrib == 'class-name':
            print("")
            print(f"===== {attrib} = {attribValue} =====")
        if result == 'a':
            logging.info(f"AJOUT    {attrib} {attribValue} {element_new.get(attrib)}")
            print(f"{path} / {attribValue} {texte}")
        elif result == 's':
            logging.info(f"SUPPR    {attrib}  {attribValue} {element_old.get(attrib)}")
            print(f"{path} / {attribValue} {texte}")
        elif result == '=':
            logging.info(f"EGAL    {attrib}  {attribValue}")
            # print(texte)
        elif result == '?':
            logging.warning(f"????    {attrib}  {attribValue} {element_new.get(attrib)} {element_old.get(attrib)}")
            # print(texte)
        else:
            print(f"???? {result}   {attrib}  {attribValue} {element_new.get(attrib)} {element_old.get(attrib)}")
        
    # print("TERMINE")

def parcours(tree, texte):
    # print(f"DEB parcours() : texte={texte} len={len(tree)}_______________")
    generator = iterOneLevelXml(tree)
    cpt = 0
    while True:
        try:
            cpt += 1
            element = next(generator)
            
        except StopIteration:
            # print("FIN_new")
            element = None
            break
        # print(f"cpt={cpt} / {len(tree)} -> {element.get('nom')}")
        if element != None:
            if element.tag == "obj":
                print(f"CLASS --> {element.get('class-name')} nom={element.get('nom')} {len(element)} éléments")
            elif element.tag == "fv":
                print(f"ELEMENT --> {element.get('nom')} {len(element)} éléments")
            elif element.tag == "a":
                print(f"A --> {element.get('nom')} {len(element)} éléments")
            else:
                print(f"??? [{element.tag}] --> nom={element.get('nom')} {len(element)} éléments")
            # print(f"cpt={cpt} / {len(tree)} -> {element.get('nom')}")
            if len(element) > 0:
                for item in element:
                    # print(f"boucle for() -> tag={item.tag} nom={item.get('nom')}")
                    pass
                # print(f"===> parcours")
                parcours(element, texte=f"parcours() --> tag={element.tag} class-name={element.get('class-name')} nbElements={len(element)}")
                # print(f"_______________ fin parcours() _______________")
        else:
            print("element=None -> ???")
    # print(f"FIN parcours() : texte={texte} _______________")

nb_par = len(sys.argv)
if nb_par not in [2, 3]:
    print("Veuillez inclure les arguments du programme en vous fiant à sa documentation")
    sys.exit()

start_time = time.time()

fichier_new = sys.argv[1]
arbre_new = ET.parse(fichier_new)
root_new = arbre_new.getroot()
gom_new = root_new[0][0]

if nb_par == 3:
    diff = True
    fichier_old = sys.argv[2]
    arbre_old = ET.parse(fichier_old)
    root_old = arbre_old.getroot()
    gom_old = root_old[0][0]
    
    diff = compareLevel(tree_new=gom_new, tree_old=gom_old, path='', attrib='class-name')
else:
    parcours(tree=gom_new, texte="gom_new")
    diff = True

end_time = time.time()
execution_time = end_time - start_time
print(execution_time)

if diff:
    exit(1)
elif not diff:
    exit(0)
