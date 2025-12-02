import ttkbootstrap as ttk
from tkinter import messagebox
from utils.data_manager import get_config, guardar_config

def preferences_view(contenedor_principal, navegacion):
    for widget in contenedor_principal.winfo_children():
        widget.destroy()
    
    if get_config() is None:
        guardar_config(3, 40, 30, 30)
    config = get_config()
    
    preferences_frame = ttk.Frame(contenedor_principal, padding=10)
    preferences_frame.pack(expand=True)
    header = ttk.Frame(preferences_frame)
    header.grid(row=0, column=0, sticky="ew")
    ttk.Label(header, text="Preferencias", font=("Helvetica", 14, "bold")).pack(pady=5)
    ttk.Separator(header).pack(fill="x", pady=10)
    content = ttk.Frame(preferences_frame)
    content.grid(row=1, column=0, sticky="ew")

    ttk.Label(content, text="Cantidad de palabras por Ronda", font=("Helvetica", 10, "bold")).grid(row=0, column=1, padx=10, pady=10, sticky="w")
    cantidad_de_palabras = ttk.Spinbox(content, from_=1, to=100, width=3, justify="center")
    cantidad_de_palabras.insert(0, config["cantidad_de_palabras"])
    cantidad_de_palabras.grid(row=0, column=0, pady=10)
    ttk.Label(content, text="Tiempo para la ronda 1", font=("Helvetica", 10, "bold")).grid(row=1, column=1, padx=10, pady=10, sticky="w")
    tiempo_ronda_1 = ttk.Spinbox(content, from_=1, to=100, width=3, justify="center")
    tiempo_ronda_1.insert(0, config["tiempo_ronda_1"])
    tiempo_ronda_1.grid(row=1, column=0, pady=10)
    ttk.Label(content, text="Tiempo para la ronda 2", font=("Helvetica", 10, "bold")).grid(row=2, column=1, padx=10, pady=10, sticky="w")
    tiempo_ronda_2 = ttk.Spinbox(content, from_=1, to=100, width=3, justify="center")
    tiempo_ronda_2.insert(0, config["tiempo_ronda_2"])
    tiempo_ronda_2.grid(row=2, column=0, pady=10)
    ttk.Label(content, text="Tiempo para la ronda 3", font=("Helvetica", 10, "bold")).grid(row=3, column=1, padx=10, pady=10, sticky="w")
    tiempo_ronda_3 = ttk.Spinbox(content, from_=1, to=100, width=3, justify="center")
    tiempo_ronda_3.insert(0, config["tiempo_ronda_3"])
    tiempo_ronda_3.grid(row=3, column=0, pady=10)
    ttk.Separator(content).grid(row=4, column=0, columnspan=2, sticky="ew", pady=10)
    ttk.Button(content, width=30, text="Guardar cambios", command=lambda:guardar_cambios(navegacion, cantidad_de_palabras, tiempo_ronda_1, tiempo_ronda_2, tiempo_ronda_3)).grid(row=5, column=0, columnspan=2, pady=10)
    ttk.Button(content, width=30, text="Volver", command=lambda: navegacion("dashboard")).grid(row=6, column=0, columnspan=2, pady=10)
    
    return preferences_frame
    
def guardar_cambios(navegacion, cantidad_de_palabras, tiempo_ronda_1, tiempo_ronda_2, tiempo_ronda_3):
    guardar_config(cantidad_de_palabras.get(), tiempo_ronda_1.get(), tiempo_ronda_2.get(), tiempo_ronda_3.get())
    messagebox.showinfo("Exito", "Configuraciones guardadas con exito")
    navegacion("dashboard")



