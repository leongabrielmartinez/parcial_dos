import pygame as py
from constantes.EOrientation import EOrientation

class Objeto:

    def __init__(self, tamaño:tuple, posicion:tuple, path=None, speed=0, rectangulos_auxiliares=False):

        self.tamaño = tamaño
        self.path = path


        if self.path == None:
            self.image = py.Surface(self.tamaño)
        else:
            self.image = py.image.load(self.path)
            self.image = py.transform.scale(self.image, self.tamaño)


        self.rect_principal = self.image.get_rect()
        self.rect_principal.x = posicion[0]
        self.rect_principal.y = posicion[1]

        self.posicion = posicion         

        self.set_speed(speed)


        self.rectangulos_auxiliares = rectangulos_auxiliares
        self.lista_rectangulos = {"rectangulo_principal":self.rect_principal}


        if self.rectangulos_auxiliares:
            self.set_rect_left()
            self.set_rect_right()
            self.set_rect_top()
            self.set_rect_bottom()
            

            self.lista_rectangulos["rectangulo_left"] = self.rect_left
            self.lista_rectangulos["rectangulo_right"] = self.rect_right
            self.lista_rectangulos["rectangulo_top"] = self.rect_top
            self.lista_rectangulos["rectangulo_bottom"] = self.rect_bottom

    def blit(self, screen):
        screen.blit(self.image, self.rect_principal)

    def set_speed(self, speed):
        self.speed = speed


    def stop(self):
        self.direction = EOrientation.IDLE
        self.move()

    def move_right(self):
        self.direction = EOrientation.RIGHT
        self.move()

    def move_left(self):
        self.direction = EOrientation.LEFT
        self.move()

    def move_up(self):
        self.direction = EOrientation.UP
        self.move()
    
    def move_down(self):
        self.direction = EOrientation.DOWN
        self.move()


    def move(self):
        if self.direction == EOrientation.LEFT:
            if self.rectangulos_auxiliares:
                for rectangulos in self.lista_rectangulos:
                    self.lista_rectangulos[rectangulos].x -= self.speed
            else:
                self.rect_principal.x -= self.speed
                


        elif self.direction == EOrientation.RIGHT:
            if self.rectangulos_auxiliares:
                for rectangulos in self.lista_rectangulos:
                    self.lista_rectangulos[rectangulos].x += self.speed
            else:
                self.rect_principal.x += self.speed


        elif self.direction == EOrientation.UP:
            if self.rectangulos_auxiliares:
                for rectangulos in self.lista_rectangulos:
                    self.lista_rectangulos[rectangulos].y -= self.speed
            else:
                self.rect_principal.y -= self.speed


        elif self.direction == EOrientation.DOWN:
            if self.rectangulos_auxiliares:
                for rectangulos in self.lista_rectangulos:
                    self.lista_rectangulos[rectangulos].y += self.speed
            else:
                self.rect_principal.y += self.speed


        elif self.direction == EOrientation.IDLE:
            pass
        else:
            raise ValueError('Invalid direction')
        
######################RECTANGULOS######################

    def set_rect_left(self, posicion = (0,0), tamaño = (0,0), default = True):
        if default:
            posicion = (self.rect_principal.x, self.rect_principal.y)
            tamaño = (self.tamaño[0]/4, self.tamaño[1])

        self.rect_left = py.Rect((posicion[0],posicion[1]), (tamaño[0],tamaño[1]))


    def set_rect_right(self, posicion = (0,0), tamaño = (0,0), default = True):
        if default:
            posicion = (self.rect_principal.right - self.tamaño[0]/4, self.rect_principal.y)
            tamaño = (self.tamaño[0]/4, self.tamaño[1])

        self.rect_right = py.Rect((posicion[0],posicion[1]), (tamaño[0], tamaño[1]))


    def set_rect_top(self, posicion = (0,0), tamaño = (0,0), default = True):
        if default:
            posicion = (self.rect_left.topright[0],self.rect_principal.y)
            tamaño = ((self.tamaño[0]/2, self.tamaño[1]/4))

        self.rect_top = py.Rect(((posicion[0],posicion[1])), (tamaño[0],tamaño[1]))


    def set_rect_bottom(self, posicion = (0,0), tamaño = (0,0), default = True):
        if default:
            tamaño = (self.tamaño[0]/2, self.tamaño[1]/4)#VOLVER A CAMBIAR
            posicion = (self.rect_left.right, self.rect_principal.bottom - tamaño[1]) 

        self.rect_bottom = py.Rect((posicion[0],posicion[1]), (tamaño[0],tamaño[1]))










