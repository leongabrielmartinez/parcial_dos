from clases.E_Class_enemigo import Enemigo
from clases.G_Class_disparo import Disparo
from animaciones.enemigo_fisico import *
import random
import pygame as py

class Enemigo_fisico(Enemigo):
    def __init__(self, tamaño:tuple, posicion:tuple, path=None, speed = 0, rectangulos_auxiliares=True, animaciones:dict=None):
        super().__init__(tamaño, posicion, path, speed, rectangulos_auxiliares, animaciones)
        

        self.esta_saltando = True
        self.vida = 4
        direcciones = ["Corre", "Corre_izquierda"]
        random.shuffle(direcciones)
        self.que_hace = direcciones[0]
        self.velocidad_animacion = 0.15

        self.distancia_ataque = 50

        self.intervalo_invulnearibildad = 1000

        self.rect_vision = py.Rect((self.rect_principal.right, self.rect_principal.y), (self.distancia_ataque, self.tamaño[1]))
        self.rect_reescalado_bliteo = py.Rect((self.rect_principal.x, self.rect_principal.y), (50, 50))
        self.rect_ataque_uno = py.Rect((-100, -10), (self.tamaño[0] - 35, self.tamaño[1]))


    def animar(self, pantalla): 
        self.animacion_actual = self.animaciones[self.que_hace]
        while self.termino_animacion == False:
            self.animacion_actual = self.animaciones[self.ultima_accion]
            break

        hubo_reescalado = False

        self.rect_ataque_uno.x = -100
        self.rect_ataque_uno.y = -10

        self.rect_reescalado_bliteo.x = self.rect_principal.x
        self.rect_reescalado_bliteo.y = self.rect_principal.y
        
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0

            if self.que_hace == "Ataque_uno": 
                self.que_hace = "Quieto"
                self.termino_animacion = True

            elif (self.que_hace == "Ataque_uno_izquierda"):
                self.que_hace = "Quieto_izquierda"
                self.termino_animacion = True

            elif (self.que_hace == "Quieto"):
                self.que_hace = "Corre"

            elif (self.que_hace == "Quieto_izquierda"):
                self.que_hace = "Corre_izquierda"


        
        if self.que_hace ==  "Ataque_uno":
            hubo_reescalado = True
            for reescala in eu_reescale_A :
                if int(reescala) == int(self.contador_pasos):
                    self.rect_reescalado_bliteo.y -= eu_reescale_A[reescala][1]

                    if int(self.contador_pasos) > 3 and int(self.contador_pasos) < 7:
                            self.rect_ataque_uno.left = self.rect_principal.right
                            self.rect_ataque_uno.topleft = self.rect_principal.topright
                    break

                
        if self.que_hace == "Ataque_uno_izquierda":   
            hubo_reescalado = True
            for reescala in eu_reescale_A:
                if int(reescala) == int(self.contador_pasos):
                    self.rect_reescalado_bliteo.y -= eu_reescale_A[reescala][1] 

                    if int(self.contador_pasos) > 3 and int(self.contador_pasos) < 7:
                            self.rect_ataque_uno.right = self.rect_principal.left
                            self.rect_ataque_uno.topright = self.rect_principal.topleft
                    break

        if hubo_reescalado:
            if self.invulnerabilidad:
                if int(self.contador_pasos) % 2 == 0:
                    pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rect_reescalado_bliteo)
                else: 
                    pass
            else:
                pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rect_reescalado_bliteo)

        else: 
            if self.invulnerabilidad:
                if int(self.contador_pasos) % 2 == 0:
                    pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rect_principal)
                else: 
                    pass
            else:
                pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rect_principal)

        self.contador_pasos += self.velocidad_animacion
        

