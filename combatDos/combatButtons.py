import pyglet
from pyglet import shapes
import combatDos.Utils as Utils

class CombatButtons():
    def __init__(self,window,dialogueMode = True,competences=["T1","T2","T3","T4"]):
        self.window = window
        self.dialogueMode = dialogueMode
        self.menuIndex = 0
        combat = pyglet.image.load('combatDos/combat.png')
        self.mouse = 0,0
        index1 = []
        fuite = Utils.loadImageButton(window,text="",img = combat,x = 0, y = 124 , width = 256,height = 256)

        fuite.setWindowRatio(5,5)
        fuite.setRelativePosition(47.5,15)
        fuite.index = -1
        if len(competences) >= 1:
            sprite = Utils.loadImageButton(window,text=competences[0].Nom,img = combat,x = 705, y = 0 , width = 268,height = 86)
            sprite.setWindowRatio(42,8)
            sprite.index = 0
            sprite.setRelativePosition(5,13)
            index1.append(sprite)
        if len(competences) >= 2:
            sprite2 = Utils.loadImageButton(window,text=competences[1].Nom,img = combat,x = 705, y = 0 , width = 268,height = 86)
            sprite2.setWindowRatio(42,8)
            sprite2.setRelativePosition(5,4)
            sprite2.index = 1
            index1.append(sprite2)

        if len(competences) >= 3:
            sprite3 = Utils.loadImageButton(window,text=competences[2].Nom,img = combat,x = 705, y = 0 , width = 268,height = 86)
            sprite3.setWindowRatio(42,8)
            sprite3.setRelativePosition(53,13)
            sprite3.index = 2
            index1.append(sprite3)

        if len(competences) >= 4:
            sprite4 = Utils.loadImageButton(window,text=competences[3].Nom,img = combat,x = 705, y = 0 , width = 268,height = 86)
            sprite4.setWindowRatio(42,8)
            sprite4.setRelativePosition(53,4)
            sprite4.index = 3
            index1.append(sprite4)
        index1.append(fuite)
        self.index = [index1]


    def setDialogueMode(self,mode):
        self.dialogueMode = mode

    def click(self,x,y):
        for sprite in self.index[self.menuIndex]:
            if sprite.isHover(x,y):
                #self.menuIndex = sprite.index
                return sprite.index

    def show(self):
        if not self.dialogueMode:
            self.display()

    def updateMouse(self,x,y):
        self.mouse = x, y

    def display(self):
        for sprite in self.index[self.menuIndex]:
            sprite.show(self.mouse[0],self.mouse[1])
