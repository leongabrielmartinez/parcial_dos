from clases.A_Class_objeto import Objeto
from animaciones.items import *
import pygame as py


class Item(Objeto):
    def __init__(self, tamaño:tuple, posicion:tuple, path=None, rectangulos_auxiliares=False, animaciones:dict = None, efecto:str = None):
        super().__init__(tamaño, posicion, path, rectangulos_auxiliares=rectangulos_auxiliares)


        self.efecto = efecto
        self.animaciones = animaciones
        self.que_hace = "Quieto"
        self.contador_pasos = 0
        self.velocidad_animacion = 0.15
        self.animacion_actual = self.animaciones[self.que_hace]
        self.aparece = True

        # self.rect_reescalado_bliteo = py.Rect((self.rect_principal.x, self.rect_principal.y), (10, 10))

    def actualizar(self, pantalla, lista_plataformas):
        self.animacion_actual = self.animaciones[self.que_hace]
        match self.que_hace:
            case "Quieto":
                self.animar(pantalla)



        if self.aparece == True:
            for plataforma in lista_plataformas:
                if not self.rect_principal.colliderect(plataforma.rect_principal):
                    self.rect_principal.y += 1
                else:
                    self.rect_principal.bottom = plataforma.rect_principal.top
                    self.rect_principal.y -= 10
                    self.aparece = False



    def animar(self, pantalla):    
        # self.rect_reescalado_bliteo.x = self.rect_principal.x  

        largo = len(self.animacion_actual)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        # if self.efecto == "aumentar_monedas":
        #     hubo_reescalado = True
        #     for reescala in moneda_reescale:
        #         if int(reescala) == int(self.contador_pasos):
        #             self.rect_reescalado_bliteo.x -= moneda_reescale[reescala][0] / 2
        #             break
        # else: 
        #     hubo_reescalado = False


        # if hubo_reescalado:
        #     pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rect_reescalado_bliteo)
        # else:
        pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rect_principal)

        self.contador_pasos += self.velocidad_animacion



    


