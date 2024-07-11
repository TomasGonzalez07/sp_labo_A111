'''
desarrollo juego
creacion del controlador
'''
from manejo_pygame import *
from biblioteca import *
import time
import random

def pantalla_inicio():
    pygame.init()
    W, H = 1280, 720
    TAMAÑO_PANTALLA = (W, H)
    fuente = pygame.font.SysFont("Times New Roman", 40)
    fuente_resultados = pygame.font.SysFont("Times New Roman", 16)

    PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
    pygame.display.set_caption("ADIVINA EL LOGO")
    imagenes = cargar_imagenes(W, H)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if 520 <= x <= 720 and 480 <= y <= 530:
                    controlador_juego()

        PANTALLA.blit(imagenes["fondo"],(0,0))
        PANTALLA.blit(imagenes["logo_juego"],(470,120))
        PANTALLA.blit(imagenes["boton_play"],(520,480))
        mostrar_resultados(PANTALLA, H, fuente_resultados) 

        pygame.display.flip()

def controlador_juego():
    W, H = 1280, 720
    TAMAÑO_PANTALLA = (W, H)
    FPS = 60

    pygame.init()
    RELOJ = pygame.time.Clock()
    PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
    pygame.display.set_caption("ADIVINA EL LOGO")
    imagenes = cargar_imagenes(W, H)

    pygame.display.set_icon(imagenes["icono"])

    #fuente
    fuente = pygame.font.SysFont("Times New Roman", 40)
    fuente_resultados = pygame.font.SysFont("Times New Roman", 16)
    
    #rectangulo marcas
    ancho_rectangulo, alto_rectangulo = 400, 200
    rect_x = (W - ancho_rectangulo) // 2
    rect = pygame.Rect(rect_x, 100, ancho_rectangulo, alto_rectangulo)

    #lista marcas
    lista_marcas =["SAMSUNG", "APPLE", "MC DONALD", "BURGER KING", "PEPSI",
                   "COCA COLA", "PUMA", "POLO", "NIKE", "ADIDAS",
                   "TOMMY HILFIGER", "MICROSOFT", "GOOGLE", "HYUNDAI", "LG"]
    
    indice_marca_actual = 0
    texto_marca = fuente.render(lista_marcas[indice_marca_actual], True, "black")
    
    #cuadrados para imágenes
    cuadrados = [
        pygame.Rect(100, 400, 250, 250),
        pygame.Rect(380, 400, 250, 250),
        pygame.Rect(660, 400, 250, 250),
        pygame.Rect(940, 400, 250, 250)
    ]
    indice_cuadrado_verde = random.randint(0, 3)

    #tiempo
    tiempo_inicial = time.time()
    tiempo_adivinar_logo = 30

    vidas = 5
    monedas = 0
    tiempo_jugado = 0

    flag = True

    while flag:
        RELOJ.tick(FPS)

        tiempo_transcurrido = time.time() - tiempo_inicial
        tiempo_resta = tiempo_adivinar_logo - tiempo_transcurrido

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                flag = False
                pygame.quit()
                sys.exit(0)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos

                for cuadrado in cuadrados:
                    if cuadrado.collidepoint(x, y):
                        if cuadrados.index(cuadrado) == indice_cuadrado_verde:
                            print("Clic en el cuadrado verde")
                            monedas += 20
                            tiempo_jugado += tiempo_transcurrido
                            tiempo_inicial = time.time() 
                            indice_cuadrado_verde = random.randint(0, 3)  
                            indice_marca_actual = indice_marca_actual + 1
                            if indice_marca_actual < len(lista_marcas):
                                texto_marca = fuente.render(lista_marcas[indice_marca_actual], True, "black")
                            else:
                                texto_marca = fuente.render("Fin de las marcas", True, "black")
                        else:
                            monedas -= 10
                            vidas -= 1
                            print("Clic en un cuadrado rojo")

        mostrar_datos(PANTALLA, imagenes, monedas, vidas, tiempo_resta, texto_marca, rect)

        for cuadrado in cuadrados:
            if cuadrados.index(cuadrado) == indice_cuadrado_verde:
                pygame.draw.rect(PANTALLA, "green", cuadrado)
            else:
                pygame.draw.rect(PANTALLA, "red", cuadrado)


        if tiempo_resta <= 0 or vidas == 0 or indice_marca_actual == len(lista_marcas): 
            tiempo_resta = 0  

            promedio_tiempo_jugado = tiempo_jugado/indice_marca_actual
            promedio_tiempo_jugado_str = "{:.2f}s".format(promedio_tiempo_jugado) #formato con dos decimales
            nombre_jugador = obtener_nombre_jugador(PANTALLA, W, H, fuente, imagenes)
            guardar_datos(nombre_jugador, monedas, promedio_tiempo_jugado_str)
            flag = False

        # mostrar_resultados(PANTALLA, H, fuente_resultados) 
              

        pygame.display.flip()