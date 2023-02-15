import pyglet
from pyglet.window import mouse
from pyglet.window import key
from pyglet.gl import *

import Utils
import ILabel
import combat

from pyglet import resource
from pyglet import font


from entitees import *

class Sort():
    def __init__(self, Competence, indice):
        self.Id=Competence[indice][0]       #Id
        self.Connue=Competence[indice][1]       #si la compétence est apprise on associe la valeur Acquis
        self.Nom=Competence[indice][2]       #Nom
        self.Cible=Competence[indice][3]       #Les cibles
        self.StatCible=Competence[indice][4]       #Les Statistiques ciblées
        self.Valeur=Competence[indice][5]       #Les valeurs associées au stats ciblées
        self.Vitesse=Competence[indice][6]  #Vitesse de la compétence
        self.Description=Competence[indice][7] #Description de la compétence
        self.ListStatCible=Sort.CibleStat(self.Cible, self.StatCible, self.Valeur)

    def CibleStat(cible, statcible, valeur):
        a=cible.split(",")
        b=statcible.split(",")
        c=valeur.split(",")
        ListCible=[]
        for i in range (len(a)):
            ListCible.append([a[i],b[i],int(c[i])])
        return(ListCible)

window = pyglet.window.Window(resizable=True)
stat = {"damage":10, "dodge":0, "heal":0, "stamina":0, "defense":0, "aptDebuff":0, "resistanceDebuff":0, "crits":0, "hp":20, "hpMax":20}
nous=Player()
nous.initPlayer(stat,[],[],"Num")
#nous.addXp(13000)
nous.addXp(13300000)
cb = combat.Combat(window,nous)
minorant = Majorant()
l = ["00/Acquis/TrippleEntaille/enemy,enemy,enemy/vie,vie,vie/10,5,4/0/attaque lente avec trois coup/".split("/"),
"01/NonAcquis/Heal/player/vie/24/1/rend de la vie a l'utilisateur/".split("/"),
"02/Acquis/Analyse synthese/enemy/vie/50/13/La meilleure attaque contre les prof de math/".split("/"),
"03/Acquis/illetre/enemy/vie/20/3/La meilleure attaque contre les prof de francais/".split("/")]
c1 = Sort(l,0)
c2 = Sort(l,1)
c3 = Sort(l,2)
c4 = Sort(l,3)
competence = [c1,c2,c3,c4]
nous.statCombat()
cb.startCombat(minorant,competence,0)

# start = True
# def on_update(dt):
#     if cb.start:
#         cb.on_update(dt)
#     if not cb.start and not cb.start:
#         #window.close()
#         pass

# pyglet.clock.schedule_interval(on_update, 0.05)

@window.event
def on_draw():
    window.clear()
    if cb.start or cb.end:
        cb.show()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if cb.start or cb.end:
        cb.on_mouse_press(x, y, button, modifiers)


@window.event
def on_mouse_motion(x, y, dx, dy):
    if cb.start:
        cb.on_mouse_motion(x, y, dx, dy)


pyglet.app.run()
