'''
ADIVINA EL LOGO

Sobre el juego:
La partida consistirá en mostrar al usuario el nombre de una empresa o marca
internacional, ofreciéndole elegir entre 4 logos similares y siendo solo 1 el
correcto.
El jugador contará con 5 vidas que se mostrarán en la pantalla, cada vez que el
usuario cometa una equivocación, se descontará una vida y se pasará a la
siguiente pregunta (si aún quedan vidas).
Cada ronda consistirá de 30 segundos para elegir el logo correcto, si se
termina el tiempo, se descuenta una vida.
Si el jugador acierta el logo, ganará 20 monedas. Cada equivocación deberá
restarle 10 monedas.
La partida consistirá como máximo de 15 rounds. Al finalizar se deberá
informar el promedio de tiempo en el que se respondieron las preguntas, el
total de monedas obtenidos y el récord de monedas previo.

'''

'''
llamada al controlador del juego
'''

from juego_p import *

pantalla_inicio()

