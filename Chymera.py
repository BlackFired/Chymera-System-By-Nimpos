import sys
import subprocess
import pygame
import os
from pygame.locals import *
def abrir():
	subprocess.call ("mugen.exe -log nimpos.txt -p1 tndhashirama -p2 tndkabuto -p2.ai 8 -rounds 1 -s planicie");
pygame.init() #Inicia el modulo pygame
screen = pygame.display.set_mode((640,480)) #Crea la ventana del juego y devuelve la surface de la misma
pygame.display.set_caption("NSBP") #Pone el titulo de la ventana
pygame.key.set_repeat(10,30) #Esta var sirve para el bucle del juego
game = True #Este objeto sirve para manejar el flujo del juego
timer = pygame.time.Clock()
#Imagenes
Main = pygame.image.load('imagenes/bg.png')
#Bucle del juego
while game:
	#Ajusta el juego a 30 FPS y devuelve el tiempo entre cada ciclo
	dtime = timer.tick(10)

	for event in pygame.event.get(): #Manejo de eventos
		if event.type == QUIT: sys.exit(0) #Cierra el juego
		if event.type == KEYDOWN: #Manejo de pulsaciones de teclas
			if event.key == K_ESCAPE: game = False #Rompe el bucle y el juego se cierra
			if event.key == K_RETURN: #Por ahora sera la única que usaremos
				abrir()
#Dibujar en la pantalla
screen.blit(Main,(0,0))
pygame.display.flip()
