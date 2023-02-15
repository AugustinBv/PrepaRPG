import pyglet
from combatDos.ISprite import ISprite
from combatDos.IButton import IButton
def loadImage(window , img = None, name="",x = 0,y = 0,width = 0, height = 0):
    if not img:
        img = pyglet.image.load(name)
    width = img.width if width <= 0 else width
    height = img.height if height <= 0 else height
    return ISprite(img.get_region(x,img.height - y - height, width, height),window = window)

def loadImageButton(window , text="Lol", img = None, name="",x = 0,y = 0,width = 0, height = 0):
    if not img:
        img = pyglet.image.load(name)
    width = img.width if width <= 0 else width
    height = img.height if height <= 0 else height
    return IButton(img.get_region(x,img.height - y - height, width, height),window = window,text = text)
