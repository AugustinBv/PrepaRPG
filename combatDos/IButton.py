import pyglet
import combatDos.ILabel as ILabel

class IButton(pyglet.sprite.Sprite):
    def __init__(self, img , window, text = "Mon texte test", x=0, y=0, blend_src=770, blend_dest=771, batch=None, group=None, usage='dynamic', subpixel=False, sW = -1, sH = -1, pW = -1, pH = -1):
        super().__init__(img = img ,x = x, y = y, blend_src = blend_src, blend_dest = blend_dest, batch=batch, group=group, usage=usage, subpixel=subpixel)
        self.widthD = self.width
        self.heightD = self.height
        self.label = ILabel.ILabel(window,text= text, font_size = 12,color = (0,0,0,255),width = self.width,height = self.height,anchor_x='center', anchor_y='center')
        self.sW = sW
        self.sH = sH
        self.pW = pW
        self.pH = pH
        self.customScale = 1
        self.DsW = window.width
        self.DsH = window.height
        self.window = window

    def setWindowRatio(self,width,height):
        self.sW = width
        self.DsW = self.window.width
        self.DsH = self.window.height
        self.sH = height
        self.label.setWindowRatio(width/2,height/2)

    def setRelativePosition(self,x,y):
        self.pW = x
        self.pH = y
        self.label.setRelativePosition(x,y)

    def rescale(self):
        self.scale_x = (self.window.width/self.widthD)*self.sW/100 if self.sW > 0 else self.customScale*self.window.width/self.DsW
        self.scale_y = (self.window.height/self.heightD)*self.sH/100 if self.sH > 0 else self.customScale*self.window.width/self.DsH

    def positionUpdate(self):
        self.x = (self.window.width)/(100/self.pW) if self.pW > 0 else self.x
        self.y = (self.window.height)/(100/self.pH) if self.pH > 0 else self.y

    def update(self):
        noFlou()
        self.rescale()
        self.positionUpdate()

    def show(self,x=0,y=0):
        self.update()
        self.label.update()
        if self.isHover(x,y):
            self.color = (18, 133, 203)
        else:
            self.color = (255,255,255)
        self.draw()
        self.label.x = self.x+self.width/2
        self.label.y = self.y-6+self.height/2
        self.label.width = self.width
        self.label.height = self.height
        if len(self.label.text) > 25:
            print(self.label.text[0:25])
            self.label.text = self.label.text[0:25]+"-"
        self.label.draw()

    def isHover(self,x,y):
        return self.x < x and self.y < y and self.x + self.width > x and self.y + self.height > y

def noFlou():
    pyglet.gl.glEnable(pyglet.gl.GL_TEXTURE_2D)
    pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)
