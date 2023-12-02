import pygame
import sys
from pygame.locals import *
from constantes.modo import *
from clases.z_direcciones_clases import *
from enemigos.z_direcciones_enemigos import *
from animaciones.z_direcciones_animaciones import *




ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
CELESTE = (0, 150, 255)


#CONFIGURACIONES GENERICAS
W, H = 1400, 850
FPS = 30

#FONDO
fondo = pygame.image.load(r"recursos\escenario\fondo_lvl_1.jpg")
fondo = pygame.transform.scale(fondo, (W, H))

corazon = pygame.image.load(r"recursos\estadisticas\hearth.png")
corazon = pygame.transform.scale(corazon, (35, 35))

coin = pygame.image.load(r"recursos\estadisticas\coin_0.png")
coin = pygame.transform.scale(coin, (35, 35))

pocion = pygame.image.load(r"recursos\items\pocion\idle_0.png")
pocion = pygame.transform.scale(pocion, (30, 50))



piso = Plataforma((W,50),(0,800) , r"recursos\escenario\piso.png")
plataforma_uno = Plataforma((1000,60),(100,500), r"recursos\escenario\17_rocas.png")
plataforma_dos = Plataforma((190,60),(1200,650), r"recursos\escenario\3_rocas.png")
plataforma_tres = Plataforma((1000,60),(0,250), r"recursos\escenario\17_rocas.png")
plataforma_cuatro = Plataforma((190,60),(1200,350), r"recursos\escenario\3_rocas.png")


item_uno = Item((30,45),(600,400), r"recursos\items\moneda\idle_0.png", False, moneda_animaciones, "aumentar_monedas")
item_dos = Item((30,45),(600,600), r"recursos\items\pocion\idle_0.png", False, pocion_animaciones, "aumentar_pociones")



heroe = Heroe((100,100),(0,300), r"recursos\heroe_img\idle\idle_0.png", 10, True, heroe_animaciones)
enemigo_uno = Enemigo_fisico((100,100),(400,500), r"recursos\enemigo_fisico_img\idle\idle_0.png", 5, True, enemigo_fisico_animaciones)
enemigo_dos = Enemigo_Magico((100,125),(400,700), r"recursos\enemigo_magico_img\idle\idle_0.png", 5, True, enemigo_magico_animaciones)


lista_plataformas = [piso, plataforma_uno, plataforma_dos, plataforma_tres, plataforma_cuatro]
lista_enemigos = [enemigo_uno, enemigo_dos]
# lista_enemigos = []
lista_items = [item_uno, item_dos]

















#PYGAME
pygame.init()
fuente = pygame.font.SysFont("Arial", 35)
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))
bandera = True

