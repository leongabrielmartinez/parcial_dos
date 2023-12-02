import pygame as py 
from constantes.personajes import *

trampa_avanza = [
py.image.load(r"recursos\trampa_explosiva_img\avanza_0.png"),
py.image.load(r"recursos\trampa_explosiva_img\avanza_1.png"),
py.image.load(r"recursos\trampa_explosiva_img\avanza_2.png"),
py.image.load(r"recursos\trampa_explosiva_img\avanza_3.png"),
py.image.load(r"recursos\trampa_explosiva_img\avanza_4.png")]


trampa_avanza = [
py.transform.scale(trampa_avanza[0], (TAMAÑO_TRAMPA_X , TAMAÑO_TRAMPA_Y)), 
py.transform.scale(trampa_avanza[1], (TAMAÑO_TRAMPA_X , TAMAÑO_TRAMPA_Y)), 
py.transform.scale(trampa_avanza[2], (TAMAÑO_TRAMPA_X , TAMAÑO_TRAMPA_Y)),  
py.transform.scale(trampa_avanza[3], (TAMAÑO_TRAMPA_X , TAMAÑO_TRAMPA_Y)), 
py.transform.scale(trampa_avanza[4], (TAMAÑO_TRAMPA_X , TAMAÑO_TRAMPA_Y)),]



trampa_explota = [
py.image.load(r"recursos\trampa_explosiva_img\explota_0.png"),
py.image.load(r"recursos\trampa_explosiva_img\explota_1.png"),
py.image.load(r"recursos\trampa_explosiva_img\explota_2.png"),
py.image.load(r"recursos\trampa_explosiva_img\explota_3.png"),
py.image.load(r"recursos\trampa_explosiva_img\explota_4.png"),
py.image.load(r"recursos\trampa_explosiva_img\explota_5.png"),
py.image.load(r"recursos\trampa_explosiva_img\explota_6.png")]

trampa_reescale = {"0":(0,0), "1":(0,0), "2":(0,0), "3":(0,0), "4":(0,0), "5":(0,0), "6":(0,0)}

trampa_explota = [
py.transform.scale(trampa_explota[0], (TAMAÑO_TRAMPA_X + trampa_reescale["0"][0], TAMAÑO_TRAMPA_Y + trampa_reescale["0"][1])), 
py.transform.scale(trampa_explota[1], (TAMAÑO_TRAMPA_X + trampa_reescale["1"][0], TAMAÑO_TRAMPA_Y + trampa_reescale["1"][1])), 
py.transform.scale(trampa_explota[2], (TAMAÑO_TRAMPA_X + trampa_reescale["2"][0], TAMAÑO_TRAMPA_Y + trampa_reescale["2"][1])),  
py.transform.scale(trampa_explota[3], (TAMAÑO_TRAMPA_X + trampa_reescale["3"][0], TAMAÑO_TRAMPA_Y + trampa_reescale["3"][1])), 
py.transform.scale(trampa_explota[4], (TAMAÑO_TRAMPA_X + trampa_reescale["4"][0], TAMAÑO_TRAMPA_Y + trampa_reescale["4"][1])),
py.transform.scale(trampa_explota[3], (TAMAÑO_TRAMPA_X + trampa_reescale["5"][0], TAMAÑO_TRAMPA_Y + trampa_reescale["5"][1])), 
py.transform.scale(trampa_explota[4], (TAMAÑO_TRAMPA_X + trampa_reescale["6"][0], TAMAÑO_TRAMPA_Y + trampa_reescale["6"][1])),]


trampa_animaciones = {}
trampa_animaciones["Avanza"] = trampa_avanza
trampa_animaciones["Explota"] = trampa_explota