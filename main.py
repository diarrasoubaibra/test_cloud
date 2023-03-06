from datetime import datetime
from time import strftime

f=open("liste.txt","a")
item=""
while item != "exit":
    print("******* bienvenue sur mon site *******")
    entrer = int(input("entrez 1 pour cosulter la liste des enregistrés entrez 2 "
                       "pour vous enregistrer"))
    if entrer==1:
        date = datetime.now()
        date_inscri = date.strftime("%d/%m/%y")
        item=input("entrez votre nom et prénom : ")
    if item!="exit":
        f.write(item + "\n")
print("***fin***")
f.close