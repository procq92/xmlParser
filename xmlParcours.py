import xml
import xml.etree.ElementTree as et
from pathlib import Path
#import xml.etree.ElementTree.tostring as ts
from pprint import pprint
import argparse
import logging

def decrireNoeud(noeud, niveau=0, decrireEnfants=False):
    print("N=", niveau, "   tag=", noeud.tag, "attrib=", noeud.attrib, "len=", len(noeud))
    if len(noeud) > 0 and decrireEnfants:
        for noeudEnfant in noeud:
            decrireNoeud(noeudEnfant, niveau + 1, decrireEnfants=True)

def decrireEnfants(noeud):
    if len(noeud) > 0:
        index = 0
        for noeudEnfant in noeud:
            print(index, "tag=", noeudEnfant.tag, "id=", noeudEnfant.attrib.get('class-name', ""))
            #xml.etree.ElementTree.tostring(noeudEnfant)
            index+= 1
        print(dir(noeudEnfant[0]))
        tt = xml.etree.ElementTree.tostring(noeudEnfant[0])
        print(f"===== tt={tt}")

def chercherEnfant(noeud, tagEnfant):
    for enfant in noeud:
        nom = enfant.attrib.get("nom")
        #print (nom)
        if nom == tagEnfant:
            return enfant
    return None

def convertToDict(noeud):
    d = {}
    d['type'] = noeud.tag
    d['nbEnfants'] = len(noeud)
    d['nbAttributs'] = len(noeud.attrib)
    d['attributs'] = {}
    for nomAttr, attr in noeud.attrib.items():
        d['attributs'][nomAttr] = attr
    numEnfant = 0
    d['enfants'] = {}
    for enfant in noeud:
        cleEnfant = "enfant_{:03d}".format(numEnfant)
        d['enfants'][cleEnfant] = convertToDict(enfant)
        numEnfant += 1
    return d

p = Path.cwd()
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', help='ajoute des traces', action='store_true')
parser.add_argument('filename', help='nom du fichier xml à parser')
#parser.add_argument('resultFolder', default='templ', help='répertoire où placer les templates')
args = parser.parse_args()
# if args.resultFolder:
#     resultFolder = args.resultFolder
# else:
#     resultFolder = "templ"
print("filename=" + args.filename)
#print("resultFolder=" + args.resultFolder)

if False:
    resultFolder = p / (args.filename + "_templParClasse")
    listeClasses =  p / (args.filename + "_listeClasses")
    if not resultFolder.exists():
        resultFolder.mkdir()
        print(f"Création du dossier {resultFolder.name}")
    if resultFolder.is_file():
        logging.error(f"Le répertoire de destination est un fichier, et pas un répertoire")
        exit(1)
    if not listeClasses.exists():
        listeClasses.touch()

tree = et.parse(args.filename)
root = tree.getroot()
for noeud in root:
    pprint("tag=" + root.tag)
    pprint(f"att={root.attrib}")
# print(type(p))
# print(p)
# print(type(resultFolder))
if False:
    groupObjectModel = root[0][1][0]
    noeud = chercherEnfant(noeud=root[0][1], tagEnfant="mcr-0-0-0")
    if noeud:
        decrireNoeud(noeud, decrireEnfants=True)
        d = convertToDict(noeud=noeud)
        pprint(d)
for noeud in root:
    dictNoeud = convertToDict(noeud=noeud)
    id = noeud.attrib['id']
    idFilename = id.replace(" ", "_").replace("/", "")
    filename = f"dict/dict_{idFilename}.py"
    with open (filename, "wt", encoding="utf-8") as out:
        pprint(dictNoeud, width=120, stream=out)

if False:
    texteListeClasses = ""
    nbClasses = 0
    for enfant in groupObjectModel:
        nbClasses += 1
        class_name = enfant.get('class-name')
        texteListeClasses += "\n" + class_name
        filename = resultFolder / ("templ_" + class_name + ".xml")
        #print(f"======  {filename.name} {filename.stem} {filename.suffix} {filename.parts}")
        filename.write_text(xml.etree.ElementTree.tostring(enfant, encoding='unicode'))
        # with open(filename, "w", encoding="utf-8") as f:
        #     f.write(xml.etree.ElementTree.tostring(enfant, encoding='unicode'))
    listeClasses.write_text(texteListeClasses)
    print(f"{nbClasses} classes trouvées")
    
if False:
    print("-----------------------------")
    #decrireNoeud(root, 0, True)
    groupObjectModel = root[0][0]
    decrireEnfants(groupObjectModel)
    print("decrireNoeud(groupObjectModel[4])")
    decrireNoeud(groupObjectModel[4])
    print("------ xml -------")
    print(dir(xml))

    print("------ xml.etree -------")
    print(dir(xml.etree))

    print("------ xml.etree.ElementTree -------")
    print(dir(xml.etree.ElementTree))

    print("=== decrireNoeud(groupObjectModel) ===")
    decrireNoeud(groupObjectModel)
    print("=== decrireEnfants(groupObjectModel) ===")
    decrireEnfants(groupObjectModel)

    print("=== decrireNoeud(groupObjectModel[12],decrireEnfants=True) ===")
    decrireNoeud(groupObjectModel[12],decrireEnfants=True)
    tt = xml.etree.ElementTree.tostring(groupObjectModel[12], encoding='unicode')
    #print("=== tt ===")
    print(tt)
    with open ('testTemplate.xml', "wt", encoding="utf-8") as out:
        pprint(tt, width=120, stream=out)

    print("=== fin ===")
#decrireNoeud(object)
#print(f"+++class-name={object.attrib.get('class-name', '')}")
#tt = xml.etree.ElementTree.tostring(groupObjectModel[5])
#print(tt)