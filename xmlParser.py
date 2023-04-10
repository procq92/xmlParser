import xml
import xml.etree.ElementTree as et
#import xml.etree.ElementTree.tostring as ts
from pprint import pprint

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

tree = et.parse('srsaip-skeleton-cmoip.xml')
root = tree.getroot()
groupObjectModel = root[0][0]
for enfant in groupObjectModel:
    class_name = enfant.get('class-name')
    filename = "templ_" + class_name + ".xml"
    print(class_name)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(xml.etree.ElementTree.tostring(enfant, encoding='unicode'))
    
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