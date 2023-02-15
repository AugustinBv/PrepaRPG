from pyglet.window import key
import pyglet
import random
import entitees
from map import *


class Monde():
    def __init__(self):
        pass
    
    def iniMonde(self, globalVariables, globalObjects):
        #width, height, mode, combat, player
        width, height = globalObjects[0]['Window'].get_size()
        
        self.dialogue = [False]
        self.Dialogue = globalObjects[0]['Dialogue']
        self.Dialogue.getDialogueState(self.dialogue)
        
        #tous les parametres de la fenetre
        self.mode = globalVariables
        self.combat = globalObjects[0]['Combat']
        self.player = globalObjects[0]['Player']
        self.menu = globalObjects[0]['Menu']
        self.nbCaseVue = 16
        self.tileSize = 32

        self.clavier = {"z": False, "s": False, "q": False, "d": False}
        self.codeTriche = ""
        self.sprint = False
        self.Duree = 15

        self.onAnim = 0
        self.animFrame = 0
        self.direction = "B"
        self.vect = (0,1)

        self.pos = [-40,-16]
        self.mapActu = 0
        self.skinActu = "Mskin"
        
        print(width, height)
        self.resize(width, height)
        self.get_case()


    def updateSkin(self, path):
        self.loadJoueur("resources/images/monde/{}.png".format(path))
        self.skinActu = path

    def initSave(self, dico):
        if dico == 'M':
            self.updateSkin("Mskin")
            self.pos = [-43, -16]
            self.mapActu = 0
            self.sex = "M"
        elif dico == 'Mme':
            self.updateSkin("Fskin")
            self.sex = "Mme"
            self.pos = [-43, -16]
            self.mapActu = 0
        else:
            self.sex = dico.get("sex","M")
            self.updateSkin(dico.get("skinActu", "perso11"))
            self.pos = [dico.get("posX", -39), dico.get("posY", -16)]
            self.mapActu = dico.get("mapActu", 0)
        
        self.loadMonde(self.mapActu)
        self.update_pos()


    def forSave(self):
        return  {"posX": self.pos[0], "posY": self.pos[1], "mapActu": self.mapActu, "skinActu": self.skinActu, "sex": self.sex}


    def loadMonde(self, location):
        if location == 0:
            self.loadMonde1("resources/images/monde/M00.png")
            self.loadMonde2("resources/images/monde/M01.png")
            self.mapNum = mapNum0

        elif location == 1:
            self.loadMonde1("resources/images/monde/M20.png")
            self.loadMonde2("resources/images/monde/M21.png")
            self.mapNum = mapNum1

        elif location == 2:
            #self.pos = [-4,-18]
            self.loadMonde1("resources/images/monde/M30.png")
            self.loadMonde2("resources/images/monde/M31.png")
            self.mapNum = mapNumL
    
    def resize(self, width, height):
        self.fenW = width
        self.fenH = height
        self.scale = self.fenW/(self.nbCaseVue*self.tileSize)
        self.sclTileSize = self.tileSize*self.scale
        
        self.Dialogue.resize(self.scale)
        
        self.loadMonde(self.mapActu)
        self.updateSkin(self.skinActu)
        self.update_pos()


    """
    methode qui permet l'affichage
    """
    def afficher(self):
        if self.mode[0] == "World" or self.mode==['Menu','Pause']:
            self.map1.draw()
            self.joueurBas.draw()
            self.map2.draw()
            self.joueurHaut.draw()
            
        if self.dialogue[0] == True and self.mode[0] == "World":
            self.Dialogue.draw()

    """
    methode qui se fait appeler toutes les 0.02 seconde (50 fois par seconde)
    """
    def tack(self):
        if self.mode[0] == "World":
            if self.onAnim != 0:
                self.anim()

    """
    methode qui determine si le deplacement est autoriser
    """
    def canMove(self):
        #print("{} to {}".format(self.get_case(), self.get_case(self.vect)))
        deux = [2,"a","b","c","d","e","f","g"]
        if self.get_case() == 1:
            if self.get_case(self.vect)==1:
                return True
            elif self.get_case(self.vect) in deux and self.vect != (0,-1) :
                return True
            elif self.get_case(self.vect)==4 and self.vect != (1,0) :
                return True

        if self.get_case() in deux:
            if self.get_case(self.vect)==1 and self.vect != (0,1):
                return True
            elif self.get_case(self.vect) in deux and self.vect != (0,-1) and self.vect != (0,1):
                return True
            elif self.get_case(self.vect)==4 and self.vect != (1,0) and self.vect != (0,1):
                return True

        if self.get_case() == 4:
            if self.get_case(self.vect)==1 and self.vect != (1,0):
                return True
            elif self.get_case(self.vect) in deux and self.vect != (0,-1) and self.vect != (-1,0) :
                return True
            elif self.get_case(self.vect)==4 and self.vect != (1,0) and self.vect != (-1,0):
                return True

    """
    methode qui renvoie l'info sur la case actuelle
    """
    def get_case(self, vect = (0,0)):
        x = -self.pos[0] - vect[0]
        y = len(self.mapNum)-2 + self.pos[1] + vect[1]
        return self.mapNum[y][x]

    """
    methode qui lance les modes
    """
    def startEvent(self):
        rnd =random.randint(0,100)
        if rnd > 60:
            if self.get_case() == "a":
                return self.randomMob(1)
            elif self.get_case() == "b":
                return self.randomMob(2)
            elif self.get_case() == "c":
                return self.randomMob(3)
            elif self.get_case() == "d":
                return self.randomMob(4)
            elif self.get_case() == "e":
                return self.randomMob(5)
            elif self.get_case() == "f":
                return self.randomMob(6)
            elif self.get_case() == "g":
                return self.randomMob(7)
            else:
                return False
        return False

    def randomMob(self, zone): #zone de 1 a 7
        rnd = random.randint(0,100)
        cp = self.menu.getSkillFromID(self.player.skills)
        if self.player.hp > 0:
            if rnd > 80:
                self.mode[0] = "fight" #on passe en mode combat
                self.mode[1] = "normal"
                self.combat.startCombat(entitees.Majorant(zone),cp,self.sex)
            elif rnd > 45:
                self.mode[0] = "fight" #on passe en mode combat
                self.mode[1] = "normal"
                self.combat.startCombat(entitees.ModulesOk(zone),cp,self.sex)
            else:
                self.mode[0] = "fight" #on passe en mode combat
                self.mode[1] = "normal"
                self.combat.startCombat(entitees.Minorant(zone),cp,self.sex)
            return True

    def clicEntre(self):
        #print(self.get_case(self.vect))
        if self.get_case(self.vect) == "s":
            self.Dialogue.addDialogue('Regardons plus précisément tes moyennes...',
                                      'self.menu.openSkillsEquipement()')
            
        if self.get_case(self.vect) == "t":
            self.Dialogue.addDialogue('Bienvenue à la boutique !',
                                      'self.menu.openCompTrade()')
            
        if self.get_case(self.vect) == "r":
            #self.player.addHp(self.player.hpMax)
            
            self.Dialogue.addDialogue(['Tu as été soigné','Fais attention la prochaine fois'],
                                      'self.player.addHp(self.player.hpMax)')
        
        
        if self.get_case(self.vect) == "h":
            print(self.pos)
            if self.mapActu == 0:
                self.mapActu = 1
                self.pos = [-45,-30]
                self.loadMonde(self.mapActu)
                self.update_pos()

            elif self.mapActu == 1:
                self.mapActu = 0
                self.pos = [-47,-26]
                self.loadMonde(self.mapActu)
                self.update_pos()

        if self.get_case(self.vect) == "i":
            print(self.pos)
            if self.mapActu == 0:
                self.mapActu = 1
                self.pos = [-18,-56]
                self.loadMonde(self.mapActu)
                self.update_pos()

            elif self.mapActu == 1:
                self.mapActu = 0
                self.pos = [-20,-52]
                self.loadMonde(self.mapActu)
                self.update_pos()

        #boss
        cp = self.menu.getSkillFromID(self.player.skills)
        if self.player.hp > 0:
            if self.get_case(self.vect) == "z":
                self.mode[0] = "fight" #on passe en mode combat
                self.mode[1] = "boss"
                self.combat.startCombat(entitees.Bernausset(),cp,self.sex)
    
            if self.get_case(self.vect) == "y":
                self.mode[0] = "fight" #on passe en mode combat
                self.mode[1] = "boss"
                self.combat.startCombat(entitees.Courcault(),cp,self.sex)
    
            if self.get_case(self.vect) == "x":
                self.mode[0] = "fight" #on passe en mode combat
                self.mode[1] = "boss"
                self.combat.startCombat(entitees.Aronivet(),cp,self.sex)
    
            if self.get_case(self.vect) == "w":
                self.mode[0] = "fight" #on passe en mode combat
                self.mode[1] = "boss"
                self.combat.startCombat(entitees.Ballouerc(),cp,self.sex)
    
            if self.get_case(self.vect) == "v":
                self.mode[0] = "fight" #on passe en mode combat
                self.mode[1] = "boss"
                self.combat.startCombat(entitees.Chastiere(),cp,self.sex)
    
            if self.get_case(self.vect) == "u":
                self.mode[0] = "fight" #on passe en mode combat
                self.mode[1] = "boss"
                self.combat.startCombat(entitees.Lamhoursse(),cp,self.sex)
    
            if self.get_case(self.vect) == "j":
                self.mode[0] = "fight" #on passe en mode combat
                self.mode[1] = "boss"
                self.combat.startCombat(entitees.Troulidra(),cp,self.sex)
    
            if self.get_case(self.vect) == "k":
                self.mode[0] = "fight" #on passe en mode combat
                self.mode[1] = "final"
                self.combat.startCombat(entitees.MonsieurG(),cp,self.sex)

    """
    methode qui lance l'anim de deplacement
    """
    def anim(self):
        nbAnim = len(self.imgJBas[self.direction]) #le nb d'image dans l'anim

        self.onAnim += 1
        if self.onAnim > self.Duree:
            self.onAnim = 0

        if self.onAnim != 0:
            for i in range(nbAnim):
                if self.onAnim >= i*(self.Duree/nbAnim) and self.onAnim <= (i+1)*(self.Duree/nbAnim):
                    delta = self.sclTileSize*self.onAnim/self.Duree
                    self.update_pos(i, delta)
        else:
            self.pos[0] += self.vect[0]
            self.pos[1] += self.vect[1]
            self.update_pos()
            if not self.startEvent():
                for val in self.clavier.values():
                    if val != False:
                        self.key_press(val)

    """
    methode qui modifie la position et l'image du personage
    """
    def update_pos(self, animFrame = 0, delta = 0):
        self.animFrame = animFrame
        self.joueurHaut.image = self.imgJHaut[self.direction][self.animFrame]
        self.joueurBas.image = self.imgJBas[self.direction][self.animFrame]
        self.map1.x = (self.fenW-self.tileSize)//2+self.pos[0]*self.scale*self.tileSize+delta*self.vect[0]
        self.map1.y = (self.fenH-self.tileSize)//2+self.pos[1]*self.scale*self.tileSize+delta*self.vect[1]
        self.map2.x = (self.fenW-self.tileSize)//2+self.pos[0]*self.scale*self.tileSize+delta*self.vect[0]
        self.map2.y = (self.fenH-self.tileSize)//2+self.pos[1]*self.scale*self.tileSize+delta*self.vect[1]

    """
    methode qui modifie les touche du clavier
    """
    def key_press(self, val, mod=0):
        if self.mode[0] == "World" and self.dialogue[0] == False:
            if val != key.LSHIFT:
                for i in self.clavier:
                    self.clavier[i] = False

            if val == key.LSHIFT:
                self.sprint = True

            elif val == key.ESCAPE:
                self.menu.openPauseMenu()
            elif val == key.RETURN:
                self.clicEntre()

            if val == key.NUM_0 :
                self.codeTriche += "0"
            elif val == key.NUM_1 :
                self.codeTriche += "1"
            elif val == key.NUM_2 :
                self.codeTriche += "2"
            elif val == key.NUM_3 :
                self.codeTriche += "3"
            elif val == key.NUM_4 :
                self.codeTriche += "4"
            elif val == key.NUM_5 :
                self.codeTriche += "5"
            elif val == key.NUM_6 :
                self.codeTriche += "6"
            elif val == key.NUM_7 :
                self.codeTriche += "8"
            elif val == key.NUM_9 :
                self.codeTriche += "9"

            elif val == key.NUM_DIVIDE :
                if self.codeTriche == "563214":
                    self.updateSkin("perso22")

                if self.codeTriche == "12":
                    self.player.money += 12000

                self.codeTriche = ""

            if val == key.UP or val == key.Z:
                self.clavier["z"] = key.UP
                if self.onAnim == 0:
                    self.vect = (0,-1)
                    self.direction = "H"
                    self.update_pos()
                    self.Duree = 15 if not self.sprint else 5
                    if self.canMove():
                        self.anim()
            if val == key.DOWN or val == key.S:
                self.clavier["s"] = key.DOWN
                if self.onAnim == 0:
                    self.vect = (0,1)
                    self.direction = "B"
                    self.update_pos()
                    self.Duree = 15 if not self.sprint else 5
                    if self.canMove():
                        self.anim()
            if val == key.LEFT or val == key.Q:
                self.clavier["q"] = key.LEFT
                if self.onAnim == 0:
                    self.vect = (1,0)
                    self.direction = "G"
                    self.update_pos()
                    self.Duree = 15 if not self.sprint else 5
                    if self.canMove():
                        self.anim()
            if val == key.RIGHT or val == key.D:
                self.clavier["d"] = key.RIGHT
                if self.onAnim == 0:
                    self.vect = (-1,0)
                    self.direction = "D"
                    self.update_pos()
                    self.Duree = 15 if not self.sprint else 5
                    if self.canMove():
                        self.anim()


    def key_release(self, val, mod):
        if self.mode[0] == "World":
            if val == key.LSHIFT:
                self.sprint = False
            if val == key.UP or val == key.Z:
                self.clavier["z"] = False
            if val == key.DOWN or val == key.S:
                self.clavier["s"] = False
            if val == key.LEFT or val == key.Q:
                self.clavier["q"] = False
            if val == key.RIGHT or val == key.D:
                self.clavier["d"] = False
    
    
    def on_mouse_press(self, x, y, button, modifiers):
        if self.mode[0] == "World" and self.dialogue[0] == True:
            self.Dialogue.nextDialogue()
            
        

    """
    methode qui charge les images
    """
    def loadMonde1(self, path):
        self.imgMap1 = pyglet.image.load(path).get_texture()
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
        self.imgMap1.height = int(self.imgMap1.height*self.scale)
        self.imgMap1.width = int(self.imgMap1.width*self.scale)
        self.map1 = pyglet.sprite.Sprite(self.imgMap1,x = -self.sclTileSize,y = -self.sclTileSize)
        self.map1.x += (self.fenW-self.tileSize)//2
        self.map1.y += (self.fenH-self.tileSize)//2

    def loadMonde2(self, path):
        self.imgMap2 = pyglet.image.load(path).get_texture()
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
        self.imgMap2.height = int(self.imgMap2.height*self.scale)
        self.imgMap2.width = int(self.imgMap2.width*self.scale)
        self.map2 = pyglet.sprite.Sprite(self.imgMap2,x = -self.sclTileSize,y = -self.sclTileSize)
        self.map2.x += (self.fenW-self.tileSize)//2
        self.map2.y += (self.fenH-self.tileSize)//2

    def loadJoueur(self, path):
        self.imgJ = pyglet.image.load(path).get_texture()
        self.imgJBas = {}
        self.imgJHaut = {}

        a = self.tileSize
        for y,direc,nbAnim in (((0,0),"G",5),((0,5),"D",5),((2,1),"B",4),((2,5),"H",4)):
            self.imgJBas[direc] = []
            self.imgJHaut[direc] = []
            for x in range(nbAnim):
                self.imgJBas[direc].append(self.imgJ.get_region(a*(y[1]+x), a*y[0], a, a))
                self.imgJHaut[direc].append(self.imgJ.get_region(a*(y[1]+x), a*(y[0]+1), a, a))

                pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)
                pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
                self.imgJBas[direc][-1].height *= self.scale
                self.imgJBas[direc][-1].width *= self.scale
                self.imgJHaut[direc][-1].height *= self.scale
                self.imgJHaut[direc][-1].width *= self.scale

        self.joueurBas = pyglet.sprite.Sprite(self.imgJBas["B"][0])
        self.joueurHaut = pyglet.sprite.Sprite(self.imgJHaut["B"][0],y = self.sclTileSize)
        self.joueurBas.x += (self.fenW-self.tileSize)//2
        self.joueurBas.y += (self.fenH-self.tileSize)//2
        self.joueurHaut.x += (self.fenW-self.tileSize)//2
        self.joueurHaut.y += (self.fenH-self.tileSize)//2
    
    
    
