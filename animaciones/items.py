import pygame as py 
from constantes.personajes import *

moneda_quieta = [
py.image.load(r"recursos\items\moneda\idle_0.png"),
py.image.load(r"recursos\items\moneda\idle_1.png"),
py.image.load(r"recursos\items\moneda\idle_2.png"),
py.image.load(r"recursos\items\moneda\idle_3.png"),
py.image.load(r"recursos\items\moneda\idle_4.png"),
py.image.load(r"recursos\items\moneda\idle_5.png"),
py.image.load(r"recursos\items\moneda\idle_6.png"),
py.image.load(r"recursos\items\moneda\idle_7.png"),
py.image.load(r"recursos\items\moneda\idle_8.png"),
py.image.load(r"recursos\items\moneda\idle_9.png"),
py.image.load(r"recursos\items\moneda\idle_10.png"),
py.image.load(r"recursos\items\moneda\idle_11.png"),
py.image.load(r"recursos\items\moneda\idle_12.png"),
py.image.load(r"recursos\items\moneda\idle_13.png"),
py.image.load(r"recursos\items\moneda\idle_14.png")]

moneda_reescale = {"2":(10,0), "3":(10,0),"4":(20,0), "5":(30,0),"6":(35,0), "7":(40,0),"8":(35,0), "9":(30,0),"10":(20,0), "11":(10,0),
                "12":(5,0)}

moneda_quieta = [
py.transform.scale(moneda_quieta[0],(TAMAÑO_MONEDA_X, TAMAÑO_MONEDA_Y)), 
py.transform.scale(moneda_quieta[1],(TAMAÑO_MONEDA_X, TAMAÑO_MONEDA_Y)),
py.transform.scale(moneda_quieta[2],(TAMAÑO_MONEDA_X - moneda_reescale["2"][0], TAMAÑO_MONEDA_Y)),
py.transform.scale(moneda_quieta[3],(TAMAÑO_MONEDA_X - moneda_reescale["3"][0], TAMAÑO_MONEDA_Y)), 
py.transform.scale(moneda_quieta[4],(TAMAÑO_MONEDA_X - moneda_reescale["4"][0], TAMAÑO_MONEDA_Y)),
py.transform.scale(moneda_quieta[5],(TAMAÑO_MONEDA_X - moneda_reescale["5"][0], TAMAÑO_MONEDA_Y)),
py.transform.scale(moneda_quieta[6],(TAMAÑO_MONEDA_X - moneda_reescale["6"][0], TAMAÑO_MONEDA_Y)), 
py.transform.scale(moneda_quieta[7],(TAMAÑO_MONEDA_X - moneda_reescale["7"][0], TAMAÑO_MONEDA_Y)),
py.transform.scale(moneda_quieta[8],(TAMAÑO_MONEDA_X - moneda_reescale["8"][0], TAMAÑO_MONEDA_Y)),
py.transform.scale(moneda_quieta[9],(TAMAÑO_MONEDA_X - moneda_reescale["9"][0], TAMAÑO_MONEDA_Y)), 
py.transform.scale(moneda_quieta[10],(TAMAÑO_MONEDA_X - moneda_reescale["10"][0], TAMAÑO_MONEDA_Y)),
py.transform.scale(moneda_quieta[11],(TAMAÑO_MONEDA_X - moneda_reescale["11"][0], TAMAÑO_MONEDA_Y)),
py.transform.scale(moneda_quieta[12],(TAMAÑO_MONEDA_X - moneda_reescale["12"][0], TAMAÑO_MONEDA_Y)), 
py.transform.scale(moneda_quieta[13],(TAMAÑO_MONEDA_X, TAMAÑO_MONEDA_Y)),
py.transform.scale(moneda_quieta[14],(TAMAÑO_MONEDA_X, TAMAÑO_MONEDA_Y))]

moneda_animaciones = {}
moneda_animaciones["Quieto"] = moneda_quieta

pocion_quieta = [py.image.load(r"recursos\items\pocion\idle_0.png")]
pocion_quieta = [py.transform.scale(pocion_quieta[0],(30, 50))]
pocion_animaciones = {}
pocion_animaciones["Quieto"] = pocion_quieta 