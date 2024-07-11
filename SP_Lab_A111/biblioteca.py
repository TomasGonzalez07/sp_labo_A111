from base_datos import *
import time,random

def mostrar_resultados(pantalla, H, fuente):
    '''
    Brief:
        muestra resultados del jugador 
    Parameters:     
        pantalla: pantalla del juego
        fuente: tipo de letra 
    '''
    lista_jugadores = traer_datos_json("puntajes.json")

    if lista_jugadores:
        jugador_con_mas_puntaje = max(lista_jugadores, key=lambda x: x["puntaje"], default=None)
        # explicar max: encuentra el elemento máximo en un iterable 
        # con lambda comparamos los valores de la clave "puntaje" de cada diccionario en lista_jugadores
        texto_max_nombre = fuente.render(f"MEJOR JUGADOR: {jugador_con_mas_puntaje['nombre']}", True, (255, 255, 255))
        texto_max_puntaje = fuente.render(f"PUNTAJE: {jugador_con_mas_puntaje['puntaje']}", True, (255, 255, 255))
        texto_max_promedio_tiempo_jugado = fuente.render(f"TIEMPO PROMEDIO: {jugador_con_mas_puntaje['promedio_tiempo']}", True, (255, 255, 255))


        jugador_prev_puntaje = lista_jugadores[len(lista_jugadores)-1]
        texto_prev_nombre = fuente.render(f"ULTIMO JUGADOR: {jugador_prev_puntaje['nombre']}", True, (255, 255, 255))
        texto_prev_puntaje = fuente.render(f"PUNTAJE: {jugador_prev_puntaje['puntaje']}", True, (255, 255, 255))
        texto_prev_promedio_tiempo_jugado = fuente.render(f"TIEMPO PROMEDIO: {jugador_prev_puntaje['promedio_tiempo']}", True, (255, 255, 255))
    else:
        texto_max_nombre = fuente.render(f"MEJOR JUGADOR: -", True, (255, 255, 255))
        texto_max_puntaje = fuente.render(f"PUNTAJE: -", True, (255, 255, 255))  
        texto_max_promedio_tiempo_jugado = fuente.render(f"TIEMPO PROMEDIO: -", True, (255, 255, 255))

        texto_prev_nombre = fuente.render(f"ULTIMO JUGADOR: -", True, (255, 255, 255))
        texto_prev_puntaje = fuente.render(f"PUNTAJE: -", True, (255, 255, 255))
        texto_prev_promedio_tiempo_jugado = fuente.render(f"TIEMPO PROMEDIO: -", True, (255, 255, 255))


    pantalla.blit(texto_max_nombre, (0, H - 45))
    pantalla.blit(texto_max_puntaje, (0, H - 30))
    pantalla.blit(texto_max_promedio_tiempo_jugado, (0, H - 15))

    pantalla.blit(texto_prev_nombre, (250, H - 45))
    pantalla.blit(texto_prev_puntaje, (250, H - 30))
    pantalla.blit(texto_prev_promedio_tiempo_jugado, (250, H - 15))

