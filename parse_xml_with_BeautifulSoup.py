from bs4 import BeautifulSoup

# Charge le fichier xml
with open('srsa-ip-skeleton-cmoip.xml', 'r') as f:
    soup = BeautifulSoup(f.read(), 'xml')

# Trouve tous les obj qui ne sont pas contenu dans d'autres obj
objs = [obj for obj in soup.find_all('obj') if not obj.find_parents('obj')]

#Parcours de tous les obj 
for obj in objs:
    # Cree un fichier xml contenant les elements obj 
    # Le fichier a pour nom l'id de l'obj
    with open(obj["id"] + ".xml", "w") as f:
        f.write(str(obj))
