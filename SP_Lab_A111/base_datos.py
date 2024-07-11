import json,os

def guardar_datos(nombre_jugador:str, puntaje:int, promedio_tiempo_jugado: float):
    '''
    Brief:
        guarda los datos de la partida del jugador
    Parameters:     
        nombre_jugador: nombre del jugador
        puntaje: puntaje del jugador
    '''
    informacion_jugador = {"nombre": nombre_jugador, "puntaje": puntaje, "promedio_tiempo": promedio_tiempo_jugado}

    archivo = "puntajes.json"

    if os.path.exists(archivo):
        lista_jugadores = traer_datos_json(archivo)
    else:
        lista_jugadores = []    
        
    lista_jugadores.append(informacion_jugador)   
    generar_json(lista_jugadores, archivo)

def generar_json(data, ruta:str)->None:
    '''
    Brief:
        genera un archivo json para almacenar los datos
    Parameters:     
        data: datos a guardar.
        ruta: ruta del archivo json.
    '''
    with open(ruta, 'w') as archivo:
        json.dump(data, archivo, indent = 4, ensure_ascii = False)
    print("Genero el archivo correctamente")  

def traer_datos_json(ruta:str)-> list:
    '''
    Brief:
       trae datos json
    Parameters:     
        ruta
    Return:
        lista    
    '''
    lista = []
    if os.path.exists(ruta):
        with open(ruta, 'r') as archivo_json:
            lista = json.load(archivo_json)

    return lista  

def traer_datos_csv():
    pass