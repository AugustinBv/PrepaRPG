# fonction qui récupére le fichier contenant les compétences
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

#classe compétence qui nous permettra de les utiliser plus facilement
class Sort():
    def __init__(self, Competence, indice):
        self.Id=Competence[indice][0]       #Id
        self.Connue=Competence[indice][1]       #si la compétence est apprise on associe la valeur Acquis
        self.Nom=Competence[indice][2]       #Nom
        self.Cible=Competence[indice][3]       #Les cibles
        self.StatCible=Competence[indice][4]       #Les Statistiques ciblées
        self.Valeur=Competence[indice][5]       #Les valeurs associées au stats ciblées
        self.Vitesse=Competence[indice][6]  #Vitesse de la compétence
        self.Description=Competence[indice][7] #Description de la compétence
        self.ListStatCible=Sort.CibleStat(self.Cible, self.StatCible, self.Valeur)#apelle une fonction qui renvoie 3 valeurs principales de chaque compétence : la personne affectée par la compétence (le joueur ou son adversair), la(les) stat(s) que la compétence affecte, et de combien la compétence affecte cette stat.

#fonction appelée à la ligne du dessous permettant de revoyer la liste ci-dessus
    def CibleStat(cible, statcible, valeur):
        a=cible.split(",")
        b=statcible.split(",")
        c=valeur.split(",")
        ListCible=[]
        for i in range (len(a)):
            ListCible.append([a[i],b[i],int(c[i])])
        return(ListCible)

#fonction utilisée par le groupe menu pour afficher le nom, la vitesse et la description d'un compétence quand on la regarde dans l'inventaire des compétences
    def InfoAffichage(self):
        Descriptionmodiffie=self.Description.replace('@','\n')
        return self.Nom,self.Vitesse,Descriptionmodiffie

#classe qui nous servira à organiser les sorts appris et le niveau auquel chaque sort sera appris
class ListeSort():
    def __init__(self):
        pass
    
    def iniListeSort(self):
        self.ListeSort = []

    def DefListeSort(self,texte):
        Competence=OuvrirFichier(texte)
        ListeSort=[]
        for i in range (len(Competence)):
            ListeSort.append(Sort(Competence,i))
        self.ListeSort=ListeSort

#fonction qui sera appelée à chaque montée en niveau qui permet de débloquer une compétence lorsque le niveau requis est atteint
    def AjoutSortAppris(self,Level):
        DicoSortLevel={3:'04',5:'05',8:'06',10:'07',14:'08',20:'09',25:'10',32:'11',39:'12',46:'13',52:'14',58:'15',67:'16',75:'17',88:'18',98:'19'}  #Level de déblocage et compétence
        for a in DicoSortLevel.keys():
            if Level==a:
                self.ListeSort[int(DicoSortLevel[a])].Connue="Acquis"

#fonction qui permet de retourner la liste des sorts appris pour le groupe menu
    def ListeSortAppris(self):
        ListeSortAppris=[]
        for i in range(len(self.ListeSort)):
            if self.ListeSort[i].Connue=="Acquis":
                ListeSortAppris.append(self.ListeSort[i].Id)
        if len(ListeSortAppris)/6-int(len(ListeSortAppris)/6)==0:
            b=int(len(ListeSortAppris)/6)
        elif len(ListeSortAppris)/6-int(len(ListeSortAppris)/6)<1:
            b=int(len(ListeSortAppris)/6)+1
        ListeSortApprisTrie=[]
        for i in range(0,b):
            ListeSortApprisTrie.append(ListeSortAppris[6*i:6*(i+1)])
        return b,ListeSortApprisTrie

    def AjoutSortPossible(self,ListeCompetence):
        a=False
        for i in ListeCompetence:
            if i=='@':
                a=True
        return a

#fonctions permettant d'ajouter ou de supprimer des sorts, elles seront utilisée par le groupe menu lorsque le joueur rendra visite à un marchand de compétence pour en changer
    def SupprimerSortActuel(self,indice,ListeCompetence):
        ListeCompetence=ListeCompetence[0:indice]+['@']+ListeCompetence[indice+1:]
        return ListeCompetence

    def AjoutSort(self,Id,ListeCompetence):
        for i in range(len(ListeCompetence)):
            if ListeCompetence[i]=='@':
                return ListeCompetence[0:i]+[Id]+ListeCompetence[i+1:]

#fonction permettant de valider le changement des compétences tout en prélevant de l'argent au joueur.
    def Validation(self,ListeInit,ListeFin,Argent):
        if '@' in ListeFin:
            return False, 0
        diff=0
        for Id in ListeFin:
            if Id not in ListeInit:
                diff+=1
            if ListeFin.count(Id) != 1:
                return False, 0
        print(diff)
        if Argent-200*diff<0:
            return False, 200*diff
        else:
            return True, 200*diff


    def ResetCompetence(self,texte):
        for i in range(4,len(self.ListeSort)):
            self.ListeSort[i].Connue="NonAqcuis"
        monFichier=open(texte,"w", encoding='utf-8')
        monFichier.write("00/{}/{}/{}/{}/{}/{}/{}/\n".format(self.ListeSort[0].Connue,self.ListeSort[0].Nom,self.ListeSort[0].Cible,self.ListeSort[0].StatCible,self.ListeSort[0].Valeur,self.ListeSort[0].Vitesse,self.ListeSort[0].Description))
        for i in range(1,len(self.ListeSort)):
            monFichier=open(texte,"a", encoding='utf-8')
            a=str(i)
            if int(a)<10:
                a="0"+a
            monFichier.write("{}/{}/{}/{}/{}/{}/{}/{}/\n".format(a,self.ListeSort[i].Connue,self.ListeSort[i].Nom,self.ListeSort[i].Cible,self.ListeSort[i].StatCible,self.ListeSort[i].Valeur,self.ListeSort[i].Vitesse,self.ListeSort[i].Description))


    def EnregistrerCompetence(self,texte):
        monFichier=open(texte,"w", encoding='utf-8')
        monFichier.write("00/{}/{}/{}/{}/{}/{}/{}/\n".format(self.ListeSort[0].Connue,self.ListeSort[0].Nom,self.ListeSort[0].Cible,self.ListeSort[0].StatCible,self.ListeSort[0].Valeur,self.ListeSort[0].Vitesse,self.ListeSort[0].Description))
        for i in range(1,len(self.ListeSort)):
            monFichier=open(texte,"a", encoding='utf-8')
            a=str(i)
            if int(a)<10:
                a="0"+a
            monFichier.write("{}/{}/{}/{}/{}/{}/{}/{}/\n".format(a,self.ListeSort[i].Connue,self.ListeSort[i].Nom,self.ListeSort[i].Cible,self.ListeSort[i].StatCible,self.ListeSort[i].Valeur,self.ListeSort[i].Vitesse,self.ListeSort[i].Description))
