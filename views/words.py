import ttkbootstrap as ttk
from tkinter import StringVar, messagebox
from utils.data_manager import players_get, guardar_palabras, get_config 

def words_view(contenedor_principal, navegacion):
    jugadores = players_get()
    palabras = []
    words_content(contenedor_principal, palabras, jugadores[0], jugadores, navegacion)

def words_content(contenedor_principal, palabras, jugador, jugadores, navegacion):
    #Limpiar pantalla
    for widget in contenedor_principal.winfo_children():
        widget.destroy()
    #declaracion de variables
    palabra = StringVar()
    mis_palabras = []
    #frame principal
    words_frame = ttk.Frame(contenedor_principal, padding=10)
    words_frame.pack(expand=True)
    #label
    ttk.Label(words_frame, text=f"Configuracion de palabras para {jugador}").pack(pady=20)
    ttk.Separator(words_frame).pack(fill="x", pady=10)
    #form frame
    form_frame = ttk.Frame(words_frame)
    form_frame.pack(pady=5)
    #entrys
    ttk.Label(form_frame, text="Palabra").grid(row=0, column=0, columnspan=2, pady=5)
    ttk.Entry(form_frame, textvariable=palabra).grid(row=1, column=0, pady=5)
    #frame de palabras
    words_list_frame = ttk.Frame(words_frame)
    words_list_frame.pack(pady=5)
    #frame de botones
    button_frame = ttk.Frame(words_frame, padding=10)
    button_frame.pack(pady=5)

    if jugador != jugadores[-1]:
        next_button = ttk.Button(button_frame, text="Siguiente", width=30, command=lambda: words_content(contenedor_principal, palabras, jugadores[jugadores.index(jugador)+1], jugadores, navegacion))
    else:
        next_button = ttk.Button(button_frame, text="Jugar", width=30, command=lambda: guardar_palabras(palabras) or navegacion("game"))

    ttk.Button(form_frame, text="Agregar", command=lambda: add_word(palabra, mis_palabras, palabras, words_list_frame, next_button)).grid(row=1, column=1, padx=5)

    ttk.Button(button_frame, text="Volver", width=30, command=lambda: navegacion("dashboard")).pack(pady=5)  


def add_word(palabra, mis_palabras, palabras, words_list_frame, next_button):
    limit = int(get_config()["cantidad_de_palabras"])
    if len(mis_palabras) >= limit:
        messagebox.showerror("Error", "Se han alcanzado el maximo de palabras")
        palabra.set("")
        return
    #Limpiar pantalla
    for widget in words_list_frame.winfo_children():
        widget.destroy()
    #agregar palabra
    mis_palabras.append(palabra.get())
    palabras.append(palabra.get())
    for word in mis_palabras:
        ttk.Label(words_list_frame, text=word).pack(pady=5)
    palabra.set("")

    if len(mis_palabras) == limit:
        next_button.pack(pady=5)



