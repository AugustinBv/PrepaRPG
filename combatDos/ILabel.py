import pyglet

class ILabel(pyglet.text.Label):
    def __init__(self, window,text='', font_name=None, font_size=None, bold=False, italic=False, color=(255, 255, 255, 255), x=0, y=0, width=None, height=None, anchor_x='left', anchor_y='baseline', align='left', multiline=False, dpi=None, batch=None, group=None, sW = -1, sH = -1, pW = -1, pH = -1):
        super().__init__(text=text, font_name=font_name, font_size=font_size, bold=bold, italic=italic, color=color, x=x, y=y, width=width, height=height, anchor_x=anchor_x, anchor_y=anchor_y, align=align, multiline=multiline, dpi=dpi, batch=batch, group=group)
        self.widthD = self.width
        self.heightD = self.height
        self.font_sizeD = self.font_size
        self.sW = sW
        self.sH = sH
        self.pW = pW
        self.pH = pH
        self.customScale = 1
        self.DsW = window.width
        self.DsH = window.height
        self.window = window
        self.sizeModif = 1.5

    def setWindowRatio(self,width,height):
        self.sW = width
        self.DsW = self.window.width
        self.DsH = self.window.height
        self.sH = height

    def setRelativePosition(self,x,y):
        self.pW = x
        self.pH = y

    def rescale(self):
        c = (self.window.width/self.widthD)*self.sW/100 if self.sW > 0 else self.customScale*self.window.width/self.DsW
        cc = (self.window.width/self.widthD)*93/100 if self.sW < 0 else self.customScale*self.window.width/self.DsW
        ccc = (self.window.height/self.heightD)*17/100 if self.sH < 0 else self.customScale*self.window.height/self.DsH
        self.width = self.widthD*c
        if cc > ccc:
            self.font_size = self.font_sizeD*cc
        else:
            self.font_size = self.font_sizeD*ccc
        self.font_size = self.font_size*self.sizeModif

        #self.font_size = self.font_sizeD*self.height/self.width
    def positionUpdate(self):
        self.x = (self.window.width)/(100/self.pW) if self.pW > 0 else self.x
        self.x = self.x - self.font_size
        self.y = (self.window.height)/(100/self.pH) if self.pH > 0 else self.y
        self.y = self.y - self.font_size

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
