from random import randint
import pyglet

pyglet.options['search_local_libs'] = True
pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')
coeff=[1]
# lvl_up = pyglet.media.load('LvlUpSound.mp3', streaming = False) (un bruitage pas utilisé)

class Monster():
    def __init__ (self, pLvl, pDrop, pXp, dStats, pType, pName= "Monstre"):#initialise les informations de bases sur les monstres
    #(leur niveau, ce qu'ils donnent en objet, leurs expériencexp(), leurs stats, leur type et leur nom)
        self.setStat(dStats)
        self.lvl = pLvl
        self.drop = pDrop
        self.giveXp = pXp
        self.name = pName
        self.statut = ""
        self.type = pType
        self.nameG = {1:"Antoine",2:"Julien", 3:"Thibaut",4:"Augustin",5:"Victor",6:"Dorian",7:"Adrien",8:"Pierre",9:"Alexis",10:"Alexandre",11:"Thomas",12:"Léo",13:"Sasha",14:"Louis",15:"Paul",16:"Maime",17:"Oscar",18:"Eliott",19:"Baptiste",20:"Maxence",
                21:"Joseph",22:"Diego",23:"Valentin",24:"Isaac",25:"Martin",26: "Harry",27:"James",28:"Neville", 29:"Sirius",30:"Albus"}

        self.nameF = {1:"Heather-Jane",2:"Agathe",3:"Inès",4:"Luna",5:"Ginny",6:"Alicia",7:"Léa",8:"Nina",9:"Lola",10:"Charlotte",11:"Candice",12:"Margot",13:"Eve",14:"Nayah",15:"Lucie",16:"Clémence",17:"Lily",18:"Capucine",19:"Gabrielle",20:"Cassandre"}

    def setStat(self,stat): #on définit les stats des monstres, leur vie et l'argent qu'ils donnent
        self.damage = stat["damage"]
        self.dodge = stat["dodge"]
        self.heal = stat["heal"]
        self.defense = stat["defense"]
        self.aptDebuff = stat["aptDebuff"]
        self.resistanceDebuff = stat["resistanceDebuff"]
        self.crits = stat["crits"]
        self.hp = stat["hp"]
        self.hpMax = stat["hpMax"]
        self.money = stat["money"]

    def dialogues(self, nb=0):  #dialogues de début et fin de combats
        if nb==1:
            return "Un " + self.name + " sauvage apparaît !"
        if nb==2:
            return "Vous avez surpassé un " + self.name + " sauvage !"
        if nb==0:
            return ""

    def death(self):
        pass

    def addHp(self,nb): #ajoute des points de vie au monstre pendant le combat
        a=self.hpMax-self.hp
        self.hp +=int(nb*(self.heal+100)/100)
        if self.hp>self.hpMax:
            self.hp = self.hpMax
            return a
        return int(nb*(self.heal+100)/100)

    def removeHp(self,nb):#enlève des points de vie au monstre pendant le combat
        a=self.hp
        self.hp -= int(nb)
        print(nb)
        if self.hp <= 0:
            self.hp=0
            return a
        return int(nb)

    def changeName(self, pGenre="G"):   #donner des noms de manière aléatoire aux minorants, moduleOk et majorants et en fonctions de si ce sont des
    #filles ou des garçons, les monstres minorants et majorants sont des garçons et les modules Ok des filles
        print(type(self))
        if pGenre == "G":
            self.name = self.nameG[randint(1,30)]
        else :
            self.name = self.nameF[randint(1,20)]

