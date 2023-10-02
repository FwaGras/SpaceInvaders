import pygame # importation de la librairie pygame
import space
import sys # pour fermer correctement l'application

# lancement des modules inclus dans pygame
pygame.init()
pygame.font.init()

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
# chargement de l'image de fond
fond = pygame.image.load('background.png')

# creation du joueur
player = space.Joueur()
# creation de la balle
tir = space.Balle(player)
tir.etat = "chargee"
# creation des ennemis
listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)
    
    
### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond,(0,0))
    font = pygame.font.Font(None, 36) #met en place font (qui est un objet)

    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement
       
       # gestion du clavier
        if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la gauche
            if event.key == pygame.K_SPACE : # espace pour tirer
                player.tirer()
                tir.etat = "tiree"

    ### Actualisation de la scene ###
    # Gestions des collisions
    for ennemi in listeEnnemis:
        if tir.etat == "tiree" and tir.toucher(ennemi): #la balle tue seulement les ennemis si elle est tirée
            ennemi.disparaitre()
            player.marquer()
    
    for ennemi in listeEnnemis:
        if player.degats(ennemi):
            ennemi.disparaitre()
    
    
    #fait apparaître le score sur l'écran du jeu
    score_text = font.render(f'Score : {player.score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    #fait apparaître lenombre de vie sur l'écran du jeu
    life_text = font.render(f'PV : {player.vie}', True, (255, 0, 0))
    screen.blit(life_text,(10, 30))
    # placement des objets
    # le joueur
    player.deplacer()
    screen.blit(tir.image,[tir.depart,tir.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur        
    # la balle
    tir.bouger()
    screen.blit(player.image,[player.position,500]) # appel de la fonction qui dessine le vaisseau du joueur
    # les ennemis
    for ennemi in listeEnnemis:
        ennemi.avancer()
        screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
    # respawn des ennemis
    for ennemi in listeEnnemis:
        if ennemi.hauteur >= 600 :
            ennemi.disparaitre()
    # le game over
    game_over_text = font.render('GAME OVER', True, (255, 0, 0))
    restart_text = font.render('->Recommencer (R)', True, (255, 255, 255))
    leave_text = font.render('->Quitter (X)', True, (255, 255, 255))
    if player.vie == 0:
        running = False
        screen.blit(game_over_text,(325, 250))
        screen.blit(restart_text,(300, 300))
        screen.blit(leave_text,(300, 350))
        touches = pygame.key.get_pressed()
        if touches[pygame.K_r]:
            running = True
        if touches[pygame.K_x]:
            sys.exit()
        
    pygame.display.update() # pour ajouter tout changement à l'écran
