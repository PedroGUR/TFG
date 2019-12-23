import pygame
import os
from personajes.minion_1 import Miniom_1

class Game:
    def __init__(self):
        self.width = 1920#TAMAÑO DE LA VENTANA
        self.height = 1080#TAMAÑO DE LA VENTANA
        self.win = pygame.display.set_mode((self.width, self.height),pygame.FULLSCREEN)#ESTA LINEA HACE QUE SE VEA EN PANTALLA COMPLETA
        self.subdito = [Miniom_1()]
        self.torres = []
        self.dinero = 100
        self.background = pygame.image.load(os.path.join("..","imagenes", "Guia.png"))# INDICA LA RUTA DE LA IMAGEN, PRIMERAS COMILLAS LA CARPETA Y LAS SEGUNDAS EL ARCHIVO
        #self.background = pygame.transform.scale(self.background,(self.width,self.height)) #ESTA SENTENCIA HARA QUE LA IMAGEN DE FONDO SE ESCALE AL TAMAÑO DE LA VENTANA, DE MOMENTO NO ES NECESARIO LO DEJAMOS COMO ANOTACION POR SI ACASO
        self.clicks = []

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    print(self.clicks)#IMPRIME POR CONSOLA LA LISTA DE CORDENADAS PULSADAS
            self.draw()
        pygame.quit()

    def draw(self):
        self.win.blit(self.background, (0,0))

        """
        #FUNCION PARA ESCRIBIR POR CONSOLA COORDENADAS
        for p in self.clicks:
            pygame.draw.circle(self.win, (255,0,0), (p[0], p[1]), 5, 0)#PARTE 1º= ¿? / PARTE 2º= Color RGB / Parte 3º=¿? / PARTE 4º= PRIMER NUMERO TAMAÑO DEL CIRCULO SEGUNDO NUMERO TAMAÑO DEL BORDE
        """
        for min in self.subdito:
            min.draw(self.win)

        pygame.display.update()

g = Game()
g.run()