class Minorant(Monster):



    def __init__(self, pZone=0, pDrop=1,  pName= " le Minorant"): #pZone donne la zone du monstre, tout s'adapte en fonction
        self.lvl=self.selectLvl(pZone)
        self.zone = pZone
        Monster.__init__(self, self.lvl, self.selectDrop(pZone), self.selectXp(pZone), self.selectStat(pZone), "Minorant", pName)
        Monster.changeName(self,"G")

    def selectLvl(self, nb): #donne le level du Minorant en fonction de la zone dans laquelle on se trouve dans la prépa
        if nb==0:
            lvl=1
        elif nb==1:
            lvl=1+randint(0,2)
        elif nb==2:
            lvl=10+randint(0,4)
        elif nb==3:
            lvl=22+randint(0,3)
        elif nb==4:
            lvl=22+randint(0,3)
        elif nb==5:
            lvl=32+randint(0,3)
        elif nb==6:
            lvl=42+randint(0,3)
        elif nb==7:
            lvl=52+randint(0,3)
        return lvl

    def selectDrop(self, nb):   #donne le nombre d'objet que le monstre va donner en fontion de la zone dans laquelle on se trouve
        if nb==0:
            drop=1
        elif nb==1:
            drop=randint(1,2)
        elif nb==2:
            drop=randint(2,3)
        elif nb==3:
            drop=randint(3,4)
        elif nb==4:
            drop=randint(4,5)
        elif nb==5:
            drop=randint(5,6)
        elif nb==6:
            drop=randint(6,7)
        elif nb==7:
            drop=randint(7,8)
        return drop

    def selectXp(self, nb): #donne le nombre de xp du minorant en fonction de la zone dans laquelle on se trouve
        if nb==0:
            xp=0
        elif nb==1:
            xp=30+(self.lvl-1)*5
        elif nb==2:
            xp=50+(self.lvl-10)*20
        elif nb==3:
            xp=130+(self.lvl-22)*30
        elif nb==4:
            xp=130+(self.lvl-22)*30
        elif nb==5:
            xp=500+(self.lvl-32)*100
        elif nb==6:
            xp=900+(self.lvl-42)*200
        elif nb==7:
            xp=8000+(self.lvl-52)*2000
        return xp

    def selectStat(self, nb):   #donne les stats du minorant en fonction de la zone et du niveau de difficulté(coeff) choisi par le joueur avec un peu d'aléatoire
        if nb==0:
            self.health=1
            stat = {"damage":1, "dodge":1, "heal":1, "defense":1, "aptDebuff":1, "resistanceDebuff":1, "crits":1, "hp":self.health, "hpMax":self.health, "money" : 1}
        elif nb==1:
            self.health=int((10+2*(self.lvl-1))*coeff[0])
            stat = {"damage":int((10+2*(self.lvl-1))*coeff[0]), "dodge":int((2+round(0.5*(self.lvl-1)))*coeff[0]), "heal":int((10+round(2.5*(self.lvl-1)))*coeff[0]),
                    "defense":int((2+round(1.5*(self.lvl-1)))*coeff[0]), "aptDebuff":int((20+(self.lvl-1))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-1))*coeff[0]),
                    "crits":int((2+(self.lvl-1))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(10,20)}
        elif nb==2:
            self.health=int((100+7*(self.lvl-10))*coeff[0])
            stat = {"damage":int((50+2*(self.lvl-10))*coeff[0]), "dodge":int((8+round(0.5*(self.lvl-10)))*coeff[0]), "heal":int((10+round(2.5*(self.lvl-10)))*coeff[0]),
                    "defense":int((25+round(1.5*(self.lvl-10)))*coeff[0]), "aptDebuff":int((20+(self.lvl-10))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-10))*coeff[0]),
                    "crits":int((8+(self.lvl-10))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(20,30)}
        elif nb==3:
            self.health=int((250+12*(self.lvl-22))*coeff[0])
            stat = {"damage":int((90+2*(self.lvl-22))*coeff[0]), "dodge":int((17+round(0.5*(self.lvl-22)))*coeff[0]), "heal":int((30+round(2.5*(self.lvl-22)))*coeff[0]),
                    "defense":int((10+round(1.5*(self.lvl-22)))*coeff[0]), "aptDebuff":int((20+(self.lvl-22))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-22))*coeff[0]),
                    "crits":int((8+randint(-2,2))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(30,40)}
        elif nb==4:
            self.health=int((200+10*(self.lvl-22))*coeff[0])
            stat = {"damage":int((115+2*(self.lvl-22))*coeff[0]), "dodge":int((12+round(0.5*(self.lvl-22)))*coeff[0]), "heal":int((10+round(2.5*(self.lvl-22)))*coeff[0]),
                    "defense":int((15+round(1.5*(self.lvl-22)))*coeff[0]), "aptDebuff":int((50+(self.lvl-22))*coeff[0]), "resistanceDebuff":int((50+(self.lvl-22))*coeff[0]),
                    "crits":int((8+(self.lvl-22))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(40,50)}
        elif nb==5:
            self.health=int((250+12*(self.lvl-32))*coeff[0])
            stat = {"damage":int((130+2*(self.lvl-32))*coeff[0]), "dodge":int((33+round(0.5*(self.lvl-32)))*coeff[0]), "heal":int((10+round(2.5*(self.lvl-32)))*coeff[0]),
                    "defense":int((40+round(1.5*(self.lvl-32)))*coeff[0]), "aptDebuff":int((20+(self.lvl-32))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-32))*coeff[0]),
                    "crits":int((2+(self.lvl-32))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(50,60)}
        elif nb==6:
            self.health=int((280+15*(self.lvl-42))*coeff[0])
            stat = {"damage":int((260+2*(self.lvl-42))*coeff[0]), "dodge":int((8+round(0.5*(self.lvl-42)))*coeff[0]), "heal":int((15+round(2.5*(self.lvl-42)))*coeff[0]),
                    "defense":int((40+round(1.5*(self.lvl-42)))*coeff[0]), "aptDebuff":int((20+(self.lvl-42))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-42))*coeff[0]),
                    "crits":int((13+(self.lvl-42))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(60,70)}
        elif nb==7:
            self.health=int((400+24*(self.lvl-52))*coeff[0])
            stat = {"damage":int((290+2*(self.lvl-52))*coeff[0]), "dodge":int((17+round(0.5*(self.lvl-52)))*coeff[0]), "heal":int((15+round(2.5*(self.lvl-52)))*coeff[0]),
                    "defense":int((140+round(1.5*(self.lvl-52)))*coeff[0]), "aptDebuff":int((20+(self.lvl-52))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-52))*coeff[0]),
                    "crits":int((23+(self.lvl-52))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(70,80)}
        return stat

    def getSkill(self): #compétences du minorant, qui peuvent tomber de manière aléatoire avec une certaine probabilité
        a=randint(0,100)
        if a <= 10 :
            skill=(30,0,"",10,"Eureka")
        elif 10<a<=90:
            skill=(10,0,"",10,"Je sais pas")
        elif 90<a<=100:
            skill=(0,10,"",10,"A l'aide")
        return skill

    def textureName(self):
        return "minorant_bg.png"

