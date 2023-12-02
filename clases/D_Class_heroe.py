from clases.C_Class_personaje import Personaje
from clases.G_Class_disparo import Disparo
import pygame as py
# import sys

from constantes import *
from animaciones.heroe import *


class Heroe(Personaje):
    def __init__(self, tamaño:tuple, posicion:tuple, path=None, speed = 0, rectangulos_auxiliares=True, animaciones:dict=None):
        super().__init__(tamaño, posicion, path, speed, rectangulos_auxiliares, animaciones)

        self.vida = 50
        self.tiempo_ultimo_hit = 0

        self.heroe_ataque_dos_disponible = True

        self.rect_reescalado_bliteo = py.Rect((self.rect_principal.x, self.rect_principal.y), (50, 50))
        self.rect_ataque_uno = py.Rect((-100 , -10), (self.tamaño[0] - 35, self.tamaño[1]))
    
        self.velocidad_animacion = 0.30
        
        self.intervalo_invulnearibildad = 1000

        self.monedas = 0
        self.pociones = 0

        self.tiempo_ultimo_dash = 0
        self.tiempo_ultimo_lanzamiento = 0
        self.puede_dashear = True
        self.puede_lanzar_ataque = True



    def actualizar(self, pantalla, lista_plataformas, listas_proyectiles_enemigos, lista_enemigos, lista_items):
        if self.invulnerabilidad == True:
            self.invulnerabilidad_momentanea(self.tiempo_ultimo_hit, self.intervalo_invulnearibildad)
        
        if self.puede_dashear == False:
            tiempo_actual = py.time.get_ticks()
            if self.tiempo_ultimo_dash + 1000 <= tiempo_actual:
                self.puede_dashear = True

        if self.puede_lanzar_ataque == False:
            tiempo_actual = py.time.get_ticks()
            if self.tiempo_ultimo_lanzamiento + 3000 <= tiempo_actual:
                self.puede_lanzar_ataque = True


        self.acciones(pantalla, lista_plataformas)
        self.detectar_colisiones(listas_proyectiles_enemigos, lista_enemigos, lista_items)
        self.aplicar_gravedad(pantalla, lista_plataformas)
        self.actualizar_proyectiles(pantalla)

        # if self.vida == 0:
        #     sys.exit()

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
            self.termino_animacion = True


        if self.ultima_accion == "Ataque_uno" and self.termino_animacion == False:
            hubo_reescalado = True
            for reescala in h_reescale_AU:
                if int(reescala) == int(self.contador_pasos):
                    self.rect_reescalado_bliteo.y -= h_reescale_AU[reescala][1]
                
                    if int(self.contador_pasos) > 0 and int(self.contador_pasos) < 4:
                            self.rect_ataque_uno.left = self.rect_principal.right
                            self.rect_ataque_uno.topleft = self.rect_principal.topright
                    break

                
        if self.ultima_accion == "Ataque_uno_izquierda" and self.termino_animacion == False:   
            hubo_reescalado = True
            for reescala in h_reescale_AU:
                if int(reescala) == int(self.contador_pasos):
                    self.rect_reescalado_bliteo.x -= h_reescale_AU[reescala][0] 
                    self.rect_reescalado_bliteo.y -= h_reescale_AU[reescala][1] 

                    if int(self.contador_pasos) > 0 and int(self.contador_pasos) < 4:
                            self.rect_ataque_uno.right = self.rect_principal.left
                            self.rect_ataque_uno.topright= self.rect_principal.topleft
                    break

        if self.ultima_accion == "Ataque_dos" and self.termino_animacion == False:
            hubo_reescalado = True
        


        if self.ultima_accion == "Ataque_dos_izquierda" and self.termino_animacion == False:   
            hubo_reescalado = True
            for reescala in h_reescale_AD:
                if int(reescala) == int(self.contador_pasos):
                    self.rect_reescalado_bliteo.x -= h_reescale_AD[reescala][0] 
                    break



        if self.ultima_accion == "Dash" and self.termino_animacion == False: 
            if int(self.contador_pasos) > 0 and int(self.contador_pasos) < 3:
                self.invulnerabilidad = True
                self.tiempo_ultimo_hit = py.time.get_ticks()
                self.tiempo_ultimo_dash = py.time.get_ticks()
                self.dash(pantalla)
            else: 
                self.puede_dashear = False



        if self.ultima_accion == "Dash_izquierda" and self.termino_animacion == False: 
            if int(self.contador_pasos) > 0 and int(self.contador_pasos) < 3:
                self.invulnerabilidad = True
                self.tiempo_ultimo_hit = py.time.get_ticks()
                self.tiempo_ultimo_dash = py.time.get_ticks()
                self.dash(pantalla)
            else: 
                self.puede_dashear = False

        if hubo_reescalado:
            if self.invulnerabilidad:
                if int(self.contador_pasos) % 2 == 0:
                    pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rect_reescalado_bliteo)
                else: 
                    pass
            else:
                pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rect_reescalado_bliteo)
                #pantalla.blit(self.animacion_actual[1], self.rect_reescalado_bliteo)
        else: 
            if self.invulnerabilidad:
                if int(self.contador_pasos) % 2 == 0:
                    pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rect_principal)#self.rect_reescalado_bliteo??
                else: 
                    pass
            else:
                pantalla.blit(self.animacion_actual[int(self.contador_pasos)], self.rect_principal)

        self.contador_pasos += self.velocidad_animacion



    def detectar_colisiones(self, listas_proyectiles_enemigos, lista_enemigos, lista_items):
        self.colision_hitbox(lista_enemigos)
        self.colision_item(lista_items)

        for lista in listas_proyectiles_enemigos:
            self.colision_proyectiles(lista)

    def colision_proyectiles(self, lista_proyectiles:list):
        i = 0
        while i < len(lista_proyectiles) and not self.invulnerabilidad:
            if self.rect_principal.colliderect(lista_proyectiles[i].rectangulo):
                lista_proyectiles.pop(i)
                self.vida -= 1 
                self.tiempo_ultimo_hit = py.time.get_ticks()
                self.invulnerabilidad = True
                self.invulnerabilidad_momentanea(self.tiempo_ultimo_hit, 1000)
                i -= i
            i += i
            break

    def colision_hitbox(self, lista_enemigos):
        for enemigo in lista_enemigos:
            if self.rect_principal.colliderect(enemigo.rect_principal) and not self.invulnerabilidad:
                self.vida -= 1 
                self.invulnerabilidad = True
                self.tiempo_ultimo_hit = py.time.get_ticks()

            elif self.rect_principal.colliderect(enemigo.rect_ataque_uno) and not self.invulnerabilidad:
                self.vida -= 1 
                self.invulnerabilidad = True
                self.tiempo_ultimo_hit = py.time.get_ticks()

    def colision_item(self, lista_items):
        i = 0

        #if len(lista_items) > 0:
        while i < len(lista_items):
            if self.rect_principal.colliderect(lista_items[i].rect_principal):
                if lista_items[i].efecto == "aumentar_monedas":
                    self.monedas += 1
                    x = lista_items.pop(i)
                    del x
                elif lista_items[i].efecto == "aumentar_pociones":
                    self.pociones += 1
                    x = lista_items.pop(i)
                    del x
            else:
                break
                
            i += i
        # rectangulos_dos = [r for r in lista_items if self.rect_principal.colliderect(r.rect_principal)]
        # rectangulos = rectangulos_dos

        # for r in rectangulos:
        #     rectangulos.remove(r)

    def habilitar_ataque_dos(self):
        if self.heroe_ataque_dos_disponible == False:
            self.heroe_ataque_dos_disponible = True








