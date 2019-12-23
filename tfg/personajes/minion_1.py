import pygame
import os
from .personaje import Personaje

class Miniom_1(Personaje):

    imgs = []

    for x in range(4):
        n = str(x)
        imgs.append(pygame.image.load(os.path.join("..","personajes/minion", "minion" + n + ".png")))#ENTRE LOS PARENTESIS LA RUTA DEL SPRITE A CONTUNIACION DE LOS PARENTESIS DEL JOIN VA LA RUTA DE LA IMAGEN / ENTRE LOS PARENTESIS DE RANGE VA EL NUMERO DE IMAGENES

    def __init__(self):
        super().__init__()