class ModulesOk(Monster):
#mêmes commentaires que pour le minorant mais cette fois pour le moduleOK

    def __init__(self, pZone=0, pDrop=randint(1,2),  pName=" la ModuleOk"):
        self.lvl=self.selectLvl(pZone)
        self.zone = pZone
        Monster.__init__(self, self.lvl, self.selectDrop(pZone), self.selectXp(pZone), self.selectStat(pZone), "ModulesOk", pName)
        Monster.changeName(self,"F")

    def selectLvl(self, nb):
        if nb==0:
            lvl=1
        elif nb==1:
            lvl=3+randint(-1,1)
        elif nb==2:
            lvl=14+randint(-2,2)
        elif nb==3:
            lvl=25+randint(-2,2)
        elif nb==4:
            lvl=25+randint(-2,2)
        elif nb==5:
            lvl=35+randint(-2,2)
        elif nb==6:
            lvl=45+randint(-2,2)
        elif nb==7:
            lvl=55+randint(-2,2)
        return lvl

    def selectDrop(self, nb):
        if nb==0:
            drop=1
        elif nb==1:
            drop=randint(2,3)
        elif nb==2:
            drop=randint(3,4)
        elif nb==3:
            drop=randint(4,5)
        elif nb==4:
            drop=randint(5,6)
        elif nb==5:
            drop=randint(6,7)
        elif nb==6:
            drop=randint(7,8)
        elif nb==7:
            drop=randint(8,9)
        return drop


    def selectXp(self, nb):
        if nb==0:
            xp=0
        elif nb==1:
            xp=50+(self.lvl-1)*8
        elif nb==2:
            xp=70+(self.lvl-10)*28
        elif nb==3:
            xp=170+(self.lvl-22)*43
        elif nb==4:
            xp=170+(self.lvl-22)*43
        elif nb==5:
            xp=700+(self.lvl-32)*130
        elif nb==6:
            xp=1100+(self.lvl-42)*300
        elif nb==7:
            xp=13000+(self.lvl-52)*3000
        return xp

    def selectStat(self, nb):
        if nb==0:
            self.health=1
            stat = {"damage":1, "dodge":1, "heal":1, "defense":1, "aptDebuff":1, "resistanceDebuff":1, "crits":1, "hp":self.health, "hpMax":self.health}
        elif nb==1:
            self.health=int((38+5*(self.lvl-3))*coeff[0])
            stat = {"damage":int((20+2*(self.lvl-3))*coeff[0]), "dodge":int((3+round(0.5*(self.lvl-3)))*coeff[0]), "heal":int((15+round(2.5*(self.lvl-3)))*coeff[0]),
                    "defense":int((3+round(1.5*(self.lvl-3)))*coeff[0]), "aptDebuff":int((20+(self.lvl-3))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-3))*coeff[0]),
                    "crits":int((3+(self.lvl-3))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(20,30)}
        elif nb==2:
            self.health=int((133+12*(self.lvl-14))*coeff[0])
            stat = {"damage":int((70+2*(self.lvl-14))*coeff[0]), "dodge":int((9+round(0.5*(self.lvl-14)))*coeff[0]), "heal":int((15+round(2.5*(self.lvl-14)))*coeff[0]),
                    "defense":int((37+round(1.5*(self.lvl-14)))*coeff[0]), "aptDebuff":int((20+(self.lvl-14))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-14))*coeff[0]),
                    "crits":int((10+(self.lvl-14))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(40,60)}
        elif nb==3:
            self.health=int((283+16*(self.lvl-25))*coeff[0])
            stat = {"damage":int((110+2*(self.lvl-25))*coeff[0]), "dodge":int((18+round(0.5*(self.lvl-25)))*coeff[0]), "heal":int((35+round(2.5*(self.lvl-25)))*coeff[0]),
                    "defense":int((23+round(1.5*(self.lvl-25)))*coeff[0]), "aptDebuff":int((20+(self.lvl-25))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-25))*coeff[0]),
                    "crits":int((10+(self.lvl-25))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(60,80)}
        elif nb==4:
            self.health=int((233+14*(self.lvl-25))*coeff[0])
            stat = {"damage":int((135+2*(self.lvl-25))*coeff[0]), "dodge":int((13+round(0.5*(self.lvl-25)))*coeff[0]), "heal":int((15+round(2.5*(self.lvl-25)))*coeff[0]),
                    "defense":int((28+round(1.5*(self.lvl-25)))*coeff[0]), "aptDebuff":int((50+(self.lvl-25))*coeff[0]), "resistanceDebuff":int((50+(self.lvl-25))*coeff[0]),
                    "crits":int((10+(self.lvl-25))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(80,100)}
        elif nb==5:
            self.health=int((283+18*(self.lvl-35))*coeff[0])
            stat = {"damage":int((150+2*(self.lvl-35))*coeff[0]), "dodge":int((32+round(0.5*(self.lvl-35)))*coeff[0]), "heal":int((15+round(2.5*(self.lvl-35)))*coeff[0]),
                    "defense":int((53+round(1.5*(self.lvl-35)))*coeff[0]), "aptDebuff":int((20+(self.lvl-35))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-35))*coeff[0]),
                    "crits":int((3+(self.lvl-35))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(100,120)}
        elif nb==6:
            self.health=int((313+20*(self.lvl-45))*coeff[0])
            stat = {"damage":int((280+2*(self.lvl-45))*coeff[0]), "dodge":int((9+round(0.5*(self.lvl-45)))*coeff[0]), "heal":int((20+round(2.5*(self.lvl-45)))*coeff[0]),
                    "defense":int((53+round(1.5*(self.lvl-45)))*coeff[0]), "aptDebuff":int((20+(self.lvl-45))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-45))*coeff[0]),
                    "crits":int((15+(self.lvl-45))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(120,140)}
        elif nb==7:
            self.health=int((433+25*(self.lvl-55))*coeff[0])
            stat = {"damage":int((310+2*(self.lvl-55))*coeff[0]), "dodge":int((18+round(0.5*(self.lvl-55)))*coeff[0]), "heal":int((20+round(2.5*(self.lvl-55)))*coeff[0]),
                    "defense":int((153+round(1.5*(self.lvl-55)))*coeff[0]), "aptDebuff":int((20+(self.lvl-55))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-55))*coeff[0]),
                    "crits":int((25+(self.lvl-55))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(140,160)}
        return stat

    def getSkill(self):
        a= randint(0,100)
        if a <= 10 :
            skill=(40,0,"",30,"Révisions")
        elif 10<a<=90:
            skill=(15,0,"",20,"TD")
        elif 90<a<=100:
            skill=(0,15,"",40,"Couché à 22h")
        return skill

    def textureName(self):
        return "lambda_bg.png"


