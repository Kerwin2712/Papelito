import ttkbootstrap as ttk
from tkinter import messagebox, StringVar 
from utils.data_manager import players_get, palabras_get, get_config
import time
import random as r

def play_game_view(contenedor_principal, navegacion):
    jugadores = players_get()
    palabras = palabras_get()
    palabras_jugadas = []
    game_content(contenedor_principal, navegacion, jugadores[0], palabras, palabras_jugadas, 1)

def game_content(contenedor_principal, navegacion, jugador, palabras, palabras_jugadas, ronda):
    for widget in contenedor_principal.winfo_children():
        widget.destroy()
    #declaracion de variables
    iniciar = False
    ver = False
    jugador_var = StringVar()
    timer_var = StringVar()
    puntaje_var = StringVar()
    ronda_var = StringVar()
    turno_var = StringVar()
    palabra_var = StringVar()

    jugador_var.set(jugador)
    ronda_var.set(ronda)
    turno_var.set(0)
    puntaje_var.set(0)
    turno(jugador, jugador, ronda, puntaje_var, palabras, turno_var.get(), palabra_var, palabras_jugadas)
    #frame principal
    play_game_frame = ttk.Frame(contenedor_principal, padding=10)
    play_game_frame.pack(expand=True)
    #frame de estadisticas
    stats_frame = ttk.Frame(play_game_frame)
    stats_frame.grid(row=0, column=0, sticky="ew")
    #stats labels
    ttk.Label(stats_frame, text=f"Turno de: {jugador_var.get()}").pack(pady=5)
    ttk.Label(stats_frame, text=f"Ronda: {ronda_var.get()}").pack(pady=5)
    ttk.Label(stats_frame, text=f"Puntos: {puntaje_var.get()}").pack(pady=5)
    #timer frame
    timer_frame = ttk.Frame(play_game_frame)
    timer_frame.grid(row=0, column=1, sticky="ew")
    ttk.Separator(timer_frame).grid(row=1, column=0, columnspan=2, sticky="ew")
    #timer label
    timer_label = ttk.Label(timer_frame, textvariable=timer_var)
    timer_label.pack(pady=10, padx=10)
    #frame de juego
    game_frame = ttk.Frame(play_game_frame)
    game_frame.grid(row=2, column=0, columnspan=2, sticky="ew")
    #frame de acciones
    ttk.Separator(play_game_frame).grid(row=3, column=0, columnspan=2, sticky="ew")
    actions_frame = ttk.Frame(play_game_frame)
    actions_frame.grid(row=4, column=0, columnspan=2, sticky="ew")
    #botones de acciones
    if iniciar:
        if ver:
            ttk.Label(game_frame, textvariable=palabra_var).pack(pady=5)
            ttk.Button(actions_frame, text="Ocultar palabra", command=lambda: ver.set(not ver.get())).pack(pady=5)
        else:
            ttk.Label(game_frame, text=f"{jugador.get()} Presiona Ver palabra!").pack(pady=5)
            ttk.Button(actions_frame, text="Ver palabra", command=lambda: ver.set(not ver.get())).pack(pady=5)
            ttk.Button(actions_frame, text="Siguiente palabra", command=lambda: siguiente_palabra(palabra_var, palabras, palabras_jugadas, puntaje)).pack(pady=5)    
    else:
        ttk.Button(actions_frame, text="Iniciar", command=lambda: start_game(timer_var timer_frame, palabras)).pack(pady=5)
    ttk.Button(actions_frame, text="Volver", command=lambda: navegacion("dashboard")).pack(pady=5)
    
def siguiente_palabra(palabra, palabras: list, palabras_jugadas: list, puntaje):
    palabras_jugadas.append(palabras.pop(palabras.index(palabra.get())))
    puntaje.set(int(puntaje.get())+1)
    palabra.set(palabras[r.randint(0, len(palabras)-1)])

def turno(
    jugador, 
    jugadores: list, 
    ronda, 
    puntaje, 
    palabras: list, 
    turno, 
    timer,
    palabraringVar,
    palabras_jugadas: list):
    jugador.set(jugadores[turno])
    turno.set(turno)
    ronda.set(f"Ronda {turno % get_config()["cantidad_de_palabras"]+1}")
    if turno % get_config()["cantidad_de_palabras"] == 0:
        timer.set(get_config()["tiempo_ronda_1"])
    elif turno % get_config()["cantidad_de_palabras"] == 1:
        timer.set(get_config()["tiempo_ronda_2"])
    else:
        timer.set(get_config()["tiempo_ronda_3"])
    palabra.set(palabras[r.randint(0, len(palabras)-1)])

def start_game(timer, timer_frame, palabras: list):
    iniciar = True
    timer_frame.after(1000, timer.set(int(timer.get())-1))
    if timer.get() == 0:
        iniciar = False
