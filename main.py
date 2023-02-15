import pyglet
from Musiques import *
from SaveMenus import *
from Inventaire import *
from entitees import *
from Competence import *
from Monde import *
from NPC import *
from Quete import *

import combatDos.ILabel
from combat import *


#----------Sound and Music-------


pyglet.options['search_local_libs'] = True
pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')


#----------Main program-------


SaveObj = Save()
Window = SaveObj.createWindow()
SaveObj.Window = Window

gameState = 'Menu'
crtState = 'Title'
globalVariables = [gameState, crtState]
globalObjects = [{'Window':         Window,
                 'Save':            SaveObj,
                 'Menu':            Menu(), 
                 'ListeSort':       ListeSort(),
                 'Player':          Player(),
                 'Inventaire':      Inventaire(),
                 'Musiques':        Musiques(),
                 'Combat':          Combat(),
                 'Monde':           Monde(),
                 'Dialogue':        Dialogue(),
                 'ListeQuete':      ListeQuete(),
                 }]

# SpellList = globalObjects[0]['ListeSort']
# PlayerObj = globalObjects[0]['Player']
# InvObj = globalObjects[0]['Inventaire']
# Music = globalObjects[0]['Musiques']
# Combat = globalObjects[0]['Combat']
# Monde = globalObjects[0]['Monde']
# MenuObj = globalObjects[0]['Menu']


globalObjects[0]['ListeSort'].iniListeSort()
globalObjects[0]['Inventaire'].iniInventaire(globalObjects)
globalObjects[0]['Musiques'].iniMusiques(globalVariables)
globalObjects[0]['Dialogue'].iniDialogue(globalObjects)
globalObjects[0]['Player'].iniPlayer(globalObjects)

globalObjects[0]['Monde'].iniMonde(globalVariables, globalObjects)
globalObjects[0]['Combat'].iniCombat(globalVariables, globalObjects)
globalObjects[0]['Menu'].iniMenu(globalVariables, globalObjects)
#globalObjects[0]['Menu'].
#globalObjects[0]['Menu'].







#Menu World Combat
@Window.event
def on_draw():
    globalObjects[0]['Window'].clear()
    globalObjects[0]['Musiques'].actualiser_musique()
    globalObjects[0]['Monde'].afficher()
    globalObjects[0]['Combat'].show()
    globalObjects[0]['Menu'].on_draw()

@Window.event
def on_mouse_press(x, y, button, modifiers):
    globalObjects[0]['Menu'].on_mouse_press(x, y)
    globalObjects[0]['Combat'].on_mouse_press(x, y, button, modifiers)
    globalObjects[0]['Monde'].on_mouse_press(x, y, button, modifiers)

@Window.event
def on_mouse_motion(x, y, dx, dy):
    globalObjects[0]['Menu'].on_mouse_motion(x, y, dx, dy)
    globalObjects[0]['Combat'].on_mouse_motion(x, y, dx, dy)

@Window.event
def on_key_press(val, mod):

    if val == key.M and True:
        globalObjects[0]['Menu'].creditsRoll()


    if val == key.ESCAPE:
        pass #pyglet.app.exit()
    
    globalObjects[0]['Menu'].on_key_press(val, mod)
    globalObjects[0]['Monde'].key_press(val, mod)
    return pyglet.event.EVENT_HANDLED

@Window.event
def on_key_release(val, mod):
    globalObjects[0]['Monde'].key_release(val, mod)

@Window.event
def on_resize(width, height):
    globalObjects[0]['Monde'].resize(int(width), int(height))


def tick(dt):
    globalObjects[0]['Monde'].tack()

pyglet.clock.schedule_interval(tick, 0.02)
pyglet.app.run()
