import ttkbootstrap as ttk
from tkinter import messagebox, StringVar 
from utils.data_manager import players_get, palabras_get, get_config, guardar_puntaje, get_puntaje, reset_puntaje
import random as r


def play_game_view(contenedor_principal, navegacion):
    jugadores = players_get()
    palabras = palabras_get()
    palabras_jugadas = []
    reset_puntaje()
    game_content(contenedor_principal, navegacion, jugadores[0], jugadores, palabras, palabras_jugadas)

def game_content(contenedor_principal, navegacion, jugador, jugadores, palabras, palabras_jugadas):
    for widget in contenedor_principal.winfo_children():
        widget.destroy()
    #frame principal
    play_game_frame = ttk.Frame(contenedor_principal, padding=10)
    play_game_frame.pack(expand=True)
    #frame de estadisticas
    stats_frame = ttk.Frame(play_game_frame, padding=10)
    stats_frame.grid(row=0, column=0, sticky="wn")
    stats_content(stats_frame, jugadores[0], 1, 0)
    #timer frame
    timer_frame = ttk.Frame(play_game_frame, padding=10)
    timer_frame.grid(row=0, column=1, sticky="en")
    #frame de juego
    game_frame = ttk.Frame(play_game_frame, padding=10, width=150, height=200)
    game_frame.grid(row=1, column=0, columnspan=2, ipadx=100, ipady=40)
    game_frame.pack_propagate(False)
    game_content_iniciar(timer_frame, game_frame, jugadores[0], palabras[r.randint(0, len(palabras)-1)], jugadores, palabras, palabras_jugadas, 1, stats_frame)
    #frame de acciones
    actions_frame = ttk.Frame(play_game_frame, padding=10)
    actions_frame.grid(row=2, column=0, columnspan=2)
    activo = False
    timer_content(timer_frame, get_config()["tiempo_ronda_1"], activo, game_frame, jugadores[0], jugadores, palabras, palabras_jugadas, 1, stats_frame)
    ttk.Button(actions_frame, text="Volver al menu", command=lambda: navegacion("dashboard")).pack(pady=10)

def stats_content(stats_frame, jugador, ronda, puntaje):
    #limpiar frame
    for widget in stats_frame.winfo_children():
        widget.destroy()
    ttk.Label(stats_frame, text=f"Turno de: {jugador}").grid(row=0, column=0, columnspan=2, pady=5, sticky="w")
    ttk.Label(stats_frame, text=f"Ronda: {ronda}").grid(row=1, column=0, columnspan=2, pady=5, sticky="w")
    ttk.Label(stats_frame, text=f"Puntos: {puntaje}").grid(row=2, column=0, columnspan=2, pady=5, sticky="w")

def timer_content(timer_frame, time, activo, game_frame, jugador, jugadores, palabras, palabras_jugadas, ronda, stats_frame):
    #limpiar frame
    for widget in timer_frame.winfo_children():
        widget.destroy()
    if not activo:
        ttk.Label(timer_frame, text=time).pack(pady=10)
        return
    #temporizador en el centro del frame
    if time == 0:
        ttk.Label(timer_frame, text="Tiempo agotado").pack(pady=10)
        siguiente_jugador(timer_frame, game_frame, jugador, jugadores, palabras, palabras_jugadas, ronda, stats_frame)
        activo = False
    else:
        ttk.Label(timer_frame, text=f"Tiempo: {time}").pack(pady=10, expand=True)
        # Llamar a esta misma función después de 1000ms (1 segundo) con tiempo - 1
        timer_frame.after(1000, lambda: timer_content(timer_frame, int(time)-1, activo, game_frame, jugador, jugadores, palabras, palabras_jugadas, ronda, stats_frame))

def start_turn(timer_frame, game_frame, jugador, palabra, jugadores, palabras, palabras_jugadas, ronda, stats_frame):
    timer_content(timer_frame, get_config()[f"tiempo_ronda_{ronda}"], True, game_frame, jugador, jugadores, palabras, palabras_jugadas, ronda, stats_frame)
    game_content_close(game_frame, jugador, palabra, timer_frame, jugadores, palabras, palabras_jugadas, ronda, stats_frame)

def game_content_iniciar(timer_frame, game_frame, jugador, palabra, jugadores, palabras, palabras_jugadas, ronda, stats_frame):
    #limpiar frame
    for widget in game_frame.winfo_children():
        widget.destroy()
    #frame de juego
    ttk.Label(game_frame, text=f"Turno de: {jugador}").pack(pady=10, padx=20)
    ttk.Label(game_frame, text=f"Presione el Boton para iniciar").pack(pady=40, expand=True)
    ttk.Button(game_frame, text="Iniciar", command=lambda: start_turn(timer_frame, game_frame, jugador, palabra, jugadores, palabras, palabras_jugadas, ronda, stats_frame) ).pack(side="bottom", pady=10)

