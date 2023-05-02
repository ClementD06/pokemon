import pygame

#nitialisation de Pygame
pygame.init()

#définir la taille de la fenêtre et la couleur de fond
screen = pygame.display.set_mode((1280, 720))
background_color = ("#DAAB3A")

#charger les images et les redimensionner
image = pygame.transform.scale(pygame.image.load("titre_pokemon.png"), (640, 360))
image2 = pygame.transform.scale(pygame.image.load("sacha.png"), (190, 360))

#définir la position des images
image_rect = image.get_rect(center=screen.get_rect().center)
image2_rect = image2.get_rect(x=100, y=250)

#Définition des couleurs utilisées
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
GRIS = (128, 128, 128)

#Définition des dimensions de la fenêtre et de la police de caractères
LARGEUR, HAUTEUR = 1280, 720
police = pygame.font.Font(None, 36)

#Définition des libellés des boutons
textes = ["Lancer une partie", "Ajouter un Pokémon", "Accéder à son Pokédex", "Quitter"]

#définir les dimensions des boutons
largeur_bouton, hauteur_bouton = 200, 50

#boucle principale
while True:
# vérifier si l'utilisateur a cliqué sur la croix pour fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
# vérifier si la souris est dans les limites d'un bouton
        for i, rect in enumerate(bouton_rects):
            if rect.collidepoint(pygame.mouse.get_pos()):
                if i == 0:
                    print("Lancer une partie")
            elif i == 1:
                print("Ajouter un Pokémon")
            elif i == 2:
                print("Accéder à son Pokédex")
            elif i == 3:
                pygame.quit()
                exit()

        # remplir l'écran avec la couleur de fond
        screen.fill(background_color)

        # dessiner les images sur l'écran
        screen.blit(image, image_rect)
        screen.blit(image2, image2_rect)

        # dessiner les boutons sur l'écran
        bouton_rects = []
        x, y = (LARGEUR - 2 * largeur_bouton - 20) / 2, (HAUTEUR - 2 * hauteur_bouton - 20) / 2
        for texte in textes:
                rect = pygame.draw.rect(screen, GRIS, (x, y, largeur_bouton, hauteur_bouton))
                bouton_rects.append(rect)
                texte_surface = police.render(texte, True, NOIR)
                texte_rect = texte_surface.get_rect(center=rect.center)
                screen.blit(texte_surface, texte_rect)
                if rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(screen, BLANC, rect, 3)
                x += largeur_bouton + 20

# mettre à jour la fenêtre
    pygame.display.update()

    pygame.quit()