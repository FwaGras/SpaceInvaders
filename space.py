import pygame  # necessaire pour charger les images et les sons
import random
import math

class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.position = 400
        self.image = pygame.image.load("Batter-battlesprite.png")
        self.sens = "O"
        self.vitesse = 12
        self.score = 0
        self.vie = 2

    def deplacer(self) :
        if (self.sens == "droite") and (self.position < 740):
            self.position = self.position + self.vitesse
        elif (self.sens == "gauche") and (self.position > 0):
            self.position = self.position - self.vitesse
           
    def tirer(self):
        self.sens = "O"
        
    def marquer(self):
        self.score += 1
        
    def degats(self, vaisseau):
        delta_x = self.position - vaisseau.depart
        delta_y = 500 - vaisseau.hauteur
        d2 = delta_x **2 + delta_y **2
        if d2 < 360 : 
            self.vie -= 1
            return True
        
        
class Balle() : # classe pour créer la balle du joueur
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.position + 16
        self.hauteur = 492
        self.image = pygame.image.load("Ballebaseball.png.png")
        self.etat = "chargee"
        self.vitesse = 20
    
    def bouger(self):
        if self.etat == "chargee": #permet à l'image de la balle de se déplacer avec le joueur
            self.depart = self.tireur.position + 16
            self.hauteur = 492
        elif self.etat == "tiree" :
            self.hauteur = self.hauteur - self.vitesse
        
        if self.hauteur < 0:#la balle "revient" vers le joueur
            self.etat = "chargee"
            
    def toucher(self, vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40):
            self.etat = "chargee"
            return True
        
        
class Ennemi() : # classe pour créer le vaisseau ennemi
    NbEnnemis = 12
    def __init__(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if  (self.type == 1):
            self.image = pygame.image.load("Commonspectre1.png")
            self.vitesse = 10
        elif (self.type ==2):
            self.image = pygame.image.load("Fatspectre.png")
            self.vitesse = 14
            
    def avancer(self):
        self.hauteur = self.hauteur + self.vitesse
    
    def disparaitre(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if  (self.type == 1):
            self.image = pygame.image.load("Commonspectre1.png")
            self.vitesse = 10
        elif (self.type ==2):
            self.image = pygame.image.load("Fatspectre.png")
            self.vitesse = 14
    
    
    
        
        
    
    