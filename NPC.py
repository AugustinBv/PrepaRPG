import Quete


class NPC():
    def __init__(self):
        pass
    
    def iniNPC(self, pMonde, pName, pBasicDialog, pFunction='@'):
        self.name = pName
        self.dialogues = []
        self.quests = []
        self.idleDialog = pBasicDialog
        self.function = pFunction
        self.Monde = pMonde
        
    def linkQuest(self, pQuestId, pDialogList):
        self.quests.append(pQuestID)
        self.append(pDialogList)

    def talk(self):
        for questID in self.quests:
            if Quete.getQuestFromSkill(questID):
                pass
                
    
    
    