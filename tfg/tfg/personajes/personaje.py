import pygame
import math

class Personaje:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.vida = 1
        self.vel = 3
        self.path = [(500, 780),(500, 774),(501, 760),(500, 751),(501, 735),(501, 722),(502, 707),(501, 691),(500, 677),(501, 663),(501, 645),(501, 630),(501, 612),(501, 595),(499, 569),(500, 553),(500, 533),(499, 519),(500, 502),(500, 482),(499, 462),(495, 446),(500, 428),(499, 411),(500, 395),(500, 376),(502, 353),(504, 338),(512, 325),(526, 312),(548, 292),(562, 282),(571, 272),(577, 258),(581, 245),(591, 230),(598, 219),(608, 212),(619, 198),(630, 190),(636, 182),(644, 173),(654, 164),(667, 157),(683, 149),(702, 149),(715, 149),(727, 145),(737, 145),(758, 144),(768, 144),(786, 143),(797, 143),(818, 141),(833, 141),(854, 141),(875, 140),(898, 140),(909, 142),(918, 142),(943, 140),(966, 140),(985, 140),(1004, 137),(1020, 139),(1038, 139),(1048, 141),(1067, 140),(1085, 139),(1098, 140),(1113, 138),(1126, 139),(1144, 138),(1165, 137),(1176, 138),(1192, 136),(1209, 137),(1221, 138),(1230,138),(1251, 139),(1259, 136),(1277, 136),(-1292, 137)]#ESTA LINEA MARCA EL RECORRIDO DEL PERSONAJE
        #self.path = [(704, 300),(704, 350),(704, 400),(704, 450),(704, 500),(704, 550),(704, 600),(704, 650),(704, 700),(704, 750),(704, 800),(750 ,-301)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.cont_mover = 0
        self.dist_mover = 0

    def draw(self, win):
        """
        DIBUJA A LOS ENEMIGOS CON LAS IMAGENES ESTABLECIDAS
        :param win: SURFACE
        :return: NADA
        """

        self.img = self.imgs[self.contador_animacion]
        self.contador_animacion += 1
        #ESTE IF REINICIARA EL CONTADOR DE ANIMACIONES PAR A SIMULAR EL MOVIMIENTO DE LA IMGANES
        if self.contador_animacion >= len(self.imgs):
            self.contador_animacion = 0

        win.blit(self.img, (self.x, self.y))
        self.mover()

    def colision(self, X, Y):
        """
        DETECTA QUE EL SUBDITO RECIBA UNA COLISION
        :param x: INT
        :param y: INT
        :return: BOOLEAN
        """
        #ESTE IF COMPROBARA MEDIANTE LAS POSICIONES EN EL EJE SI HAN GOLPEADO AL SUBDITO
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >=self.y:
                return True
        return False


    def mover(self):
        """
        MUEVE AL SUBDITO
        :return: NADA
        """
        #TODA ESTA MIERDA ES PARA CALCULAR EL MOVIMIENTO ENTRE PUNTOS MEDIANTE EL TEOREMA DE PITAGORAS(VECTORES)
        x1,y1 = self.path[self.path_pos]
        print(self.path[self.path_pos])
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (-10, 571)
        else:
            x2,y2 = self.path[self.path_pos+1]

        move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.cont_mover += 0.2
        dirn = (x2-x1, y2-y1)


        mover_x, mover_y = (self.x + dirn[0] * self.cont_mover, self.y + dirn[1] * self.cont_mover)
        self.dis += math.sqrt((mover_x - x1) ** 2 + (mover_y - y1) ** 2)

        #VA AL SIGUIENTE PUNTO
        if self.dis >= move_dis:
            self.dis = 0
            self.cont_mover = 0
            """self.path_pos += 1
            if self.path_pos >= len(self.path):
                print(self.path_pos)
                return False"""
                #self.path_pos=0
                #self.path_pos += 1
            if self.path_pos < len(self.path)-1:
                self.path_pos += 1
            else:
                return False
        self.x = mover_x
        self.y = mover_y
        return True

    def hit(self):
        """
        DEVUELVE SI EL SUBDITO HA SIDO GOLPEADO Y LE RESTA VIDA
        :return: BOOLEAN
        """