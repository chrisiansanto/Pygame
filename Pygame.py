#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys
import pygame
import random

#Contaste
Ancho = 800
Alto = 600
color_rojo = (255,0,0)
color_negro = (0,0,0)
color_azul = (0,0,255)

#jugador
jugadro_size = 50
jugadro_pos = [Ancho/2,Alto - jugadro_size * 2]

#enemigo
enemigo_size = 50
enemigo_pos = [random.randint(0, Ancho-enemigo_size),0]

#Ventana en pantalla
ventana = pygame.display.set_mode((Ancho,Alto))

game_over = False
clock = pygame.time.Clock()

def detectar_colision(jugador_pos,enemigo_pos):
    jx = jugador_pos[0]
    jy = jugador_pos[1]
    ex = enemigo_pos[0]
    ey = enemigo_pos[1]

    if (ex >= jx and ex < (jx + jugadro_size)) or (jx >= ex and jx <(ex + enemigo_size)):
        if (ey >= jy and ey < (jy + jugadro_size)) or (jy >= ey and jy <(ey + enemigo_size)):
            return True
        return False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = jugadro_pos[0]
            if event.key == pygame.K_LEFT:
                x -= jugadro_size
            if event.key == pygame.K_RIGHT:
                x += jugadro_size
            jugadro_pos[0] = x
    ventana.fill(color_negro)

    if enemigo_pos[1] >= 0 and enemigo_pos[1] < Alto:
        enemigo_pos[1] += 20
    else:
        enemigo_pos[0] = random.randint(0, Ancho - enemigo_size)
        enemigo_pos[1] = 0
    #Colisiones
    if detectar_colision(jugadro_pos, enemigo_pos):
        game_over = True
    #Dubujo de enemigo
    pygame.draw.rect(ventana, (color_azul), (enemigo_pos[0],enemigo_pos[1],
                                            enemigo_size,enemigo_size))
    #Dibujo de jugador
    pygame.draw.rect(ventana, (color_rojo), (jugadro_pos[0],jugadro_pos[1],
                                            jugadro_size,jugadro_size))
    clock.tick(30)
    pygame.display.update()


# In[ ]:




