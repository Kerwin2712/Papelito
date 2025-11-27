import time
import threading
import random as rnd
from utils.utils import *


# Evento para indicar al temporizador que se detenga
stop_timer_event = threading.Event()
tiempo_restante = 0

def instrucciones(ronda: int, jugador):
    if ronda == 1:
        instrucciones_texto = f'''Turno de {jugador}
        
        {jugador} tienes 40 segundos para que tu compañero adivine las palabras.
        
        Debes leer la palabra en tu mente.
        
        Debes decirle a tu compañero en voz alta 3 palabras relacionadas a esa palabra.
        
        Tu compañero debe adivinar la palabra basandose en las pistas que le diste.
        '''
    elif ronda == 2:
        instrucciones_texto = f'''Turno de {jugador}
        
        {jugador} tienes 30 segundos para que tu compañero adivine las palabras.
        
        Debes leer la palabra en tu mente.
        
        Debes decirle a tu compañero en voz alta 1 palabra relacionada a esa palabra.
        
        Tu compañero debe adivinar la palabra basandose en la pista que le diste.
        '''
    else:
        instrucciones_texto = f'''Turno de {jugador}
        
        {jugador} tienes 30 segundos para que tu compañero adivine las palabras.
        
        Debes leer la palabra en tu mente.
        
        Debes hacer mimica (no puedes hablar) para que tu compañero adivine la palabra.
        
        Tu compañero debe adivinar la palabra basandose en la mimica que hiciste.
        '''
    print(instrucciones_texto)

def run_timer(segundos: int, stop_event: threading.Event):
    global tiempo_restante
    tiempo_restante = segundos
    while tiempo_restante > 0 and not stop_event.is_set():
        time.sleep(1)
        tiempo_restante -= 1
    if not stop_event.is_set():
        limpiar()
        print("\n¡Tiempo agotado! Presiona ENTER para continuar.")
    stop_event.set()

def play_round(ronda: int, jugadores: dict, palabras: list, aux_palabras: list):
    global stop_timer_event, tiempo_restante
    while palabras:
        for jugador in jugadores:
            while palabras:
                limpiar()
                print(f"Ronda {ronda}")
                instrucciones(ronda, jugador)
                input("Presione ENTER para iniciar.")
                limpiar()

                stop_timer_event.clear()
                if ronda == 1:
                    timer_thread = threading.Thread(target=run_timer, args=(40, stop_timer_event))
                else:
                    timer_thread = threading.Thread(target=run_timer, args=(30, stop_timer_event))
                timer_thread.start()

                intento = 0
                while not stop_timer_event.is_set():
                    if palabras:
                        palabra_index = rnd.randint(0, len(palabras) - 1)
                        limpiar()
                        print(f"Ronda {ronda}")
                        print(f"Tiempo restante: {tiempo_restante} segundos")
                        print(f"\n    Palabra {intento + 1}: {palabras[palabra_index]}")
                        print(f"\nPalabras restantes: {len(palabras)}")
                        input("Presiona ENTER para la siguiente palabra...")
                        if not stop_timer_event.is_set():
                            aux_palabras.append(palabras.pop(palabra_index))
                            intento += 1
                    else:
                        limpiar()
                        print("\nNo hay más palabras.\n")
                        stop_timer_event.set()  # Detener el temporizador
                        break
                
                # Espera a que el hilo del temporizador termine
                timer_thread.join()

                print(f"    {jugador} ha adivinado {intento} palabras.")
                jugadores[jugador] += intento
                input("\nPresione ENTER para pasar al siguiente jugador.")
                break
    limpiar()
    print(f"Ronda {ronda} completada.")
    print("\nPuntajes actuales:\n")
    for jugador, puntaje in jugadores.items():
        print(f"    {jugador}: {puntaje} puntos")
    if ronda == 3:
        print("\n¡Gracias por jugar!")
        aux_palabras.clear()
        palabras.clear()
        jugadores.clear()
        input("\nPresione ENTER para volver al menu principal.")
        from main import iniciar
        iniciar()
    else:
        input("\nPresione ENTER para pasar a la siguiente ronda.")

def play_game(jugadores: dict, palabras: list, axu_palabras: list):
    print("Iniciando Ronda 1...")
    play_round(1, jugadores, palabras, axu_palabras)
    print("Iniciando Ronda 2...")
    play_round(2, jugadores, axu_palabras, palabras)
    print("Iniciando Ronda 3...")
    play_round(3, jugadores, palabras, axu_palabras)