import pyglet
import math
import random
from pyglet.window import mouse
from pyglet.window import key
from pyglet.gl import *
import combatDos.Utils as Utils
import combatDos.ILabel as ILabel
import combatDos.combatButtons as combatButtons

class Combat():
    def __init__(self):
        pass
    
    def iniCombat(self, globalVariables, globalObjects):#initialise le combat
        
        self.globalvar = globalVariables
        self.player = globalObjects[0]['Player']
        self.window = globalObjects[0]['Window']
        self.msgs = []
        self.start = False
        self.end = False
        self.inventaire= globalObjects[0]['Inventaire']


    def getMenu(self, pObjMenu):
        self.menu=pObjMenu


    def startCombat(self,enemy,competences,sex):# lance le combat

        self.msgs.clear()
        self.player.statCombat()
        self.competences = competences # liste de competence
        ##une competance possede une liste [[target;statcible;value]...]"""
        self.enemy = enemy
        self.msgs.append(self.enemy.dialogues(1))
        ##self.enemy.dialogue(.)  #dialogue de début de combat""
        if sex == "M":
            self.sex = "M"
        else:
            self.sex = "Mme"
        self.initTextures()
        self.start = True
        self.end = False
        self.depression = 0
        self.clickC = False

    def calcul(self,lvlPlayer,attack,defense,puissance,C1=1,C2=1):  #calcul brut des dégats
        R = int(math.floor((random.randint(217,255)*100)/255))
        degat = math.floor((((((((lvlPlayer*2/5)+2)*puissance*attack/50)/(defense+1))*C1)+2)*C2*R/100))
        return int(degat)

    def applyDmg(self,num): #vérifie les éffets de statues avant d'appliquer la compétence
        if self.player.statut == "para":
            R = random.randint(0,1)

        elif self.player.statut == "dodo":
            R = random.randint(0,2)
            if self.player.statut== "dodo" and R == 0:
                self.player.statut=""
                self.addDialogue("Vous vous réveillez",1)

        elif self.player.statut=="stun":
            R=1
        else:
            R=0
        if R == 0:
            self.attack(num)
        else:
            self.addDialogue("Vous ne pouvez pas attaquer",1)
        if self.player.statut=="stun":
            self.player.statut = ""

    def attack(self,num):   #applique la compétence en prenant en compte les taux de critique, esquive et précision et effets de statut
        R = random.randint(0,100)
        D = random.randint(0,100)

        for index,i in enumerate(self.competences[num].ListStatCible):
            if index >= 1:
                self.addDialogue("Encore...",1)
            if i[0] == "player":
                if i[1]=="vie" and i[2]>0:
                    montant = self.player.addHp(i[2])
                    self.addDialogue("Vous vous soignez de "+str(montant),1)
                if i[1]=="vie" and i[2]<0:
                    montant = self.player.removeHp(-i[2])
                    self.addDialogue("Vous perdez "+str(montant)+" hp",1)

                if i[1]=='attaque' and i[2]>0:
                    self.player.damageTemp += i[2]*self.player.damageTemp/100     #influe sur la stat damage temp
                    self.addDialogue("Vous augmentez votre attaque",1)
                if i[1]=='attaque' and i[2]<0:
                    if self.player.damageTemp>i[2]*self.player.damageTemp/100:
                        self.player.damageTemp += i[2]*self.player.damageTemp/100
                        self.addDialogue("Vous diminuez votre attaque",1)
                    else:
                        self.player.damageTemp = 0
                        self.addDialogue("Vous diminuez votre attaque",1)

                if i[1]=='esquive' and i[2]>0:
                    self.player.dodgeTemp += i[2]*self.player.dodgeTemp/100    #influe sur la stat temp
                    self.addDialogue("Vous augmentez votre esquive",1)
                if i[1]=='esquive' and i[2]<0:
                    if self.player.dodgeTemp>i[2]*self.player.dodgeTemp/100:
                        self.player.dodgeTemp += i[2]*self.player.dodgeTemp/100
                        self.addDialogue("Vous diminuez votre esquive",1)
                    else:
                        self.player.dodgeTemp = 0
                        self.addDialogue("Vous diminuez votre esquive",1)

                if i[1]=='defense' and i[2]>0:
                    self.player.defenseTemp += i[2]*self.player.defenseTemp/100    #influe sur la stat temp
                    self.addDialogue("Vous augmentez votre defense",1)
                if i[1]=='defense' and i[2]<0:
                    if self.player.defenseTemp>i[2]*self.player.defenseTemp/100:
                        self.player.defenseTemp += i[2]*self.player.defenseTemp/100
                        self.addDialogue("Vous diminuez votre defense",1)
                    else:
                        self.player.defenseTemp = 0
                        self.addDialogue("Vous diminuez votre defense",1)

                if i[1]=='critique'and i[2]>0:
                    self.player.critsTemp += i[2]*self.player.critsTemp/100   #influe sur la stat temp
                    self.addDialogue("Vous augmentez votre taux critique",1)
                if i[1]=='critique'and i[2]<0:
                    if self.player.critsTemp>i[2]*self.player.critsTemp/100:
                        self.player.critseTemp += i[2]*self.player.critsTemp/100
                        self.addDialogue("Vous diminuez votre defense",1)
                    else:
                        self.player.defenseTemp = 0
                        self.addDialogue("Vous diminuez votre defense",1)

                if i[1]=='para' and self.player.statut=='para':
                    self.player.statut=''
                    self.addDialogue("Vous n'êtes plus paralysé",1)

                if i[1]=='dodo' :
                    self.player.statut='dodo'
                    self.addDialogue("Vous vous endormez",1)

                if i[1]=='poison' and self.player.statut=='poison':
                    self.player.statut=''
                    self.addDialogue("Vous n'êtes plus empoisonné",1)

                if i[1]=='covid' and self.player.statut=='covid':
                    self.player.statut=''
                    self.addDialogue("Vous n'êtes plus covidé",1)



            if i[0] == 'enemy':
                if i[1]=='vie':
                    dmg = self.calcul(self.player.lvl,self.player.damageTemp,self.enemy.defense,i[2])
                    if D>self.enemy.dodge:
                        if R<=self.player.critsTemp:
                            if dmg*1.5 < self.enemy.hp:
                                montant = self.enemy.removeHp(dmg*1.5)
                                self.addDialogue("Coup critique",1)
                                self.addDialogue("Vous infligez "+str(montant)+" dégâts",1)
                            else:
                                montant = self.enemy.removeHp(dmg*1.5)
                                self.addDialogue("Coup critique",1)
                                self.addDialogue("Vous infligez "+str(montant)+" dégâts",1)
                        else:
                            if dmg < self.enemy.hp:
                                montant = self.enemy.removeHp(dmg)
                                self.addDialogue("Vous infligez "+str(montant)+" dégâts",1)
                            elif dmg >= self.enemy.hp:
                                montant = self.enemy.removeHp(dmg)
                                self.addDialogue("Vous infligez "+ str(montant) +" dégâts",1)
                    else:
                        self.addDialogue(self.getMobNom()+" a esquivé",1)
                if i[1]=='attaque':
                    self.enemy.damage -= i[2]*self.enemy.damage/100
                    self.addDialogue("L'attaque de "+self.getMobNom()+" diminue",1)
                if i[1]=='esquive':
                    self.enemy.dodge -= i[2]*self.enemy.dodge/100
                    self.addDialogue("L'esquive de "+self.getMobNom()+" diminue",1)
                if i[1]=='defense':
                    self.enemy.defense -= i[2]*self.enemy.defense/100
                    self.addDialogue("La défense de "+self.getMobNom()+" diminue",1)
                if i[1]=='crits':
                    self.enemy.crits -= i[2]*self.enemy.crits/100
                    self.addDialogue("Le taux critique de "+self.getMobNom()+" diminue",1)
                if i[1]=='para' or i[1]=='dodo' or i[1]=='poison' or i[1]=='stun' or i[1]=='covid':
                    prec = random.randint(1,100)
                    if prec < 50+self.player.aptDebuffTemp:
                        self.enemy.statut = i[1]
                        self.addDialogue(self.getMobNom()+" subit l'effet "+i[1],1)

        if self.player.statut =="poison":
            self.player.removeHp(int(0.05*self.player.hpMax))
            self.addDialogue("Vous subissez des dégâts du poison",1)

        if self.player.statut =="covid":
            self.player.removeHp(int(0.10*self.player.hpMax))
            self.addDialogue("Vous souffrez du covid",1)

    def monsterattack(self,skill=[0,0,'',0]):   # applique la compétence ennemie

        C = random.randint(0,100)
        E = random.randint(0,100)
        Precision = random.randint(0,100)
        if self.enemy.statut == "para":
            R = random.randint(0,1)

        elif self.enemy.statut == "dodo":
            R = random.randint(0,4)
            if self.enemy.statut== "dodo" and R == 0:
                self.enemy.statut=""
                self.addDialogue(self.getMobNom()+" se réveille ",1)
        elif self.enemy.statut =="poison":
            self.enemy.removeHp(int(0.05*self.enemy.hpMax))
            self.addDialogue(self.getMobNom()+" est blessé par le poison",1)
            R =0
        elif self.enemy.statut=='Covid':
            self.enemy.removeHp(int(0.10*self.enemy.hpMax))
            self.addDialogue(self.getMobNom()+" est blessé par le Covid",1)
            R =0
        elif self.enemy.statut=="stun":
            R =1
            self.enemy.statut=""
            self.addDialogue(self.getMobNom()+" ne peut pas attaquer",1)
        else:
            R=0

        if self.enemy.statut =="":
            if R == 0:
                if E>self.player.dodgeTemp:
                    if C<=self.enemy.crits:
                        if skill[0]!=0:
                            montant = self.player.removeHp(1.5*self.calcul(self.enemy.lvl,self.enemy.damage,self.player.defenseTemp,skill[0]))
                            self.addDialogue("Coup critique!",1)
                            self.addDialogue(self.getMobNom()+" vous inflige " + str(montant) ,1)
                        if skill[1]!=0:
                            montant = self.enemy.addHp(skill[1]*1.5)
                            self.addDialogue(self.getMobNom()+" se soigne de " + str(montant) ,1)
                        if skill[2]!="":
                            if Precision>40+self.player.resistanceDebuffTemp:
                                self.player.statut = skill[2]
                                self.addDialogue("Vous subissez l'effet "+self.player.statut,1)
                            else:
                                self.addDialogue("Vous avez résisté à l'effet "+skill[2])
                    else:
                        if skill[0]!=0:
                            montant = self.player.removeHp(self.calcul(self.enemy.lvl,self.enemy.damage,self.player.defenseTemp,skill[0]))
                            self.addDialogue(self.getMobNom()+" vous inflige " + str(montant),1)
                        if skill[1]!=0:
                            montant = self.enemy.addHp(skill[1])
                            self.addDialogue(self.getMobNom()+" se soigne de " + str(montant) ,1)
                        if skill[2]!="":
                            if Precision>40+self.player.resistanceDebuffTemp:
                                self.player.statut = skill[2]
                                self.addDialogue("Vous subissez l'effet "+self.player.statut,1)
                            else:
                                self.addDialogue("Vous avez résisté à l'effet "+skill[2])
                else:
                    if skill[1]!=0:
                        if C<=self.enemy.crits:
                            montant = self.enemy.addHp(skill[1]*1.5)
                            self.addDialogue(self.getMobNom()+" se soigne de " + str(montant) ,1)
                            if Precision>40+self.player.resistanceDebuffTemp:
                                self.player.statut = skill[2]
                                self.addDialogue("Vous subissez l'effet "+self.player.statut,1)
                            else:
                                self.addDialogue("Vous avez résisté à l'effet "+skill[2])
                        else:
                            montant = self.enemy.addHp(skill[1])
                            self.addDialogue(self.getMobNom()+" se soigne de " + str(montant) ,1)
                            if Precision>40+self.player.resistanceDebuffTemp:
                                self.player.statut = skill[2]
                                self.addDialogue("Vous subissez l'effet "+self.player.statut,1)
                            else:
                                self.addDialogue("Vous avez résisté à l'effet "+skill[2])
                    else:
                        self.addDialogue("Vous avez esquivé l'attaque" ,1)
            else:
                self.addDialogue(self.getMobNom()+" ne peux pas attaquer",1)
        if self.enemy.statut != "":
            if R == 0:
                if E>self.player.dodgeTemp:
                    if C<=self.enemy.crits:
                        if skill[0]!=0:
                            montant = self.player.removeHp(1.5*self.calcul(self.enemy.lvl,self.enemy.damage,self.player.defenseTemp,skill[0]))
                            self.addDialogue("Coup critique",1)
                            self.addDialogue(self.getMobNom()+" vous inflige " + str(montant),1)
                        if skill[1]!=0:
                            montant = self.enemy.addHp(skill[1]*self.enemy.heal)
                            self.addDialogue(self.getMobNom()+" se soigne de " + str(montant) ,1)
                        if skill[2]!="":
                            if Precision>40+self.player.resistanceDebuffTemp:
                                self.player.statut = skill[2]
                                self.addDialogue("Vous subissez l'effet "+self.player.statut,1)
                            else:
                                self.addDialogue("Vous avez résisté à l'effet "+skill[2])
                    else:
                        if skill[0]!=0:
                            montant = self.player.removeHp(self.calcul(self.enemy.lvl,self.enemy.damage,self.player.defenseTemp,skill[0]))
                            self.addDialogue(self.getMobNom()+" vous inflige " + str(montant),1)
                        if skill[1]!=0:
                            montant = self.enemy.addHp(skill[1]*self.enemy.heal)
                            self.addDialogue(self.getMobNom()+" se soigne de " + str(montant) ,1)
                        if skill[2]!="":
                            if Precision>40+self.player.resistanceDebuffTemp:
                                self.player.statut = skill[2]
                                self.addDialogue("Vous subissez l'effet "+self.player.statut,1)
                            else:
                                self.addDialogue("Vous avez résisté à l'effet "+skill[2])
                else:
                    self.addDialogue("Vous avez esquivé",1)
            else:
               self.addDialogue(self.getMobNom()+" ne peut pas attaquer",1)


    def dropxp(self):   # ajoute l'expérience obtenue
        self.player.addXp(self.enemy.giveXp)
        self.addDialogue("Vous avez gagné " + str(self.enemy.giveXp) + " xp.")

    def dropmoney(self):    # ajoute l'argent obtenue
        self.player.money += self.enemy.money
        self.addDialogue("Vous avez gagné "+str(self.enemy.money)+ " prepacoins.")

    def dropitems(self): # ajoute les items en fonction de l'enemi
        if self.enemy.type =="Troulidra":
            self.inventaire.Ajouter('13',self.enemy.drop)
            self.addDialogue("Vous avez gagné "+str(self.enemy.drop)+" circuits imprimés",1)
        elif self.enemy.type =="Lamhoursse":
            self.inventaire.Ajouter('07',self.enemy.drop)
            self.addDialogue("Vous avez gagné "+str(self.enemy.drop)+" formules",1)
        elif self.enemy.type =="Chastière":
            self.inventaire.Ajouter('08',self.enemy.drop)
            self.addDialogue("Vous avez gagné "+str(self.enemy.drop)+" fils électriques",1)
        elif self.enemy.type =="Ballouerc":
            self.inventaire.Ajouter('10',self.enemy.drop)
            self.addDialogue("Vous avez gagné "+str(self.enemy.drop)+" engrenages",1)
        elif self.enemy.type =="Aronivet":
            self.inventaire.Ajouter('09',self.enemy.drop)
            self.addDialogue("Vous avez gagné "+str(self.enemy.drop)+" éléments",1)
        elif self.enemy.type =="Courcault":
            self.inventaire.Ajouter('11',self.enemy.drop)
            self.addDialogue("Vous avez gagné "+str(self.enemy.drop)+" pages",1)
        elif self.enemy.type =="Bernausset":
            self.inventaire.Ajouter('12',self.enemy.drop)
            self.addDialogue("Vous avez gagné "+str(self.enemy.drop)+" poils de moustache",1)
        elif self.enemy.type =="MonsieurG":
            self.inventaire.Ajouter('07',self.enemy.drop)
            self.addDialogue("Vous avez gagné "+str(self.enemy.drop)+" formules",1)
        else:
            if self.enemy.zone==1:
                self.inventaire.Ajouter('12',self.enemy.drop)
                self.addDialogue("Vous avez gagné "+str(self.enemy.drop)+" poils de moustache",1)
            elif self.enemy.zone==2:
                self.inventaire.Ajouter('11',self.enemy.drop)
                self.addDialogue("Vous avez gagné "+str(self.enemy.drop)+" pages",1)
            elif self.enemy.zone==3:
                self.inventaire.Ajouter('09',self.enemy.drop)
                self.addDialogue("Vous avez gagné "+str(self.enemy.drop)+" éléments",1)
            elif self.enemy.zone==4:
                self.inventaire.Ajouter('10',self.enemy.drop)
                self.addDialogue("Vous avez gagné "+str(self.enemy.drop)+" engrenages",1)
            elif self.enemy.zone==5:
                self.inventaire.Ajouter('08',self.enemy.drop)
                self.addDialogue("Vous avez gagné "+str(self.enemy.drop)+" fils electriques",1)
            elif self.enemy.zone==6:
                self.inventaire.Ajouter('07',self.enemy.drop)
                self.addDialogue("Vous avez gagné "+str(self.enemy.drop)+" formules",1)
            elif self.enemy.zone==7:
                self.inventaire.Ajouter('13',self.enemy.drop)
                self.addDialogue("Vous avez gagné "+str(self.enemy.drop)+" circuits imprimés",1)


    def enemySelectAttack(self):
        self.currentAttack = self.enemy.getSkill()

    def playerFirst(self,num):
        if self.competences[num].Vitesse >= self.currentAttack[2]:
            return True
        return False

    def attackpriority(self,num):
        if self.competences[num].Vitesse >= skill[2]:
            applyDmg(num)
            ##.dialogue()  # le joueur attaque en premier"""
            monsterattack(skill)
            self.enemy.dialogue() # le monstre attaque en deuxieme"""
        else:
            monsterattack(skill)
            self.enemy.dialogue() # le monstre attaque en premier"""
            self.applyDmg(num)

    def isFinish(self):
        return self.player.hp == 0 or self.enemy.hp == 0

    def realEnd(self):
        self.end = False
        self.start = False
        if self.player.hp == 0:
            print("0.00000")
            self.globalvar[0] = "Menu"
            self.globalvar[1] = "Title"
            self.menu.crtMenu = "Title"
            print('Player Death')
        else:
            self.globalvar[0] = "World"

    def finCombat(self):
        self.msgs.clear()
        if self.player.hp == 0:
            self.addDialogue("La prépa a eu raison de vous...")
            #self.addDialogue(":fonction:self.globalvar = [\"Menu\",\"Title\"]")
            #restart a la derniere save"""
        if self.enemy.hp == 0:
            self.enemy.death()
            self.addDialogue(self.enemy.dialogues(2))  #dialogue de fin de combat en cas de victoire"""
            self.dropxp()
            self.dropitems()
            self.dropmoney()
            a = random.randint(3,7)
            self.player.modDepressed(a)
            self.addDialogue("Vous déprimez de " + str(a))
            if self.enemy.type=="MonsieurG":
                self.menu.saveGame()
                self.menu.creditsRoll()

        self.addDialogue(":END:")
        self.end = True
        self.start = False


    def initTextures(self):
        combat = pyglet.image.load('combatDos/combat.png')
        battle = pyglet.image.load('combatDos/battle.png')
        backgroundImg = pyglet.image.load('resources/images/combatBg/'+self.sex+"/"+self.enemy.textureName())
        #combat = pyglet.image.load('33690.png')
        #sprite = pyglet.sprite.Sprite(combat.get_region(0,combat.height - 100 - 0,100, 100))
        self.background =   Utils.loadImage(self.window,img = backgroundImg,x = 0, y = 0, width = 1920,height = 1080)
        self.sprite =       Utils.loadImage(self.window,img = combat,x = 0, y = 0, width = 240,height = 48)
        self.sprite2 =      Utils.loadImage(self.window,img = combat,x = 240, y = 0, width = 120,height = 48)
        self.lifeBarMob =   Utils.loadImage(self.window,img = combat,x = 0, y = 48, width = 547,height = 76)
        self.vieMob =       Utils.loadImage(self.window,img = combat,x = 360, y = 0, width = 181,height = 22)
        self.vieMob2 =      Utils.loadImage(self.window,img = combat,x = 541, y = 0, width = 164,height = 22)

        self.lifeBar =  Utils.loadImage(self.window,img = combat,x = 0, y = 48, width = 547,height = 76)
        self.vie =      Utils.loadImage(self.window,img = combat,x = 360, y = 0, width = 181,height = 22)
        self.vie2 =     Utils.loadImage(self.window,img = combat,x = 541, y = 0, width = 164,height = 22)
        self.xp =       Utils.loadImage(self.window,img = combat,x = 973, y = 0, width = 1,height = 1)

        self.cbBts = combatButtons.CombatButtons(window=self.window,dialogueMode=True,competences = self.competences)

        self.label = ILabel.ILabel(self.window,text= "", font_size = 8,multiline = True,width = 300,height = 48,color = (255,255,255,255))
        self.lvl =   ILabel.ILabel(self.window,text= "Lv."+str(self.getLevel()), font_size = 3 ,multiline = True,width = 300,height = 48,color = (255,255,255,255))
        self.lvlMob = ILabel.ILabel(self.window,text= "Lv."+str(self.getMobLevel()), font_size = 3 ,multiline = True,width = 300,height = 48,color = (255,255,255,255))
        #nomMobLbl = ILabel.ILabel(self.window,text= str(getMobNom()), font_size = 7,font_name="SAO UI TT Regular" ,multiline = True,width = 300,height = 48,color = (255,255,255,255),anchor_x='center', anchor_y='center')

        self.nomMobLbl = Utils.loadImageButton(self.window,text=str(self.getMobNom()),img = combat,x = 973, y = 1 , width = 1,height = 1)
        self.nomMobLbl.label.color = (255,255,255,255)
        self.nomMobLbl.label.sizeModif= 1.5

        self.nomLbl = Utils.loadImageButton(self.window,text=str(self.getNom()),img = combat,x = 973, y = 1 , width = 1,height = 1)
        self.nomLbl.label.color = (255,255,255,255)
        self.nomLbl.label.sizeModif = 1.5

        self.lifeMobTexte = Utils.loadImageButton(self.window,text="0/0",img = combat,x = 973, y = 1 , width = 1,height = 1)
        self.lifeMobTexte.label.color = (255,255,255,255)
        self.lifeMobTexte.label.sizeModif = 1.5
        self.lifeTexte = Utils.loadImageButton(self.window,text="0/0",img = combat,x = 973, y = 1 , width = 1,height = 1)
        self.lifeTexte.label.color = (255,255,255,255)
        self.lifeTexte.label.sizeModif = 1.5


        self.background.setRelativePosition(0,0)
        self.background.setWindowRatio(100,100)

        self.label.setRelativePosition(7,18)
        self.label.setWindowRatio(93,17)
        self.sprite.setWindowRatio(100,25)
        self.sprite.setRelativePosition(0,0)
        self.sprite2.setWindowRatio(100,25)
        self.sprite2.setRelativePosition(0,0)
        #sprite3.setWindowRatio(25,20)
        self.lifeBarMob.setWindowRatio(50,12)
        self.lifeBarMob.setRelativePosition(0,87)
        self.vieMob.setWindowRatio(17.3,6)
        self.vieMob.setRelativePosition(15.5,91)
        self.vieMob2.setWindowRatio(14.3,6)
        self.vieMob2.setRelativePosition(32.8,91)
        self.lvlMob.setRelativePosition(45,90.5)
        self.nomMobLbl.setRelativePosition(47,90.5)

        self.nomMobLbl.setWindowRatio(12,6)
        self.nomMobLbl.setRelativePosition(3,91)
        self.lifeMobTexte.setWindowRatio(12,6)
        self.lifeMobTexte.setRelativePosition(32,86)

        self.lifeBar.setWindowRatio(50,12)
        self.lifeBar.setRelativePosition(0+50,87-60)
        self.vie.setWindowRatio(17.3,6)
        self.vie.setRelativePosition(15.5+50,91-60)
        self.vie2.setWindowRatio(14.3,6)
        self.vie2.setRelativePosition(32.8+50,91-60)
        self.lvl.setRelativePosition(45+50,90.5-60)

        self.nomLbl.setWindowRatio(12,6)
        self.nomLbl.setRelativePosition(3+50,91-60)
        self.lifeTexte.setWindowRatio(12,6)
        self.lifeTexte.setRelativePosition(32+50,86-60)

        self.xp.setWindowRatio(30,2)
        self.xp.setRelativePosition(15.5+37.3,91-63.3)

    def show(self):
        if self.start or self.end:
            self.background.show()
            pyglet.gl.glClearColor(255, 255, 255, 255)
            self.sprite.show()
            #print(label.height)
            #print(label.width)
            self.label.text = self.getCurrentText()
            if not self.isDialogue():
                self.sprite2.show()
                #label.content_height = 600
            ##vie.show()

            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            #vie.update()
            mobHealth = self.getMobHealtPourcent()
            health = self.getHealtPourcent()
            cMob = (255-(255*mobHealth/100),(255*mobHealth/100),0);

            c = (255-(255*health/100),(255*health/100),0);
            self.vieMob.color = cMob
            self.vieMob2.color = cMob
            self.vie.color = c
            self.vie2.color = c
            if mobHealth > 53:
                r = (14.3*(mobHealth-53))/47
                self.vieMob2.setWindowRatio(r,6)
                self.vieMob.setWindowRatio(17.3,6)
                self.vieMob2.show()
                self.vieMob.show()
            elif mobHealth != 0:
                r = (17.3*(mobHealth))/53
                self.vieMob.setWindowRatio(r,6)
                self.vieMob.show()


            if health > 53:
                r = (14.3*(health-53))/47
                self.vie2.setWindowRatio(r,6)
                self.vie.setWindowRatio(17.3,6)
                self.vie2.show()
                self.vie.show()
            elif health != 0:
                r = (17.3*(health))/53
                self.vie.setWindowRatio(r,6)
                self.vie.show()

            self.lifeBarMob.show()
            self.lifeBar.show()
            if self.player.lvl >= 100:
                self.xp.color = (169, 151, 18)
                self.xp.setWindowRatio(30,2)
            else:
                self.xp.color = (18, 133, 203)
                r = (30*(self.getXpPourcent()))/100
                self.xp.setWindowRatio(r,2)

            self.xp.show()

            if self.isDialogue():
                self.label.show()
            self.lvlMob.text = "Lv."+str(self.getMobLevel())
            self.lvlMob.show()
            self.lifeMobTexte.label.text = str(self.getMobHealt())+"/"+str(self.getMobMaxHealt())
            self.lifeMobTexte.show()
            self.lifeTexte.label.text = str(self.getHealt())+"/"+str(self.getMaxHealt())
            self.lifeTexte.show()

            self.lvl.text = "Lv."+str(self.getLevel())
            self.lvl.show()
            self.nomMobLbl.show()
            self.nomLbl.show()
            self.cbBts.show()

    def on_mouse_press(self,x, y, button, modifiers):
        if self.start or self.end:
            #print("x: " + str(x*100/window.width))
            #print("y: " + str(y*100/window.height))
            #cbBts.sprite.setRelativePosition(x*100/window.width,y*100/window.height)
            if button == mouse.LEFT:
                if y > self.window.height*0.25:
                    self.nextDialogue()
                if not self.clickC :
                    ret = self.cbBts.click(x,y)
                    if ret != None:
                        self.clickC = True
                        if ret == -1:
                            self.realEnd()
                            print("FUITTTTE")
                        else:
                            self.genereteMessages(ret)

    def on_mouse_motion(self,x, y, dx, dy):
        if self.start:
            self.cbBts.updateMouse(x,y)

    def getMobLevel(self):
        return self.enemy.lvl

    def getMobNom(self):
        nom = self.enemy.name
        if(len(nom)>12):
            nom = nom[0:12]
        return nom

    def getNom(self):
        nom = self.player.name
        if(len(nom)>12):
            nom = nom[0:12]
        return nom

    def getLevel(self):
        return self.player.lvl

    def getMobHealt(self):
        return self.enemy.hp

    def getMobMaxHealt(self):
        return self.enemy.hpMax

    def getMobHealtPourcent(self):
        return self.getMobHealt()*100/self.getMobMaxHealt()

    def getHealt(self):
        return self.player.hp

    def getMaxHealt(self):
        return self.player.hpMax

    def getHealtPourcent(self):
        return self.getHealt()*100/self.getMaxHealt()

    def getXp(self):
        return self.player.xp

    def getMaxXp(self):
        return self.player.maxXp

    def getXpPourcent(self):
        return self.getXp()*100/self.getMaxXp()

    def isDialogue(self):
        return self.cbBts.dialogueMode

    def getTextToDraw(self):
        return self.textToDraw

    def getCurrentText(self):
        return self.msgs[0] if len(self.msgs) >=1 else "Mon texte par défault"

    def ma_fonction(self,a):
        self.health = self.health - a

    def heal(self,a):
        self.health = self.health + a

    def setDialogueMode(self,mode):
        self.cbBts.setDialogueMode(mode)

    def nextDialogue(self):
        if len(self.msgs) != 0:
            self.msgs.pop(0)
            if len(self.msgs) == 0:
                self.setDialogueMode(False)
                self.clickC = False
                self.end = True
            elif self.msgs[0].startswith(':fonction:'):
                msg = self.msgs[0]
                msg = msg.replace(":fonction:","")
                exec(msg)
                if len(self.msgs) == 0:
                    self.setDialogueMode(False)
                    self.clickC = False
                    self.end = True
                else:
                    self.nextDialogue()
            elif self.msgs[0].startswith(':END:'):
                self.realEnd()
            elif self.msgs[0].startswith(':NEXT:'):
                if self.isFinish():
                    self.finCombat()
                else:
                    if len(self.msgs) == 0:
                        self.setDialogueMode(False)
                        self.clickC = False
                        self.end = True
                    else:
                        self.nextDialogue()

    def addDialogue(self,message,index=-1):
        if index == -1:
            self.msgs.append(message)
        else:
            self.msgs.insert(1,message)

    def addExecFonction(self,fonction):
        self.msgs.append(":fonction:"+fonction)

    def genereteMessages(self,i):
        self.msgs.clear()
        self.setDialogueMode(True)
        self.enemySelectAttack()
        if self.playerFirst(i):
            self.addDialogue(str(self.player.name)+" utilise " + self.competences[i].Nom)
            self.addDialogue(":fonction:self.applyDmg("+str(i)+")")
            self.addDialogue(":NEXT:")
            self.addDialogue(":NEXT:")
            if random.randint(0,3) < 2:
                diagB = self.enemy.dialogues()
                if not diagB == "":
                    self.addDialogue(str(self.enemy.name)+": " + diagB)
            self.addDialogue(str(self.enemy.name)+" utilise "+ self.currentAttack[4])
            self.addDialogue(":fonction:self.monsterattack(self.currentAttack)")
            self.addDialogue(":NEXT:")
            self.addDialogue(":NEXT:")
        else:
            if random.randint(0,3) < 2:
                diagB = self.enemy.dialogues()
                if not diagB == "":
                    self.addDialogue(str(self.enemy.name)+": " + diagB)
            self.addDialogue(str(self.enemy.name)+" utilise "+self.currentAttack[4])
            self.addDialogue(":fonction:self.monsterattack(self.currentAttack)")
            self.addDialogue(":NEXT:")
            self.addDialogue(":NEXT:")
            self.addDialogue(str(self.player.name)+" utilise "+ self.competences[i].Nom)
            self.addDialogue(":fonction:self.applyDmg("+str(i)+")")
            self.addDialogue(":NEXT:")
            self.addDialogue(":NEXT:")
