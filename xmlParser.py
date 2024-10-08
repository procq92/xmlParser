#import xml
import lxml
from lxml import etree
#import xml.etree.ElementTree as et
from pathlib import Path
#import xml.etree.ElementTree.tostring as ts
from pprint import pprint
import argparse
import logging, time
from infosClasses import numeros_de_classe, classes_a_exclure

classes_a_exclure = ()

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
        tt = etree.ElementTree.tostring(noeudEnfant[0])
        print(f"===== tt={tt}")

gmTime = time.gmtime()
dateTexte = f"{gmTime.tm_year}-{gmTime.tm_mon:02d}-{gmTime.tm_mday:02d} {gmTime.tm_hour:02d}:{gmTime.tm_min:02d}:{gmTime.tm_sec:02d}"

p = Path.cwd()

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', help='ajoute des traces', action='store_true')
parser.add_argument('filename', help='nom du fichier xml à parser')
parser.add_argument('version', help='version CMoIP')
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
listeClassesInclues =  p / (args.filename + "_listeClassesInclues.txt")
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
if not listeClassesInclues.exists():
    listeClassesInclues.touch()

tree = etree.parse(args.filename)
root = tree.getroot()
groupObjectModel = root[0][0]

version_cmoip = root.attrib.get('sw_cmoip_version')
if version_cmoip is None:
    version_cmoip = args.version
texte_description = f"<!-- date : {dateTexte} squelette : {args.filename} -->\n"
print("texte_description=" + texte_description)

# print(type(p))
# print(p)
# print(type(resultFolder))
texteListeClasses = ""
texteListeClassesInclues = ""
texteListeClassesExclues = ""
nbClasses = 0
nbClassesExclues = 0
nbClassesInclues = 0
for enfant in groupObjectModel:
    class_name = enfant.get('class-name')
    nbClasses += 1
    texteListeClasses += "\n" + class_name
    if class_name in classes_a_exclure:
        nbClassesExclues += 1
        texteListeClassesExclues += "\n" + class_name
    else:
        nbClassesInclues += 1
        #print (class_name)
        #if class_name == "ithTphConfiguration.IDomains":
        #    print (enfant)
        info_classe = numeros_de_classe.get(class_name)
        if info_classe is not None:
            numero_classe = info_classe.get('numero')
            if numero_classe is not None:
                if numero_classe == "":
                    texte_numero = "na"
                    print("class_name={} -> numéro vide".format(class_name))
                else:
                    texte_numero = f"{numero_classe}"
            else:
                texte_numero = "null"
                print("class_name={} -> pas de numéro".format(class_name))
            dossier_classe = info_classe.get('dossier', "inconnu")
            resultFolderClasse = resultFolder / dossier_classe
            if not resultFolderClasse.exists():
                resultFolderClasse.mkdir()
                print(f"Création du dossier {resultFolderClasse.name}")
            if resultFolderClasse.is_file():
                logging.error(f"Le répertoire de destination est un fichier, et pas un répertoire")
                exit(1)

        texte_fichier =  f'<!-- fichier : {"templ_" + texte_numero + class_name + ".xml"} classe : {texte_numero + " === " + class_name} -->\n\n'
        texteListeClassesInclues += "\n" + class_name
        filename = resultFolderClasse / ("templ_" + texte_numero + "_" + class_name + ".xml")
        print(f"======  name={filename.name} stem={filename.stem} suffix={filename.suffix} parts={filename.parts}")
        enfant_str = etree.tostring(enfant, encoding='unicode')
        print(f"Ecriture du fichier {filename.name}")
        filename.write_text(texte_description + texte_fichier + enfant_str, encoding='utf-8')
        # with open(filename, "w", encoding="utf-8") as f:
        #     f.write(xml.etree.ElementTree.tostring(enfant, encoding='unicode'))
listeClasses.write_text(texteListeClasses)
listeClassesInclues.write_text(texteListeClassesInclues)
listeClassesExclues.write_text(texteListeClassesExclues)
print(f"{nbClasses} classes trouvées")
print(f"{nbClassesInclues} classes inclues")
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