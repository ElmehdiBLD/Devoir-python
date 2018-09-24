#on importe les bibliotheques
import calendar
from datetime import *
#fonction permettant de savoir combien on ajoute selon le mois
def calculJourDeLaSemaine(mois) :
    moi = int(0)
    if mois <= 1 or mois == 10:
        moi = 0
    elif mois <= 3 or mois == 11:
        moi = 3
    elif mois == 4 or mois == 7:
        moi = 6
    elif mois == 5:
        moi = 1
    elif mois == 6:
        moi = 4
    elif mois == 8:
        moi = 2
    elif mois == 9 or mois == 12:
        moi = 5
    return moi
#fonction qui permet de savoir combien on ajoute selon le siecle
def CalculSiecle(année) :
    result = int(0)
    if année-année % 100 == 1600:
        result = 6
    elif année-année % 100 == 1700:
        result = 4
    elif année-année % 100 == 1800:
        result = 2
    elif année-année % 100 == 1900:
        result = 0
    elif année-année % 100 == 2000:
        result = 6
    elif année-année % 100 == 2100:
        result = 4
    return result
#fonction qui permet d'enoncé le jour obtenue ce qui rend le programme plus comprehensible
def Traduction(resultat):
    result =str("blabla")
    if resultat == 0:
        result = "Dimanche"
    elif resultat == 1:
        result = "lundi"
    elif resultat == 2:
        result = "Mardi"
    elif resultat == 3:
        result = "Mercredi"
    elif resultat == 4:
        result = "Jeudi"
    elif resultat == 5:
        result = "Vendredi"
    elif resultat == 6:
        result = "Samedi"
    return result
#on demande  a l'utilisateur de rentréé le jour , le mois puis l'année
jour=int(input("entrer le jour "))
mois=int(input("entrer le mois"))
année=int(input("entrer lannée"))

#on récupere les deux derniers chiffres de l'année et on les stocke dans une variable annéeResultat pour ne pas confondre avec l'année
annéeResultat= année % 100

#on crée une variable resultat qui contiendra le resultat
resultat=int(0)
#on lui ajoute les deux derniers chiffres de l'année
resultat=annéeResultat
#On ajoute 1/4 de ce chiffre en ignorant les restes;
resultat+=int(annéeResultat/4)
#On ajoute la journée du mois
resultat+=jour
#on ajoute la valeur associé au mois
resultat+=calculJourDeLaSemaine(mois)
#on verifie si l'année est bissextile
if calendar.isleap(année)==True and mois==1 or mois ==2:
    resultat -= 1

#on ajoute le resultat trouver grace au siecle
resultat=resultat+CalculSiecle(année)
#On divise la somme par 7 et on garde le reste
resultat = resultat % 7
#on affiche la reponse
print("le",jour,"jour du ",mois,"mois de l'année",année,"est le jour",resultat," de la semaine,c'est a dire",Traduction(resultat))

