from clases.B_Class_plataforma import PlataformaDeslizante
import pygame as py




class Trampa(PlataformaDeslizante):
    def __init__(self, tamaño:tuple, posicion:tuple, path=None, rectangulos_auxiliares = False, barreras = False, movimiento_x = True, 
        movimiento_y = False, rango = 1400, animaciones:dict=None):
        super().__init__(tamaño, posicion, path, rectangulos_auxiliares, barreras, movimiento_x, movimiento_y, rango)


        self.desplazamiento_x = 3
        self.animaciones = animaciones
        self.que_hace = "Avanza"
        self.animacion_actual = self.animaciones[self.que_hace]
        self.velocidad_animacion = 0.30
        self.contador_pasos = 0

    def actualizar(self):
        self.animacion_actual = self.animaciones[self.que_hace]

        if self.que_hace == "Avanza":
            #rect_comun
            #else_rectangulo_bliteo
            pass


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

        # self.blit(pantalla)        HACER LO DEL REESCALDO




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