class Dialogue():
    def __init__(self):
        pass
    
    def iniDialogue(self, objDict):
        self.msgs = []
        self.textZone = pyglet.text.Label(text='Default',
                                        x = 20,
                                        y = 94,
                                        width=300,
                                        color = (0,0,0,255),
                                        font_size= 20,
                                        #anchor_x=self.anchor_x,
                                        #anchor_y=self.anchor_y,
                                        multiline=True)
        self.textBackGround = self.Image = self.Image = pyglet.image.load('resources/images/monde/dialogueBox.png')
        self.textBackGround = pyglet.sprite.Sprite(self.textBackGround, x=0, y=0)
        
        self.function = '@'
        
        self.menu = objDict[0]['Menu']
        self.player = objDict[0]['Player']
        self.combat = objDict[0]['Combat']

    
    def getDialogueState(self, pDialogue):
            self.dialogueState = pDialogue
    
    
    def resize(self, scale):
        self.textZone.width = 450*scale
        self.textZone.font_size = 10*scale
        self.textZone.y = 64*scale
        self.textZone.x = 20*scale
        self.textBackGround.scale = 2.09*scale
        
    def addDialogue(self, text, pEndFunction='@'):
        self.dialogueState[0] = True
        if isinstance(text, str):
            self.msgs.append(text)
        elif isinstance(text, list):
            self.msgs += text
            
        self.function = pEndFunction
        
    
    def nextDialogue(self):
        if len(self.msgs) > 0:
            self.textZone.text = self.msgs.pop(0)
            self.dialogueState[0] = True
        else:
            self.textZone.text = 'Default'
            self.dialogueState[0] = False
            return self.endFunction()
        
    def endFunction(self):
        if self.function != '@':
            return exec(self.function)
        else:
            return None

    def draw(self):
        if self.textZone.text == 'Default':
            self.nextDialogue()
        self.textBackGround.draw()
        self.textZone.draw()