class Majorant(Monster):
#mêmes commentaires que pour le minorant mais cette fois pour le Majorant
    nameG = {1:"Antoine",2:"Julien", 3:"Thibaut",4:"Augustin",5:"Victor",6:"Dorian",7:"Adrien",8:"Pierre",9:"Alexis",10:"Alexandre",11:"Thomas",12:"Léo",13:"Sasha",14:"Louis",15:"Paul",16:"Maime",17:"Oscar",18:"Eliott",19:"Baptiste",20:"Maxence",21:"Joseph",22:"Diego",23:"Valentin",24:"Isaac",25:"Martin",26: "Harry",27:"James",28:"Neville", 29:"Sirius",30:"Albus"}

    def __init__(self, pZone=0, pDrop=1,  pName=" le Majorant"):#pZone donne la zone du monstre, tout s'adapte en fonction
        self.lvl=self.selectLvl(pZone)
        self.zone = pZone
        Monster.__init__(self, self.lvl, self.selectDrop(pZone), self.selectXp(pZone), self.selectStat(pZone), "Majorant", pName)
        Monster.changeName(self,"G")

    def selectLvl(self, nb):
        if nb==0:
            lvl=1
        elif nb==1:
            lvl=4+randint(-1,1)
        elif nb==2:
            lvl=16+randint(-2,2)
        elif nb==3:
            lvl=27+randint(-2,2)
        elif nb==4:
            lvl=27+randint(-2,2)
        elif nb==5:
            lvl=37+randint(-2,2)
        elif nb==6:
            lvl=47+randint(-2,2)
        elif nb==7:
            lvl=57+randint(-2,2)
        return lvl

    def selectDrop(self, nb):
        if nb==0:
            drop=1
        elif nb==1:
            drop=randint(3,4)
        elif nb==2:
            drop=randint(4,5)
        elif nb==3:
            drop=randint(5,6)
        elif nb==4:
            drop=randint(6,7)
        elif nb==5:
            drop=randint(7,8)
        elif nb==6:
            drop=randint(8,9)
        elif nb==7:
            drop=randint(9,10)
        return drop


    def selectXp(self, nb):
        if nb==0:
            xp=0
        elif nb==1:
            xp=80+(self.lvl-1)*13
        elif nb==2:
            xp=100+(self.lvl-10)*35
        elif nb==3:
            xp=220+(self.lvl-22)*65
        elif nb==4:
            xp=220+(self.lvl-22)*65
        elif nb==5:
            xp=1000+(self.lvl-32)*195
        elif nb==6:
            xp=1700+(self.lvl-42)*420
        elif nb==7:
            xp=20000+(self.lvl-52)*6000
        return xp

    def selectStat(self, nb):
        if nb==0:
            self.health=1
            stat = {"damage":1, "dodge":1, "heal":1, "defense":1, "aptDebuff":1, "resistanceDebuff":1, "crits":1, "hp":self.health, "hpMax":self.health}
        elif nb==1:
            self.health=int((65+7*(self.lvl-4))*coeff[0])
            stat = {"damage":int((30+2*(self.lvl-4))*coeff[0]), "dodge":int((5+round(0.5*(self.lvl-4)))*coeff[0]), "heal":int((20+round(2.5*(self.lvl-4)))*coeff[0]),
                    "defense":int((5+round(1.5*(self.lvl-4)))*coeff[0]), "aptDebuff":int((20+(self.lvl-4))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-4))*coeff[0]),
                    "crits":int((5+(self.lvl-4))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(30,60)}
        elif nb==2:
            self.health=int((165+14*(self.lvl-16))*coeff[0])
            stat = {"damage":int((90+2*(self.lvl-16))*coeff[0]), "dodge":int((9+round(0.5*(self.lvl-16)))*coeff[0]), "heal":int((20+round(2.5*(self.lvl-16)))*coeff[0]),
                    "defense":int((50+round(1.5*(self.lvl-16)))*coeff[0]), "aptDebuff":int((20+(self.lvl-16))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-16))*coeff[0]),
                    "crits":int((12+(self.lvl-16))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(60,90)}
        elif nb==3:
            self.health=int((315+20*(self.lvl-27))*coeff[0])
            stat = {"damage":int((130+2*(self.lvl-27))*coeff[0]), "dodge":int((19+round(0.5*(self.lvl-27)))*coeff[0]), "heal":int((40+round(2.5*(self.lvl-27)))*coeff[0]),
                    "defense":int((35+round(1.5*(self.lvl-27)))*coeff[0]), "aptDebuff":int((20+(self.lvl-27))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-27))*coeff[0]),
                    "crits":int((12+(self.lvl-27))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(90,110)}
        elif nb==4:
            self.health=int((265+19*(self.lvl-27))*coeff[0])
            stat = {"damage":int((155+2*(self.lvl-27))*coeff[0]), "dodge":int((14+round(0.5*(self.lvl-27)))*coeff[0]), "heal":int((20+round(2.5*(self.lvl-27)))*coeff[0]),
                    "defense":int((40+round(1.5*(self.lvl-27)))*coeff[0]), "aptDebuff":int((50+(self.lvl-27))*coeff[0]), "resistanceDebuff":int((50+(self.lvl-27))*coeff[0]),
                    "crits":int((12+(self.lvl-27))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(110,140)}
        elif nb==5:
            self.health=int((315+23*(self.lvl-37))*coeff[0])
            stat = {"damage":int((170+2*(self.lvl-37))*coeff[0]), "dodge":int((25+round(0.5*(self.lvl-37)))*coeff[0]), "heal":int((20+round(2.5*(self.lvl-37)))*coeff[0]),
                    "defense":int((65+round(1.5*(self.lvl-37)))*coeff[0]), "aptDebuff":int((20+(self.lvl-37))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-37))*coeff[0]),
                    "crits":int((5+(self.lvl-37))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(140,170)}
        elif nb==6:
            self.health=int((345+26*(self.lvl-47))*coeff[0])
            stat = {"damage":int((300+2*(self.lvl-47))*coeff[0]), "dodge":int((9+round(0.5*(self.lvl-47)))*coeff[0]), "heal":int((25+round(2.5*(self.lvl-47)))*coeff[0]),
                    "defense":int((65+round(1.5*(self.lvl-47)))*coeff[0]), "aptDebuff":int((20+(self.lvl-47))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-47))*coeff[0]),
                    "crits":int((17+(self.lvl-47))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(170,200)}
        elif nb==7:
            self.health=int((465+30*(self.lvl-57))*coeff[0])
            stat = {"damage":int((330+2*(self.lvl-57))*coeff[0]), "dodge":int((19+round(0.5*(self.lvl-57)))*coeff[0]), "heal":int((25+round(2.5*(self.lvl-57)))*coeff[0]),
                    "defense":int((165+round(1.5*(self.lvl-57)))*coeff[0]), "aptDebuff":int((20+(self.lvl-57))*coeff[0]), "resistanceDebuff":int((20+(self.lvl-57))*coeff[0]),
                    "crits":int((27+(self.lvl-57))*coeff[0]), "hp":self.health, "hpMax":self.health, "money" : randint(200,230)}
        return stat

    def getSkill(self):
        a=randint(0,100)
        if a <= 10 :
            skill=(60,0,"para",30,"Trivial")
        elif 10<a<=90:
            skill=(35,0,"",30,"CQFD")
        elif 90<a<=100:
            skill=(0,20,"",30,"Couché à 21h")
        return skill

    def textureName(self):
        return "majorant1_bg.png"


