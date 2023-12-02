import pygame as py 
from constantes.personajes import *


def rotar_imagen(imagenes:list):
    lista_imagenes = []
    for i in range(len(imagenes)):
        imagen_rotada = py.transform.flip(imagenes[i],True,False)
        lista_imagenes.append(imagen_rotada)
    
    return lista_imagenes


enemigo_fisico_quieto = [
py.image.load(r"recursos\enemigo_fisico_img\idle\idle_0.png"),
py.image.load(r"recursos\enemigo_fisico_img\idle\idle_1.png"),
py.image.load(r"recursos\enemigo_fisico_img\idle\idle_2.png"),
py.image.load(r"recursos\enemigo_fisico_img\idle\idle_3.png"),
py.image.load(r"recursos\enemigo_fisico_img\idle\idle_4.png"),
py.image.load(r"recursos\enemigo_fisico_img\idle\idle_5.png")]


enemigo_fisico_quieto = [
py.transform.scale(enemigo_fisico_quieto[0], (TAMAÑO_ENEMIGO_FISICO_X , TAMAÑO_ENEMIGO_FISICO_Y )), 
py.transform.scale(enemigo_fisico_quieto[1], (TAMAÑO_ENEMIGO_FISICO_X , TAMAÑO_ENEMIGO_FISICO_Y )), 
py.transform.scale(enemigo_fisico_quieto[2], (TAMAÑO_ENEMIGO_FISICO_X , TAMAÑO_ENEMIGO_FISICO_Y )),  
py.transform.scale(enemigo_fisico_quieto[3], (TAMAÑO_ENEMIGO_FISICO_X , TAMAÑO_ENEMIGO_FISICO_Y )), 
py.transform.scale(enemigo_fisico_quieto[4], (TAMAÑO_ENEMIGO_FISICO_X , TAMAÑO_ENEMIGO_FISICO_Y )),
py.transform.scale(enemigo_fisico_quieto[5], (TAMAÑO_ENEMIGO_FISICO_X , TAMAÑO_ENEMIGO_FISICO_Y ))]


enemigo_fisico_camina = [
py.image.load(r"recursos\enemigo_fisico_img\walk\walk_0.png"),
py.image.load(r"recursos\enemigo_fisico_img\walk\walk_1.png"),
py.image.load(r"recursos\enemigo_fisico_img\walk\walk_2.png"),
py.image.load(r"recursos\enemigo_fisico_img\walk\walk_3.png"),
py.image.load(r"recursos\enemigo_fisico_img\walk\walk_4.png"),
py.image.load(r"recursos\enemigo_fisico_img\walk\walk_5.png")]


enemigo_fisico_camina = [
py.transform.scale(enemigo_fisico_camina[0], (TAMAÑO_ENEMIGO_FISICO_X , TAMAÑO_ENEMIGO_FISICO_Y )), 
py.transform.scale(enemigo_fisico_camina[1], (TAMAÑO_ENEMIGO_FISICO_X , TAMAÑO_ENEMIGO_FISICO_Y )), 
py.transform.scale(enemigo_fisico_camina[2], (TAMAÑO_ENEMIGO_FISICO_X , TAMAÑO_ENEMIGO_FISICO_Y )),  
py.transform.scale(enemigo_fisico_camina[3], (TAMAÑO_ENEMIGO_FISICO_X , TAMAÑO_ENEMIGO_FISICO_Y )), 
py.transform.scale(enemigo_fisico_camina[4], (TAMAÑO_ENEMIGO_FISICO_X , TAMAÑO_ENEMIGO_FISICO_Y )),
py.transform.scale(enemigo_fisico_camina[5], (TAMAÑO_ENEMIGO_FISICO_X , TAMAÑO_ENEMIGO_FISICO_Y ))]

