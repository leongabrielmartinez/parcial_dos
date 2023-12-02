import pygame as py 
from constantes.personajes import *


def rotar_imagen(imagenes:list):
    lista_imagenes = []
    for i in range(len(imagenes)):
        imagen_rotada = py.transform.flip(imagenes[i],True,False)
        lista_imagenes.append(imagen_rotada)
    
    return lista_imagenes

heroe_quieto = [
py.image.load("recursos\heroe_img\idle\idle_0.png"),
py.image.load("recursos\heroe_img\idle\idle_1.png"),
py.image.load("recursos\heroe_img\idle\idle_2.png"),
py.image.load("recursos\heroe_img\idle\idle_3.png"),
py.image.load("recursos\heroe_img\idle\idle_4.png"),
py.image.load("recursos\heroe_img\idle\idle_5.png"),
py.image.load("recursos\heroe_img\idle\idle_6.png")]

h_reescale_QD = {"0":(0,0), "1":(0,0), "2":(0,0), "3":(0,0), "4":(0,0)}

heroe_quieto = [
py.transform.scale(heroe_quieto[0], (TAMAÑO_HEROE_X + h_reescale_QD["0"][0],TAMAÑO_HEROE_Y + h_reescale_QD["0"][1])), 
py.transform.scale(heroe_quieto[1], (TAMAÑO_HEROE_X + h_reescale_QD["1"][0],TAMAÑO_HEROE_Y + h_reescale_QD["1"][1])), 
py.transform.scale(heroe_quieto[2], (TAMAÑO_HEROE_X + h_reescale_QD["2"][0],TAMAÑO_HEROE_Y + h_reescale_QD["2"][1])),  
py.transform.scale(heroe_quieto[3], (TAMAÑO_HEROE_X + h_reescale_QD["3"][0],TAMAÑO_HEROE_Y + h_reescale_QD["3"][1])), 
py.transform.scale(heroe_quieto[4], (TAMAÑO_HEROE_X + h_reescale_QD["4"][0],TAMAÑO_HEROE_Y + h_reescale_QD["4"][1])),  
py.transform.scale(heroe_quieto[5], (TAMAÑO_HEROE_X,TAMAÑO_HEROE_Y)),
py.transform.scale(heroe_quieto[6], (TAMAÑO_HEROE_X,TAMAÑO_HEROE_Y))]



heroe_camina = [
py.image.load("recursos\heroe_img\walk\walk_0.png"),
py.image.load("recursos\heroe_img\walk\walk_1.png"),
py.image.load("recursos\heroe_img\walk\walk_2.png"),
py.image.load("recursos\heroe_img\walk\walk_3.png"),
py.image.load("recursos\heroe_img\walk\walk_4.png"),
py.image.load("recursos\heroe_img\walk\walk_5.png")]

heroe_camina = [
py.transform.scale(heroe_camina[0],(TAMAÑO_HEROE_X,TAMAÑO_HEROE_Y)), 
py.transform.scale(heroe_camina[1],(TAMAÑO_HEROE_X,TAMAÑO_HEROE_Y)),
py.transform.scale(heroe_camina[2],(TAMAÑO_HEROE_X,TAMAÑO_HEROE_Y)), 
py.transform.scale(heroe_camina[3],(TAMAÑO_HEROE_X,TAMAÑO_HEROE_Y)),
py.transform.scale(heroe_camina[4],(TAMAÑO_HEROE_X,TAMAÑO_HEROE_Y)), 
py.transform.scale(heroe_camina[5],(TAMAÑO_HEROE_X,TAMAÑO_HEROE_Y))]



heroe_salta = [
py.image.load("recursos\heroe_img\jump\jump_0.png"),
py.image.load("recursos\heroe_img\jump\jump_1.png"),
py.image.load("recursos\heroe_img\jump\jump_2.png"),
py.image.load("recursos\heroe_img\jump\jump_3.png"),
py.image.load("recursos\heroe_img\jump\jump_4.png")]

heroe_salta = [
py.transform.scale(heroe_salta[0],(TAMAÑO_HEROE_X,TAMAÑO_HEROE_Y)), 
py.transform.scale(heroe_salta[1],(TAMAÑO_HEROE_X,TAMAÑO_HEROE_Y)),
py.transform.scale(heroe_salta[2],(TAMAÑO_HEROE_X,TAMAÑO_HEROE_Y)), 
py.transform.scale(heroe_salta[3],(TAMAÑO_HEROE_X,TAMAÑO_HEROE_Y)),
py.transform.scale(heroe_salta[4],(TAMAÑO_HEROE_X,TAMAÑO_HEROE_Y))]



heroe_ataque_uno = [
py.image.load(r"recursos\heroe_img\atack_one\atack_0.png"),
py.image.load(r"recursos\heroe_img\atack_one\atack_1.png"),
py.image.load(r"recursos\heroe_img\atack_one\atack_2.png"),
py.image.load(r"recursos\heroe_img\atack_one\atack_3.png"),
py.image.load(r"recursos\heroe_img\atack_one\atack_4.png"),
py.image.load(r"recursos\heroe_img\atack_one\atack_5.png")]

