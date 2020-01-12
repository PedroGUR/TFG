import pygame
import os
from .personaje import Personaje

class Miniom_1(Personaje):

    imgs = []

    for x in range(3):
        n = str(x)
        if x < 10:
            n = "0"+n
        imgs.append(pygame.image.load(os.path.join("..","personajes/minion3", "1_enemies_1_run_0" + n + ".png")))#ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES

    def __init__(self):
        super().__init__()