#ici aussi on ne va détailler que MonsieurG car c'est la même chose pour tous les boss
class MonsieurG(Monster):#informations de base sur le boss qui sont tirés de la classe "Monstre" que l'on a expliqué plus haut
    def __init__(self):
        Monster.__init__(self, 75, 50, 700000, {"damage":int(360*coeff[0]), "dodge":int(25*coeff[0]), "heal":int(40*coeff[0]), "defense":int(250*coeff[0]), "aptDebuff":int(50*coeff[0]),
                                                "resistanceDebuff":int(50*coeff[0]), "crits":int(35*coeff[0]), "hp":int(800*coeff[0]), "hpMax":int(800*coeff[0]), "money" : 10000},"MonsieurG", "Monsieur G")

    def getSkill(self):#Compétences du boss qui sont aléatoires avec une certaine probabilité, la puissance de l'attaque, la puissance de soin
    #l'effet particulier qui peut par exemple paralyser ou endormir le joueur, la vitesse de l'attaque (qui tape en premier dans les combats), puis le nom de l'attaque
        a=randint(0,100)
        if a < 1 :
            skill=(100000,0,"",100,"Redoublement")
        elif 0<a<=21:
            skill=(130,0,"dodo",40,"Cours de chimie")
        elif 21<a<=81:
            skill=(95,0,"",30,"Mail à 1h47")
        elif 81<a<=100:
            skill=(0,40,"",60,"Retard")
        return skill

    def dialogues(self, nb=0):#phrases que prononce le boss au début du combat (1), à la fin (2) et pendant(else)
        if nb==1:
            return "Excusez moi du retard, j'étais en rendez vous"
        if nb==2:
            return "Vous êtes à la chimie ce qu'Hanouna est à la télévision."
        else :
            a = randint(1,7)
            if a==1:
                return "On connait la technique, on arrivera toujours à vous coincer aux partiels"
            elif a==2:
                return "On ne vous demande pas de réinventer la poudre"
            elif a==3:
                return "Il faut aider nounours à trouver sa grotte"
            elif a==4:
                return "Les courants de Foucault ne vous permettront pas d'être millionnaire"
            elif a==5:
                return "Vous faites de l'espionnage industriel ?"
            elif a==6:
                return "C'est vrai que pour réfléchir il faut un cerveau"
            elif a==7:
                return "Vous êtes cons à bouffer du foin !"

    def textureName(self):
        return "GAGNEUR.png"


class Troulidra(Monster):
    def __init__(self):
        Monster.__init__(self, 60, 45, 70000, {"damage":int(360*coeff[0]), "dodge":int(25*coeff[0]), "heal":int(25*coeff[0]), "defense":int(200*coeff[0]), "aptDebuff":int(20*coeff[0]),
                                                "resistanceDebuff":int(20*coeff[0]), "crits":int(35*coeff[0]), "hp":int(500*coeff[0]), "hpMax":int(500*coeff[0]), "money" : 2500},"Troulidra", "Troulidra")

    def getSkill(self):
        a=randint(0,100)
        if a <= 25 :
            skill=(110,0,"para",100,"Résolution d'équa diff")
        elif 25<a<=80:
            skill=(65,0,"",50,"QCM")
        elif 80<a<=100:
            skill=(0,25,"",60,"Pause café")
        return skill

    def dialogues(self, nb=0):
        if nb==1:
            return "C'est moi le boss."
        if nb==2:
            return "Je vous laisse fermer derrière vous ?"
        else :
            a = randint(1,3)
            if a==1:
                return "Je vous parle de votre avenir et vous, vous jouez au shifumi"
            elif a==2:
                return "Pourquoi tu utilises une variable globale ? C'est les noobs qui font ça !"
            elif a==3:
                return "Alors, ça Pythonne ?"

    def textureName(self):
        return "TROULIDRA.png"

