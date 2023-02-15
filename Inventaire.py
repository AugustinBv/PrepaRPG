#fonction permettant d'ouvrir le dossier des items
def OuvrirFichier(nom,numero='@',car='/'):
    monFichier=open(nom, encoding='utf-8')
    Fichier=monFichier.readlines()
    monFichier.close()
    if numero=='@':
        for i in range(len(Fichier)):
            a=Fichier[i].split(car)
            Fichier[i]=a[0:-1]
        return Fichier
    else:
        Ligne=Fichier[numero].split(car)
        Ligne=Ligne[0:-1]
        return Ligne

#classe servant à définir l'objet item
class Item() :
    def __init__(self,Items, indice) :
        self.Id=Items[indice][0]
        self.Nom=Items[indice][1]
        self.Type=Items[indice][2]
        self.Attribut=Items[indice][3]

#classe servant à définir l'objet inventaire
class Inventaire():
    def __init__(self):
        pass
    
    def iniInventaire(self, globalObjects):
        self.Player =       globalObjects[0].get('Player', None)
        self.ListeItems = []
        self.DicoInventaire= {}
        self.ListePrix=[200,70,500,300,250,200,350]


#fonction permettant de trier l'inventaire sous forme de lsite, elle sera particulièrement utile pour le groupe menu
    def DefInventaire(self,texte1="Item.txt",texte2="Inventaire.txt"):
        Items=OuvrirFichier(texte1)
        ListeItems=[]
        for i in range (len(Items)):
            ListeItems.append(Item(Items,i))
        self.ListeItems=ListeItems
        Inventaire=OuvrirFichier(texte2)
        DicoInventaire={}
        for i in range (len(Inventaire)):
            DicoInventaire[Inventaire[i][0]]=int(Inventaire[i][1])
        self.DicoInventaire=DicoInventaire

#fonction qui ajoute un item dans l'inventaire
    def Ajouter(self,Id, nombre) :
        self.DicoInventaire[Id]+=nombre
        if self.DicoInventaire[Id]>999:
            self.DicoInventaire[Id]=999
        return self.DicoInventaire

#fonction qui permet d'améliorer les statistiques du joueurs lorsqu'il a ramassé suffisemment d'objets pour les améliorer.
    def Ameliorer(self,Id) :
        Idc=str(7+int(Id))
        if int(Idc)<10:
            Idc="0"+Idc
        self.DicoInventaire[Idc]-=2*self.DicoInventaire[Id]+1
        self.DicoInventaire[Id]+=1
        if self.ListeItems[int(Id)].Attribut=="Maths" :  #Dégat
            self.Player.damage += 3
        elif self.ListeItems[int(Id)].Attribut=="Physique" :  #Esquive
            self.Player.dodge += 0.4
        elif self.ListeItems[int(Id)].Attribut=="Chimie" :  #Soin
            self.Player.heal += 3
        elif self.ListeItems[int(Id)].Attribut=="SI" :  #Résistance au Débuffs
            self.Player.resistanceDebuff += 1
        elif self.ListeItems[int(Id)].Attribut=="Francais" :  #Défense
            self.Player.defense += 3
        elif self.ListeItems[int(Id)].Attribut=="Langues" :  #Aptitude au débuff
            self.Player.aptDebuff += 1
        elif self.ListeItems[int(Id)].Attribut=="Informatique" :  #Critique
            self.Player.crits += 0.4

        return self.DicoInventaire

#fonction qui permet de vérifier si le joueur possède suffisemment de composants pour améliorer sa caractéristique
    def ComposantSuffisant(self,Id):
        Idc=str(7+int(Id))
        if int(Idc)<10:
            Idc="0"+Idc
        if self.DicoInventaire[Id]==20:
            return self.DicoInventaire[Idc], 0,'MAX'
        elif self.DicoInventaire[Idc] - (2*self.DicoInventaire[Id]+1) <0:
            return self.DicoInventaire[Idc], (2*self.DicoInventaire[Id]+1),False
        else:
            return self.DicoInventaire[Idc], (2*self.DicoInventaire[Id]+1),True

#fonction qui vérifie si le joueur possède suffisemment d'argent pour améliorer sa caractéristique ou acheter un objet (ou autre)
    def ArgentSuffisant(self,Argent,Liste):
        PrixTotal=0
        ListePrix=[]
        for i in range(len(Liste)):
            PrixTotal+=Liste[i]*self.ListePrix[i]
            ListePrix.append(Liste[i]*self.ListePrix[i])
        if Argent - PrixTotal<0:
            return False,PrixTotal,ListePrix
        else:
            return True,PrixTotal,ListePrix

#fonction permettant au joueur d'acheter un item
    def Achat(self,Liste):
        for i in range(7,len(Liste)+7):
            if int(i)<10:
                Id="0"+str(i)
            else:
                Id=str(i)
            self.Ajouter(Id,Liste[i-7])

#fonction permettant de réinitialiser l'inventaire
    def ResetInventaire (self,texte):
        monFichier=open(texte,"w")
        monFichier.write("00/{}/\n".format("00"))
        for i in range(1,14):
            monFichier=open(texte,"a")
            a=str(i)
            if int(a)<10:
                a="0"+a
            monFichier.write("{}/{}/\n".format(a,"00"))

#fonction qui enregistre l'inventaire du joueur suite à une modification quelconque
    def EnregistrerInv(self, texte):
        monFichier=open(texte,"w", encoding='utf-8')
        a=str(self.DicoInventaire["00"])
        if int(a)<10:
                a="0"+a
        monFichier.write("00/{}/\n".format(a))
        for i in range(1,len(self.DicoInventaire)):
            monFichier=open(texte,"a", encoding='utf-8')
            b=str(i)
            if int(b)<10:
                b="0"+b
            c=str(self.DicoInventaire[b])
            if self.DicoInventaire[b]<10:
                c="0"+c
            monFichier.write("{}/{}/\n".format(b,c))
