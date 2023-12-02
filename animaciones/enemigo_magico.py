import pygame as py 
from constantes.personajes import *


def rotar_imagen(imagenes:list):
    lista_imagenes = []
    for i in range(len(imagenes)):
        imagen_rotada = py.transform.flip(imagenes[i],True,False)
        lista_imagenes.append(imagen_rotada)
    
    return lista_imagenes


enemigo_magico_quieto = [
py.image.load(r"recursos\enemigo_magico_img\idle\idle_0.png"),
py.image.load(r"recursos\enemigo_magico_img\idle\idle_1.png"),
py.image.load(r"recursos\enemigo_magico_img\idle\idle_2.png"),
py.image.load(r"recursos\enemigo_magico_img\idle\idle_3.png"),
py.image.load(r"recursos\enemigo_magico_img\idle\idle_4.png"),
py.image.load(r"recursos\enemigo_magico_img\idle\idle_5.png")]


enemigo_magico_quieto = [
py.transform.scale(enemigo_magico_quieto[0], (TAMAÑO_ENEMIGO_MAGICO_X , TAMAÑO_ENEMIGO_MAGICO_Y)), 
py.transform.scale(enemigo_magico_quieto[1], (TAMAÑO_ENEMIGO_MAGICO_X , TAMAÑO_ENEMIGO_MAGICO_Y)), 
py.transform.scale(enemigo_magico_quieto[2], (TAMAÑO_ENEMIGO_MAGICO_X , TAMAÑO_ENEMIGO_MAGICO_Y)),  
py.transform.scale(enemigo_magico_quieto[3], (TAMAÑO_ENEMIGO_MAGICO_X , TAMAÑO_ENEMIGO_MAGICO_Y)), 
py.transform.scale(enemigo_magico_quieto[4], (TAMAÑO_ENEMIGO_MAGICO_X , TAMAÑO_ENEMIGO_MAGICO_Y)),
py.transform.scale(enemigo_magico_quieto[5], (TAMAÑO_ENEMIGO_MAGICO_X , TAMAÑO_ENEMIGO_MAGICO_Y))]


enemigo_magico_corre = [
py.image.load(r"recursos\enemigo_magico_img\walk\walk_0.png"),
py.image.load(r"recursos\enemigo_magico_img\walk\walk_1.png"),
py.image.load(r"recursos\enemigo_magico_img\walk\walk_2.png"),
py.image.load(r"recursos\enemigo_magico_img\walk\walk_3.png"),
py.image.load(r"recursos\enemigo_magico_img\walk\walk_4.png"),
py.image.load(r"recursos\enemigo_magico_img\walk\walk_5.png")]


enemigo_magico_corre = [
py.transform.scale(enemigo_magico_corre[0], (TAMAÑO_ENEMIGO_MAGICO_X , TAMAÑO_ENEMIGO_MAGICO_Y)), 
py.transform.scale(enemigo_magico_corre[1], (TAMAÑO_ENEMIGO_MAGICO_X , TAMAÑO_ENEMIGO_MAGICO_Y)), 
py.transform.scale(enemigo_magico_corre[2], (TAMAÑO_ENEMIGO_MAGICO_X , TAMAÑO_ENEMIGO_MAGICO_Y)),  
py.transform.scale(enemigo_magico_corre[3], (TAMAÑO_ENEMIGO_MAGICO_X , TAMAÑO_ENEMIGO_MAGICO_Y)), 
py.transform.scale(enemigo_magico_corre[4], (TAMAÑO_ENEMIGO_MAGICO_X , TAMAÑO_ENEMIGO_MAGICO_Y)),
py.transform.scale(enemigo_magico_corre[5], (TAMAÑO_ENEMIGO_MAGICO_X , TAMAÑO_ENEMIGO_MAGICO_Y))]

#########################################################
enemigo_magico_ataque_uno = [
py.image.load(r"recursos\enemigo_magico_img\ataque\atack_0.png"),
py.image.load(r"recursos\enemigo_magico_img\ataque\atack_1.png"),
py.image.load(r"recursos\enemigo_magico_img\ataque\atack_2.png"),
py.image.load(r"recursos\enemigo_magico_img\ataque\atack_3.png"),
py.image.load(r"recursos\enemigo_magico_img\ataque\atack_4.png"),
py.image.load(r"recursos\enemigo_magico_img\ataque\atack_5.png"),
py.image.load(r"recursos\enemigo_magico_img\ataque\atack_6.png"),
py.image.load(r"recursos\enemigo_magico_img\ataque\atack_7.png"),]



enemigo_magico_ataque_uno = [
py.transform.scale(enemigo_magico_ataque_uno[0], (TAMAÑO_ENEMIGO_MAGICO_X + 10 ,TAMAÑO_ENEMIGO_MAGICO_Y)), 
py.transform.scale(enemigo_magico_ataque_uno[1], (TAMAÑO_ENEMIGO_MAGICO_X + 10 ,TAMAÑO_ENEMIGO_MAGICO_Y)), 
py.transform.scale(enemigo_magico_ataque_uno[2], (TAMAÑO_ENEMIGO_MAGICO_X + 10 ,TAMAÑO_ENEMIGO_MAGICO_Y)),  
py.transform.scale(enemigo_magico_ataque_uno[3], (TAMAÑO_ENEMIGO_MAGICO_X + 10 ,TAMAÑO_ENEMIGO_MAGICO_Y)), 
py.transform.scale(enemigo_magico_ataque_uno[4], (TAMAÑO_ENEMIGO_MAGICO_X + 10 ,TAMAÑO_ENEMIGO_MAGICO_Y)),  
py.transform.scale(enemigo_magico_ataque_uno[5], (TAMAÑO_ENEMIGO_MAGICO_X + 10 ,TAMAÑO_ENEMIGO_MAGICO_Y)), 
py.transform.scale(enemigo_magico_ataque_uno[6], (TAMAÑO_ENEMIGO_MAGICO_X + 10 ,TAMAÑO_ENEMIGO_MAGICO_Y)),  
py.transform.scale(enemigo_magico_ataque_uno[7], (TAMAÑO_ENEMIGO_MAGICO_X + 10 ,TAMAÑO_ENEMIGO_MAGICO_Y))]


enemigo_magico_quieto_izquierda = rotar_imagen(enemigo_magico_quieto)
enemigo_magico_corre_izquierda = rotar_imagen(enemigo_magico_corre)
enemigo_magico_ataque_uno_izquierda = rotar_imagen(enemigo_magico_ataque_uno)

enemigo_magico_animaciones = {}
enemigo_magico_animaciones["Quieto"] = enemigo_magico_quieto
enemigo_magico_animaciones["Quieto_izquierda"] = enemigo_magico_quieto_izquierda
enemigo_magico_animaciones["Corre"] = enemigo_magico_corre
enemigo_magico_animaciones["Corre_izquierda"] = enemigo_magico_corre_izquierda
enemigo_magico_animaciones["Ataque_uno"] = enemigo_magico_ataque_uno
enemigo_magico_animaciones["Ataque_uno_izquierda"] = enemigo_magico_ataque_uno_izquierda


bola_de_fuego = r"recursos\enemigo_magico_img\proyectil\108.png"