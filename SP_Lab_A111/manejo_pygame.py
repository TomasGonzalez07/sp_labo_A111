'''
puntaje y tiempo
carga de imagenes
'''
import pygame,sys

def mostrar_datos(pantalla, imagenes, monedas, vidas, tiempo_r, texto_marca, rect):
    fuente = pygame.font.SysFont("Times New Roman",26)

    texto_vidas = fuente.render(str(vidas), True, "white")
    texto_monedas = fuente.render(str(monedas), True, "white")
    texto_tiempo = fuente.render(f"{tiempo_r:.2f}s", True, "white")


    pantalla.blit(imagenes["fondo"], (0, 0))
    pantalla.blit(imagenes["icono_vida"], (10, 10))
    pantalla.blit(texto_vidas, (70, 10))
    pantalla.blit(imagenes["icono_moneda"], (10, 80))
    pantalla.blit(texto_monedas, (70, 80))
    pantalla.blit(imagenes["icono_reloj"], (1140, 10))
    pantalla.blit(texto_tiempo, (1190, 10))

    pygame.draw.rect(pantalla, "white", rect)
    text_rectangulo = texto_marca.get_rect(center=rect.center)
    pantalla.blit(texto_marca, text_rectangulo)

def obtener_nombre_jugador(pantalla, W,H, fuente, imagenes):
    '''
    Brief:
        capta el nombre que ingresa por pantalla del jugador
    Parameters:     
        pantalla: pantalla del juego
        W: ancho
        H: alto
        fuente: tipo de letra
    Return: 
        nombre
    '''
    nombre = ""
    entrada_activa = True

    while entrada_activa:
        pantalla.blit(imagenes["fondo"],(0,0))

        texto_final = fuente.render(f"SU PARTIDA TERMINO", True, (255, 255, 255))
        texto_final_rect = texto_final.get_rect(center=(W // 2, H // 2 - 100))
        pantalla.blit(texto_final, texto_final_rect)

        texto = fuente.render(f"Ingrese su nombre: {nombre}", True, (255, 255, 255))
        pantalla.blit(texto, (450,450))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    entrada_activa = False
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += event.unicode

    return nombre
    
def cargar_imagenes(W,H):
    imagenes = {}

    imagenes["icono"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\icono.png")

    imagenes["fondo"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\\fondo.jpg")
    imagenes["fondo"] = pygame.transform.scale(imagenes["fondo"], (W, H))

    imagenes["logo_juego"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\\logo_juego.png")
    imagenes["logo_juego"] = pygame.transform.scale(imagenes["logo_juego"], (300, 300))

    imagenes["boton_play"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\\boton_play.png")
    imagenes["boton_play"] = pygame.transform.scale(imagenes["boton_play"], (200, 80))

    imagenes["icono_vida"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\\icono_vida.png")
    imagenes["icono_vida"] = pygame.transform.scale(imagenes["icono_vida"], (40, 40))

    imagenes["icono_moneda"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\\icono_moneda.png")
    imagenes["icono_moneda"] = pygame.transform.scale(imagenes["icono_moneda"], (40, 40))

    imagenes["icono_reloj"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\\icono_reloj.png")
    imagenes["icono_reloj"] = pygame.transform.scale(imagenes["icono_reloj"], (40, 40))

    imagenes["samsung(1)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\samsung(1).jpeg")
    imagenes["samsung(1)"] = pygame.transform.scale(imagenes["samsung(1)"], (250, 250))
    imagenes["samsung(2)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\samsung(2).jpeg")
    imagenes["samsung(2)"] = pygame.transform.scale(imagenes["samsung(2)"], (250, 250))
    imagenes["samsung(3)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\samsung(3).jpeg")
    imagenes["samsung(3)"] = pygame.transform.scale(imagenes["samsung(3)"], (250, 250))
    imagenes["samsung(4)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\samsung(4).jpeg")
    imagenes["samsung(4)"] = pygame.transform.scale(imagenes["samsung(4)"], (250, 250))

    imagenes["apple(1)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\apple(1).jpeg")
    imagenes["apple(1)"] = pygame.transform.scale(imagenes["apple(1)"], (250, 250))
    imagenes["apple(2)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\apple(2).jpeg")
    imagenes["apple(2)"] = pygame.transform.scale(imagenes["apple(2)"], (250, 250))
    imagenes["apple(3)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\apple(3).jpeg")
    imagenes["apple(3)"] = pygame.transform.scale(imagenes["apple(3)"], (250, 250))
    imagenes["apple(4)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\apple(4).jpeg")
    imagenes["apple(4)"] = pygame.transform.scale(imagenes["apple(4)"], (250, 250))

    imagenes["mcdonalds(1)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\mcdonalds(1).jpeg")
    imagenes["mcdonalds(1)"] = pygame.transform.scale(imagenes["mcdonalds(1)"], (250, 250))
    imagenes["mcdonalds(2)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\mcdonalds(2).jpeg")
    imagenes["mcdonalds(2)"] = pygame.transform.scale(imagenes["mcdonalds(2)"], (250, 250))
    imagenes["mcdonalds(3)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\mcdonalds(3).jpeg")
    imagenes["mcdonalds(3)"] = pygame.transform.scale(imagenes["mcdonalds(3)"], (250, 250))
    imagenes["mcdonalds(4)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\mcdonalds(4).jpeg")
    imagenes["mcdonalds(4)"] = pygame.transform.scale(imagenes["mcdonalds(4)"], (250, 250))

    imagenes["burgerking(1)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\burgerking(1).jpeg")
    imagenes["burgerking(1)"] = pygame.transform.scale(imagenes["burgerking(1)"], (250, 250))
    imagenes["burgerking(2)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\burgerking(2).jpeg")
    imagenes["burgerking(2)"] = pygame.transform.scale(imagenes["burgerking(2)"], (250, 250))
    imagenes["burgerking(3)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\burgerking(3).jpeg")
    imagenes["burgerking(3)"] = pygame.transform.scale(imagenes["burgerking(3)"], (250, 250))
    imagenes["burgerking(4)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\burgerking(4).jpeg")
    imagenes["burgerking(4)"] = pygame.transform.scale(imagenes["burgerking(4)"], (250, 250))

    imagenes["pepsi(1)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\pepsi(1).jpeg")
    imagenes["pepsi(1)"] = pygame.transform.scale(imagenes["pepsi(1)"], (250, 250))
    imagenes["pepsi(2)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\pepsi(2).jpeg")
    imagenes["pepsi(2)"] = pygame.transform.scale(imagenes["pepsi(2)"], (250, 250))
    imagenes["pepsi(3)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\pepsi(3).jpeg")
    imagenes["pepsi(3)"] = pygame.transform.scale(imagenes["pepsi(3)"], (250, 250))
    imagenes["pepsi(4)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\pepsi(4).jpeg")
    imagenes["pepsi(4)"] = pygame.transform.scale(imagenes[""], (250, 250))

    imagenes["cocacola(1)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\cocacola(1).jpeg")
    imagenes["cocacola(1)"] = pygame.transform.scale(imagenes["cocacola(1)"], (250, 250))
    imagenes["cocacola(2)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\cocacola(2).jpeg")
    imagenes["cocacola(2)"] = pygame.transform.scale(imagenes["cocacola(2)"], (250, 250))
    imagenes["cocacola(3)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\cocacola(3).jpeg")
    imagenes["cocacola(3)"] = pygame.transform.scale(imagenes["cocacola(3)"], (250, 250))
    imagenes["cocacola(4)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\cocacola(4).jpeg")
    imagenes["cocacola(4)"] = pygame.transform.scale(imagenes["cocacola(4)"], (250, 250))

    imagenes["puma(1)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\puma(1).jpeg")
    imagenes["puma(1)"] = pygame.transform.scale(imagenes["puma(1)"], (250, 250))
    imagenes["puma(2)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\puma(2).jpeg")
    imagenes["puma(2)"] = pygame.transform.scale(imagenes["puma(2)"], (250, 250))
    imagenes["puma(3)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\puma(3).jpeg")
    imagenes["puma(3)"] = pygame.transform.scale(imagenes["puma(3)"], (250, 250))
    imagenes["puma(4)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\puma(4).jpeg")
    imagenes["puma(4)"] = pygame.transform.scale(imagenes["puma(4)"], (250, 250))

    imagenes["polo(1)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\polo(1).jpeg")
    imagenes["polo(1)"] = pygame.transform.scale(imagenes["polo(1)"], (250, 250))
    imagenes["polo(2)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\polo(2).jpeg")
    imagenes["polo(2)"] = pygame.transform.scale(imagenes["polo(2)"], (250, 250))
    imagenes["polo(3)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\polo(3).jpeg")
    imagenes["polo(3)"] = pygame.transform.scale(imagenes["polo(3)"], (250, 250))
    imagenes["polo(4)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\polo(4).jpeg")
    imagenes["polo(4)"] = pygame.transform.scale(imagenes["polo(4)"], (250, 250))

    imagenes["nike(1)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\nike(1).jpeg")
    imagenes["nike(1)"] = pygame.transform.scale(imagenes["nike(1)"], (250, 250))
    imagenes["nike(2)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\nike(2).jpeg")
    imagenes["nike(2)"] = pygame.transform.scale(imagenes["nike(2)"], (250, 250))
    imagenes["nike(3)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\nike(3).jpeg")
    imagenes["nike(3)"] = pygame.transform.scale(imagenes["nike(3)"], (250, 250))
    imagenes["nike(4)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\nike(4).jpeg")
    imagenes["nike(4)"] = pygame.transform.scale(imagenes["nike(4)"], (250, 250))

    imagenes["adidas(1)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\adidas(1).jpeg")
    imagenes["adidas(1)"] = pygame.transform.scale(imagenes["adidas(1)"], (250, 250))
    imagenes["adidas(2)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\adidas(2).jpeg")
    imagenes["adidas(2)"] = pygame.transform.scale(imagenes["adidas(2)"], (250, 250))
    imagenes["adidas(3)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\adidas(3).jpeg")
    imagenes["adidas(3)"] = pygame.transform.scale(imagenes["adidas(3)"], (250, 250))
    imagenes["adidas(4)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\adidas(4).jpeg")
    imagenes["adidas(4)"] = pygame.transform.scale(imagenes["adidas(4)"], (250, 250))

    imagenes["tommy(1)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\tommy(1).jpeg")
    imagenes["tommy(1)"] = pygame.transform.scale(imagenes["tommy(1)"], (250, 250))
    imagenes["tommy(2)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\tommy(2).jpeg")
    imagenes["tommy(2)"] = pygame.transform.scale(imagenes["tommy(2)"], (250, 250))
    imagenes["tommy(3)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\tommy(3).jpeg")
    imagenes["tommy(3)"] = pygame.transform.scale(imagenes["tommy(3)"], (250, 250))
    imagenes["tommy(4)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\\tommy(4).jpeg")
    imagenes["tommy(4)"] = pygame.transform.scale(imagenes["tommy(4)"], (250, 250))

    imagenes["microsoft(1)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\microsoft(1).jpeg")
    imagenes["microsoft(1)"] = pygame.transform.scale(imagenes["microsoft(1)"], (250, 250))
    imagenes["microsoft(2)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\microsoft(2).jpeg")
    imagenes["microsoft(2)"] = pygame.transform.scale(imagenes["microsoft(2)"], (250, 250))
    imagenes["microsoft(3)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\microsoft(3).jpeg")
    imagenes["microsoft(3)"] = pygame.transform.scale(imagenes["microsoft(3)"], (250, 250))
    imagenes["microsoft(4)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\microsoft(4).jpeg")
    imagenes["microsoft(4)"] = pygame.transform.scale(imagenes["microsoft(4)"], (250, 250))

    imagenes["google(1)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\google(1).jpeg")
    imagenes["google(1)"] = pygame.transform.scale(imagenes["google(1)"], (250, 250))
    imagenes["google(2)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\google(2).jpeg")
    imagenes["google(2)"] = pygame.transform.scale(imagenes["google(2)"], (250, 250))
    imagenes["google(3)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\google(3).jpeg")
    imagenes["google(3)"] = pygame.transform.scale(imagenes["google(3)"], (250, 250))
    imagenes["google(4)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\google(4).jpeg")
    imagenes["google(4)"] = pygame.transform.scale(imagenes["google(4)"], (250, 250))

    imagenes["hyundai(1)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\hyundai(1).jpeg")
    imagenes["hyundai(1)"] = pygame.transform.scale(imagenes["hyundai(1)"], (250, 250))
    imagenes["hyundai(2)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\hyundai(2).jpeg")
    imagenes["hyundai(2)"] = pygame.transform.scale(imagenes["hyundai(2)"], (250, 250))
    imagenes["hyundai(3)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\hyundai(3).jpeg")
    imagenes["hyundai(3)"] = pygame.transform.scale(imagenes["hyundai(3)"], (250, 250))
    imagenes["hyundai(4)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\hyundai(4).jpeg")
    imagenes["hyundai(4)"] = pygame.transform.scale(imagenes["hyundai(4)"], (250, 250))

    imagenes["lg(1)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\lg(1).jpeg")
    imagenes["lg(1)"] = pygame.transform.scale(imagenes["lg(1)"], (250, 250))
    imagenes["lg(2)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\lg(2).jpeg")
    imagenes["lg(2)"] = pygame.transform.scale(imagenes["lg(2)"], (250, 250))
    imagenes["lg(3)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\lg(3).jpeg")
    imagenes["lg(3)"] = pygame.transform.scale(imagenes["lg(3)"], (250, 250))
    imagenes["lg(4)"] = pygame.image.load("1A111\SP_Lab_A111\imagenes\logos\lg(4).jpeg")
    imagenes["lg(4)"] = pygame.transform.scale(imagenes["lg(4)"], (250, 250))

    return imagenes