class Lamhoursse(Monster):
    def __init__(self):
        Monster.__init__(self, 50, 40, 38000, {"damage":int(330*coeff[0]), "dodge":int(15*coeff[0]), "heal":int(25*coeff[0]), "defense":int(100*coeff[0]), "aptDebuff":int(20*coeff[0]),
                                                "resistanceDebuff":int(20*coeff[0]), "crits":int(25*coeff[0]), "hp":int(380*coeff[0]), "hpMax":int(380*coeff[0]), "money" : 1800}, "Lamhoursse", "Lamhoursse")

    def getSkill(self):
        a=randint(0,100)
        if a <= 20 :
            skill=(110,0,"stun",100,"Ça dépend")
        elif 20<a<=80:
            skill=(65,0,"",40,"A démontrer")
        elif 80<a<=100:
            skill=(0,20,"",50,"Théorème de l'Hospital")
        return skill

    def dialogues(self, nb=0):
        if nb==1:
            return "Je vais te passer à la moulinette de l'exponentielle"
        if nb==2:
            return "Devoirs pour demain: un exposé sur la mort de Claude François"
        else :
            a = randint(1,8)
            if a==1:
                return "Il faut que lui et lui se touchent"
            elif a==2:
                return "Si je te dis 'Va à Saint-Germain-de-Calberte', tu sais pas où c'est"
            elif a==3:
                return "Mets un petit caillou dans ta chaussure"
            elif a==4:
                return "'Admis' ça veut pas dire 'non exigible en colle'"
            elif a==5:
                return "Le DL c'est comme l'arme atomique, c'est génial !"
            elif a==6:
                return "C'est depuis Tchernobyl qu'on est rigoureux en maths"
            elif a==7:
                return "C'est le bouquet final de la partie d'analyse en prépa"
            elif a==8:
                return "Quelqu'un aurait un boulon de diamètre 5mm, longueur 2cm ?"

    def textureName(self):
        return "LAMHOURSSE.png"

class Chastiere(Monster):
    def __init__(self):
        Monster.__init__(self, 40, 35, 12000, {"damage":int(200*coeff[0]), "dodge":int(30*coeff[0]), "heal":int(20*coeff[0]), "defense":int(100*coeff[0]), "aptDebuff":int(20*coeff[0]),
                                                "resistanceDebuff":int(20*coeff[0]), "crits":int(10*coeff[0]), "hp":int(350*coeff[0]), "hpMax":int(350*coeff[0]), "money" : 1100}, "Chastière", "Chastière")

    def getSkill(self):
        a=randint(0,100)
        if a <= 25 :
            skill=(90,0,"para",70,"Court circuit")
        elif 25<a<=80:
            skill=(50,0,"",80,"Théorème de Millman")
        elif 80<a<=100:
            skill=(0,20,"",70,"Au premier rang !")
        return skill

    def dialogues(self, nb=0):
        if nb==1:
            return "Priez le dieu de l'oscilloscope et de l'AO, ça marchera peut-être"
        if nb==2:
            return "Je sais c'est un peu bizarre, moi même j'essaye encore de comprendre..."
        else :
            a = randint(1,4)
            if a==1:
                return "Le prochain qui parle je le défonce, au sens littéral du terme"
            elif a==2:
                return "Vous avez déjà passé une échographie ?"
            elif a==3:
                return "Vous utilisez des résultats faux pour trouver des résultats justes"
            elif a==4:
                return "La saison des amours chez les écureuils, c'est quelque chose !"

    def textureName(self):
        return "CHASTIERE.png"

class Ballouerc(Monster):
    def __init__(self):
        Monster.__init__(self, 30, 30, 3000, {"damage":int(185*coeff[0]), "dodge":int(20*coeff[0]), "heal":int(20*coeff[0]), "defense":int(75*coeff[0]), "aptDebuff":int(50*coeff[0]),
                                                "resistanceDebuff":int(50*coeff[0]), "crits":int(20*coeff[0]), "hp":int(300*coeff[0]), "hpMax":int(300*coeff[0]), "money" : 800}, "Ballouerc", "Ballouerc")

    def getSkill(self):
        a=randint(0,100)
        if a <= 20 :
            skill=(90,0,"stun",40,"Tenseur cinématique")
        elif 20<a<=80:
            skill=(50,0,"",40,"Tenseur cinétique")
        elif 80<a<=100:
            skill=(0,30,"",40,"Tenseur mécanique")
        return skill

    def dialogues(self, nb=0):
        if nb==1:
            return "Comment on trouve le point G ? Avec de l'expérience."
        if nb==2:
            return "Tout à l'heure j'étais heureux, mais là je vais pleurer"
        else :
            a = randint(1,3)
            if a==1:
                return "Ça c'est facile"
            elif a==2:
                return "Ah mon collègue est en panique, je le laisse en panique"
            elif a==3:
                return "J'ai une bombe anti agression, et en plus ça nettoie"

    def textureName(self):
        return "BALLOUERC.png"

class Aronivet(Monster):
    def __init__(self):
        Monster.__init__(self, 30, 30, 3000, {"damage":int(160*coeff[0]), "dodge":int(25*coeff[0]), "heal":int(40*coeff[0]), "defense":int(75*coeff[0]), "aptDebuff":int(20*coeff[0]),
                                                "resistanceDebuff":int(20*coeff[0]), "crits":int(20*coeff[0]), "hp":int(350*coeff[0]), "hpMax":int(350*coeff[0]), "money" : 800}, "Aronivet", "Aronivet")

    def getSkill(self):
        a=randint(0,100)
        if a <= 20 :
            skill=(75,0,"poison",50,"Courbes IE")
        elif 20<a<=75:
            skill=(40,0,"",50,"Thermo")
        elif 75<a<=100:
            skill=(0,40,"",50,"Photosynthèse")
        return skill

    def dialogues(self, nb=0):
        if nb==1:
            return "On s'en balek de mon cours ! Hein, on s'en balek ?"
        if nb==2:
            return "Gardez votre dignité"
        else :
            a = randint(1,11)
            if a==1:
                return "Et là je fais genre que je connais la programmation Python"
            elif a==2:
                return "On ne panique pas devant le diagramme"
            elif a==3:
                return "Raconte pas ta vie, on s'en fout"
            elif a==4:
                return "Ça va aller chaton miaou miaou ?"
            elif a==5:
                return "Pour les handicapés comme..."
            elif a==6:
                return "Je suis une extrémiste de la nomenclature"
            elif a==7:
                return "On va pas se taper une chaise !"
            elif a==8:
                return "Bande de rebelles à 3 balles, un bon petit covid pour vous calmer"
            elif a==9:
                return "Et mémé elle sait pas nager, faut pas la jeter dans la piscine"
            elif a==10:
                return "J'espère qu'il n'y a pas d'Allemands dans la salle, ça sert à rien"
            elif a==11:
                return "Ah bah je savais pas qu'il y avait des autistes dans ma classe"

    def textureName(self):
        return "ARONIVET.png"