def game_content_close(game_frame, jugador, palabra, timer_frame, jugadores, palabras, palabras_jugadas, ronda, stats_frame):
    #limpiar frame
    for widget in game_frame.winfo_children():
        widget.destroy()
    #frame de juego
    ttk.Label(game_frame, text=f"{jugador} presiona el Boton para ver la palabra").pack(expand=True)
    ttk.Button(game_frame, text="Ver Palabra", command=lambda: game_content_open(game_frame, jugador, palabra, timer_frame, jugadores, palabras, palabras_jugadas, ronda, stats_frame)).pack(side="bottom", pady=10)

def game_content_open(game_frame, jugador, palabra, timer_frame, jugadores, palabras, palabras_jugadas, ronda, stats_frame):
    #limpiar frame
    for widget in game_frame.winfo_children():
        widget.destroy()
    #frame de juego
    ttk.Label(game_frame, text=palabra, style="TLabel", font=("Arial", 23), foreground="yellow").pack(expand=True)
    botones_frame = ttk.Frame(game_frame)
    botones_frame.pack(side="bottom", pady=10)
    ttk.Button(botones_frame, text="Ocultar Palabra", command=lambda: game_content_close(game_frame, jugador, palabra, timer_frame, jugadores, palabras, palabras_jugadas, ronda, stats_frame)).grid(row=0, column=1, pady=10, padx=10)
    ttk.Button(botones_frame, text="Siguiente Palabra", command=lambda: siguiente_palabra(timer_frame, game_frame, jugador, jugadores, palabra, palabras, palabras_jugadas, ronda, stats_frame)).grid(row=0, column=0, pady=10, padx=10)
    
def siguiente_jugador(timer_frame, game_frame, jugador, jugadores, palabras, palabras_jugadas, ronda, stats_frame):
    #limpiar frame
    for widget in game_frame.winfo_children():
        widget.destroy()
    if jugador != jugadores[-1]:
        if len(palabras) == 0:
            siguiente_ronda(timer_frame, game_frame, jugador, jugadores, palabras, palabras_jugadas, ronda, stats_frame)
        timer_content(timer_frame, get_config()[f"tiempo_ronda_{ronda}"], False, game_frame, jugador[0], jugadores, palabras, palabras_jugadas, ronda, stats_frame)
        game_content_iniciar(timer_frame, game_frame, jugadores[jugadores.index(jugador) + 1], palabras[r.randint(0, len(palabras)-1)], jugadores, palabras, palabras_jugadas, ronda, stats_frame)
    else:
        if len(palabras) == 0:
            siguiente_ronda(timer_frame, game_frame, jugador, jugadores, palabras, palabras_jugadas, ronda, stats_frame)
        timer_content(timer_frame, get_config()[f"tiempo_ronda_{ronda}"], False, game_frame, jugador[0], jugadores, palabras, palabras_jugadas, ronda, stats_frame)
        game_content_iniciar(timer_frame, game_frame, jugadores[0], palabras[r.randint(0, len(palabras)-1)], jugadores, palabras, palabras_jugadas, ronda, stats_frame)

def siguiente_palabra(timer_frame, game_frame, jugador, jugadores, palabra, palabras, palabras_jugadas, ronda, stats_frame):
    #limpiar frame
    for widget in game_frame.winfo_children():
        widget.destroy()
    #agregar puntaje
    guardar_puntaje(jugador, 1)
    stats_content(stats_frame, jugador, ronda, get_puntaje(jugador))
    #agregar palabra jugada
    palabras_jugadas.append(palabras.pop(palabras.index(palabra)))
    #mostrar siguiente palabra
    if len(palabras) == 0:
        siguiente_ronda(timer_frame, game_frame, jugador, jugadores, palabras, palabras_jugadas, ronda, stats_frame)
    else:
        game_content_close(game_frame, jugador, palabras[r.randint(0, len(palabras)-1)], timer_frame, jugadores, palabras, palabras_jugadas, ronda, stats_frame)

def siguiente_ronda(timer_frame, game_frame, jugador, jugadores, palabras, palabras_jugadas, ronda, stats_frame):
    palabras = palabras_jugadas
    palabras_jugadas = []
    ronda += 1
    timer_content(timer_frame, 0, False, game_frame, jugador, jugadores, palabras, palabras_jugadas, ronda, stats_frame)