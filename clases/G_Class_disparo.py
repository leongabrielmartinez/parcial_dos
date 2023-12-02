import pygame as py

def rotar_imagen(imagen):
    imagen_rotada = py.transform.flip(imagen,True,False)
    return imagen_rotada

class Disparo:
    def __init__(self, posicion:tuple, tamaño:tuple,  direccion, path, rotado):
        


        self.superficie = py.image.load(path)

        if rotado:
            self.superficie = rotar_imagen(self.superficie)
            

        self.superficie = py.transform.scale(self.superficie, tamaño)
        self.rectangulo = self.superficie.get_rect()

        self.rectangulo.x = posicion[0]
        self.rectangulo.centery = posicion[1] - 10
        self.direccion = direccion

    def actualizar(self):
        if self.direccion == "Derecha":
            self.rectangulo.x += 10 #aca iria vel de disparo
        else:
            self.rectangulo.x -= 10