class Courcault(Monster):
    def __init__(self):
        Monster.__init__(self, 20, 25, 1500, {"damage":int(120*coeff[0]), "dodge":int(15*coeff[0]), "heal":int(20*coeff[0]), "defense":int(85*coeff[0]), "aptDebuff":int(20*coeff[0]),
                                                "resistanceDebuff":int(20*coeff[0]), "crits":int(20*coeff[0]), "hp":int(200*coeff[0]), "hpMax":int(200*coeff[0]), "money" : 500}, "Courcault", "Courcault")

    def getSkill(self):
        a=randint(0,100)
        if a <= 20 :
            skill=(65,0,"dodo",20,"Contemplations")
        elif 20<a<=80:
            skill=(35,0,"",20,"Dissertation")
        elif 80<a<=100:
            skill=(0,25,"",20,"Libretto")
        return skill

    def dialogues(self, nb=0):
        if nb==1:
            return "Pour être en marche il vaut mieux être debout"
        if nb==2:
            return "C'est pas trop ça mais au moins vous avez proposé quelque chose"
        else :
            a = randint(1,6)
            if a==1:
                return "On va dire que tout le monde est intelligent"
            elif a==2:
                return "Je t'aime comme un macdo"
            elif a==3:
                return "Ne me dite pas que vous êtes chinoise ?"
            elif a==4:
                return "Mais quelle est cette force de vivre qui me pousse à ne pas vous assassiner ?"
            elif a==5:
                return "La cave de ce théâtre c'est comme un utérus"
            elif a==6:
                return "Tchernobyl c'est un complot pedojuif"

    def textureName(self):
        return "COURCAULT.png"

class Bernausset(Monster):
    def __init__(self):
        Monster.__init__(self, 8, 20, 400, {"damage":int(50*coeff[0]), "dodge":int(10*coeff[0]), "heal":int(20*coeff[0]), "defense":int(20*coeff[0]), "aptDebuff":int(20*coeff[0]),
                                            "resistanceDebuff":int(20*coeff[0]), "crits":int(10*coeff[0]), "hp":int(100*coeff[0]), "hpMax":int(100*coeff[0]), "money" : 250}, "Bernausset", "Bernausset")

    def getSkill(self):
        a=randint(0,100)
        if a <= 25 :
            skill=(70,0,"poison",40,"Grammar sheet")
        elif 25<a<=80:
            skill=(45,0,"",50,"Press review")
        elif 80<a<=100:
            skill=(0,20,"",40,"Duolingo")
        return skill

    def dialogues(self, nb=0):
        if nb==1:
            return "Vous pouvez ouvrir la fenêtre ? Car vous puez"
        if nb==2:
            return "Je suis con mais pas à ce point"
        else :
            a = randint(1,6)
            if a==1:
                return "If Karens had guns, it would be the end of the world"
            elif a==2:
                return "Tu peux pas dire 'he have', c'est interdit par la loi"
            elif a==3:
                return "Cacaboudin is the future"
            elif a==4:
                return "Tout en moi est désirable"
            elif a==5:
                return "Pour dire putain il faut manger le cul"
            elif a==6:
                return "Merci messieurs mais je ne parlais pas de tournante dans la cave"

    def textureName(self):
        return "BERNAUSSET.png"

