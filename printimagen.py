import pygame
pantalla = pygame.display.set_caption("Piedra, Papel, Tijera")
def printimagen():
    imagentijeras = pygame.image.load("imagentijera.jpeg").convert()
    imagenpiedra = pygame.image.load("imagenpiedra.jpeg").convert()
    imagenpapel = pygame.image.load("imagenpapel.jpeg").convert()
    imagenpapelver = pygame.image.load("imagenpapelverde.jpg").convert()

    pantalla.blit(imagentijeras, [100, 100])
    pantalla.blit(imagenpapel, [300, 100])
    pantalla.blit(imagenpiedra, [500, 100])
