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
    ttk.Label(header, text="Preferencias", font=("Helvetica", 12, "bold")).pack(pady=5)
    ttk.Separator(header).pack(fill="x", pady=10)
    content = ttk.Frame(preferences_frame)
    content.grid(row=1, column=0, sticky="ew")

    ttk.Label(content, text="Cantidad de palabras por Ronda").pack(pady=5)
    cantidad_de_palabras = ttk.Spinbox(content, from_=1, to=100)
    cantidad_de_palabras.insert(0, config["cantidad_de_palabras"])
    cantidad_de_palabras.pack(pady=5)
    ttk.Label(content, text="Tiempo para la ronda 1").pack(pady=5)
    tiempo_ronda_1 = ttk.Spinbox(content, from_=1, to=100)
    tiempo_ronda_1.insert(0, config["tiempo_ronda_1"])
    tiempo_ronda_1.pack(pady=5)
    ttk.Label(content, text="Tiempo para la ronda 2").pack(pady=5)
    tiempo_ronda_2 = ttk.Spinbox(content, from_=1, to=100)
    tiempo_ronda_2.insert(0, config["tiempo_ronda_2"])
    tiempo_ronda_2.pack(pady=5)
    ttk.Label(content, text="Tiempo para la ronda 3").pack(pady=5)
    tiempo_ronda_3 = ttk.Spinbox(content, from_=1, to=100)
    tiempo_ronda_3.insert(0, config["tiempo_ronda_3"])
    tiempo_ronda_3.pack(pady=5)
    ttk.Separator(content).pack(fill="x", pady=10)
    ttk.Button(content, width=30, text="Guardar cambios", command=lambda:guardar_cambios(navegacion, cantidad_de_palabras, tiempo_ronda_1, tiempo_ronda_2, tiempo_ronda_3)).pack(pady=5)
    ttk.Button(content, width=30, text="Volver", command=lambda: navegacion("dashboard")).pack(pady=5)
    
    return preferences_frame
    
def guardar_cambios(navegacion, cantidad_de_palabras, tiempo_ronda_1, tiempo_ronda_2, tiempo_ronda_3):
    guardar_config(cantidad_de_palabras.get(), tiempo_ronda_1.get(), tiempo_ronda_2.get(), tiempo_ronda_3.get())
    messagebox.showinfo("Exito", "Configuraciones guardadas con exito")
    navegacion("dashboard")



