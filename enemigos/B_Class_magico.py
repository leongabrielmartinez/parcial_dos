from clases.E_Class_enemigo import Enemigo
from clases.G_Class_disparo import Disparo
from animaciones.enemigo_magico import *
import random
import pygame as py

class Enemigo_Magico(Enemigo):
    def __init__(self, tamaño:tuple, posicion:tuple, path=None, speed = 0, rectangulos_auxiliares=True, animaciones:dict=None):
        super().__init__(tamaño, posicion, path, speed, rectangulos_auxiliares, animaciones)
        

        self.esta_saltando = True
        self.vida = 4
        direcciones = ["Corre", "Corre_izquierda"]
        random.shuffle(direcciones)
        self.que_hace = direcciones[0]
        self.velocidad_animacion = 0.15

        self.distancia_ataque = 300

        self.intervalo_invulnearibildad = 1000

        self.rect_vision = py.Rect((self.rect_principal.right, self.rect_principal.y), (self.distancia_ataque, self.tamaño[1]))
#        self.rect_reescalado_bliteo = py.Rect((self.rect_principal.x, self.rect_principal.y), (50, 50))
        self.rect_ataque_uno = py.Rect((-100, -10), (self.tamaño[0] - 35, self.tamaño[1]))


        self.path_disparo = bola_de_fuego
        self.tamaño_proyectil = (150, 75)

    def animar(self, pantalla): 
        self.animacion_actual = self.animaciones[self.que_hace]
        while self.termino_animacion == False:
            self.animacion_actual = self.animaciones[self.ultima_accion]
            break



        # self.rect_ataque_uno.x = -100
        # self.rect_ataque_uno.y = -10

        # self.rect_reescalado_bliteo.x = self.rect_principal.x
        # self.rect_reescalado_bliteo.y = self.rect_principal.y
        
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


        
        if self.que_hace ==  "Ataque_uno" or self.que_hace == "Ataque_uno_izquierda":
            if int(self.contador_pasos) == 7:
                self.lanzar_proyectil(self.path_disparo)

        # if hubo_reescalado:
        #     if self.invulnerabilidad:
        #         if int(self.contador_pasos) % 2 == 0:
        #             pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rect_reescalado_bliteo)
        #         else: 
        #             pass
        #     else:
        #         pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rect_reescalado_bliteo)

        # else: 
        if self.invulnerabilidad:
            if int(self.contador_pasos) % 2 == 0:
                pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rect_principal)
            else: 
                pass
        else:
            pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rect_principal)

        self.contador_pasos += self.velocidad_animacion
        

    def actualizar(self, pantalla, lista_plataformas, rect_heroe, rect_heroe_ataque_uno, lista_proyectiles_heroe):

        self.comprobar_vitalidad()

        if self.invulnerabilidad == True:
            self.invulnerabilidad_momentanea(self.tiempo_ultimo_hit, self.intervalo_invulnearibildad)

        self.detectar_colisiones(lista_proyectiles_heroe, rect_heroe_ataque_uno)
        self.acciones(pantalla, lista_plataformas)

        self.aplicar_gravedad(pantalla, lista_plataformas)
        self.actualizar_proyectiles(pantalla)

        self.patrullar(lista_plataformas)
        self.atacar(rect_heroe)