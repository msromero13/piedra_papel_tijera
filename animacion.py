# -*- coding: utf-8 -*-
import pygame
import math
import random
import time
import __init__

import printimagen

####
pygame.init()
####
def printimagen():
    pygame.draw.rect(pantalla,BLANCO,[0,100,700,100],100)
    imagentijeras = pygame.image.load("imagentijera.jpeg").convert()
    imagenpiedra = pygame.image.load("imagenpiedra.jpeg").convert()
    imagenpapel = pygame.image.load("imagenpapel.jpeg").convert()

    pantalla.blit(imagentijeras, [100, 100])
    pantalla.blit(imagenpapel, [300, 100])
    pantalla.blit(imagenpiedra, [500, 100])
def printcontador(victorias, derrotas):
    texto_contador_victorias = fuente.render("Victorias", True, NEGRO)
    contador_victorias = fuente.render(str(victorias), True, NEGRO)
    texto_contador_derrotas = fuente.render("Derrotas",True, NEGRO)
    contador_derrotas = fuente.render(str(derrotas),True, NEGRO)

    pantalla.blit(texto_contador_victorias, [0,430])
    pantalla.blit(contador_victorias, [40,460])
    pantalla.blit(texto_contador_derrotas, [590,430])
    pantalla.blit(contador_derrotas, [640,460])
###Colores
NEGRO   = (   0,   0,   0)
BLANCO  = ( 255, 255, 255)
VERDE   = (   0, 255,   0)
ROJO    = ( 255,   0,   0)
###

###Imprescindible pantalla
dimensiones = (700, 500)
pantalla = pygame.display.set_caption("Piedra, Papel, Tijera")
pantalla = pygame.display.set_mode(dimensiones)
reloj = pygame.time.Clock()
fuente = pygame.font.Font(None, 35)

hecho = False
pantalla.fill(BLANCO)
###
printcontador(0,0)
printimagen()
pygame.display.flip()

numeroderrotas = 0
numerovictorias = 0
while hecho == False:
    ###Bucle salida
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho= True
    ###

    pos = pygame.mouse.get_pos()
    x = pos [0]
    y = pos [1]
    
    opciones = ["piedra", "papel", "tijeras"]
    random_index = random.randrange(3)
    rival = opciones[random_index]
    respuesta=""

    if evento.type == pygame.MOUSEBUTTONDOWN or evento.type == pygame.KEYDOWN:
        
        pygame.display.flip()
        if y >=100 and y<=200:
        
            if x>=100 and x<=200 and evento.type == pygame.MOUSEBUTTONDOWN:
               # pantalla.blit(imagentijerasver, [100,100])
                respuesta = "tijeras"
            
            elif x>=300 and x<=400 and evento.type == pygame.MOUSEBUTTONDOWN:
               # pantalla.blit(imagenpapelver, [300,100])
                respuesta = "papel"
            elif x>=500 and x<=600 and evento.type == pygame.MOUSEBUTTONDOWN:
               # pantalla.blit(imagenpiedraver, [500,100])
                respuesta = "piedra"

                
        if respuesta == "papel":
            if rival == "piedra":
                resultado = "victoria"
            elif rival == "tijeras":
                resultado = "derrota"
            else:
                resultado = "empate"

        elif respuesta == "piedra":
            if rival == "tijeras":
                resultado = "victoria"
            elif rival == "papel":
                resultado = "derrota"
            else:
                resultado = "empate"

        elif respuesta == "tijeras":
            if rival == "papel":
                resultado = "victoria"
            elif rival == "piedra":
                resultado = "derrota"
            else:
                resultado = "empate"
                
        victoria = fuente.render("VICTORIA",True,NEGRO)
        derrota = fuente.render("DERROTA",True,NEGRO)
        empate = fuente.render("EMPATE",True,NEGRO)
        if resultado == "victoria":
            pantalla.fill(VERDE)
            printimagen()
            pantalla.blit(victoria, [280,400])
            numerovictorias += 1
        elif resultado == "derrota":
            pantalla.fill(ROJO)
            printimagen()
            pantalla.blit(derrota, [280,400])
            numeroderrotas += 1
        elif resultado == "empate":
            pantalla.fill(BLANCO)
            pantalla.blit(empate, [280,400])
            
        if respuesta != "":
            texto1 = fuente.render(str(respuesta),True, NEGRO)
            texto2 = fuente.render("VS",True, NEGRO)
            texto3 = fuente.render(str(rival),True,NEGRO)

            pantalla.blit(texto1, [200,300])
            pantalla.blit(texto2, [320,300])
            pantalla.blit(texto3, [400,300])

        printimagen()    
        printcontador(numerovictorias, numeroderrotas)    
        reloj.tick(30)
        pygame.display.flip()
        time.sleep(0.7)
    
pygame.quit()