class Player():
    
    def __init__(self):
        pass
    
    def iniPlayer(self,globalObjects):
        self.spells = globalObjects[0]['ListeSort']

    def initPlayer(self, pDiff=1, dStats={"damage":25, "dodge":1, "heal":10, "defense":3, "aptDebuff":1, "resistanceDebuff":1, "crits":1, "hp":60, "hpMax":60},lSkills=(),lAchievements={},pClasse="Num",pXp=0,pMaxXp=100,pName="Jean Castex",pNiveauS="Sup",pLvl=1,pDepressed=0, pMoney=0):
        #informations de base sur le player (la difficulté, les stats,les compétences,les actions accomplies (pas eu le temps de s'en servir proprement),
        #la filière,les Xp,les Xp maximum,le nom,la classe,le level,la jauge de  dépression, l'argent) et on définit également la difficulté (coeff)
        self.name=pName
        self.classe=pClasse
        self.niveauS=pNiveauS
        self.lvl=pLvl
        self.skills=lSkills
        self.achievements=lAchievements
        self.xp=pXp
        self.maxXp=pMaxXp
        self.setStat(dStats)
        self.depressed=pDepressed
        self.maxDepressed=100
        self.statut = ""
        self.money=pMoney
        coeff[0]=pDiff

    def changeName(self, pNewName):#choisir un nouveau nom
        self.name=pNewName

    def addXp(self,nb):#doit être lancé à la fin de chaque combat ou évènement qui donne de l'xp
        if self.lvl<100:
            self.xp+= nb
        if self.xp>self.maxXp and self.lvl<=100:
            self.levelUp()
            # lvl_up.play() si jamais, pas eu le temps de gérer les bruitages
        if self.xp>self.maxXp and self.lvl>=100:
            self.xp = self.maxXp

    def levelUp(self): #définit ce qu'il se passe lors d'un level up
        while self.xp>=self.maxXp and self.lvl<100:
            self.xp-=self.maxXp
            self.maxXp=int(self.maxXp*1.1)
            self.lvl+=1
            self.spells.AjoutSortAppris(self.lvl)
            if self.classe=="Num":
                self.hpMax+=5
                self.hp+=5
                if self.hp>=self.hpMax:
                    self.hp=self.hpMax
                self.damage +=5             #flat
                if self.dodge<=35:#%
                    self.dodge=round(self.dodge+0.2,2)
                    if self.dodge>=35:
                        self.dodge=35
                self.heal +=3               #flat
                self.defense +=3            #flat
                if self.aptDebuff<=75:
                    self.aptDebuff = round(self.aptDebuff+0.5,2)
                    if self.aptDebuff>=75:
                        self.aptDebuff=75#%
                if self.resistanceDebuff<=75:
                    self.resistanceDebuff = round(self.resistanceDebuff+0.5,2)
                    if self.resistanceDebuff>=75:
                        self.resistanceDebuff=75#%
                if self.crits<=40:
                    self.crits=round(self.crits+0.3,2)
                    if self.crits>=40:
                        self.crits=40#%
            else :
                self.hpMax+=7
                self.hp+=7
                if self.hp>=self.hpMax:
                    self.hp=self.hpMax
                self.damage +=3
                if self.dodge<=35:
                    self.dodge = round(self.dodge+0.25,2)
                    if self.dodge>=35:
                        self.dodge=35
                self.heal +=10
                self.defense +=5
                if self.aptDebuff<=75:
                    self.aptDebuff = round(self.aptDebuff+0.5,2)
                    if self.aptDebuff>=75:
                        self.aptDebuff=75
                if self.resistanceDebuff<=75:
                    self.resistanceDebuff = round(self.resistanceDebuff+0.5,2)
                    if self.resistanceDebuff>=75:
                        self.resistanceDebuff=75
                if self.crits<=40 :
                    self.crits = round(self.crits+0.2,2)
                    if self.crits>=40:
                        self.crits=40
            if self.niveauS=="Sup":
                if self.lvl>=20:
                    self.niveauS="Spe"
                    if self.classe=="Num":
                        self.damage = round(self.damage*1.3,2)
                        self.dodge = round(self.dodge*1.1,2)
                        if self.dodge>=35:
                            self.dodge=35
                        self.heal = round(self.heal*1.1,2)
                        self.defense = round(self.defense*1.1,2)
                        self.aptDebuff =round(self.aptDebuff* 1.1)
                        if self.aptDebuff>=75:
                            self.aptDebuff=75
                        self.resistanceDebuff =round(self.resistanceDebuff*1.1)
                        if self.resistanceDebuff>=75:
                            self.resistanceDebuff=75
                        self.crits = round(self.crits*1.3)
                        if self.crits>=40:
                            self.crits=40
                    else :
                        print(self.classe)
                        self.damage = round(self.damage*1.3)
                        self.dodge = round(self.dodge*1.1)
                        if self.dodge>=35:
                            self.dodge=35
                        self.heal = round(self.heal*1.1)
                        self.defense = round(self.defense*1.1)
                        self.aptDebuff = round(self.aptDebuff*1.1)
                        if self.aptDebuff>=75:
                            self.aptDebuff=75
                        self.resistanceDebuff = round(self.resistanceDebuff*1.1)
                        if self.resistanceDebuff>=75:
                            self.resistanceDebuff=75
                        self.crits = round(self.crits* 1.2)
                        if self.crits>=40:
                            self.crits=40

        if self.lvl>100:
            self.lvl=100

    def setStat(self,stat):#définit les stats de base du joueur
        self.damage = stat["damage"]
        self.dodge = stat["dodge"]
        self.heal = stat["heal"]
        self.defense = stat["defense"]
        self.aptDebuff = stat["aptDebuff"]
        self.resistanceDebuff = stat["resistanceDebuff"]
        self.crits = stat["crits"]
        self.hp = stat["hp"]
        self.hpMax = stat["hpMax"]

    def savePlayer(self):#faire une sauvegarde des informations du player
        return {"difficulty": coeff[0], "stats" : {"damage":self.damage, "dodge":self.dodge, "heal":self.heal, "defense":self.defense, "aptDebuff":self.aptDebuff, "resistanceDebuff":self.resistanceDebuff, "crits":self.crits, "hp":self.hp, "hpMax":self.hpMax},
                "skills" : self.skills, "achievements" : self.achievements, "classe" : self.classe, "xp" : self.xp, "maxXp" : self.maxXp, "name" : self.name, "niveauS" : self.niveauS,
                "lvl" : self.lvl, "depressed" : self.depressed, "money" : self.money}

    def statCombat(self):#stat temporaires qui vont être modifiées au cours du combat en fonction des attaques lancées et reçues
        #et revenir à ce qu'elles étaient une fois le combat terminé
        self.damageTemp=self.damage
        self.dodgeTemp=self.dodge
        self.healTemp=self.heal
        self.defenseTemp=self.defense
        self.aptDebuffTemp=self.aptDebuff
        self.resistanceDebuffTemp=self.resistanceDebuff
        self.critsTemp=self.crits

    def addHp(self,nb):#Remonte les points de vie du personnage
        a=self.hpMax-self.hp
        self.hp += int(nb*(self.heal+100)/100)
        if self.hp>self.hpMax:
            self.hp = self.hpMax
            return a
        return int(nb*(self.heal+100)/400)

    def addHpC(self,nb):#Remonte les points de vie du personnage pendant le combat
        a=self.hpMax-self.hp
        self.hp +=int(nb*(self.heal+100)/100)
        if self.hp>self.hpMax:
            self.hp = self.hpMax
            return a
        return int(nb*(self.healTemp+100)/400)

    def removeHp(self,nb):#enlève des points de vie au personnage (uniquement possible pendant les combats)
        a=self.hp
        self.hp -= int(nb)
        if self.hp <= 0:
            self.hp=0
            return a
        return int(nb)

    def death(self): #Mort gérée ailleurs, juste au cas où
        self.hp = self.hpMax

    def modDepressed(self,nb):#jauge de dépression qui baisse au  fur et à mesure qu'on avance dans le temps et que l'on combat,
    #mais on peut la faire remonter (Sauf qu'on a pas eu le temps de gérer ça)
        self.depressed+=nb
        if self.depressed>=self.maxDepressed:
            self.depressed = self.maxDepressed
        if self.depressed<=0:
            self.depressed=0
