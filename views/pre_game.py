import ttkbootstrap as ttk
from tkinter import StringVar
from utils.data_manager import guardar_participantes

def pre_game_view(contenedor_principal, navegacion):
    #Limpiar pantalla
    for widget in contenedor_principal.winfo_children():
        widget.destroy()
    #declaracion de variables
    jugador = StringVar()
    jugadores = []
    #frame principal
    pre_game_frame = ttk.Frame(contenedor_principal, padding=10)
    pre_game_frame.pack(expand=True)
    #labels
    ttk.Label(pre_game_frame, text="Preparacion del juego").grid(row=0, column=0, columnspan=3, pady=20)
    ttk.Separator(pre_game_frame).grid(row=1, column=0, columnspan=3, pady=10, sticky="ew")
    ttk.Label(pre_game_frame, text="Jugador").grid(row=2, column=0, padx=5)
    ttk.Entry(pre_game_frame, textvariable=jugador).grid(row=2, column=1, padx=5)
    ttk.Button(pre_game_frame, text="Agregar", command=lambda: add_player(players_frame, jugador, jugadores)).grid(row=2, column=2, padx=5)
    #frame de jugadores
    players_frame = ttk.Frame(pre_game_frame)
    players_frame.grid(row=3, column=0, columnspan=3, pady=5)
    #frame de botones
    botones_frame = ttk.Frame(pre_game_frame)
    botones_frame.grid(row=4, column=0, columnspan=3, pady=5)
    #botones
    ttk.Button(botones_frame, width=30, text="Continuar", command=lambda: continuar(jugadores, navegacion)).pack(pady=10)
    ttk.Button(botones_frame, width=30, text="Volver", command=lambda: navegacion("dashboard")).pack(pady=10)
    return pre_game_frame

def add_player(players_frame, jugador, jugadores):
    #Limpiar pantalla
    for widget in players_frame.winfo_children():
        widget.destroy()
    #agregar jugador
    jugadores.append(jugador.get())
    jugador.set("")
    #mostrar jugadores
    for player in jugadores:
        ttk.Label(players_frame, text=player).pack(pady=5)

def continuar(jugadores, navegacion):
    #Guardar jugadores
    guardar_participantes(jugadores)
    #navegar a la vista de palabras
    navegacion("words")
        
