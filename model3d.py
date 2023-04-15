#!/usr/bin/env python3

import pygame
import time
import sys
import numpy as np 

pantalla_x= 1200
pantalla_y= 800


def pv(punto,obs):
    pv=np.zeros(2)
    pv[0]=obs[0]+(punto[0]-obs[0])/(punto[1]-obs[1])*(-obs[1])
    pv[1]=obs[2]+(punto[2]-obs[2])/(punto[1]-obs[1])*(-obs[1])
    pv[1]=pantalla_y-pv[1]
    return pv

pygame.init()
pygame.font.init()

fps=25

pygame.display.set_caption('Modelo3D')
window = pygame.display.set_mode((pantalla_x, pantalla_y))


fps_controller = pygame.time.Clock()

colorfondo=pygame.Color(0,0,0)
rojo=pygame.Color(255,0,0)
amarillo=pygame.Color(255,255,0)
azul=pygame.Color(0,0,255)
blanco=pygame.Color(255,255,200)
cyan=pygame.Color(0,255,255)
magenta=pygame.Color(255,0,255)

vi=np.array([1,0,0])
vj=np.array([0,1,0])
vk=np.array([0,0,1])

direc=""

d=np.array([0,0,0])
salto=5

while True:


    sepojos=50
    ob=np.array([600,-500,500])
    obd=ob+sepojos*vi+2*vk

    c=np.array([800,3000,500])
    rd=1000
    
    v1=c+d+rd*(vi+vj+vk)
    v2=c+d+rd*(vi+vj-vk)
    v3=c+d+rd*(vi-vj+vk)
    v4=c+d+rd*(vi-vj-vk)
    v5=c+d+rd*(-vi+vj+vk)
    v6=c+d+rd*(-vi+vj-vk)
    v7=c+d+rd*(-vi-vj+vk)
    v8=c+d+rd*(-vi-vj-vk)

    window.fill(colorfondo)

    pygame.draw.line(window, cyan, pv(v1,ob),pv(v2,ob),width=2)
    pygame.draw.line(window, cyan, pv(v3,ob),pv(v4,ob),width=2)
    pygame.draw.line(window, cyan, pv(v5,ob),pv(v6,ob),width=2)
    pygame.draw.line(window, cyan, pv(v7,ob),pv(v8,ob),width=2)
    pygame.draw.line(window, cyan, pv(v1,ob),pv(v5,ob),width=2)
    pygame.draw.line(window, cyan, pv(v3,ob),pv(v7,ob),width=2)
    pygame.draw.line(window, cyan, pv(v1,ob),pv(v3,ob),width=2)
    pygame.draw.line(window, cyan, pv(v5,ob),pv(v7,ob),width=2)
    pygame.draw.line(window, cyan, pv(v2,ob),pv(v6,ob),width=2)
    pygame.draw.line(window, cyan, pv(v4,ob),pv(v8,ob),width=2)
    pygame.draw.line(window, cyan, pv(v2,ob),pv(v4,ob),width=2)
    pygame.draw.line(window, cyan, pv(v6,ob),pv(v8,ob),width=2)
    
    pygame.draw.line(window, amarillo, pv(v1,obd),pv(v2,obd),width=2)
    pygame.draw.line(window, amarillo, pv(v3,obd),pv(v4,obd),width=2)
    pygame.draw.line(window, amarillo, pv(v5,obd),pv(v6,obd),width=2)
    pygame.draw.line(window, amarillo, pv(v7,obd),pv(v8,obd),width=2)
    pygame.draw.line(window, amarillo, pv(v1,obd),pv(v5,obd),width=2)
    pygame.draw.line(window, amarillo, pv(v3,obd),pv(v7,obd),width=2)
    pygame.draw.line(window, amarillo, pv(v1,obd),pv(v3,obd),width=2)
    pygame.draw.line(window, amarillo, pv(v5,obd),pv(v7,obd),width=2)
    pygame.draw.line(window, amarillo, pv(v2,obd),pv(v6,obd),width=2)
    pygame.draw.line(window, amarillo, pv(v4,obd),pv(v8,obd),width=2)
    pygame.draw.line(window, amarillo, pv(v2,obd),pv(v4,obd),width=2)
    pygame.draw.line(window, amarillo, pv(v6,obd),pv(v8,obd),width=2)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            if event.key == pygame.K_UP or event.key == pygame.K_k:
                direc="up"
            if event.key == pygame.K_DOWN or event.key == pygame.K_j:
                direc="down"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_l:
                direc="right"
            if event.key == pygame.K_LEFT or event.key == pygame.K_h:
                direc="left"
            if event.key == pygame.K_PAGEDOWN or event.key == pygame.K_y:
                direc="ford"
            if event.key == pygame.K_PAGEUP or event.key == pygame.K_n:
                direc="back"
            if event.key == pygame.K_RSHIFT or event.key == pygame.K_u:
                direc="stop"


    if direc == "up":
        d=d+vk*salto
    if direc == "down":
        d=d-vk*salto
    if direc == "right":
        d=d+vi*salto
    if direc == "left":
        d=d-vi*salto
    if direc == "ford":
        d=d+vj*salto
    if direc == "back":
        d=d-vj*salto
    if direc == "stop":
        d=d

    pygame.display.flip()
    fps_controller.tick(25)