h_reescale_AU = {"0":(0,60), "1":(10,50), "2":(60,70), "3":(60,70), "4":(20,70), "5":(20,70)}

heroe_ataque_uno = [
py.transform.scale(heroe_ataque_uno[0], (TAMAÑO_HEROE_X + h_reescale_AU["0"][0],TAMAÑO_HEROE_Y + h_reescale_AU["0"][1])), 
py.transform.scale(heroe_ataque_uno[1], (TAMAÑO_HEROE_X + h_reescale_AU["1"][0],TAMAÑO_HEROE_Y + h_reescale_AU["1"][1])), 
py.transform.scale(heroe_ataque_uno[2], (TAMAÑO_HEROE_X + h_reescale_AU["2"][0] ,TAMAÑO_HEROE_Y + h_reescale_AU["2"][1] + 50)),  
py.transform.scale(heroe_ataque_uno[3], (TAMAÑO_HEROE_X + h_reescale_AU["3"][0] ,TAMAÑO_HEROE_Y + h_reescale_AU["3"][1] + 60)), 
py.transform.scale(heroe_ataque_uno[4], (TAMAÑO_HEROE_X + h_reescale_AU["4"][0]  ,TAMAÑO_HEROE_Y + h_reescale_AU["4"][1] + 25)),
py.transform.scale(heroe_ataque_uno[5], (TAMAÑO_HEROE_X + h_reescale_AU["5"][0]  ,TAMAÑO_HEROE_Y + h_reescale_AU["5"][1] + 25))]
#############
heroe_ataque_dos = [
py.image.load(r"recursos\heroe_img\atack_two\atack_0.png"),
py.image.load(r"recursos\heroe_img\atack_two\atack_1.png")]

h_reescale_AD = {"0":(0,0), "1":(60,0)}

heroe_ataque_dos = [
py.transform.scale(heroe_ataque_dos[0], (TAMAÑO_HEROE_X + h_reescale_AD["0"][0],TAMAÑO_HEROE_Y + h_reescale_AD["0"][1])), 
py.transform.scale(heroe_ataque_dos[1], (TAMAÑO_HEROE_X + h_reescale_AD["1"][0],TAMAÑO_HEROE_Y + h_reescale_AD["1"][1]))]


heroe_dash = [
py.image.load(r"recursos\heroe_img\dash\dash_0.png"),
py.image.load(r"recursos\heroe_img\dash\dash_1.png"),
py.image.load(r"recursos\heroe_img\dash\dash_2.png")]

heroe_dash = [
py.transform.scale(heroe_dash[0],(TAMAÑO_HEROE_X,TAMAÑO_HEROE_Y)), 
py.transform.scale(heroe_dash[1],(TAMAÑO_HEROE_X,TAMAÑO_HEROE_Y)),
py.transform.scale(heroe_dash[2],(TAMAÑO_HEROE_X,TAMAÑO_HEROE_Y))]

heroe_quieto_izquierda = rotar_imagen(heroe_quieto)
heroe_camina_izquierda = rotar_imagen(heroe_camina)
heroe_salta_izquierda = rotar_imagen(heroe_salta)
heroe_ataque_uno_izquierda = rotar_imagen(heroe_ataque_uno)
heroe_ataque_dos_izquierda = rotar_imagen(heroe_ataque_dos)
heroe_dash_izquierda = rotar_imagen(heroe_dash)


heroe_animaciones = {}
heroe_animaciones["Quieto"] = heroe_quieto
heroe_animaciones["Quieto_izquierda"] = heroe_quieto_izquierda


heroe_animaciones["Corre"] = heroe_camina
heroe_animaciones["Corre_izquierda"] = heroe_camina_izquierda

heroe_animaciones["Salta"] = heroe_salta
heroe_animaciones["Salta_izquierda"] = heroe_salta_izquierda

heroe_animaciones["Ataque_uno"] = heroe_ataque_uno
heroe_animaciones["Ataque_uno_izquierda"] = heroe_ataque_uno_izquierda

heroe_animaciones["Ataque_dos"] = heroe_ataque_dos
heroe_animaciones["Ataque_dos_izquierda"] = heroe_ataque_dos_izquierda

heroe_animaciones["Dash"] = heroe_dash
heroe_animaciones["Dash_izquierda"] = heroe_dash_izquierda 



# #ITEM
# moneda_quieta = [py.image.load("recursos\moneda\idle_0.png"),py.image.load("recursos\moneda\idle_1.png")]
# moneda_quieta = [py.transform.scale(moneda_quieta[0],(30,45)), py.transform.scale(moneda_quieta[1],(30,45))]
# moneda_animaciones = {}
# moneda_animaciones["Quieta"] = moneda_quieta


