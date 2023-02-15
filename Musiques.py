import pyglet


pyglet.options['search_local_libs'] = True
pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')



class Musiques():   #classe pour définir tous les fichiers audio et leur chemin d'accès

    def __init__(self):
        pass
    
    def iniMusiques(self, globalVariables):
        self.musiqueListe ={"menu_theme" : pyglet.media.load('resources/Sounds/musics/MenuTheme.mp3', streaming = True),
                            "credits_theme" : pyglet.media.load('resources/Sounds/musics/CreditsTheme.mp3', streaming = True),
                            "combat_theme" : pyglet.media.load('resources/Sounds/musics/CombatTheme.mp3', streaming = False),
                            "boss_combat_theme" : pyglet.media.load('resources/Sounds/musics/BossCombatTheme.mp3', streaming = True),
                            "final_combat_theme" : pyglet.media.load('resources/Sounds/musics/FinalBossCombatTheme.mp3', streaming = True),
                            "world_theme" : pyglet.media.load('resources/Sounds/musics/WorldTheme.mp3', streaming = False),
                            "world_theme2" : pyglet.media.load('resources/Sounds/musics/WorldTheme2.wav', streaming = False)}
                            # "IGUIs_theme" : pyglet.media.load('resources/Sounds/musics/IGUIsTheme.mp3', streaming = False)}
        self.soundListe ={"button_press" : pyglet.media.load('resources/Sounds/sounds/ButtonSound.mp3', streaming = False),
                          "start_press" : pyglet.media.load('resources/Sounds/sounds/StartSound.mp3', streaming = False),
                          "pause_press" : pyglet.media.load('resources/Sounds/sounds/PauseSound.mp3', streaming = False)}
        self.globalVariables = globalVariables
        self.Player = pyglet.media.Player()
        self.Player.queue(self.soundListe['start_press']) #initialise artificiellement la Q
        self.previous_state = (None,None)








    def jouer_musique(self, Piste):     #Permet de créer une nouvelle playlist (en effaçant la précédente) et de jouer la musique invoquée
        self.Player.queue(self.musiqueListe[Piste])
        self.Player.pause()

        self.Player.next_source()
        self.Player.play()
        self.Player.loop = True


    def jouer_son(self, Son):
        self.soundListe[Son].play()


    def actualiser_musique(self):       #fonction qui actualise la musique à jouer en fonction de la situation. Pour cela on se base une variable globale qui décrit l'état du jeu à un moment donné
        if self.previous_state != self.globalVariables:
            print(self.globalVariables)
            if self.globalVariables[0] == 'Menu':

                if self.globalVariables[1] == 'Title':
                    self.jouer_musique('menu_theme')



                elif self.globalVariables[1] == 'IGUIs':
                    self.jouer_musique('world_theme')



                elif self.globalVariables[1] == 'Credits':
                    self.jouer_musique('credits_theme')




            elif self.globalVariables[0] == 'World':
                 self.jouer_musique('world_theme')
                #if self.globalVariables[1] == 'World1':
                #    self.jouer_musique('world_theme')

                #if self.globalVariables[1] == 'World2':
                #    self.jouer_musique('world_theme2')


            elif self.globalVariables[0] == 'fight':

                if self.globalVariables[1] == 'normal':
                    self.jouer_musique('combat_theme')

                if self.globalVariables[1] == 'boss':
                    self.jouer_musique('boss_combat_theme')

                if self.globalVariables[1] == 'final':
                    self.jouer_musique('final_combat_theme')


            self.previous_state = self.globalVariables[:]
