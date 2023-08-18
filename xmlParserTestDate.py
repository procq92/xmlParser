import xml, os
import xml.etree.ElementTree as et
from pathlib import Path
#import xml.etree.ElementTree.tostring as ts
from pprint import pprint
import argparse
import logging
from datetime import datetime
import time
import datetime

classes_a_exclure = ("cmoip.ICMoIPDistant",
                    "cmoip.ICmoipCie",
                    "cmoip.ICmoipClient",
                    "cmoip.ICmoipClientCie",
                    "cmoip.ICmoipServerStandaloneCie",
                    "cmoip.ICmoipServerStandaloneSnmp",
                    "cmoip.ICmoipSnmp",
                    "ithTphAnnuaire.ICorrespExterne",
                    "mg2s.IAtelierEnergie",
                    "mg2s.IAtelierEnergieCie",
                    "mg2s.IAtelierEnergie"
                    "mg2s.IAtelierEnergieCie",
                    "mg2s.IFarCerCie"
                    "mg2s.IFarCerSnmp"
                    "mg2s.IFarCexCie"
                    "mg2s.IFarCexSnmp"
                    )

def decrireNoeud(noeud, niveau=0, decrireEnfants=False):
    print("N=", niveau, "   tag=", noeud.tag, "attrib=", noeud.attrib, "len=", len(noeud))
    if len(noeud) > 0 and decrireEnfants:
        for noeudEnfant in noeud:
            decrireNoeud(noeudEnfant, niveau + 1)

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
#print("aaaaaaaaaaa")
resultFolder = p / (args.filename + "_templParClasse")
listeClasses =  p / (args.filename + "_listeClasses.txt")
listeClassesExclues =  p / (args.filename + "_listeClassesExclues.txt")
if not resultFolder.exists():
    resultFolder.mkdir()
    print(f"Création du dossier {resultFolder.name}")
if resultFolder.is_file():
    logging.error(f"Le répertoire de destination est un fichier, et pas un répertoire")
    exit(1)
if not listeClasses.exists():
    listeClasses.touch()
if not listeClassesExclues.exists():
    listeClassesExclues.touch()
statinfo = os.stat(args.filename)
info = statinfo
print(info.st_mtime)
dateheure = datetime.datetime.fromtimestamp(info.st_mtime)
print(f"{dateheure.day:02d}/{dateheure.month:02d}/{dateheure.year}  {dateheure.hour:02d}:{dateheure.minute:02d}:{dateheure.second:02d}")
tree = et.parse(args.filename)
root = tree.getroot()

# print(type(p))
# print(p)
# print(type(resultFolder))
groupObjectModel = root[0][0]
texteListeClasses = ""
texteListeClassesExclues = ""
nbClasses = 0
nbClassesExclues = 0
for enfant in groupObjectModel:
    class_name = enfant.get('class-name')
    if class_name in classes_a_exclure:
        nbClassesExclues += 1
    else:
        nbClasses += 1
        #print (class_name)
        #if class_name == "ithTphConfiguration.IDomains":
        #    print (enfant)
        texteListeClasses += "\n" + class_name
        filename = resultFolder / ("templ_" + class_name + ".xml")
        #print(f"======  {filename.name} {filename.stem} {filename.suffix} {filename.parts}")
        enfant_str = xml.etree.ElementTree.tostring(enfant, encoding='unicode')
        filename.write_text(enfant_str, encoding='utf-8')
        # with open(filename, "w", encoding="utf-8") as f:
        #     f.write(xml.etree.ElementTree.tostring(enfant, encoding='unicode'))
listeClasses.write_text(texteListeClasses)
listeClassesExclues.write_text(texteListeClassesExclues)
print(f"{nbClasses} classes trouvées")
print(f"{nbClassesExclues} classes exclues")

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