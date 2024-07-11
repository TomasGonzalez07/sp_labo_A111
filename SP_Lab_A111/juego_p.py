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
    logos_imagenes = {
    "SAMSUNG": [imagenes["samsung(1)"], imagenes["samsung(2)"], imagenes["samsung(3)"], imagenes["samsung(4)"]],
    "APPLE": [imagenes["apple(1)"], imagenes["apple(2)"], imagenes["apple(3)"], imagenes["apple(4)"]],
    "MC DONALD": [imagenes["mcdonalds(1)"], imagenes["mcdonalds(2)"], imagenes["mcdonalds(3)"], imagenes["mcdonalds(4)"]],
    "BURGER KING": [imagenes["burgerking(1)"], imagenes["burgerking(2)"], imagenes["burgerking(3)"], imagenes["burgerking(4)"]],
    "PEPSI": [imagenes["pepsi(1)"], imagenes["pepsi(2)"], imagenes["pepsi(3)"], imagenes["pepsi(4)"]],
    "COCA COLA": [imagenes["cocacola(1)"], imagenes["cocacola(2)"], imagenes["cocacola(3)"], imagenes["cocacola(4)"]],
    "PUMA": [imagenes["puma(1)"], imagenes["puma(2)"], imagenes["puma(3)"], imagenes["puma(4)"]],
    "POLO": [imagenes["polo(1)"], imagenes["polo(2)"], imagenes["polo(3)"], imagenes["polo(4)"]],
    "NIKE": [imagenes["nike(1)"], imagenes["nike(2)"], imagenes["nike(3)"], imagenes["nike(4)"]],
    "ADIDAS": [imagenes["adidas(1)"], imagenes["adidas(2)"], imagenes["adidas(3)"], imagenes["adidas(4)"]],
    "TOMMY HILFIGER": [imagenes["tommy(1)"], imagenes["tommy(2)"], imagenes["tommy(3)"], imagenes["tommy(4)"]],
    "MICROSOFT": [imagenes["microsoft(1)"], imagenes["microsoft(2)"], imagenes["microsoft(3)"], imagenes["microsoft(4)"]],
    "GOOGLE": [imagenes["google(1)"], imagenes["google(2)"], imagenes["google(3)"], imagenes["google(4)"]],
    "HYUNDAI": [imagenes["hyundai(1)"], imagenes["hyundai(2)"], imagenes["hyundai(3)"], imagenes["hyundai(4)"]],
    "LG": [imagenes["lg(1)"], imagenes["lg(2)"], imagenes["lg(3)"], imagenes["lg(4)"]]
    }

    pygame.display.set_icon(imagenes["icono"])

    #fuente
    fuente = pygame.font.SysFont("Times New Roman", 40)
    
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

    mostrando_imagen = False
    imagen_mostrada = None
    tiempo_mostrado = 0
    espera_mostrar = 20 


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
                            imagen_mostrada = imagenes["check_verde"]
                            coordenadas = (cuadrado.x, cuadrado.y)
                            monedas += 20
                            tiempo_jugado += tiempo_transcurrido
                        else:
                            imagen_mostrada = imagenes["x_roja"]
                            coordenadas = (cuadrado.x, cuadrado.y)
                            monedas -= 10
                            vidas -= 1

                        mostrando_imagen = True
                        tiempo_mostrado = pygame.time.get_ticks()  
                        tiempo_inicial = time.time() 
                        indice_cuadrado_verde = random.randint(0, 3)  
                        indice_marca_actual = indice_marca_actual + 1
                        if indice_marca_actual < len(lista_marcas):
                            texto_marca = fuente.render(lista_marcas[indice_marca_actual], True, "black")
                        else:
                            texto_marca = fuente.render("Fin de las marcas", True, "black")


        if tiempo_resta <= 0:
            monedas -= 10
            vidas -= 1
            tiempo_inicial = time.time() 
            indice_cuadrado_verde = random.randint(0, 3)  
            indice_marca_actual = indice_marca_actual + 1
            if indice_marca_actual < len(lista_marcas):
                texto_marca = fuente.render(lista_marcas[indice_marca_actual], True, "black")
            else:
                texto_marca = fuente.render("Fin de las marcas", True, "black")
            print("Clic en un cuadrado rojo")        
                   

        mostrar_datos(PANTALLA, imagenes, monedas, vidas, tiempo_resta, texto_marca, rect)
        mostrar_cuadrados_con_logos(PANTALLA, cuadrados, logos_imagenes, lista_marcas, indice_marca_actual, indice_cuadrado_verde)  

        if mostrando_imagen:
                    tiempo_actual = pygame.time.get_ticks()
                    PANTALLA.blit(imagen_mostrada, coordenadas)   
                    if tiempo_actual - tiempo_mostrado >= espera_mostrar:
                        mostrando_imagen = False  

        if vidas == 0 or indice_marca_actual == len(lista_marcas): 
            tiempo_resta = 0  

            if indice_marca_actual == 0:
                indice_marca_actual = 1
            promedio_tiempo_jugado = tiempo_jugado/indice_marca_actual
            promedio_tiempo_jugado_str = "{:.2f}s".format(promedio_tiempo_jugado) #formato con dos decimales
            nombre_jugador = obtener_nombre_jugador(PANTALLA, W, H, fuente, imagenes)
            guardar_datos(nombre_jugador, monedas, promedio_tiempo_jugado_str)
            flag = False
              

        pygame.display.flip()