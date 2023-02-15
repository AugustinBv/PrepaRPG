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

class Quete():
    def __init__(self, Quete, indice):
        self.Id=Quete[indice][0]       
        self.Etat=Quete[indice][1]      
        self.Nom=Quete[indice][2]           
        self.Description=Quete[indice][3] 

    def InfoAffichage(self):
        Descriptionmodiffie=self.Description.replace('@','\n')
        return self.Nom,Descriptionmodiffie

class ListeQuete():
    def __init__(self):
        self.ListeQuete = []
        self.ListeQuetePNG = []

    def DefListeQuete(self,texte):
        Quete=OuvrirFichier(texte)
        ListeQuete=[]
        ListeQuetePNG = []
        for i in range (len(Quete)-4):
            ListeQuete.append(Quete(Quete,i))
        self.ListeQuete = ListeQuete
        for i in range(len(Quete)-4,len(Quete)):
            ListeQuetePNG.append(Quete(Quete,i))
        self.ListeQuetePNG = ListeQuetePNG

    def AjoutSortAppris(self,Level):
        DicoSortLevel={3:'04',5:'05',8:'06',10:'07',14:'08',20:'09',25:'10',32:'11',39:'12',46:'13',52:'14',58:'15',67:'16',75:'17',88:'18',98:'19'}  #Level de déblocage et compétence
        for a in DicoSortLevel.keys():
            if Level==a:
                self.ListeSort[int(DicoSortLevel[a])].Connue="Acquis"

    def ListeQueteParEtat(self,etat):
        if etat=="Done":
            ListeQueteEtat=[]
            for i in range(len(self.ListeQuete)):
                if self.ListeQuete[i].Connue=="Done":
                    ListeQueteEtat.append(self.ListeQuete[i].Id)
            if len(ListeQueteEtat)/6-int(len(ListeQueteEtat)/6)==0:
                b=int(len(ListeQueteEtat)/6)
            elif len(ListeQueteEtat)/6-int(len(ListeQueteEtat)/6)<1:
                b=int(len(ListeQueteEtat)/6)+1
            ListeQueteEtatTrie=[]
            for i in range(0,b):
                ListeQueteEtatTrie.append(ListeQueteEtat[6*i:6*(i+1)])
        elif etat!="Done" and etat!="Invisible":
            ListeQueteEtat=[]
            for i in range(len(self.ListeQuete)):
                if self.ListeQuete[i].Connue=="Done":
                    ListeQueteEtat.append(self.ListeQuete[i].Id)
            if len(ListeQueteEtat)/6-int(len(ListeQueteEtat)/6)==0:
                b=int(len(ListeQueteEtat)/6)
            elif len(ListeQueteEtat)/6-int(len(ListeQueteEtat)/6)<1:
                b=int(len(ListeQueteEtat)/6)+1
            ListeQueteEtatTrie=[]
            for i in range(0,b):
                ListeQueteEtatTrie.append(ListeQueteEtat[6*i:6*(i+1)])
        return b,ListeQueteEtatTrie


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

    def EnregistrerQuete(self,texte):
        monFichier=open(texte,"w", encoding='utf-8')
        monFichier.write("00/{}/{}/{}/\n".format(self.ListeQuete[0].Etat,self.ListeQuete[0].Nom,self.ListeQuete[0].Description))
        for i in range(1,len(self.ListeQuete)):
            monFichier=open(texte,"a", encoding='utf-8')
            a=str(i)
            if int(a)<10:
                a="0"+a
            monFichier.write("{}/{}/{}/{}/\n".format(a,self.ListeQuete[0].Etat,self.ListeQuete[0].Nom,self.ListeQuete[0].Description))
        for i in range(0,len(self.ListeQuetePNG)):
            monFichier=open(texte,"a", encoding='utf-8')
            a=i+len(self.ListeQuete)
            a=str(i)
            monFichier.write("{}/{}/{}/{}/\n".format(a,self.ListeQuetePNG[0].Etat,self.ListeQuetePNG[0].Nom,self.ListeQuetePNG[0].Description))