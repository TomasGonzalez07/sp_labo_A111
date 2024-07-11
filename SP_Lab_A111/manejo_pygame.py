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

    return imagenes