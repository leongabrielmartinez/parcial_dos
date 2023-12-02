from clases.A_Class_objeto import Objeto
import pygame as py
from clases.G_Class_disparo import Disparo
from constantes.personajes import *


class Personaje(Objeto):
    def __init__(self, tamaño:tuple, posicion:tuple, path=None, speed = 0, rectangulos_auxiliares=True, animaciones:dict=None, es_heroe=True):
        super().__init__(tamaño, posicion, path, speed, rectangulos_auxiliares)

        self.animaciones = animaciones
        self.ultima_accion = "Quieto"
        self.que_hace = "Quieto"
        self.esta_mirando = "Derecha"
        self.animacion_actual = self.animaciones[self.que_hace]
        self.velocidad_animacion = 0.30
        self.contador_pasos = 0

        self.velocidad = speed
        self.desplazamiento_y = 0
        self.potencia_salto = -17     
        self.limite_velocidad_salto = 15 
        self.desplazamiento_dash = 40
        self.gravedad = 1
        self.esta_saltando = True#PARA QUE CAIGA

        
        self.invulnerabilidad = False
        self.esta_vivo = True
        self.lista_proyectiles = []

        self.termino_animacion = True
        self.tamaño_proyectil = (100,100)
        self.path_disparo = "recursos\heroe_img\disparo\disparo.png"


###########################referencia borrar
    def actualizar(self, pantalla, lista_plataformas, listas_proyectiles_enemigos, lista_enemigos, lista_items):
        
        self.comprobar_vitalidad()
        if self.invulnerabilidad == True:
            self.invulnerabilidad_momentanea(self.tiempo_ultimo_hit, self.intervalo_invulnearibildad)


        self.acciones(pantalla, lista_plataformas)
        self.detectar_colisiones(listas_proyectiles_enemigos, lista_enemigos, lista_items)
        #self.invulnerabilidad_momentanea(self.tiempo_ultimo_hit, 2000)
        self.aplicar_gravedad(pantalla, lista_plataformas)
        self.actualizar_proyectiles(pantalla)
###########################referencia borrar
    def comprobar_vitalidad(self):
        if self.vida <= 0:
            self.esta_vivo = False


    def acciones(self, pantalla, lista_plataformas):#MUCHAS ACCIONES DEPENDEN DEL FRAME DE ANIMACION
        match self.que_hace:

            case "Quieto":
                if not self.esta_saltando:
                    self.animar(pantalla)


            case "Quieto_izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla)


            case "Corre":
                if not self.esta_saltando:
                    self.animar(pantalla)
                self.correr(pantalla, lista_plataformas)

            case "Corre_izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla)
                self.correr(pantalla, lista_plataformas)


            case "Salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto

            case "Salta_izquierda":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto


            case "Ataque_uno":
                if not self.esta_saltando:
                    self.animar(pantalla)
            case "Ataque_uno_izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla)


            case "Ataque_dos":
                if self.heroe_ataque_dos_disponible:
                    self.animar(pantalla)
                    self.lanzar_proyectil(self.path_disparo)
            case "Ataque_dos_izquierda":
                if self.heroe_ataque_dos_disponible:
                    self.animar(pantalla)
                    self.lanzar_proyectil(self.path_disparo)#se llama el dash dentro del animar


            case "Dash":
                if not self.esta_saltando:#se llama el dash dentro del animar
                    self.animar(pantalla)

            case "Dash_izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla)

            
            case "Habilidad_extra":
                pass


    def correr(self, pantalla, lista_plataformas):
        velocidad_actual = self.velocidad
        colision_derecha = False
        colision_izquierda = False

        for plataforma in lista_plataformas:
            if self.rect_principal.colliderect(plataforma.rect_principal):
                if self.rect_right.colliderect(plataforma.rect_principal) and not (self.rect_bottom.colliderect(plataforma.rect_principal)):
                    colision_derecha = True
                elif self.rect_left.colliderect(plataforma.rect_principal) and not (self.rect_bottom.colliderect(plataforma.rect_principal)):
                    colision_izquierda = True

        if self.que_hace == "Corre_izquierda":
            velocidad_actual *= -1
        nueva_x = self.rect_principal.x + velocidad_actual


        if nueva_x >= 0 and nueva_x <= pantalla.get_width() - self.rect_principal.width:
            if self.que_hace == "Corre_izquierda" and not colision_izquierda:
                self.move_left()
            elif self.que_hace == "Corre" and not colision_derecha:
                self.move_right()


    def dash(self, pantalla):
        if self.esta_mirando == "Derecha":
            self.que_hace = "Dash"
            if self.rect_principal.right + self.desplazamiento_dash < pantalla.get_width():
                for rectangulos in self.lista_rectangulos:
                    self.lista_rectangulos[rectangulos].x += self.desplazamiento_dash

        else: 
            self.que_hace = "Dash_izquierda"
            if self.rect_principal.left - self.desplazamiento_dash > 0:
                for rectangulos in self.lista_rectangulos:
                    self.lista_rectangulos[rectangulos].x -= self.desplazamiento_dash



    def aplicar_gravedad(self, pantalla, lista_plataformas):

        if self.esta_saltando:
            self.animar(pantalla)


            for rectangulos in self.lista_rectangulos:
                self.lista_rectangulos[rectangulos].y += self.desplazamiento_y
            for plataforma in lista_plataformas:
                if self.rect_top.colliderect(plataforma.rect_principal):
                    self.rect_principal.top = plataforma.rect_principal.bottom
                    self.rect_bottom.bottom = self.rect_principal.bottom
                    self.desplazamiento_y += self.gravedad

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad
                

        for plataforma in lista_plataformas:
            if self.rect_bottom.colliderect(plataforma.rect_principal):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                
            
                self.rect_principal.bottom = plataforma.rect_principal.top
                self.rect_left.bottom = plataforma.rect_principal.top
                self.rect_right.bottom = plataforma.rect_principal.top
                self.rect_top.top = self.rect_principal.top
                self.rect_bottom.bottom = self.rect_principal.bottom
                break
            else:
                self.esta_saltando = True


    def invulnerabilidad_momentanea(self, tiempo_ultimo_hit, tiempo_activo):
        tiempo_actual = py.time.get_ticks()
        if tiempo_actual >= tiempo_ultimo_hit + tiempo_activo and self.invulnerabilidad == True:
            self.invulnerabilidad = False


    def lanzar_proyectil(self, path):
        x = None
        margen = 47
        y = self.rect_principal.centery + 10

        if self.esta_mirando == "Derecha":
            x = self.rect_principal.right - margen
            rotado = False
        else:
            x = self.rect_principal.left - 100 + margen
            rotado = True

        if x is not None:
            self.lista_proyectiles.append(Disparo((x,y),self.tamaño_proyectil, self.esta_mirando, path, rotado))

    
    def actualizar_proyectiles(self, pantalla):
        i = 0
        while i < len(self.lista_proyectiles):
            p = self.lista_proyectiles[i]
            pantalla.blit(p.superficie, p.rectangulo)
            p.actualizar()
            #py.draw.rect(pantalla, "red", p.rectangulo, 3)

            if p.rectangulo.centerx < 0 or p.rectangulo.centerx > pantalla.get_width() or len(self.lista_proyectiles) > 1:
                self.lista_proyectiles.pop(i)
                i -= i
            i += i
            break






