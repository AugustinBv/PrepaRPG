import pyglet

class ISprite(pyglet.sprite.Sprite):
    def __init__(self, img , window, x=0, y=0, blend_src=770, blend_dest=771, batch=None, group=None, usage='dynamic', subpixel=False, sW = -1, sH = -1, pW = -1, pH = -1):
        super().__init__(img = img ,x = x, y = y, blend_src = blend_src, blend_dest = blend_dest, batch=batch, group=group, usage=usage, subpixel=subpixel)
        self.widthD = self.width
        self.heightD = self.height
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

    def setRelativePosition(self,x,y):
        self.pW = x
        self.pH = y

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

    def show(self):
        self.update()
        self.draw()

def noFlou():
    pyglet.gl.glEnable(pyglet.gl.GL_TEXTURE_2D)
    pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)
