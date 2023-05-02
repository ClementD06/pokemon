import pygame
from tkinter.colorchooser import askcolor


#askcolor()
# initialisation de Pygame
pygame.init()

# définir la taille de la fenêtre
screen = pygame.display.set_mode((1280, 720))

# définir la couleur de fond
background_color = ("#DAAB3A")

# charger l'image
image = pygame.image.load("titre_pokemon.png")
image2 = pygame.image.load("sacha.png")

#definir taille de l'image
image2 = pygame.transform.scale(image2, (190, 360))

# définir la position de l'image
x = 100
y = 250

image_rect = image.get_rect()
image_rect.center = (640, 360)

image2_rect = image2.get_rect()
image2_rect.topleft = (x, y)

# définir les dimensions et la position du bouton
button_rect = pygame.Rect(535, 540, 250, 60)

# créer une police de caractères
button_font = pygame.font.SysFont("Showcard Gothic", 22)

# créer une surface de texte
text_surface = button_font.render("Lancer le jeu", True, (255, 255, 255))

# centrer le texte sur le bouton
text_rect = text_surface.get_rect(center=button_rect.center)

# boucle principale
running = True
while running:
    # vérifier si l'utilisateur a cliqué sur la croix pour fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # vérifier si la souris est dans les limites du bouton
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                print("Bouton cliqué !")

    # remplir l'écran avec la couleur de fond
    screen.fill(background_color)

    # dessiner l'image sur l'écran
    screen.blit(image, image_rect)
    screen.blit(image2, image2_rect)

    # dessiner le bouton sur l'écran
    pygame.draw.rect(screen, (120, 0, 0), button_rect, border_radius=80)

    # dessiner le texte sur le bouton
    screen.blit(text_surface, text_rect)

    # mettre à jour la fenêtre
    pygame.display.update()

# quitter Pygame
pygame.quit()
