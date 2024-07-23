import xml.etree.ElementTree as ET
from lxml import etree
import sys
import time
import logging
from typing import Generator, Tuple
from enum import Enum
from infosClasses import numeros_de_classe, classes_a_exclure
from pprint import pprint

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

listeClassesExclues = []
listeClassesAjoutees = []
listeClassesSupprimees = []
modificationsClasse = []
modificationsAjoutsClasse = []
modificationsSuppressionsClasse = []
listeModifications = {}
verbose = False

class CompareResult(Enum):
    EGAL = 0
    ADD = 1
    SUPPR = 2
    INC = 3

def verbosePrint(texte: str):
    global verbose
    if verbose:
        print(texte)

def getAttribFromTag(tag: str) -> str:
    if tag == 'obj':
        attrib = 'class-name'
    elif tag == 'fv':
        attrib = 'nom'
    elif tag == 'a':
        attrib = 'i'
    return attrib

def compareElement(element_new: ET.Element, element_old: ET.Element, attrib: str) -> Tuple[str, str, str, bool, bool]:
    result = '?'
    texte = "--------"
    if element_new is not None and element_old is not None:
        # on a obtenu 1 element dans new et dans old
        tagValueNew = element_new.tag
        tagValueOld = element_old.tag
        if tagValueNew != tagValueOld or tagValueNew is None:
            return '?', None, None, None, None
        attrib = getAttribFromTag(tag=tagValueNew)
        attribValue_new = element_new.get(attrib)
        attribValue_old = element_old.get(attrib)
        # print(f"compareElement() attrib={attrib} {attribValue_new} <--> {attribValue_old}")
        if attribValue_new == attribValue_old:
            result = '='
            texte = f""
            # compareLevel(element_new, element_old, path=f"{path} / {attribValue_new}", attrib='nom')
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
        tagValueNew = element_new.tag
        attrib = getAttribFromTag(tag=tagValueNew)
        attribValue_new = element_new.get(attrib)
        texte = "--> ajouté"
        attribValue = attribValue_new
        get_new = True
        get_old = False
    elif element_old is not None:
        result = 's'
        tagValueOld = element_old.tag
        attrib = getAttribFromTag(tag=tagValueOld)
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

def compareLevel(tree_new, tree_old, attrib, path, level, nomClasse):
    global listeClassesExclues, listeClassesAjoutees, listeClassesSupprimees, listeModifications
    global modificationsClasse, modificationsAjoutsClasse, modificationsSuppressionsClasse
    
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
        if element_new is None and element_old is None:
            break

        result, texte, attribValue, get_new, get_old = compareElement(element_new, element_old, attrib)
        logging.info(f"result={result}, texte={texte}, attribValue={attribValue}, get_new={get_new}, get_old={get_old}")

        if level == 0:
            nomClasse = attribValue
            verbosePrint("")
            verbosePrint(f"===== {attrib} = {nomClasse} [{numeros_de_classe.get(nomClasse)}] =====")
            if nomClasse in classes_a_exclure:
                verbosePrint("--------> IGNOREE")
                listeClassesExclues.append(nomClasse)
                continue

        if path == '':
            textePath = f'{attribValue}'
        else:
            textePath = f"{path} / {attribValue}"

        if result == 'a':
            ### AJOUT ###
            logging.info(f"AJOUT    {attrib} {attribValue} {element_new.get(attrib)}")
            if level == 0:
                # on est au premier niveau  => ajout de classe
                listeClassesAjoutees.append(nomClasse)
                verbosePrint(f"CLASSE {texte}")
            else:
                modificationsClasse.append(f"{textePath} {texte}")
                modificationsAjoutsClasse.append(textePath)
                verbosePrint(f"{textePath} {texte}")
        elif result == 's':
            ### SUPPRESSION ###
            logging.info(f"SUPPR    {attrib}  {attribValue} {element_old.get(attrib)}")
            if level == 0:
                listeClassesSupprimees.append(nomClasse)
                verbosePrint(f"CLASSE {texte}")
            else:
                modificationsClasse.append(f"{textePath} {texte}")
                modificationsSuppressionsClasse.append(textePath)
                verbosePrint(f"{textePath} {texte}")
        elif result == '=':
            logging.info(f"EGAL    {attrib}  {attribValue}")
            # print(texte)
        elif result == '?':
            verbosePrint(f"???? result={result} attrib={attrib}  attribValue={attribValue} ")
            # print(texte)
        else:
            logging.warning(f"???? result={result}   attrib={attrib}  attribValue={attribValue} ")
        if element_new is None:
            lg = '--'
        else:
            lg = len(element_new)
        # print(f"compareLevel(attrib={attrib}, path={path}, level={level}) result={result}, texte={texte}, attribValue={attribValue}, get_new={get_new}, get_old={get_old} len(element_new)={lg}")
        if result == '=' and len(element_new) > 0:
            logging.info(f"EGAL => compareLevel()    {attrib}  {attribValue}")
            if level == 0:
                pathForCompare = f""
                modificationsClasse = []
                modificationsAjoutsClasse = []
                modificationsSuppressionsClasse = []
            elif level == 1:
                pathForCompare = f"{attribValue}"
            else:
                pathForCompare=f"{path} / {attribValue}"
            compareLevel(element_new, element_old, attrib='nom', path=pathForCompare, level=level + 1, nomClasse=nomClasse)
            if level == 0:
                if len(modificationsClasse) > 0:
                    listeModifications[nomClasse] = {}
                    listeModifications[nomClasse]['AJOUT'] = modificationsAjoutsClasse
                    listeModifications[nomClasse]['SUPPR'] = modificationsSuppressionsClasse

                # on a terminé de parcourir toute la classe

    # print("TERMINE")

def parcours(tree, texte):
    # print(f"DEB parcours() : texte={texte} len={len(tree)}_______________")
    generator = iterOneLevelXml(tree)
    pprint(tree)
    print(f"len(tree)={len(tree)}")
    cpt = 0
    while True:
        try:
            cpt += 1
            element = next(generator)
            # print(f"cpt={cpt} -> {element}")
            
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
pprint(root_new)
gom_new = root_new[0][0]

if nb_par == 3:
    diff = True
    fichier_old = sys.argv[2]
    arbre_old = ET.parse(fichier_old)
    root_old = arbre_old.getroot()
    gom_old = root_old[0][0]
    diff = compareLevel(tree_new=gom_new, tree_old=gom_old, attrib='class-name', path='', level=0, nomClasse=None)
else:
    parcours(tree=gom_new, texte="gom_new")
    diff = True

end_time = time.time()
execution_time = end_time - start_time
print(execution_time)

print("============= listeClassesExclues =============")
pprint(listeClassesExclues)
print("")

print("============= listeClassesAjoutees =============")
pprint(listeClassesAjoutees)
print("")

print("============= listeClassesSupprimees =============")
pprint(listeClassesSupprimees)
print("")

print("============= listeModifications =============")
pprint(listeModifications)
print("")

if diff:
    exit(1)
elif not diff:
    exit(0)
