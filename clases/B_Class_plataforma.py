#from clases.A_Class_Objeto import *
from clases.A_Class_objeto import Objeto
import pygame as py


class Plataforma(Objeto):
    def __init__(self, tamaño:tuple, posicion:tuple, path=None, rectangulos_auxiliares=False, barreras = True):
        super().__init__(tamaño, posicion, path, rectangulos_auxiliares=rectangulos_auxiliares)
        self.es_deslizante = False
        self.barreras = barreras

        if self.barreras:
            self.crear_barreras()
            self.lista_rectangulos = {"barrera_izquierda":self.barrera_uno}
            self.lista_rectangulos = {"barrera_derecha":self.barrera_dos}


    def crear_barreras(self):
        self.barrera_uno = py.Rect((self.rect_principal.topleft[0], (self.rect_principal.topleft[1] - 40)), (10,40))
        self.barrera_dos = py.Rect((self.rect_principal.topright[0] - 10, (self.rect_principal.topleft[1] - 40)), (10,40))




class PlataformaDeslizante(Objeto):
    def __init__(self, tamaño:tuple, posicion:tuple, path=None, rectangulos_auxiliares=False, barreras = True, movimiento_x = False, movimiento_y = False,  rango = 0):
        super().__init__(tamaño, posicion, path, rectangulos_auxiliares=rectangulos_auxiliares)

        self.barreras = barreras
        self.es_deslizante = True

        if self.barreras:
            self.crear_barreras()
            self.lista_rectangulos = {"barrera_izquierda":self.barrera_uno}
            self.lista_rectangulos = {"barrera_derecha":self.barrera_dos}


        self.desplazamiento_x = 3
        self.desplazamiento_y = 1

        self.movimiento_x = movimiento_x
        self.movimiento_y = movimiento_y
        self.rango = rango

        self.desplazamiento_acumulado_x = 0
        self.desplazamiento_acumulado_y = 0

    def actualizar(self, pantalla):
        if self.desplazamiento_acumulado_x >= self.rango: 
            self.desplazamiento_x *= -1
        elif self.desplazamiento_acumulado_x <= self.rango * -1: 
            self.desplazamiento_x *= -1

        if self.desplazamiento_acumulado_y >= self.rango: 
            self.desplazamiento_y *= -1
        elif self.desplazamiento_acumulado_y <= self.rango * -1: 
            self.desplazamiento_y *= -1

        self.moverse()
        if self.barreras:
            self.barrera_uno.x = self.rect_principal.topleft[0]
            self.barrera_uno.y = self.rect_principal.topleft[1] - 40

            self.barrera_dos.x = self.rect_principal.topright[0] - 10
            self.barrera_dos.y = self.rect_principal.topleft[1] - 40

        self.blit(pantalla)



    def moverse(self):

        if self.movimiento_x:
            self.rect_principal.x += self.desplazamiento_x
            self.desplazamiento_acumulado_x += self.desplazamiento_x

        if self.movimiento_y:
            self.rect_principal.y += self.desplazamiento_y
            self.desplazamiento_acumulado_y += self.desplazamiento_y



    def crear_barreras(self):
        self.barrera_uno = py.Rect((self.rect_principal.topleft[0], (self.rect_principal.topleft[1] - 40)), (10,40))
        self.barrera_dos = py.Rect((self.rect_principal.topright[0] - 10, (self.rect_principal.topleft[1] - 40)), (10,40))




































        #self.lista = super().rect_principal#el programa no permite acceder directamente a la lista


        # if self.barreras:
        #     for rectangulos in super().lista_rectangulos:
        #         if rectangulos["rectangulo_left"]:
        #             rectangulo_izquierdo =  rectangulos["rectangulo_left"]







        #self.rectizq = rectangulo_izquierdo




            #barrera_1 = py.rect(super().rect_left.top,super().rect_right.top,50,50)
            # barrera_1
            # super().set_rect_left((tamaño[0]/4,100))
            # super().set_rect_left(False,100,100,100,100)




#QUE TENGA 4 RECTANGULOS Y SE PUEDA ELEVAR LOS DE LA IZQ Y DERECHA PARA SERVIR DE TOPE

# def crear_plataforma(visible,esPremio, tamaño,x, y, path="", ):
#     plataforma = {}
#     if visible:
#         plataforma["superficie"] = pygame.image.load(path)
#         print(plataforma["superficie"] )
#         plataforma["superficie"] = pygame.transform.scale(plataforma["superficie"],tamaño)
#     else:
#         plataforma["superficie"] = pygame.Surface(tamaño)
#     plataforma["rectangulo"] = plataforma["superficie"].get_rect()
#     plataforma["rectangulo"].x = x
#     plataforma["rectangulo"].y = y
#     plataforma["premio"] = esPremio
    
#     return plataforma