#########################################################
enemigo_fisico_ataca = [
py.image.load(r"recursos\enemigo_fisico_img\atack\atack_0.png"),
py.image.load(r"recursos\enemigo_fisico_img\atack\atack_1.png"),
py.image.load(r"recursos\enemigo_fisico_img\atack\atack_2.png"),
py.image.load(r"recursos\enemigo_fisico_img\atack\atack_3.png"),
py.image.load(r"recursos\enemigo_fisico_img\atack\atack_4.png"),
py.image.load(r"recursos\enemigo_fisico_img\atack\atack_5.png"),
py.image.load(r"recursos\enemigo_fisico_img\atack\atack_6.png"),
py.image.load(r"recursos\enemigo_fisico_img\atack\atack_7.png"),]

eu_reescale_A = {"0":(60,30), "1":(60,30), "2":(60,30), "3":(125,125), "4":(125,125), "5":(130,60), "6":(135,60), "7":(0,0)}

enemigo_fisico_ataca = [
py.transform.scale(enemigo_fisico_ataca[0], (TAMAÑO_ENEMIGO_FISICO_X + eu_reescale_A ["0"][0],TAMAÑO_ENEMIGO_FISICO_Y + eu_reescale_A ["0"][1])), 
py.transform.scale(enemigo_fisico_ataca[1], (TAMAÑO_ENEMIGO_FISICO_X + eu_reescale_A ["1"][0],TAMAÑO_ENEMIGO_FISICO_Y + eu_reescale_A ["1"][1])), 
py.transform.scale(enemigo_fisico_ataca[2], (TAMAÑO_ENEMIGO_FISICO_X + eu_reescale_A ["2"][0],TAMAÑO_ENEMIGO_FISICO_Y + eu_reescale_A ["2"][1])),  
py.transform.scale(enemigo_fisico_ataca[3], (TAMAÑO_ENEMIGO_FISICO_X + eu_reescale_A ["3"][0],TAMAÑO_ENEMIGO_FISICO_Y + eu_reescale_A ["3"][1])), 
py.transform.scale(enemigo_fisico_ataca[4], (TAMAÑO_ENEMIGO_FISICO_X + eu_reescale_A ["4"][0],TAMAÑO_ENEMIGO_FISICO_Y + eu_reescale_A ["4"][1])),  
py.transform.scale(enemigo_fisico_ataca[5], (TAMAÑO_ENEMIGO_FISICO_X + eu_reescale_A ["5"][0],TAMAÑO_ENEMIGO_FISICO_Y + eu_reescale_A ["5"][1])), 
py.transform.scale(enemigo_fisico_ataca[6], (TAMAÑO_ENEMIGO_FISICO_X + eu_reescale_A ["6"][0],TAMAÑO_ENEMIGO_FISICO_Y + eu_reescale_A ["6"][1])),  
py.transform.scale(enemigo_fisico_ataca[7], (TAMAÑO_ENEMIGO_FISICO_X + eu_reescale_A ["7"][0],TAMAÑO_ENEMIGO_FISICO_Y + eu_reescale_A ["7"][1]))]


enemigo_fisico_quieto_izquierda = rotar_imagen(enemigo_fisico_quieto)
enemigo_fisico_camina_izquierda = rotar_imagen(enemigo_fisico_camina)
enemigo_fisico_ataca_izquierda = rotar_imagen(enemigo_fisico_ataca)

enemigo_fisico_animaciones = {}
enemigo_fisico_animaciones["Quieto"] = enemigo_fisico_quieto
enemigo_fisico_animaciones["Quieto_izquierda"] = enemigo_fisico_quieto_izquierda
enemigo_fisico_animaciones["Corre"] = enemigo_fisico_quieto
enemigo_fisico_animaciones["Corre_izquierda"] = enemigo_fisico_camina_izquierda
enemigo_fisico_animaciones["Ataque_uno"] = enemigo_fisico_ataca
enemigo_fisico_animaciones["Ataque_uno_izquierda"] = enemigo_fisico_ataca_izquierda