while bandera:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == MOUSEBUTTONDOWN:#PRINTEAR LA UBICACION DEL CLIKEO EN PANTALLA
            print(evento.pos)
        elif evento.type == KEYDOWN:
            if evento.key == K_TAB:
                cambiar_modo()

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_RIGHT]:
        heroe.que_hace = "Corre"
        heroe.esta_mirando = "Derecha"

        if(teclas[pygame.K_SPACE]):
            heroe.que_hace = "Salta"
        flag_disparo = True

        if (teclas[pygame.K_q]):
            heroe.contador_pasos = 0
            heroe.termino_animacion = False
            heroe.ultima_accion = "Ataque_uno"
            heroe.que_hace = "Ataque_uno" 
        
        if teclas[pygame.K_e] and heroe.puede_dashear:
            heroe.contador_pasos = 0
            heroe.termino_animacion = False
            heroe.ultima_accion = "Dash" 
            heroe.que_hace = "Dash" 

        if teclas[pygame.K_w] and heroe.puede_lanzar_ataque:
            heroe.tiempo_ultimo_lanzamiento = py.time.get_ticks()
            heroe.puede_lanzar_ataque = False
            heroe.contador_pasos = 0
            heroe.termino_animacion = False
            heroe.ultima_accion = "Ataque_dos"
            heroe.que_hace = "Ataque_dos" 


    elif teclas[pygame.K_LEFT]:
        heroe.que_hace = "Corre_izquierda"
        heroe.esta_mirando = "Izquierda"
        flag_disparo = True

        if(teclas[pygame.K_SPACE]):
            heroe.que_hace = "Salta_izquierda"

        if (teclas[pygame.K_q]):
            heroe.contador_pasos = 0
            heroe.termino_animacion = False
            heroe.ultima_accion = "Ataque_uno_izquierda"
            heroe.que_hace = "Ataque_uno_izquierda" 

        if teclas[pygame.K_e] and heroe.puede_dashear:
            heroe.contador_pasos = 0
            heroe.ultima_accion = "Dash_izquierda" 
            heroe.termino_animacion = False
            heroe.que_hace = "Dash_izquierda" 

        if teclas[pygame.K_w] and heroe.puede_lanzar_ataque:
            heroe.tiempo_ultimo_lanzamiento = py.time.get_ticks()
            heroe.puede_lanzar_ataque = False
            heroe.contador_pasos = 0
            heroe.termino_animacion = False
            heroe.ultima_accion = "Ataque_dos_izquierda"
            heroe.que_hace = "Ataque_dos_izquierda" 


    elif(teclas[pygame.K_SPACE]):
        heroe.contador_pasos = 0
        if heroe.esta_mirando == "Derecha":
            heroe.que_hace = "Salta"   
        else:
            heroe.que_hace = "Salta_izquierda" 

    elif (teclas[pygame.K_q]):
        heroe.contador_pasos = 0
        heroe.termino_animacion = False
        
        if heroe.esta_mirando == "Derecha":
            heroe.ultima_accion = "Ataque_uno"
            heroe.que_hace = "Ataque_uno" 
        else:
            heroe.ultima_accion = "Ataque_uno_izquierda"
            heroe.que_hace = "Ataque_uno_izquierda" 

    elif teclas[pygame.K_w] and heroe.puede_lanzar_ataque:
        heroe.contador_pasos = 0
        heroe.termino_animacion = False
        heroe.tiempo_ultimo_lanzamiento = py.time.get_ticks()
        heroe.puede_lanzar_ataque = False
        
        if heroe.esta_mirando == "Derecha":
            heroe.ultima_accion = "Ataque_dos"
            heroe.que_hace = "Ataque_dos" 
        else:
            heroe.ultima_accion = "Ataque_dos_izquierda"
            heroe.que_hace = "Ataque_dos_izquierda" 



    elif teclas[pygame.K_e] and heroe.puede_dashear:
        heroe.contador_pasos = 0
        heroe.termino_animacion = False

        if heroe.esta_mirando == "Derecha":
            heroe.ultima_accion = "Dash"
            heroe.que_hace = "Dash" 
        else:
            heroe.que_hace = "Dash_izquierda" 
            heroe.ultima_accion = "Dash_izquierda"



    elif teclas[pygame.K_r] and heroe.pociones > 0:
        heroe.vida += 1
        heroe.pociones -= 1

    else:                          
        if heroe.esta_mirando == "Izquierda":
            heroe.que_hace = "Quieto_izquierda"
        else:
            heroe.que_hace = "Quieto"  

    

    listas_proyectiles_enemigos = [enemigo_dos.lista_proyectiles]

    PANTALLA.blit(fondo, (0, 0))

    for plataforma in lista_plataformas:
        plataforma.blit(PANTALLA)

    for i in range(len(lista_enemigos)):
        lista_enemigos[i].actualizar(PANTALLA, lista_plataformas, heroe.rect_principal, heroe.rect_ataque_uno, heroe.lista_proyectiles)
        if not lista_enemigos[i].esta_vivo:

            # lista_items.append(Item((30,45),(lista_enemigos[i].rect_principal.x, lista_enemigos[i].rect_principal.y),
            # r"recursos\items\moneda\idle_0.png", False, moneda_animaciones, "aumentar_monedas"))

            # if lista_enemigos[i].probabilidad_de_pocion < 26:
            #     lista_items.append(Item((30,45),(lista_enemigos[i].rect_principal.x + 35, lista_enemigos[i].rect_principal.y), 
            #     r"recursos\items\pocion\idle_0.png", False, pocion_animaciones, "aumentar_pociones"))

            del lista_enemigos[i]
            break

    for i in range(len(lista_items)):
        lista_items[i].actualizar(PANTALLA, lista_plataformas)
    


    a,b = 0,0
    for corazones in range(heroe.vida):
        PANTALLA.blit(corazon, (a, b))
        a += 35

    a,b = 0,75
    PANTALLA.blit(pocion, (a, b))
    cantidad_pociones = fuente.render(f"{heroe.pociones}", False, NEGRO, AZUL)
    PANTALLA.blit(cantidad_pociones,(45,85))


    a,b = 0,35
    PANTALLA.blit(coin, (a, b))
    cantidad_monedas = fuente.render(f"{heroe.monedas}", False, NEGRO, AZUL)
    PANTALLA.blit(cantidad_monedas,(45,35))


    heroe.actualizar(PANTALLA, lista_plataformas, listas_proyectiles_enemigos, lista_enemigos, lista_items)


    #print(heroe.monedas)


    if obtener_modo():
        #METER ALL DENTRO DE UNA FUNCION, Y QUE ESA FUNCIONES LLAME A OTRA FUNCIONES DE CLAD PJ, Y COMENTAR LO QUE NO NECESITE, 
        pygame.draw.rect(PANTALLA, "cyan", heroe.rect_principal, 3)
        
        # pygame.draw.rect(PANTALLA, "red", heroe.rect_left, 3)
        # pygame.draw.rect(PANTALLA, "blue", heroe.rect_right, 3)
        # pygame.draw.rect(PANTALLA, "grey", heroe.rect_top, 3)
        # pygame.draw.rect(PANTALLA, "green", heroe.rect_bottom, 3)


        pygame.draw.rect(PANTALLA, "red", piso.rect_principal, 3)

        pygame.draw.rect(PANTALLA, "red", plataforma_uno.rect_principal, 3)
        

        pygame.draw.rect(PANTALLA, "cyan", piso.barrera_uno, 3)
        pygame.draw.rect(PANTALLA, "cyan", piso.barrera_dos, 3)

        pygame.draw.rect(PANTALLA, "cyan", item_uno.rect_principal, 3)

        # pygame.draw.rect(PANTALLA, "red", enemigo_uno.rect_principal, 3)
        # pygame.draw.rect(PANTALLA, "cyan", enemigo_uno.rect_vision, 3)


        pygame.draw.rect(PANTALLA, "cyan", heroe.rect_reescalado_bliteo, 3)
        pygame.draw.rect(PANTALLA, "red", heroe.rect_ataque_uno, 3)





        pygame.draw.rect(PANTALLA, "red", enemigo_uno.rect_left, 3)
        pygame.draw.rect(PANTALLA, "blue", enemigo_uno.rect_right, 3)
        pygame.draw.rect(PANTALLA, "grey", enemigo_uno.rect_top, 3)
        pygame.draw.rect(PANTALLA, "green", enemigo_uno.rect_reescalado_bliteo, 3)
        pygame.draw.rect(PANTALLA, "green", enemigo_uno.rect_ataque_uno, 3)
        pygame.draw.rect(PANTALLA, "green", enemigo_uno.rect_vision, 3)


        pygame.draw.rect(PANTALLA, "green", enemigo_dos.rect_vision, 3)





    pygame.display.update()


