from clases.C_Class_personaje import Personaje
from clases.G_Class_disparo import Disparo
from animaciones.enemigo_fisico import *
import random
import pygame as py

class Enemigo(Personaje):
    def __init__(self, tamaño:tuple, posicion:tuple, path=None, speed = 0, rectangulos_auxiliares=True, animaciones:dict=None):
        super().__init__(tamaño, posicion, path, speed, rectangulos_auxiliares, animaciones)
        
        self.esta_saltando = True
        self.vida = 4

        direcciones = ["Corre", "Corre_izquierda"]
        random.shuffle(direcciones)
        self.que_hace = direcciones[0]
        self.velocidad_animacion = 0.15
        self.lista_proyectiles = []

        self.intervalo_invulnearibildad = 1000

        self.probabilidad_de_pocion = random.randint(0, 100)

        # self.rect_vision = py.Rect((self.rect_principal.right, self.rect_principal.y), (self.distancia_ataque, self.tamaño[1]))
        # self.rect_reescalado_bliteo = py.Rect((self.rect_principal.x, self.rect_principal.y), (50, 50))
        # self.rect_ataque_uno = py.Rect((-100, -10), (self.tamaño[0] - 35, self.tamaño[1]))


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


    def patrullar(self, lista_plataformas):
        if self.que_hace == "Corre":
            self.rect_vision.x = self.rect_principal.right
            self.rect_vision.y = self.rect_principal.y
            self.esta_mirando = "Derecha"

        elif(self.que_hace == "Corre_izquierda"):
            self.rect_vision.x = self.rect_principal.left - self.distancia_ataque
            self.rect_vision.y = self.rect_principal.y
            self.esta_mirando = "Izquierda"

        for plataforma in lista_plataformas:
            if self.rect_left.colliderect(plataforma.barrera_uno):
                self.que_hace = "Corre"

            elif self.rect_right.colliderect(plataforma.barrera_dos):
                self.que_hace = "Corre_izquierda"

            elif self.rect_right.colliderect(plataforma.rect_principal) and not self.rect_bottom.colliderect(plataforma.rect_principal):
                    self.que_hace = "Corre_izquierda"

            elif self.rect_left.colliderect(plataforma.rect_principal) and not self.rect_bottom.colliderect(plataforma.rect_principal):
                    self.que_hace = "Corre"


    def atacar(self, rect_heroe):
        if self.rect_vision.colliderect(rect_heroe):
            if self.esta_mirando == "Derecha":
                if self.termino_animacion == True:
                    self.contador_pasos = 0
                self.que_hace = "Ataque_uno"
                self.termino_animacion = False
                self.ultima_accion = "Ataque_uno"

            elif self.esta_mirando == "Izquierda":
                if self.termino_animacion == True:
                    self.contador_pasos = 0
                self.que_hace = "Ataque_uno_izquierda"
                self.termino_animacion = False
                self.ultima_accion = "Ataque_uno_izquierda"



    def detectar_colisiones(self, listas_proyectiles_heroe, rect_ataque_heroe):
        self.colision_hitbox(rect_ataque_heroe)
        self.colision_proyectiles(listas_proyectiles_heroe)


    def colision_proyectiles(self, lista_proyectiles:list):
        
        i = 0
        while i < len(lista_proyectiles) and not self.invulnerabilidad:
            if self.rect_principal.colliderect(lista_proyectiles[i].rectangulo):
                lista_proyectiles.pop(i)
                self.vida -= 1 
                self.tiempo_ultimo_hit = py.time.get_ticks()
                self.intervalo_invulnearibildad = 1000
                self.invulnerabilidad = True
                self.invulnerabilidad_momentanea(self.tiempo_ultimo_hit, self.intervalo_invulnearibildad)
                

                i -= i
            i += i
            break

    def colision_hitbox(self, rect_heroe_ataque_uno):
        if self.rect_principal.colliderect(rect_heroe_ataque_uno) and not self.invulnerabilidad:
            self.vida -= 1 
            self.tiempo_ultimo_hit = py.time.get_ticks()
            self.intervalo_invulnearibildad = 1000
            self.invulnerabilidad = True
            self.invulnerabilidad_momentanea(self.tiempo_ultimo_hit, self.intervalo_invulnearibildad)
