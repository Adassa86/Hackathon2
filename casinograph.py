#importation des modules necessaires
import pygame
import numpy


pygame.init()

#creation d une fonction avec emplacement pour bien positionner les differents fruits
class emplacement(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
      super().__init__()
      self.image = pygame.image.load('picture/pomme_dore.jpg')
      self.rect = self.image.get_rect()
      self.rect.x = pos_x
      self.rect.y = pos_y

    def set_image (self, image):
      self.image = image

# lancement du jeu
def lancement():
      
    global jetons
   
    #choix au hasard selon les proba defini
    hasard = numpy.random.choice(fruits, 3 , p= proba_fruits)
    fruit_gauche = fruits_dict[hasard[0]]
    fruit_milieu =fruits_dict[hasard[1]]
    fruit_droite =fruits_dict[ hasard[2]]
  
    emplacement_gauche.set_image(fruit_gauche)
    emplacement_milieu.set_image(fruit_milieu)
    emplacement_droite.set_image(fruit_droite)

   
    #faire la verification des lots 
    if hasard[0] == hasard[1]== hasard[2]:
        fruit = hasard[0]
        jetons_gagnes = fruits_dict_gains[fruit]
        jetons += jetons_gagnes  
        print(f"ligne of {fruit}  a ete faite! + {jetons_gagnes} jetons ")

#creation de la fentre de la machine a sous 
largeur = 513
hauteur = 525
ecran = pygame.display.set_mode ((largeur, hauteur))
pygame.display.set_caption("Casino Game")
blanc = [ 255, 255, 255]
jetons = 800 

#dict de fruit
fruits_dict={
        "cerise": pygame.image.load('picture/cerise.png'),
        "ananas": pygame.image.load('picture/ananas.png'),
        "orange": pygame.image.load('picture/orange.png'),
        "pasteque":pygame.image.load('picture/pasteque.png'),
        "pomme_dore":pygame.image.load('picture/pomme_dore.jpg')
} 

#creation de probabilite pour apparition des fruits
fruits = [ "ananas" , "cerise" ,"orange", "pasteque", "pomme_dore"]
proba_fruits =[ 0.2, 0.25 , 0.4 , 0.1, 0.05]

    # faire un dictionnaire de fruits avec des valeurs pour les points 
fruits_dict_gains = {
      "orange" : 5,
      "cerise" : 15,
      "ananas": 50,
      "pasteque": 150, 
      "pomme_dore" : 10000
    }

# les emplacements
hauteur_emplacement = hauteur /3 +10
emplacement_x_milieu = largeur/3 + 50
emplacement_x_gauche = emplacement_x_milieu - 95
emplacement_x_droite = emplacement_x_milieu + 105

emplacements = pygame.sprite.Group()
emplacement_gauche = emplacement(emplacement_x_gauche, hauteur_emplacement)
emplacement_milieu = emplacement(emplacement_x_milieu, hauteur_emplacement)
emplacement_droite = emplacement(emplacement_x_droite, hauteur_emplacement)

#rangement des emplacement dans le group
emplacements.add (emplacement_gauche)
emplacements.add (emplacement_milieu)
emplacements.add (emplacement_droite)


#machine a sous photo 
fond = pygame.image.load('picture/photo.png')
police = pygame.font.SysFont("fantasy", 33 )

#on maintient la boucle tant que le jeu tourne tant qu il a des jetons 
running = True

#tant que l afenetre est en eveil alors fais touner le jeu 
#verifier que le joueur mn a pas fermer la fentre 
  #  si le joueur ferme la fenetre alors on va devoir fermer le jeu 
    # pour recuperer evenement qui se produise sur le jeu on va faire une boucle for qui va s appeler event 
    #pour voir si il ferme o  u pas la femetre 

while running:

    ecran.fill (blanc) 
    ecran.blit (fond, (0,0))
    emplacements.draw(ecran)
    
    text = police.render(str(jetons) + "jetons", True , (0,0,0))
    ecran.blit (text , (10,0))

    pygame.display.flip() 

    for event in pygame.event.get():
  
        if event.type == pygame.QUIT:
            running = False
            quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and jetons >= 10:
                 lancement() 
                 jetons -= 10 
      
                 #a chaque fois qu il joue c 10 jetons en moins ( c est le cout de la partie)