#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 09:58:08 2021

@author: an.languille
"""

import pyglet
import time

import tkinter
from pyglet.window import key

# globalVariables[0] = 'Menu' #,'Monde','Combat'
# currentMenu = 'Tittle'
# #Tittle, SavedGamesLoad, SavedGamesNew, Options, Inventory, PauseMenu...


#--------------ScreensFunctions-------------------


class Menu():

    def __init__(self):
        pass
    
    def iniMenu(self, globalVariables, globalObjects):

        self.globalVariables = globalVariables

        self.Window = globalObjects[0]['Window']
        self.crtMenu = 'Title'

        self.scale = 1
        self.path = 'resources/images/'

        self.menuItems = {'Title':('TitleText',
                                   'NewSavedGame', 'LoadSavedGame', 'Options', 'Quit'),
                            'Options':('FullScreenOption', 'FullScreenLabel', 'KeyControlOption', 'KeyControlLabel', #(fonctionnalité retirée)
                            'ResolutionOption','ResolutionLabel','ApplySettings','GoBack'),
                            'NewSavedGame':('GoBack','GameFile1','GameFile2','GameFile3'),
                            'LoadSavedGame':('GoBack','GameFile1','GameFile2','GameFile3'),
                            'Inventory':('UpgradeLabel','LevelLabel','CountLabel','MaterialLabel',
                                         'CalcUpgrade','OsciUpgrade','PerTUpgrade','MotoUpgrade','BookUpgrade','TireUpgrade','CompUpgrade',
                                         'CalcLevel','OsciLevel','PerTLevel','MotoLevel','BookLevel','TireLevel','CompLevel',
                                         'FormLabel','WireLabel','ElemLabel','GearLabel','PageLabel','HairLabel','CircLabel',
                                         'FormCount','WireCount','ElemCount','GearCount','PageCount','HairCount','CircCount',
                                          'GoBack','MoneyCount'),
                            'PauseMenu':('Resume','SkillsOverview','Inventory','SaveGame','QuitGame'),
                            'Credits': [],
                            'CompTrade':('GoBack','MoneyCount','MaterialBuyLabel','MaterialBuyCountLabel','MaterialBuyCostLabel','MaterialCrtCountLabel',
                                            'FormBuyLabel','WireBuyLabel','ElemBuyLabel','GearBuyLabel','PageBuyLabel','HairBuyLabel','CircBuyLabel',
                                            'FormBuyCount','WireBuyCount','ElemBuyCount','GearBuyCount','PageBuyCount','HairBuyCount','CircBuyCount',
                                            'FormCrtCount','WireCrtCount','ElemCrtCount','GearCrtCount','PageCrtCount','HairCrtCount','CircCrtCount',
                                            'FormBuyCost', 'WireBuyCost','ElemBuyCost','GearBuyCost','PageBuyCost','HairBuyCost','CircBuyCost',
                                            'BuyCountUp','BuyCountDown','CompBuy','CompBuyCost'),

                            'SkillsTrade':('GoBack','MoneyCount'),
                            'SkillsOverview':('GoBack','MoneyCount','SkillsLabel','InfoLabel',#'StatsLabel',
                                              'Skill1','Skill2','Skill3','Skill4',
                                              'SkillDescription',
                                              'HpStat', 'HpMaxStat','HealStat','DamageStat','CritsStat','DodgeStat','DefenseStat','AptDebuffStat','ResisDebuffStat',
                                              ),
                            'SkillsEquipement':('GoBack','MoneyCount','ApplySkills','ApplySkillsCost','NextPage','PrevPage','PageNumber',
                                                'SkillsLabel','InfoLabel','LearnedSkillsLabel',
                                              'Skill1','Skill2','Skill3','Skill4',
                                              'SkillB1','SkillB2','SkillB3','SkillB4','SkillB5','SkillB6',
                                              'DelSkill1','DelSkill2','DelSkill3','DelSkill4',
                                              'SkillDescription'),
                            'AskDelete':('AskDelete','ConfirmDelete','InfirmDelete'),
                            'CharacSelect':('GoBack',
                                            'NameSelectLabel','ClassChoiceLabel','DifficultyLabel','SkinLabel',
                                            'ClassChoiceChim','ClassChoiceNum',
                                            'Difficulty5/2','DifficultyNormal','DifficultyMajorant',
                                            'SkinSelectM','SkinSelectMme',
                                            'CreateNewGame')
                            }


        matLabColor = (220,220,220)
        objLevColor = (200,200,250)
        StatColor = (200,250,200)
        compCrtColor = (200,160,200)
        compCostColor = (200,200,160)

        self.buttons = {

            'TitleText':        Item( x=500, y=550, imagePath=str(self.path + 'menus/title/Title.png')),

            'NewSavedGame':     Item( x=623, y=800 - 361 - 63,   width=353, height=63, text='  Nouvelle Partie'),
            'LoadSavedGame':    Item( x=623, y=800 - 361 - 63*2.5, width=353, height=63, text='  Charger Partie'),
            'Options':          Item( x=623, y=800 - 361 - 63*4, width=353, height=63, text='  Options'),
            'Quit':             Item( x=623, y=800 - 361 - 63*5.5, width=353, height=63, text='  Quitter'),

            'FullScreenOption': Item( x=800, y=489, width=100, height=63),
            'FullScreenLabel':  Item( x=600, y=489 + 32, text='Full Screen'),

            'KeyControlOption': Item( x=800, y=389, width=150, height=63),
            'KeyControlLabel':  Item( x=600, y=389 + 32, text='Mouvement keys'),

            'ResolutionOption': Item( x=800, y=289, width=150, height=63),
            'ResolutionLabel':  Item( x=600, y=289 + 32, text='Resolution'),

            'ApplySettings':    Item(x=700, y=100, width=150, height=63, text='Appliquer'),

            'GoBack':           Item( x=160, y=90, imagePath=str(self.path + 'menus/arrowLeft.png')),

            'GameFile1':    Item( x=500, y=900 - 348 - 63,    align_x='left', width=500, height=2*63, text='Empty', multiline=True, color=(200,200,200)),
            'GameFile2':    Item( x=500, y=900 - 348 - 63*4,  align_x='left', width=500, height=2*63, text='Empty', multiline=True, color=(200,200,200)),
            'GameFile3':    Item( x=500, y=900 - 348 - 63*7,  align_x='left', width=500, height=2*63, text='Empty', multiline=True, color=(200,200,200)),


            'Resume':        Item( x=623, y=900 - 361 + 32,   width=353, height=63, text='Reprendre'),
            'SkillsOverview':Item( x=623, y=900 - 361 - 63,   width=353, height=63, text='Compétences'),
            'Inventory':     Item( x=623, y=900 - 361 - 63*2-32, width=353, height=63, text='Inventaire'),
            'SaveGame':      Item( x=623, y=900 - 361 - 63*3-32*2, width=353, height=63, text='Sauvegarder'),
            'QuitGame':      Item( x=623, y=900 - 361 - 63*4-32*3, width=353, height=63, text='Quitter'),

            'UpgradeLabel':Item( x=500, y=700, text='Objets améliorables'),
            'CalcUpgrade': Item( x=350, y=600, width=300, height=50, align_x='left', text=' Calculatrice'),
            'OsciUpgrade': Item( x=350, y=525, width=300, height=50, align_x='left', text=' Oscilloscope'),
            'PerTUpgrade': Item( x=350, y=450, width=300, height=50, align_x='left', text=' Tableau périodique'),
            'MotoUpgrade': Item( x=350, y=375, width=300, height=50, align_x='left', text=' Moteur'),
            'BookUpgrade': Item( x=350, y=300, width=300, height=50, align_x='left', text=' Livre'),
            'TireUpgrade': Item( x=350, y=225, width=300, height=50, align_x='left', text=' Tirelitler'),
            'CompUpgrade': Item( x=350, y=150, width=300, height=50, align_x='left', text=' Ordinateur'),

            'LevelLabel':Item( x=750, y=700, text='Niveau'),
            'CalcLevel': Item( x=700, y=600, width=100, height=50, text='00/20', allowHighlight=False, color=objLevColor),
            'OsciLevel': Item( x=700, y=525, width=100, height=50, text='00/20', allowHighlight=False, color=objLevColor),
            'PerTLevel': Item( x=700, y=450, width=100, height=50, text='00/20', allowHighlight=False, color=objLevColor),
            'MotoLevel': Item( x=700, y=375, width=100, height=50, text='00/20', allowHighlight=False, color=objLevColor),
            'BookLevel': Item( x=700, y=300, width=100, height=50, text='00/20', allowHighlight=False, color=objLevColor),
            'TireLevel': Item( x=700, y=225, width=100, height=50, text='00/20', allowHighlight=False, color=objLevColor),
            'CompLevel': Item( x=700, y=150, width=100, height=50, text='00/20', allowHighlight=False, color=objLevColor),


            'MaterialLabel':Item( x=1100, y=700, text='Matériaux'),
            'FormLabel':    Item( x=1000, y=600, width=250, height=50, align_x='left', allowHighlight=False, color=matLabColor, text=' Formules'),
            'WireLabel':    Item( x=1000, y=525, width=250, height=50, align_x='left', allowHighlight=False, color=matLabColor, text=' Fils'),
            'ElemLabel':    Item( x=1000, y=450, width=250, height=50, align_x='left', allowHighlight=False, color=matLabColor, text=' Éléments'),
            'GearLabel':    Item( x=1000, y=375, width=250, height=50, align_x='left', allowHighlight=False, color=matLabColor, text=' Engrenages'),
            'PageLabel':    Item( x=1000, y=300, width=250, height=50, align_x='left', allowHighlight=False, color=matLabColor, text=' Pages'),
            'HairLabel':    Item( x=1000, y=225, width=250, height=50, align_x='left', allowHighlight=False, color=matLabColor, text=' Poils moustache'),
            'CircLabel':    Item( x=1000, y=150, width=250, height=50, align_x='left', allowHighlight=False, color=matLabColor, text=' Circuits'),

            'CountLabel':   Item( x=900, y=700, text='Nombre'),
            'FormCount':    Item( x=850, y=600, width=100, height=50, text='00/00', allowHighlight=False, color=(220,220,220)),
            'WireCount':    Item( x=850, y=525, width=100, height=50, text='00/00', allowHighlight=False, color=(220,220,220)),
            'ElemCount':    Item( x=850, y=450, width=100, height=50, text='00/00', allowHighlight=False, color=(220,220,220)),
            'GearCount':    Item( x=850, y=375, width=100, height=50, text='00/00', allowHighlight=False, color=(220,220,220)),
            'PageCount':    Item( x=850, y=300, width=100, height=50, text='00/00', allowHighlight=False, color=(220,220,220)),
            'HairCount':    Item( x=850, y=225, width=100, height=50, text='00/00', allowHighlight=False, color=(220,220,220)),
            'CircCount':    Item( x=850, y=150, width=100, height=50, text='00/00', allowHighlight=False, color=(220,220,220)),

            'MoneyCount':   Item(x=750, y=50, width=150, height=50, text='0 PC', allowHighlight=False, color=(200,200,160)),

            'SkillsLabel':  Item(x=350, y=700, text='Compétences équipées'),
            'Skill1':       Item(x=200, y=575, width=300, height=75, text=''),
            'Skill2':       Item(x=200, y=475, width=300, height=75, text=''),
            'Skill3':       Item(x=200, y=375, width=300, height=75, text=''),
            'Skill4':       Item(x=200, y=275, width=300, height=75, text=''),


            'StatsLabel':       Item( x=1175, y=825, allowHighlight=False, text=' Statistiques: '),
            'HpStat':           Item( x=1100, y=725, width=300, height=50, align_x='left', allowHighlight=False, color=StatColor, multiline=True, text=' Vie: \t\t15 PV'),
            'HpMaxStat':        Item( x=1100, y=650, width=300, height=50, align_x='left', allowHighlight=False, color=StatColor, multiline=True, text=' Vie Max: \t100 PV'),
            'HealStat':         Item( x=1100, y=575, width=300, height=50, align_x='left', allowHighlight=False, color=StatColor, multiline=True, text=' Dégâts: \t 10%'),
            'DamageStat':       Item( x=1100, y=500, width=300, height=50, align_x='left', allowHighlight=False, color=StatColor, multiline=True, text=' Soin: \t\t 10%'),
            'CritsStat':        Item( x=1100, y=425, width=300, height=50, align_x='left', allowHighlight=False, color=StatColor, multiline=True, text=' Critiques: \t 10%'),
            'DodgeStat':        Item( x=1100, y=350, width=300, height=50, align_x='left', allowHighlight=False, color=StatColor, multiline=True, text=' Esquive: \t 10%'),
            'DefenseStat':      Item( x=1100, y=275, width=300, height=50, align_x='left', allowHighlight=False, color=StatColor, multiline=True, text=' Défense: \t 10%'),
            'AptDebuffStat':    Item( x=1100, y=200, width=300, height=50, align_x='left', allowHighlight=False, color=StatColor, multiline=True, text=' Vulnérabilité: \t+10%'),
            'ResisDebuffStat':  Item( x=1100, y=125, width=300, height=50, align_x='left', allowHighlight=False, color=StatColor, multiline=True, text=' Résistance: \t-10%'),


            'LearnedSkillsLabel':  Item(x=1250, y=700, allowHighlight=False, text='Compétences apprises'),
            'SkillB1':Item(x=1100, y=600, width=300, height=50, text=''),
            'SkillB2':Item(x=1100, y=525, width=300, height=50, text=''),
            'SkillB3':Item(x=1100, y=450, width=300, height=50, text=''),
            'SkillB4':Item(x=1100, y=375, width=300, height=50, text=''),
            'SkillB5':Item(x=1100, y=300, width=300, height=50, text=''),
            'SkillB6':Item(x=1100, y=225, width=300, height=50, text=''),

            'InfoLabel':         Item(x=600-10+210, y=725, text='Informations compétence'),
            'SkillDescription':  Item(x=600, y=665, align_x='left', align_y='top', allowHighlight=False, width=210, multiline=True, text=' Description:', text_color=(0,0,0,255)),

            'NextPage': Item(x=1100 + 300 -82, y=225 - 25 - 54,  imagePath=str(self.path + 'menus/arrowRight.png')),
            'PrevPage': Item(x=1100,           y=225 - 25 - 54,  imagePath=str(self.path + 'menus/arrowLeft.png')),
            'PageNumber':  Item(x=1250, y=225 - 25 - 27, allowHighlight=False, text='Page 0/0'),

            'DelSkill1':Item(x=125, y=575 + 15,  imagePath=str(self.path + 'menus/cross.png')),
            'DelSkill2':Item(x=125, y=475 + 15,  imagePath=str(self.path + 'menus/cross.png')),
            'DelSkill3':Item(x=125, y=375 + 15,  imagePath=str(self.path + 'menus/cross.png')),
            'DelSkill4':Item(x=125, y=275 + 15,  imagePath=str(self.path + 'menus/cross.png')),

            'ApplySkills':Item(x=250, y=200, width=200, height=50, text='Appliquer'),
            'ApplySkillsCost':Item(x=350, y=175, text='0/0 PC'),


            'MaterialBuyLabel':    Item( x=375, y=700+75, text='Matériaux'),
            'FormBuyLabel':    Item( x=300, y=700, width=250, height=50, align_x='left', allowHighlight=False, text=' Formules'),
            'WireBuyLabel':    Item( x=300, y=625, width=250, height=50, align_x='left', allowHighlight=False, text=' Fils'),
            'ElemBuyLabel':    Item( x=300, y=550, width=250, height=50, align_x='left', allowHighlight=False, text=' Éléments'),
            'GearBuyLabel':    Item( x=300, y=475, width=250, height=50, align_x='left', allowHighlight=False, text=' Engrenages'),
            'PageBuyLabel':    Item( x=300, y=400, width=250, height=50, align_x='left', allowHighlight=False, text=' Pages'),
            'HairBuyLabel':    Item( x=300, y=325, width=250, height=50, align_x='left', allowHighlight=False, text=' Poils moustache'),
            'CircBuyLabel':    Item( x=300, y=250, width=250, height=50, align_x='left', allowHighlight=False, text=' Circuits'),

            'MaterialCrtCountLabel':    Item( x=650, y=700+75, text='Possédés'),
            'FormCrtCount':    Item( x=600, y=700, width=100, height=50, allowHighlight=False, text='0', color=compCrtColor),
            'WireCrtCount':    Item( x=600, y=625, width=100, height=50, allowHighlight=False, text='0', color=compCrtColor),
            'ElemCrtCount':    Item( x=600, y=550, width=100, height=50, allowHighlight=False, text='0', color=compCrtColor),
            'GearCrtCount':    Item( x=600, y=475, width=100, height=50, allowHighlight=False, text='0', color=compCrtColor),
            'PageCrtCount':    Item( x=600, y=400, width=100, height=50, allowHighlight=False, text='0', color=compCrtColor),
            'HairCrtCount':    Item( x=600, y=325, width=100, height=50, allowHighlight=False, text='0', color=compCrtColor),
            'CircCrtCount':    Item( x=600, y=250, width=100, height=50, allowHighlight=False, text='0', color=compCrtColor),

            'MaterialBuyCountLabel':    Item( x=900, y=700+75, text='Montant'),
            'FormBuyCount':    Item( x=850, y=700, width=100, height=50, allowHighlight=False, text='0'),
            'WireBuyCount':    Item( x=850, y=625, width=100, height=50, allowHighlight=False, text='0'),
            'ElemBuyCount':    Item( x=850, y=550, width=100, height=50, allowHighlight=False, text='0'),
            'GearBuyCount':    Item( x=850, y=475, width=100, height=50, allowHighlight=False, text='0'),
            'PageBuyCount':    Item( x=850, y=400, width=100, height=50, allowHighlight=False, text='0'),
            'HairBuyCount':    Item( x=850, y=325, width=100, height=50, allowHighlight=False, text='0'),
            'CircBuyCount':    Item( x=850, y=250, width=100, height=50, allowHighlight=False, text='0'),

            'MaterialBuyCostLabel':    Item( x=1175, y=700+75, text='Prix'),
            'FormBuyCost':    Item( x=1100, y=700, width=150, height=50, allowHighlight=False, color=compCostColor, text='75 PC'),
            'WireBuyCost':    Item( x=1100, y=625, width=150, height=50, allowHighlight=False, color=compCostColor, text='100 PC'),
            'ElemBuyCost':    Item( x=1100, y=550, width=150, height=50, allowHighlight=False, color=compCostColor, text='500 PC'),
            'GearBuyCost':    Item( x=1100, y=475, width=150, height=50, allowHighlight=False, color=compCostColor, text='1k PC'),
            'PageBuyCost':    Item( x=1100, y=400, width=150, height=50, allowHighlight=False, color=compCostColor, text='3k PC'),
            'HairBuyCost':    Item( x=1100, y=325, width=150, height=50, allowHighlight=False, color=compCostColor, text='5k PC'),
            'CircBuyCost':    Item( x=1100, y=250, width=150, height=50, allowHighlight=False, color=compCostColor, text='10k PC'),

            'BuyCountDown':   Item(x=950 - 125 - 82, y=700,  imagePath=str(self.path + 'menus/arrowLeft.png')),
            'BuyCountUp': Item(x=950+25,            y=700,  imagePath=str(self.path + 'menus/arrowRight.png')),

            'CompBuy':      Item(x=700, y=175, width=200, height=50, text='Acheter'),
            'CompBuyCost':  Item(x=800, y=150, text='0/0 PC'),

            'AskDelete':    Item(x=800-250, y=450, width=500, height=50, text='Voulez vous écraser ce fichier ?', color=(250,250,250)),
            'ConfirmDelete':Item(x=900, y=350, width=200, height=75, text='OUI', color=(160,250,160)),
            'InfirmDelete': Item(x=500, y=350, width=200, height=75, text='NON', color=(250,160,160)),


            'NameSelectLabel':      Item(x=800-250, y=650, width=500, height=50, text='Choisissez un nom'),

            'ClassChoiceLabel':     Item(x=800, y=500+100,text='Filière'),
            'ClassChoiceChim':      Item(x=801, y=500, width=199, height=75, text='Chimiste'),
            'ClassChoiceNum':       Item(x=600, y=500, width=199, height=75, text='Numérique'),

            'DifficultyLabel':     Item(x=800, y=350+75,text='Difficulté'),
            'Difficulty5/2':       Item(x=500, y=350, width=199, height=50, text='5/2'),
            'DifficultyNormal':    Item(x=700, y=350, width=200, height=50, text='Normal'),
            'DifficultyMajorant':  Item(x=901, y=350, width=199, height=50, text='Majorant'),

            'SkinLabel':         Item(x=800, y=200+75,text='Apparence'),
            'SkinSelectM':       Item(x=801, y=200, width=199, height=50, text='M'),
            'SkinSelectMme':     Item(x=600, y=200, width=199, height=50, text='Mme'),

            'CreateNewGame':     Item(x=700, y=100, width=200, height=50, text='Créer'),

            }

        #self.doneOperations = {}
        # self.variableArchive = {}

        self.Monde =        globalObjects[0]['Monde']
        self.Inventory =    globalObjects[0]['Inventaire']
        self.Save =         globalObjects[0]['Save']
        self.Player =       globalObjects[0]['Player']
        self.SpellList =    globalObjects[0]['ListeSort']
        self.Music =        globalObjects[0]['Musiques']

        self.gameFile = 0

        self.optionsDict = self.Save.getOptions()
        #print(self.optionsDict)

        self.crtPage = 0
        self.maxPagse = 0
        self.modifiedSkills = []
        self.learnedSkills = []

        self.selectedComp = 0
        self.buyList = [0]*7

        self.askDelete = False
        self.textInput = (False, None)

        self.characterSettings = {'name':'Choisissez un nom',
                               'skin':'Mme',
                               'difficulty':'Normal',
                               'class':'Chimiste'}

        self.classList = {'Numérique':'ClassChoiceNum',
                            'Chimiste':'ClassChoiceChim'}

        self.skinList = {'M':'SkinSelectM',
                            'Mme':'SkinSelectMme'}

        self.diffList = {'5/2':'Difficulty5/2',
                            'Normal':'DifficultyNormal',
                            'Majorant':'DifficultyMajorant'}

        self.timeLoadGame = {'total':0, 'referenceTime':0}
        #time at loading/last save, total time played at load/last save



    def getScale(self):
        """
        Returns
        -------
        scaleRatio : int
            Ratio of current window to the reference window size 1600x900.
            Based on the width of the current window.
        """
        width, height = self.Window.get_size()
        scaleRatio = width / 1600
        return scaleRatio


    def scaleAll(self, ratio=1):
        """
        Parameters
        ----------
        ratio : float, optional
            Ratio to which every item in self.buttons will be scaled. The default is 1.

        Returns
        -------
        None.

        """
        for button in self.buttons.values():
            button.scale = ratio
    
    def strLenFromat(self, string, length):
        
        if len(string) < length:
            outStr += '\t'* (len(string)-length)//2
        else:
            outStr = string
        return outStr

    

    def getButton(self, x, y):
        """
        Parameters
        ----------
        x : int
            Y coordonate of the mouse cursor.
        y : int
            X coordonate of the mouse cursor.

        Returns
        -------
        buttonID : str
            Key referencing the item corresponding to the x,y inputed coordinates.
        """

        priorButtons = {'ConfirmDelete':self.buttons['ConfirmDelete'],
                        'InfirmDelete':self.buttons['InfirmDelete']}
        if self.askDelete:
            for buttonID, button in priorButtons.items():
                X1, X2 = button.getX(),  button.getX() + button.getWidth()
                Y1, Y2 = button.getY(), button.getY() + button.getHeight()
                condX = (X1 <= x <= X2)
                condY = (Y1 <= y <= Y2)

                if condX and condY:
                    return buttonID

        else:
            for buttonID, button in self.buttons.items():
                X1, X2 = button.getX(),  button.getX() + button.getWidth()
                Y1, Y2 = button.getY(), button.getY() + button.getHeight()
                condX = (X1 <= x <= X2)
                condY = (Y1 <= y <= Y2)

                if condX and condY:
                    if buttonID in self.menuItems.get(self.crtMenu, []):
                        return buttonID
        return None

    def form10(self, number):
        """
        Formats the given number by converting thousands to 'k' and milions by 'M'

        Parameters
        ----------
        number : int/float
            Number to format.

        Returns
        -------
        outStr : Str
            Formated number.
        """
        outStr = ''

        if number >= 10**6:
            outStr = str(round(number/10**6,2))+'M'

        elif number >= 10**3:
            outStr = str(round(number/10**3,2))+'k'

        else:
            outStr = str(number)

        return outStr

    def formHour(self, inNum):
        """
        Formats the given time into an hour display: hours/minutes/seconds

        Parameters
        ----------
        number : int/float
            Time to format in seconds (s).

        Returns
        -------
        outStr : Str
            Formated time '{}h {}m {}s'.
        """
        inNum = float(inNum)

        hours, reminder = inNum // 3600, inNum % 3600
        minutes, seconds = reminder // 60, inNum % 60

        return '{}h {}m {}s'.format(int(hours), int(minutes), round(seconds,3))



    #Title, NewSavedGame, LoadSavedGame, Options, Inventory

    def on_mouse_press(self, x, y):
        """
        To call with the on_mouse_press(x,y) method in the main program

        Returns
        -------
        None.
        """
        if self.globalVariables[0] == 'Menu':
            self.scaleAll(self.getScale())

            button = self.getButton(x, y)

            # print(self.globalVariables, 'Event: on_mouse_press:', x, y, button)

            if button != None:
                if self.buttons[button].allowHighlight == True:
                    self.Music.jouer_son('button_press')

            if self.askDelete:
                if button == 'ConfirmDelete':
                    self.characterSettings = {'name':'Choisissez un nom','skin':'Mme','difficulty':'Normal','class':'Chimiste'}
                    self.globalVariables[0] = 'Menu'
                    self.globalVariables[1] = 'Title'
                    self.crtMenu = 'CharacSelect'
                    self.askDelete = False

                if button == 'InfirmDelete':
                    self.askDelete = False


            elif button == 'GoBack':
                if self.crtMenu in ('Title', 'NewSavedGame', 'LoadSavedGame', 'Options', 'CharacSelect'):
                    self.crtMenu = 'Title'

                if self.crtMenu in ('Inventory', 'SkillsOverview'):
                    self.crtMenu = 'PauseMenu'

                if self.crtMenu in ('CompTrade','SkillsTrade','SkillsEquipement'):
                    self.globalVariables[0] = 'World'
                    self.globalVariables[1] = None



            elif self.crtMenu == 'Title':
                if button == 'NewSavedGame':
                    self.crtMenu = 'NewSavedGame'
                    self.openSavedGamesList()

                elif button == 'LoadSavedGame':
                    self.crtMenu = 'LoadSavedGame'
                    self.openSavedGamesList()


                elif button == 'Options':
                    self.optionsDict = self.Save.getOptions()
                    self.crtMenu = 'Options'

                elif button == 'Quit':
                    self.Music.Player.pause()
                    self.Window.close()
                    print(self.globalVariables, 'Button pressed: Window closed with "Quit" button')



            elif self.crtMenu == 'CharacSelect':
                if button == 'CreateNewGame':
                    if self.characterSettings['name'] != 'Choisissez un nom':
                        self.newGame()

                elif button == 'NameSelectLabel':
                    self.textInput = (True, button)
                    if self.characterSettings['name'] == 'Choisissez un nom':
                        self.characterSettings['name'] = ''
                else:
                    characDictList = {'class':      self.classList,
                                      'difficulty': self.diffList,
                                      'skin':       self.skinList}

                    for pref, characPrefDict in characDictList.items():
                        for option, buttonID in characPrefDict.items():
                            if button == buttonID:
                                self.characterSettings[pref] = option



            elif self.crtMenu == 'PauseMenu':
                if button == 'QuitGame':
                    self.crtMenu = 'Title'
                    self.globalVariables[0] = 'Menu'
                    self.globalVariables[1] = 'Title'

                elif button == 'SkillsOverview':
                    self.crtMenu == 'SkillsOverview'
                    self.openSkillsOverview()

                elif button == 'Inventory':
                    self.crtMenu = 'Inventory'
                    self.openInventory()

                elif button == 'Resume':
                    self.globalVariables[0] = 'World'
                    self.globalVariables[1] = None
                    # self.openSkillsEquipement()
                    # self.openCompTrade()

                elif button == 'SaveGame':
                    self.saveGame()



            elif self.crtMenu == 'Options':
                if button == 'FullScreenOption':
                    # optionButtonObj = self.buttons[button]
                    self.optionDict = self.Save.getOptions()

                    newChoice = str(self.optionsDict['fullscreen'] in ('False', False))

                    self.optionsDict['fullscreen'] = newChoice
                    self.Save.saveOptions(self.optionsDict)


                elif button == 'KeyControlOption':
                    # optionButtonObj = self.buttons[button]
                    crtOption = self.optionsDict['controls']

                    possibleChoices = ('Flèches', 'ZQSD', 'WASD')
                    try:
                        newChoice = possibleChoices[ (possibleChoices.index(crtOption) + 1) % len(possibleChoices)]
                    except ValueError:
                        newChoice = 'ZQSD'

                    self.optionsDict['controls'] = newChoice


                elif button == 'ResolutionOption':
                    crtOption = self.optionsDict['resolution']

                    possibleChoices = ('256x144','640x360','854x480','1280x720','1600x900')

                    try:
                        newChoice = possibleChoices[ (possibleChoices.index(crtOption) + 1) % len(possibleChoices)]
                    except ValueError:
                        newChoice = '1600x900'
                        print(self.globalVariables, 'Option update: Resolution: Value not in stock:', crtOption)

                    self.optionsDict['resolution'] = newChoice


                elif button == 'ApplySettings':
                     self.Save.saveOptions(self.optionsDict)
                     print(self.globalVariables, 'Option update: New settings applied and saved')
                     self.Save.resizeWindow()


            elif self.crtMenu == 'SkillsEquipement':
                if button == 'NextPage' and self.crtPage+1 < self.maxPages:
                    self.crtPage += 1
                    self.refreshSkillsEquipement()
                elif button == 'PrevPage' and 0 < self.crtPage:
                    self.crtPage -= 1
                    self.refreshSkillsEquipement()


                whitelist = [f'DelSkill{i}' for i in range(1,5)]
                if button in whitelist:
                    self.modifiedSkills = self.SpellList.SupprimerSortActuel(whitelist.index(button), self.modifiedSkills)
                    self.refreshSkillsEquipement()


                whitelist = [f'SkillB{i}' for i in range(1,7)]
                if button in whitelist and self.SpellList.AjoutSortPossible(self.modifiedSkills):

                    IDPagesList = self.SpellList.ListeSortAppris()[1]
                    ID = IDPagesList[self.crtPage][whitelist.index(button)]

                    newIDList = self.SpellList.AjoutSort(str(ID), self.modifiedSkills)

                    self.modifiedSkills = self.getSkillFromID(newIDList)
                    self.refreshSkillsEquipement()

                if button == 'ApplySkills':
                    allowApply, moneyDue = self.SpellList.Validation(self.loadEquipedSkills(), self.modifiedSkills, self.Player.money)
                    if allowApply:
                        self.Player.skills = [skill.Id for skill in self.modifiedSkills]
                        self.Player.money -= moneyDue
                        self.openSkillsEquipement()



            elif self.crtMenu == 'CompTrade':
                if button == 'BuyCountUp':
                    self.buyList[self.selectedComp] += 1

                elif button == 'BuyCountDown':
                    if self.buyList[self.selectedComp] > 0:
                        self.buyList[self.selectedComp] -= 1

                elif button == 'CompBuy':
                    buyCond, totPrice, compPrice = self.Inventory.ArgentSuffisant(self.Player.money, self.buyList)

                    if buyCond:
                        self.Player.money -= totPrice
                        self.Inventory.Achat(self.buyList)
                        self.openCompTrade()


            elif self.crtMenu == 'Inventory':
                buttonIDList = ('CalcUpgrade','OsciUpgrade','PerTUpgrade','MotoUpgrade','BookUpgrade','TireUpgrade','CompUpgrade')

                if button in buttonIDList:
                    objID = '0' + str(buttonIDList.index(button))

                    if self.Inventory.ComposantSuffisant(objID)[2] == True:
                        self.Inventory.Ameliorer(objID)
                        self.openInventory()


            elif self.crtMenu == 'NewSavedGame':
                if button in ('GameFile1','GameFile2','GameFile3'):
                    self.gameFile = int(button[-1])
                    self.askDelete = True


            elif self.crtMenu == 'LoadSavedGame':
                if button in ('GameFile1','GameFile2','GameFile3'):
                    self.gameFile = int(button[-1])
                    self.loadGame()


    def on_mouse_motion(self, x, y, dx, dy):
        """
        To call with the on_mouse_motion(x,y,dx,dy) method in the main program

        Returns
        -------
        None.
        """
        if self.globalVariables[0] == 'Menu':

            buttonTest = self.getButton(x, y)
            for button in self.buttons.values():
                button.highlight = False

            if buttonTest != None:
                button = self.buttons[buttonTest]
                button.highlight = True

            whitelist = ['Skill' + str(i) for i in range(1,5)] + ['SkillB' + str(i+1) for i in range(0,6)]
            if buttonTest in whitelist:
                self.showSkillDescription( whitelist.index(buttonTest) )

            whitelist = ('FormBuyLabel','WireBuyLabel','ElemBuyLabel','GearBuyLabel','PageBuyLabel','HairBuyLabel','CircBuyLabel',
                                            'FormBuyCount','WireBuyCount','ElemBuyCount','GearBuyCount','PageBuyCount','HairBuyCount','CircBuyCount',
                                            'FormCrtCount','WireCrtCount','ElemCrtCount','GearCrtCount','PageCrtCount','HairCrtCount','CircCrtCount',
                                            'FormBuyCost', 'WireBuyCost','ElemBuyCost','GearBuyCost','PageBuyCost','HairBuyCost','CircBuyCost',)
            if buttonTest in whitelist:
                self.selectedComp = (whitelist.index(buttonTest) % 7)
                self.buttons['BuyCountUp'].y = 700 - 75 * self.selectedComp
                self.buttons['BuyCountDown'].y = 700 - 75 * self.selectedComp


    def on_key_press(self, symbol, modifiers):
        """
        To call with the on_key_press(self, symbol, modifiers) method in the main program

        Returns
        -------
        None.
        """
        if self.globalVariables[0] == 'Menu':

            #print(key.symbol_string(symbol), key.modifiers_string(modifiers))
            if symbol == key.ESCAPE:

                if self.askDelete:
                    self.askDelete = False

                elif self.crtMenu in ('Title', 'NewSavedGame', 'LoadSavedGame', 'Options', 'CharacSelect','Credits'):
                    self.crtMenu = 'Title'

                elif self.crtMenu in ('Inventory', 'SkillsOverview'):
                    self.crtMenu = 'PauseMenu'

                elif self.crtMenu in ('CompTrade','SkillsTrade','SkillsEquipement'):
                    self.globalVariables[0] = 'World'
                    self.globalVariables[1] = None


            if self.textInput[0] == True and isinstance(self.textInput[1], str):
                text = self.characterSettings['name']

                if symbol == key.ENTER:
                    self.characterSettings['name'] = text.strip()
                    self.textInput = (False, None)

                elif symbol == key.BACKSPACE:
                    if len(text) > 0:
                        text = text[:-1]
                elif len(text) <= 12:
                    if symbol == key.SPACE:
                        text += ' '
                    if symbol not in (key.CAPSLOCK, key.BACKSPACE, key.SPACE):
                        if key.symbol_string(symbol) in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                            if 'MOD_CAPSLOCK' not in key.modifiers_string(modifiers):
                                text += key.symbol_string(symbol).lower()
                            else:
                                text += key.symbol_string(symbol)

                self.characterSettings['name'] = text


    def on_draw(self):
        """
        To call with the on_draw() method in the main program

        Returns
        -------
        None.
        """
        self.scaleAll(self.getScale())

        if self.globalVariables[0] == 'Menu':

            if self.crtMenu == 'Title':             self.titleScreen()
            elif self.crtMenu == 'NewSavedGame':    self.newGameScreen()
            elif self.crtMenu == 'LoadSavedGame':   self.loadGameScreen()
            elif self.crtMenu == 'Options':         self.optionsScreen()
            elif self.crtMenu == 'Inventory':       self.inventoryScreen()
            elif self.crtMenu == 'PauseMenu':       self.pauseScreen()
            elif self.crtMenu == 'Credits':         self.creditsScreen()
            elif self.crtMenu == 'SkillsOverview':  self.skillsOverviewScreen()
            elif self.crtMenu == 'SkillsEquipement':self.skillsEquipementScreen()
            elif self.crtMenu == 'CompTrade':       self.compTradeScreen()
            elif self.crtMenu == 'CharacSelect':    self.characterSelectScreen()

            if self.askDelete: self.askDeleteBox()




    def openSavedGamesList(self):
        """
        Displays the basic information from all saved games in the game selection screen

        Returns
        -------
        None.
        """
        savedGames = self.Save.getSavedGamesStats()

        for i in range(1,4):
            button = self.buttons['GameFile'+str(i)]
            gameStats = savedGames[i-1]

            # length = len( str( gameStats['Player'].get('name','N/A') ) )
            # tabNum = (12-length) // 4 - 1
            text = '   Nom: {}\n   Niveau: {}\n   Temps de jeu: {}'

            button.text = text.format(
                gameStats['Player'].get('name','N/A'),
                gameStats['Player'].get('lvl','N/A'),
                self.formHour( gameStats['Game'].get('time','N/A') ))




    def openInventory(self):
        """
        Opens inventory and updates the materials labels

        Returns
        -------
        None.
        """

        self.globalVariables[0] = 'Menu'
        self.globalVariables[1] = 'IGUIs'
        self.crtMenu = 'Inventory'

        # ('FormCount','WireCount','ElemCount','GearCount','PageCount','HairCount','CircCount')

        self.buttons['MoneyCount'].text = str(self.Player.money) + ' PC'

        upgradeLabel = ('CalcUpgrade','OsciUpgrade','PerTUpgrade','MotoUpgrade','BookUpgrade','TireUpgrade','CompUpgrade')
        countLabel = ('FormCount','WireCount','ElemCount','GearCount','PageCount','HairCount','CircCount')
        levelLabel = ('CalcLevel','OsciLevel','PerTLevel','MotoLevel','BookLevel','TireLevel','CompLevel')
        for i in range(0,7):

            objID = '0' + str(i)

            crtNum, reqNum, upAvailable = self.Inventory.ComposantSuffisant(objID)


            maxLevel = ''
            if upAvailable != 'MAX':
                maxLevel = '/20'
                reqStr = '/' + str(reqNum)
            else:
                self.buttons[upgradeLabel[i]].allowHighlight = False
                reqStr = ''

            self.buttons[levelLabel[i]].text =  str(self.Inventory.DicoInventaire[objID]) + maxLevel
            self.buttons[countLabel[i]].text = str(crtNum)  +  reqStr

            if  upAvailable == True:
                self.buttons[countLabel[i]].color = (200,250,200)
            elif upAvailable == 'MAX':
                self.buttons[countLabel[i]].color = (200,200,200)
                self.buttons[levelLabel[i]].color = (250,250,200)
            else:
                self.buttons[countLabel[i]].color = (250,200,200)


    def getSkillFromID(self, IDObj):
        """
        Converts every ID to the corresponding associated Sort object

        Parameters
        ----------
        IDObj : Str/List of Str
            ID/List of IDs of the Sort

        Returns
        -------
        TYPE
            Sort object / list of Sort objects
        """
        if IDObj == '@':
            return IDObj
        if isinstance(IDObj, str):
            return self.SpellList.ListeSort[ int( IDObj ) ]
        elif isinstance(IDObj, list):
            return [self.getSkillFromID(ID) for ID in IDObj]
        return IDObj



    def showSkillDescription(self, index):
        """
        Displays the skill description in the description Item object

        Parameters
        ----------
        index : int
            Index of the selected skill in the paged learned skill list.

        Returns
        -------
        None.
        """
        if index <= 3:
            SkillObj = self.modifiedSkills[index]

            if SkillObj == '@':
                return None

        else:
            pages, pagesList = self.SpellList.ListeSortAppris()

            if index-4 < len(pagesList[self.crtPage]):
                SkillObj = self.getSkillFromID( pagesList[self.crtPage][index-4] )
            else:
                return None

        name, speed, description = SkillObj.InfoAffichage()
        text = ''
        text += 'Nom: \t' + name + '\n\n'
        text += 'Vitesse: ' + speed + '\n\n'
        self.buttons['SkillDescription'].text = text + 'Description:\n\n' + description



    def loadEquipedSkills(self):
        """
        Loads the list of currently equiped skills objects

        Returns
        -------
        equipedSkills : list
            List of equiped skill objects.
        """
        equipedSkills = []

        indList = self.Player.skills
        for i in range(0,4):
            if len(indList) - (i+1) >= 0:
                equipedSkills.append( self.getSkillFromID( indList[i] ) )
            else:
                equipedSkills.append('@')

        return equipedSkills


    def openSkillsOverview(self):
        """
        Opens skill overview and statistics screen

        Returns
        -------
        None.
        """
        self.globalVariables[0] = 'Menu'
        self.globalVariables[1] = 'IGUIs'
        self.crtMenu = 'SkillsOverview'

        self.modifiedSkills = self.loadEquipedSkills()
        self.buttons['MoneyCount'].text = str(self.Player.money) + ' PC'

        for i in range(0,4):
            if self.modifiedSkills[i] != '@':
                self.buttons[f'Skill{i+1}'].text = self.modifiedSkills[i].Nom
        #{"stats" : {
        # "damage":self.damage,
        # "dodge":self.dodge,
        # "heal":self.heal,
        # "defense":self.defense,
        # "aptDebuff":self.aptDebuff,
        # "resistanceDebuff":self.resistanceDebuff,
        # "crits":self.crits,
        # "hp":self.hp,
        # "hpMax":self.hpMax},
        # pv, pvmax, degats, defense, soin -> flat
        # crit, dodge, resistance, vulnerabilité -> pourcentage
        statLabel = {'HpStat':          ('flat',     '\tVie'     ,self.Player.hp),
                     'HpMaxStat':       ('flat',     '\tVie max'       ,self.Player.hpMax),
                     'HealStat':        ('flat',     '\tSoin'     ,self.Player.heal),
                     'DamageStat':      ('flat',     '\tDégâts'   ,self.Player.damage),
                     'CritsStat':       ('percent',  '\tCritiques'   ,self.Player.crits),
                     'DodgeStat':       ('percent',  '\tEsquive'   ,self.Player.dodge),
                     'DefenseStat':     ('flat',     '\tDefense'   ,self.Player.defense),
                     'AptDebuffStat':   ('percent',  '\tVulnérabilité'   ,self.Player.aptDebuff),
                     'ResisDebuffStat': ('percent',  '\tRésistance'   ,self.Player.resistanceDebuff),
                     }
        for buttonID, valInfo in statLabel.items():
            if valInfo[0] == 'flat':
                self.buttons[buttonID].text = '     ' + self.strLenFormat(str(valInfo[2]),10) + valInfo[1]
            elif valInfo[0] == 'percent':
                self.buttons[buttonID].text = '     ' + self.strLenFormat(str(valInfo[2]),10) + '%' + valInfo[1]


    def openSkillsEquipement(self):
        """
        Opens skill equipement screen

        Returns
        -------
        None.
        """
        self.globalVariables[0] = 'Menu'
        self.globalVariables[1] = 'IGUIs'
        self.crtMenu = 'SkillsEquipement'

        self.crtPage = 0
        self.modifiedSkills = self.loadEquipedSkills()
        self.maxPages, self.learnedSkills = self.SpellList.ListeSortAppris()

        self.refreshSkillsEquipement()


    def refreshSkillsEquipement(self):
        """
        Refreshes skill equipement screen

        Returns
        -------
        None.

        """
        self.globalVariables[0] = 'Menu'
        self.globalVariables[1] = 'IGUIs'
        self.crtMenu = 'SkillsEquipement'

        cost = self.SpellList.Validation(self.loadEquipedSkills(), self.modifiedSkills, self.Player.money)[1]

        self.buttons['ApplySkillsCost'].text='{}/{} PC'.format(cost, self.Player.money)

        self.buttons['MoneyCount'].text = str(self.Player.money) + ' PC'
        self.buttons['PageNumber'].text = 'Page {}/{}'.format(self.crtPage+1, self.maxPages)

        for i in range(0,4):
            if self.modifiedSkills[i] != '@':
                self.buttons[f'Skill{i+1}'].text = self.modifiedSkills[i].Nom
            else:
                self.buttons[f'Skill{i+1}'].text = ''

        for i in range(0,6):
            if i < len(self.learnedSkills[self.crtPage]):
                SkillObj = self.getSkillFromID( self.learnedSkills[self.crtPage][i] )
                self.buttons[f'SkillB{i+1}'].text = SkillObj.Nom
            else:
                self.buttons[f'SkillB{i+1}'].text = ''

    def openCompTrade(self):
        """
        Opens component trade screen

        Returns
        -------
        None.
        """
        self.globalVariables[0] = 'Menu'
        self.globalVariables[1] = 'IGUIs'
        self.crtMenu = 'CompTrade'

        self.buttons['MoneyCount'].text = str(self.Player.money) + ' PC'

        self.buyList = [0]*7

        crtCompCountLabel = ('FormCrtCount','WireCrtCount','ElemCrtCount','GearCrtCount','PageCrtCount','HairCrtCount','CircCrtCount',)

        for i in range(0,7):

            objID = str(i+7)
            if int(objID)<10:
                objID = "0" + str(objID)

            self.buttons[crtCompCountLabel[i]].text = str(self.Inventory.DicoInventaire[objID])


    def openPauseMenu(self):
        """
        Opens the Pause Menu

        Returns
        -------
        None.
        """
        if self.globalVariables[0] == 'World':
            self.globalVariables[0] = 'Menu'
            self.globalVariables[1] = 'Pause'
            self.crtMenu = 'PauseMenu'
            self.Music.jouer_son('pause_press')





    def creditsRoll(self):
        """
        Lauches the credits screen

        Returns
        -------
        None.
        """

        self.globalVariables[0] = 'Menu'
        self.globalVariables[1] = 'Credits'
        self.crtMenu = 'Credits'
        
        if self.gameFile != 0:
            self.saveGame()


        file = open('resources/credits.txt','tr', encoding='utf-8')
        rawlines = file.readlines()
        file.close()
        
        
        
        self.menuItems['Credits'] = []

        for ind, line in enumerate(rawlines):
            if line.strip() != '':
                self.menuItems['Credits'].append('Credit ' + str(ind))
                self.buttons['Credit ' + str(ind)] = Item( x=600, y=0 - 30*(ind),
                                              text=line.strip(), text_color=(255,255,255,255),
                                              align_x='left')





    def loadImage(self, path2, mainFile='menus'):
        """
        Loads the image corresponding to the inputed path
        If said image is unavailable, will load the 'ErrorImage.png'

        Parameters
        ----------
        path2 : str
            Specific path to the image from the basic path: 'resources/images/menus/'.

        Returns
        -------
        Image : pyglet.sprite.Sprite
        """
        try:
            Image = pyglet.image.load(self.path + mainFile+'/' + path2)
        except:
            Image = pyglet.image.load(self.path +'menus/'+ 'ErrorImage.png')
            print(self.globalVariables, 'Failed to load image at', self.path +'menus/'+ path2)

        return Image


    def saveGame(self):
        """
        Saves the Inventory, Player, Skills and Game statistics in the selected gameFile.

        Returns
        -------
        None.
        """
        #self.Player.getStats
        gameFile=self.gameFile

        newRefTime = time.time()
        self.timeLoadGame['total'] += newRefTime - self.timeLoadGame['referenceTime']
        self.timeLoadGame['referenceTime'] = newRefTime

        tmp = self.Monde.forSave()
        tmp['time'] = self.timeLoadGame['total']
        self.Save.saveGameStats(gameFile, tmp)

        self.Save.savePlayerStats(gameFile, self.Player.savePlayer())
        self.Inventory.EnregistrerInv('saves/game-{}/Inventaire.txt'.format(str(self.gameFile)))
        self.SpellList.EnregistrerCompetence('saves/game-{}/Competences.txt'.format(str(self.gameFile)))

        print(self.globalVariables, 'game-{} saved'.format(gameFile))

    def loadGame(self):
        """
        Loads the Inventory, Player, Skills and Game statistics in the selected gameFile.

        Returns
        -------
        None.
        """
        gameFile=self.gameFile

        self.Inventory.DefInventaire('resources/Item.txt','saves/game-{}/Inventaire.txt'.format(str(self.gameFile)))
        self.SpellList.DefListeSort('saves/game-{}/Competences.txt'.format(str(self.gameFile)))

        playerData = self.Save.getPlayerStats(self.gameFile)
        self.Player.initPlayer(playerData["difficulty"],
                               playerData["stats"],
                               playerData["skills"],
                               playerData["achievements"],
                               playerData["classe"],
                               playerData["xp"],
                               playerData["maxXp"],
                               playerData["name"],
                               playerData["niveauS"],
                               playerData["lvl"],
                               playerData["depressed"],
                               playerData["money"])

        self.Inventory.Player = self.Player

        gameData = self.Save.getGameStats(self.gameFile)
        print(gameData)
        self.Monde.initSave(gameData)
        self.globalVariables[0] = 'World'
        self.globalVariables[1] = None

        self.timeLoadGame['referenceTime'] = time.time()
        self.timeLoadGame['total'] = gameData['time']

        print(self.globalVariables, 'game-{} loaded'.format(gameFile))


    def newGame(self):
        """
        Resets the Inventory, Player, Skills and Game statistics in the selected gameFile
        and loads the reseted game.

        Returns
        -------
        None.
        """
        gameFile=self.gameFile
        self.Inventory.ResetInventaire('saves/game-{}/Inventaire.txt'.format(str(self.gameFile)))
        self.Inventory.DefInventaire('resources/Item.txt','saves/game-{}/Inventaire.txt'.format(str(self.gameFile)))

        self.SpellList.DefListeSort('saves/game-{}/Competences.txt'.format(str(self.gameFile)))
        self.SpellList.ResetCompetence('saves/game-{}/Competences.txt'.format(str(self.gameFile)))

        #print(self.characterSettings['name'],self.characterSettings['class'],self.SpellList.ListeSortAppris()[1][0][:4] )

        diffCoeff = {'5/2':        0.8,
                      'Normal':     1,
                      'Majorant':   1.2}.get(self.characterSettings['difficulty'], 1)

        print(diffCoeff)
        self.Player.initPlayer(pDiff= float(diffCoeff),
                                pName=self.characterSettings['name'],
                               pClasse=self.characterSettings['class'][:3],
                               lSkills=self.SpellList.ListeSortAppris()[1][0][:4])

        self.Save.savePlayerStats(gameFile, self.Player.savePlayer())


        self.Monde.initSave(self.characterSettings['skin'])

        print(self.globalVariables, 'game-{} reseted'.format(gameFile))
        self.timeLoadGame['referenceTime'] = time.time()
        
        self.saveGame()

        self.globalVariables[0] = 'World'
        self.globalVariables[1] = None


    def askDeleteBox(self):
        """
        Displays the confirmation screen for deletion of a gameFile

        Returns
        -------
        None.
        """
        width, height = self.Window.get_size()
        body = pyglet.shapes.Rectangle(x=0,
                                       y=0,
                                       width= width,
                                       height= height,
                                       color = (160,160,160))
        body.opacity = 150
        body.draw()

        for buttonID in self.menuItems['AskDelete']:
            self.buttons[buttonID].draw()



    def titleScreen(self):
        titlePic = self.loadImage('title/TitleScreen.png' )
        titlePic = pyglet.sprite.Sprite(titlePic, x=0, y=0)
        titlePic.scale = self.getScale() * 5/6
        titlePic.draw()


        for buttonID in self.menuItems['Title']:
            self.buttons[buttonID].draw()


    def newGameScreen(self):
        NewGameUI = self.loadImage('newGame/savedGamesUI.png')
        NewGameUI = pyglet.sprite.Sprite(NewGameUI, x=0, y=0)
        NewGameUI.scale = self.getScale() * 5/6
        NewGameUI.draw()

        for buttonID in self.menuItems['NewSavedGame']:
            self.buttons[buttonID].draw()


    def loadGameScreen(self):
        LoadGameUI = self.loadImage('loadGame/savedGamesUI.png')
        LoadGameUI = pyglet.sprite.Sprite(LoadGameUI, x=0, y=0)
        LoadGameUI.scale = self.getScale()* 5/6
        LoadGameUI.draw()

        for buttonID in self.menuItems['LoadSavedGame']:
            self.buttons[buttonID].draw()


    def inventoryScreen(self):
        InventoryUI = self.loadImage('inventory/InventoryUI.png')
        InventoryUI = pyglet.sprite.Sprite(InventoryUI, x=0, y=0)
        InventoryUI.scale = self.getScale()* 5/6
        InventoryUI.draw()

        for buttonID in self.menuItems['Inventory']:
            self.buttons[buttonID].draw()


    def optionsScreen(self):
        OptionsUI = self.loadImage('options/OptionsUI.png')

        OptionsUI = pyglet.sprite.Sprite(OptionsUI, x=0, y=0)
        OptionsUI.scale = self.getScale() * 5/6
        OptionsUI.draw()


        if self.optionsDict['fullscreen'] in ('True', True):
            self.buttons['FullScreenOption'].text = 'OUI'
            self.buttons['FullScreenOption'].color = (160, 250, 160)
        else:
            self.buttons['FullScreenOption'].text = 'NON'
            self.buttons['FullScreenOption'].color = (250,160,160)


        self.buttons['KeyControlOption'].text = self.optionsDict['controls']

        self.buttons['ResolutionOption'].text = self.optionsDict['resolution']
        for buttonID in self.menuItems['Options']:
            self.buttons[buttonID].draw()


    def pauseScreen(self):
        width, height = self.Window.get_size()
        blurFilter = pyglet.shapes.Rectangle(x=0, y=0, width=width, height=height,color=(200,200,200))
        blurFilter.opacity = 100
        blurFilter.draw()

        for buttonID in self.menuItems['PauseMenu']:
            self.buttons[buttonID].draw()


    def creditsScreen(self):
        MemesBackGround = self.loadImage('Tableau_meme.png')

        MemesBackGround = pyglet.sprite.Sprite(MemesBackGround, x=0, y=0)
        MemesBackGround.scale = self.getScale()* 5/6
        MemesBackGround.draw()



        for buttonID in self.menuItems['Credits']:
            buttonObj = self.buttons[buttonID]
            buttonObj.y += 5

            if -60+200 <= buttonObj.y <= 900-100:
                buttonObj.draw()

        if self.buttons[ self.menuItems['Credits'][-1] ].y > 900-100:
            self.globalVariables[0] = 'Menu'
            self.globalVariables[1] = 'Title'
            self.crtMenu = 'Title'


    def skillsOverviewScreen(self):
        SkillsOverviewUI = self.loadImage('skills/SkillsOverviewUI.png')

        SkillsOverviewUI = pyglet.sprite.Sprite(SkillsOverviewUI, x=0, y=0)
        SkillsOverviewUI.scale = self.getScale()* 5/6
        SkillsOverviewUI.draw()

        descrText = self.buttons['SkillDescription']

        body = pyglet.shapes.Rectangle(x=       int(    (descrText.x - 10)*self.getScale()),
                                       y=       int(    (descrText.y - 475 +10)*self.getScale()), #475
                                       width=   int(    (420)*self.getScale()),
                                       height=  int(    (475)*self.getScale()),
                                       color=(250,250,250))
        body.draw()

        for buttonID in self.menuItems['SkillsOverview']:
            self.buttons[buttonID].draw()
#'SkillDescription': x=600, y=650, width=250, text=' Description:'),


    def skillsEquipementScreen(self):
        SkillsEquipementUI = self.loadImage('skills/SkillsEquipementUI.png')

        SkillsEquipementUI = pyglet.sprite.Sprite(SkillsEquipementUI, x=0, y=0)
        SkillsEquipementUI.scale = self.getScale() * 5/6
        SkillsEquipementUI.draw()

        descrText = self.buttons['SkillDescription']

        body = pyglet.shapes.Rectangle(x=       int(    (descrText.x - 10)*self.getScale()),
                                       y=       int(    (descrText.y - 475 + 10)*self.getScale()),
                                       width=   int(    (420)*self.getScale()),
                                       height=  int(    (475)*self.getScale()),
                                       color=(250,250,250))
        body.draw()


        if self.loadEquipedSkills() == self.modifiedSkills:
            self.buttons['ApplySkills'].color = (160, 160, 160)
        elif self.SpellList.Validation(self.loadEquipedSkills(), self.modifiedSkills, self.Player.money)[0]:
            self.buttons['ApplySkills'].color = (160, 250, 160)
        else:
            self.buttons['ApplySkills'].color = (250,160,160)


        for buttonID in self.menuItems['SkillsEquipement']:
            self.buttons[buttonID].draw()



    def compTradeScreen(self):
        CompTradeUI = self.loadImage('/componentTrade/ComponentTradeUI.png')

        CompTradeUI = pyglet.sprite.Sprite(CompTradeUI, x=0, y=0)
        CompTradeUI.scale = self.getScale() * 5/6
        CompTradeUI.draw()

        buyCountLabel = ('FormBuyCount','WireBuyCount','ElemBuyCount','GearBuyCount','PageBuyCount','HairBuyCount','CircBuyCount',)
        buyCostLabel = ('FormBuyCost', 'WireBuyCost','ElemBuyCost','GearBuyCost','PageBuyCost','HairBuyCost','CircBuyCost',)

        buyCond, totPrice, compPrice = self.Inventory.ArgentSuffisant(self.Player.money, self.buyList)

        self.buttons['CompBuyCost'].text='{}/{} PC'.format(totPrice, self.Player.money)

        for i in range(0,7):
            buyCount = self.buyList[i]
            self.buttons[buyCountLabel[i]].text = str(buyCount)
            self.buttons[buyCostLabel[i]].text = str(self.form10(compPrice[i]))  + ' PC'

        if self.buyList == [0]*7:
            self.buttons['CompBuy'].color = (160, 160, 160)
        elif buyCond:
            self.buttons['CompBuy'].color = (160, 250, 160)
        else:
            self.buttons['CompBuy'].color = (250,160,160)


        for buttonID in self.menuItems['CompTrade']:
            self.buttons[buttonID].draw()


    def characterSelectScreen(self):
        CharacterSelectUI = self.loadImage('/characterSelect/CharacterSelectUI.png')

        CharacterSelectUI = pyglet.sprite.Sprite(CharacterSelectUI, x=0, y=0)
        CharacterSelectUI.scale = self.getScale() * 5/6
        CharacterSelectUI.draw()

        self.buttons['NameSelectLabel'].text = self.characterSettings['name']

        if self.textInput == (True, 'NameSelectLabel'):
            self.buttons['NameSelectLabel'].allowHighLight = False
        else:
            self.buttons['NameSelectLabel'].allowHighLight = True


        for option, value in self.characterSettings.items():

            if option == 'difficulty':
                for difficulty, buttonID in self.diffList.items():
                    if value == difficulty:
                        self.buttons[ buttonID ].color = (250,250,200)
                    else:
                        self.buttons[ buttonID ].color = (200,200,200)

            elif option == 'skin':
                for skin, buttonID in self.skinList.items():
                    if value == skin:
                        self.buttons[ buttonID ].color = (250,250,200)
                        # SkinFace = self.loadImage()
                        # SkinFace = pyglet.sprite.Sprite(SkinFace, x=200, y=200)
                        # SkinFace.scale = self.getScale()
                        # SkinFace.draw()
                    else:
                        self.buttons[ buttonID ].color = (200,200,200)

            elif option == 'class':
                for playerClass, buttonID in self.classList.items():
                    if value == playerClass:
                        self.buttons[ buttonID ].color = (250,250,200)
                    else:
                        self.buttons[ buttonID ].color = (200,200,200)



        for buttonID in self.menuItems['CharacSelect']:
            self.buttons[buttonID].draw()





class Item():
    def __init__(self, x, y, width=0, height=0, text='', color='Auto', text_color='Auto',
                 imagePath=None,
                 multiline=False,
                 align_x='center', align_y='center', allowHighlight=True):

        self.x = x
        self.y = y
        self.height = height
        self.width = width

        self.anchor_x = align_x
        self.anchor_y = align_y

        self.text = text
        self.scale = 1

        self.color = color
        if color == 'Auto':
            self.color = (220,220,220)

        self.textColor = text_color
        if text_color == 'Auto':
            self.textColor = (0,0,0,255)
            if height==0 or width==0:
                self.textColor = (255,255,255,255)

        #print(self.text,self.width, self.height, self.text_color)

        self.allowHighlight = allowHighlight
        self.highlight = False

        self.multiline = multiline

        self.Image = None
        if imagePath != None:
            self.Image = self.Image = pyglet.image.load(imagePath)
            self.width = self.Image.width
            self.height = self.Image.height

    def getX(self):
        return int(self.x * self.scale)

    def getY(self):
        return int(self.y * self.scale)

    def getHeight(self):
        return int(self.height * self.scale)

    def getWidth(self):
        return int(self.width * self.scale)

    def draw(self):

        if self.Image != None:
            ButtonImage = pyglet.sprite.Sprite(self.Image, x=self.getX(), y=self.getY())
            ButtonImage.scale = self.scale
            ButtonImage.draw()



        else:

            body = pyglet.shapes.Rectangle(x = self.getX(),
                                           y = self.getY(),
                                           width = self.getWidth(),
                                           height = self.getHeight(),
                                           color = self.color)
            body.draw()

            if self.anchor_x == 'left':
                textX = self.getX()
            else:
                textX = int(self.getX() + self.getWidth() / 2)

            if self.anchor_y == 'top':
                textY = int(self.getY())
            else:
                textY = int(self.getY() + self.getHeight() / 2)


            if self.multiline == True:
                width=self.width
            else:
                width=None

            label = pyglet.text.Label(  text=self.text,
                                        x = textX,
                                        y = textY,
                                        width=self.getWidth()*2,
                                        color = self.textColor,
                                        font_size= 20*self.scale,
                                        anchor_x=self.anchor_x,
                                        anchor_y=self.anchor_y,
                                        multiline=self.multiline)
            label.draw()

            if self.highlight and self.allowHighlight:
                highlight = pyglet.shapes.Rectangle(x = self.getX(),
                                                    y = self.getY(),
                                                    width = self.getWidth(),
                                                    height = self.getHeight(),
                                                    color = (230,230,230) )
                highlight.opacity = 75
                highlight.draw()

class Save():
    def __init__(self):
        self.Window = None

    def convertFromStr(self, rawStr):
        """
        Tries to convert an string back into its original value

        Parameters
        ----------
        rawStr : Str
            String to convert.

        Returns
        -------
        List/Dict/int/bool/float
            Corresponding value.
        """
        rawStr = rawStr.strip()

        try:
            return int(rawStr)
        except ValueError:
            try:
                return float(rawStr)
            except ValueError:
                    if rawStr == 'False':
                        return False

                    if rawStr == 'True':
                        return True

        try:
            if rawStr[0] == '[' and rawStr[-1] == ']':
                outList = []

                for value in rawStr[1:-1].split(','):
                    outList.append(self.convertFromStr(value))
                return outList

            elif rawStr[0] == '{' and rawStr[-1] == '}':
                outDict = {}

                for couple in rawStr[1:-1].split(','):
                    key, value = couple.split(':')
                    outDict[self.convertFromStr(key)] = self.convertFromStr(value)
                return outDict

            if rawStr[0] == "'" and rawStr[-1] == "'":
                outStr = rawStr[1:-1]
                return outStr
        except:
            pass

        return rawStr


    def getSavedGamesStats(self):
        """
        Reads and returns info about all 3 saved games
        """

        savedGamesStats = []
        for i in range(1,4):
            path = f'./saves/game-{i}/'
            dictStat = {'Player':self.readFileInDict( path+'playerStats.txt'),
                        'Game':  self.readFileInDict( path+'gameStats.txt' )}
            savedGamesStats.append(dictStat)
        return savedGamesStats


    def readFileInDict(self, path):
        """
        Reads and returns a dictionnary corresponding to all lines with each associated value
        """
        try:
            File = open(path, 'tr', encoding='utf-8')
            rawlines = File.readlines()
            File.close()
        except:
            return 'NoFile'

        while '\n' in rawlines:
            del rawlines[rawlines.index('\n')]

        #○print(rawlines)

        lineDict = {}
        for line in rawlines:
            data = line.strip().split(':', maxsplit=1)
            lineDict[ data[0].strip() ] = self.convertFromStr(data[1].strip())
        return lineDict


    def getPlayerStats(self, gameFile):
        path = 'saves/game-' + str(gameFile) + '/playerStats.txt'
        return self.readFileInDict(path)


    def getGameStats(self, gameFile):
        path = 'saves/game-' + str(gameFile) + '/gameStats.txt'
        return self.readFileInDict(path)


    def getOptions(self):
        path = 'options.txt'
        return self.readFileInDict(path)


    def saveOptions(self, rawOptions):
        savedOptions = self.getOptions()

        writeOptions = ''

        for optionName in savedOptions.keys():

            optionGet = rawOptions.get(optionName, 'N/A')

            if optionGet != 'N/A':
                writeOptions += str(optionName) + ': ' + str(optionGet) + '\n'

        file = open('options.txt', 'wt', encoding='utf-8')
        file.seek(0)
        file.write(writeOptions[:-1])
        file.close()


    def savePlayerStats(self, gameFile, statsDict):
        writePlayerStats = ''

        for playerStatID, value in statsDict.items():
            writePlayerStats += str(playerStatID) + ': ' + str(value) + '\n'

        #print(writePlayerStats)

        file = open('saves/game-' + str(gameFile) + '/playerStats.txt', 'wt', encoding='utf-8')
        file.seek(0)
        file.write(writePlayerStats[:-1])
        file.close()



    def saveGameStats(self, gameFile, statsDict):
        writeGameStats = ''

        for gameStatID, value in statsDict.items():
            writeGameStats += str(gameStatID) + ': ' + str(value) + '\n'

        #print(writeGameStats)

        file = open('saves/game-' + str(gameFile) + '/gameStats.txt', 'wt', encoding='utf-8')
        file.seek(0)
        file.write(writeGameStats[:-1])
        file.close()


    def createWindow(self):
        """
        Creates the main app window according to the saved settings

        Returns
        -------
        Window : pyglet Window ovject
            Window root.
        """

        #screenX, screenY = GetSystemMetrics(0), GetSystemMetrics(1)

        options = self.getOptions()
        width, height = options['resolution'].split('x')
        fullscreen = (options['fullscreen'] in (True, 'True'))

        Window = pyglet.window.Window(width=1600, height=900)

        if fullscreen:
            Window.set_size(self.screenSize()[0], self.screenSize()[1])
            Window.set_fullscreen(True)
        else:
            Window.set_fullscreen(False)
            Window.set_size(int(width), int(height))

        Window.set_icon(pyglet.image.load('resources/images/icon.png'))
        Window.set_caption('Prépa Wars')

        self.Window = Window

        return Window


    def resizeWindow(self):
        """
        Resizes the main app window or turns ON/OFF fullscreen

        Returns
        -------
        None
        """
        options = self.getOptions()
        width, height = options['resolution'].split('x')
        print('[Save] Window Uptdate: new resolution:', width + 'x' + height)

        fullscreen = options['fullscreen'] in ('True',True)

        if fullscreen:
            self.Window.set_size(self.screenSize()[0], self.screenSize()[1])
            self.Window.set_fullscreen(True)
        else:
            self.Window.set_fullscreen(False)
            self.Window.set_size(int(width), int(height))


    def screenSize(self):
        root = tkinter.Tk()
        screenX = root.winfo_screenwidth()
        screenY = root.winfo_screenheight()
        root.destroy()

        return screenX, screenY
