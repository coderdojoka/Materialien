from algorithmus import *
from arena import *


__author__ = 'Mark Weinreuter'

GRENZE = 50

def inv(richtung):
    if(richtung == OBEN):return UNTEN
    if(richtung == UNTEN): return OBEN
    if(richtung == RECHTS):return LINKS
    if(richtung == LINKS): return RECHTS

class DaC(Algorithmus):
    
    def gib_richtung(self, letzter_zustand):

        #Phase 0: Konfession festlegen
        if self.stufe == 0:
            if abs(self.x - 50) < abs(self.y - 50):
                self.konfession = 1
            print("Konfession:",self.konfession)
            self.stufe += 1

        #Phase zwei: Mitte finden
        if self.stufe == 1:
            if self.konfession == 1:
                if self.x > 50:
                    return LINKS
                if self.x < 50:
                    return RECHTS
                if self.x == 50:
                    self.stufe += 1
                    if(self.y >= 50):self.onedirection = UNTEN
                    if(self.y < 50):self.onedirection = OBEN 
            else:
                if self.y > 50:
                    return OBEN
                if self.y < 50:
                    return UNTEN
                if self.y == 50:
                    self.stufe += 1
                    if(self.x >= 50):self.onedirection = LINKS
                    if(self.x < 50):self.onedirection = RECHTS 

        #Phase drei: DIVIDE!!!                              
        if self.stufe == 2:
            if letzter_zustand != RAND and self.magischer == 0:
                return self.onedirection
            self.magischer += 1
            if self.magischer < 100:
                return inv(self.onedirection)
            if self.magischer < 150:
                return self.onedirection
            self.stufe += 1
            self.magischer = 0

        #Phase vier: DIVIDE some more!
        if self.stufe == 3:
            if self.konfession == 1:
                if self.magischer < 50:
                    self.magischer += 1
                    return RECHTS
                #print("Magischer1",self.magischer)
                if self.magischer < 150:
                    self.magischer += 1
                    return LINKS
                #print("Magischer2",self.magischer)
                self.magischer = 0
                self.onedirection = RECHTS
                self.stufe +=1
            else:
                if self.magischer < 50:
                    self.magischer += 1
                    return OBEN
                #print("Magischer1",self.magischer)
                if self.magischer < 150:
                    self.magischer += 1
                    return UNTEN
                #print("Magischer2",self.magischer)
                self.magischer = 0
                self.stufe +=1
    
        #Conquer!
        if self.stufe == 4:
            if self.konfession == 1:
                #Position ist links mitte, fuelle links unten
                if self.magischer == 0 and self.bubbericher%2 == 0:
                    self.bubbericher += 1
                    return UNTEN
                if self.magischer < 50:
                    self.magischer += 1
                    return RECHTS
                if self.magischer == 50 and self.bubbericher%2 == 1:
                    self.bubbericher += 1
                    return UNTEN
                if self.magischer < 99:
                    self.magischer +=1
                    return LINKS
                if self.magischer == 99 and self.bubbericher < 50:
                    self.magischer = 0
                    return LINKS
                if self.bubbericher == 50:
                    self.bubbericher = 0
                    self.magischer = 0
                    self.stufe += 1
                    return LINKS
            else:
                #Position ist unten mitte, fuelle rechts unten
                if self.magischer == 0 and self.bubbericher%2 == 0:
                    self.bubbericher += 1
                    return OBEN
                if self.magischer < 50:
                    self.magischer += 1
                    return RECHTS
                if self.magischer == 50 and self.bubbericher%2 == 1:
                    self.bubbericher += 1
                    return OBEN
                if self.magischer < 99:
                    self.magischer +=1
                    return LINKS
                if self.magischer == 99 and self.bubbericher < 50:
                    self.magischer = 0
                    return LINKS
                if self.bubbericher == 50:
                    self.bubbericher = 0
                    self.magischer = 0
                    self.stufe += 1
                    return LINKS
        #rearrange
        if self.stufe == 5:
            if self.konfession == 1:
                if self.magischer < 50:
                    self.magischer += 1
                    return OBEN
                self.magischer = 0
                self.stufe +=1

            else:
                if self.magischer < 50:
                    self.magischer += 1
                    return OBEN
                self.magischer = 0
                self.stufe +=1

        if self.stufe == 6:
            if self.konfession == 1:
                #Position ist links mitte, fuelle links oben
                if self.magischer == 0 and self.bubbericher%2 == 0:
                    self.bubbericher += 1
                    return OBEN
                if self.magischer < 50:
                    self.magischer += 1
                    return RECHTS
                if self.magischer == 50 and self.bubbericher%2 == 1:
                    self.bubbericher += 1
                    return OBEN
                if self.magischer < 99:
                    self.magischer +=1
                    return LINKS
                if self.magischer == 99 and self.bubbericher < 50:
                    self.magischer = 0
                    return LINKS
                if self.bubbericher == 50:
                    self.bubbericher = 0
                    self.magischer = 0
                    self.stufe += 1
                    return LINKS
            else:
                #Position ist oben mitte, fuelle rechts oben
                if self.magischer == 0 and self.bubbericher%2 == 0:
                    self.bubbericher += 1
                    return UNTEN
                if self.magischer < 50:
                    self.magischer += 1
                    return RECHTS
                if self.magischer == 50 and self.bubbericher%2 == 1:
                    self.bubbericher += 1
                    return UNTEN
                if self.magischer < 99:
                    self.magischer +=1
                    return LINKS
                if self.magischer == 99 and self.bubbericher < 50:
                    self.magischer = 0
                    return LINKS
                if self.bubbericher == 50:
                    self.bubbericher = 0
                    self.magischer = 0
                    self.stufe += 1
                    return LINKS

        #rearrange
        if self.stufe == 7:
            if self.konfession == 1:
                if self.magischer < 50:
                    self.magischer += 1
                    return RECHTS
                self.magischer = 0
                self.stufe +=1

            else:
                if self.magischer < 50:
                    self.magischer += 1
                    return LINKS
                self.magischer = 0
                self.stufe +=1

        if self.stufe == 8:
            if self.konfession == 1:
                #Position ist oben mitte, fuelle rechts oben
                if self.magischer == 0 and self.bubbericher%2 == 0:
                    self.bubbericher += 1
                    return UNTEN
                if self.magischer < 50:
                    self.magischer += 1
                    return RECHTS
                if self.magischer == 50 and self.bubbericher%2 == 1:
                    self.bubbericher += 1
                    return UNTEN
                if self.magischer < 99:
                    self.magischer +=1
                    return LINKS
                if self.magischer == 99 and self.bubbericher < 50:
                    self.magischer = 0
                    return LINKS
                if self.bubbericher == 50:
                    self.bubbericher = 0
                    self.magischer = 0
                    self.stufe += 1
                    return LINKS
            else:
                #Position ist links mitte, fuelle links oben
                if self.magischer == 0 and self.bubbericher%2 == 0:
                    self.bubbericher += 1
                    return OBEN
                if self.magischer < 50:
                    self.magischer += 1
                    return RECHTS
                if self.magischer == 50 and self.bubbericher%2 == 1:
                    self.bubbericher += 1
                    return OBEN
                if self.magischer < 99:
                    self.magischer +=1
                    return LINKS
                if self.magischer == 99 and self.bubbericher < 50:
                    self.magischer = 0
                    return LINKS
                if self.bubbericher == 50:
                    self.bubbericher = 0
                    self.magischer = 0
                    self.stufe += 1
                    return LINKS        

        #rearrange
        if self.stufe == 9:
            if self.konfession == 1:
                if self.magischer < 50:
                    self.magischer += 1
                    return UNTEN
                self.magischer = 0
                self.stufe +=1

            else:
                if self.magischer < 50:
                    self.magischer += 1
                    return UNTEN
                self.magischer = 0
                self.stufe +=1

        if self.stufe == 10:
            if self.konfession == 1:
                #Position ist unten mitte, fuelle rechts unten
                if self.magischer == 0 and self.bubbericher%2 == 0:
                    self.bubbericher += 1
                    return OBEN
                if self.magischer < 50:
                    self.magischer += 1
                    return RECHTS
                if self.magischer == 50 and self.bubbericher%2 == 1:
                    self.bubbericher += 1
                    return OBEN
                if self.magischer < 99:
                    self.magischer +=1
                    return LINKS
                if self.magischer == 99 and self.bubbericher < 50:
                    self.magischer = 0
                    return LINKS
                if self.bubbericher == 50:
                    self.bubbericher = 0
                    self.magischer = 0
                    self.stufe += 1
                    return LINKS
            else:
                #Position ist links mitte, fuelle links unten
                if self.magischer == 0 and self.bubbericher%2 == 0:
                    self.bubbericher += 1
                    return UNTEN
                if self.magischer < 50:
                    self.magischer += 1
                    return RECHTS
                if self.magischer == 50 and self.bubbericher%2 == 1:
                    self.bubbericher += 1
                    return UNTEN
                if self.magischer < 99:
                    self.magischer +=1
                    return LINKS
                if self.magischer == 99 and self.bubbericher < 50:
                    self.magischer = 0
                    return LINKS
                if self.bubbericher == 50:
                    self.bubbericher = 0
                    self.magischer = 0
                    self.stufe += 1
                    return LINKS                                        
        return OBEN
        # Überprüfen, ob wir nicht mehr weiter können
        if (self.counter == self.offset) or letzter_zustand == RAND or letzter_zustand == BELEGT:

            self.counter = 0
            random.seed()
            self.offset = random.randint(10, GRENZE)

            r = random.randint(0, 1)
            # Neue Richtung ermitteln, die NICHT die alte ist

            if self.richtung == RECHTS or self.richtung == LINKS:
                self.richtung = OBEN + r
            else:
                self.richtung = LINKS + r

        self.counter += 1
        return self.richtung

    def __init__(self):

        super().__init__("Zufall 1")
        self.counter = 0
        self.offset = random.randint(10, GRENZE)
        self.richtung = random.randint(1, 4)
        self.stufe = 0
        self.magischer = 0
        self.bubbericher = 0
        self.konfession = 0
        self.onedirection = 0
