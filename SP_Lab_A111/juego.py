'''
desarrollo juego
creacion del controlador
'''
from manejo_pygame import *
import time
import random

def controlador_juego():

    W, H = 1280,720
    TAMAÑO_PANTALLA = (W,H)
    FPS = 30

    pygame.init()
    RELOJ = pygame.time.Clock()
    PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
    pygame.display.set_caption("ADIVINA EL LOGO")
    imagenes = cargar_imagenes(W,H)

    pygame.display.set_icon(imagenes["icono"])

    #fuente y textos
    fuente = pygame.font.SysFont("Times New Roman",40)
    texto_samsung = fuente.render("SAMSUNG", True, "black")
    fuente = pygame.font.SysFont("Times New Roman",30)
    vidas = 5
    monedas = 0
    texto_vidas = fuente.render(str(vidas), True, "white")
    texto_monedas = fuente.render(str(monedas), True, "white")
    

    #rectangulo marcas
    ancho_rectangulo, alto_rectangulo = 400, 200
    rect_x = (W - ancho_rectangulo) // 2
    rect = pygame.Rect(rect_x, 100, ancho_rectangulo, alto_rectangulo)

    #cuadrados para imagenes
    cuadrados = [pygame.Rect(100, 400, 250, 250),
                 pygame.Rect(380, 400, 250, 250),
                 pygame.Rect(660, 400, 250, 250),
                 pygame.Rect(940, 400, 250, 250)]
    indice_cuadrado_verde = random.randint(0,3)

    tiempo_inicial = time.time() #
    tiempo_adivinar_logo = 30 #
    # tiempo_resta = tiempo_adivinar_logo #

    flag = True

    PANTALLA.blit(imagenes["fondo"],(0,0))
    PANTALLA.blit(imagenes["logo_juego"],(470,120))
    PANTALLA.blit(imagenes["boton_play"],(520,480))

    while flag == True:
        RELOJ.tick(FPS)
        
        tiempo_transcurrido = time.time() - tiempo_inicial #
        tiempo_resta = tiempo_adivinar_logo - tiempo_transcurrido #
    
        texto_tiempo = fuente.render(f"{tiempo_resta:.2f}s", True, "white")

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                flag = False
                pygame.quit()
                sys.exit(0) 
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x = evento.pos[0]
                y = evento.pos[1]
                if (x >= 520 and x <= 720) and (y >= 480 and y <= 800):
                    print("se hizo click en el boton") 
                    PANTALLA.blit(imagenes["fondo"],(0,0))

                    pygame.draw.rect(PANTALLA, "white", rect)
                    text_rectangulo = texto_samsung.get_rect(center=rect.center)
                    PANTALLA.blit(texto_samsung, text_rectangulo)

                    PANTALLA.blit(imagenes["icono_vida"],(0,0))
                    PANTALLA.blit(texto_vidas, (50,0))

                    PANTALLA.blit(imagenes["icono_moneda"],(0,80))
                    PANTALLA.blit(texto_monedas, (50,85))

                    PANTALLA.blit(imagenes["icono_reloj"],(W-130,0))
                    PANTALLA.blit(texto_tiempo, (1200, 0))
                    
                for cuadrado in cuadrados:
                    if cuadrado == cuadrados[indice_cuadrado_verde]:
                        pygame.draw.rect(PANTALLA, "green", cuadrado) 
                    else:
                        pygame.draw.rect(PANTALLA, "red", cuadrado)


                for cuadrado in cuadrados:
                    if cuadrado.collidepoint(x, y):
                        indice_cuadrado_verde = random.randint(0,3)
                        if cuadrados.index(cuadrado) == indice_cuadrado_verde:
                            monedas += 20
                            # acumulador_tiempo 
                            tiempo_inicial = time.time()
                            print("verde")
                        else:
                            monedas -= 10
                            vidas -=1     
                            print("rojo")     
                        pygame.display.update()    
                
                            


        pygame.display.update()



        # mostrar_puntaje_y_tiempo(PANTALLA, imagenes, monedas, vidas, tiempo_resta)

        #     if tiempo_resta <= 0 or vidas == 0: #
        #         tiempo_resta = 0 #
        #         # guardar_datos(nombre_jugador, puntaje)
        #         # mostrar_resultados(PANTALLA, fuente)            
        
                    
        # PANTALLA.blit(imagenes["fondo"],(0,0))    

            

               
    
