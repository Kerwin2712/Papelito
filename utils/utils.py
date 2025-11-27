import os

def limpiar():
    #Sistema operativo Windows
    if os.name == "nt":
        os.system("cls")
    #Para otro sistema operativo
    else:
        os.system("clear")
        
def guardar_palabras(palabras):
    with open("palabras.txt", "w") as archivo:
        for palabra in palabras:
            archivo.write(f"{palabra}\n")

def guardar_participantes(jugadores):
    with open("participantes.txt", "w") as archivo:
        for jugador in jugadores:
            archivo.write(f"{jugador}:{jugadores[jugador]}\n")

def cargar_palabras():
    palabras = []
    with open("palabras.txt", "r") as archivo:
        for linea in archivo:
            palabras.append(linea.strip())
    return palabras

def cargar_participantes():
    jugadores = {}
    with open("participantes.txt", "r") as archivo:
        for linea in archivo:
            jugador, puntaje = linea.strip().split(":")
            jugadores[jugador] = int(puntaje)
    return jugadores

