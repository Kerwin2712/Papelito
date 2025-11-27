from utils.utils import *
from views.welcome import mostrar_bienvenida
from views.dashboard import dashboard_view
from views.preferences import preferences_view
from views.pre_game import pre_game_view
from views.words import words_view
from views.game import play_game_view
from tkinter import messagebox
import ttkbootstrap as ttk
import juego


jugadores = {}
palabras = []
aux_palabras = []
VISTAS = {
    "dashboard": dashboard_view,
    "preferences": preferences_view,
    "pre_game": pre_game_view,
    "words": words_view,
    "game": play_game_view
}


def interfaz():
    app = ttk.Window(themename="superhero")
    app.title("Papelito")
    app.geometry("400x500")
    
    contenedor_principal = ttk.Frame(app, padding=10)
    contenedor_principal.pack(expand=True)
    
    def navegacion(vista_clave):
       manejar_vista(vista_clave, contenedor_principal, navegacion)
    
    navegacion("dashboard")
    app.mainloop()

def manejar_vista(vista_clave, contenedor_principal, navegacion):
    if vista_clave not in VISTAS:
        messagebox.showerror("Error", "Vista no encontrada")
        return
    vista = VISTAS[vista_clave]
    vista(contenedor_principal, navegacion)

    

def set_palabras(jugadores: dict):
    nuevas_palabras = []
    for jugador in jugadores:
        n = 1
        for i in range(3):
            limpiar()
            palabra = input(f"Ingrese la palabra {i+1} para {jugador}: ")
            nuevas_palabras.append(palabra)
        n += 1
    return nuevas_palabras

def set_name():
    while True:
        limpiar()
        n = 1
        name = input(f"Ingrese al participante {n}: ")
        while name == "" or name == " ":
            limpiar()
            print("El nombre no puede estar vacio.")
            name = input(f"Ingrese al participante {n}: ") 
        opciones = f'''
    0. Agregar a {name}
    1. Volver a intentarlo
    
Ingrese una opcion:'''
        try:
            opcion = int(input(opciones))
        except:
            print("Solo puede ingresar numeros enteros.")
            continue
        if opcion == 0:
            limpiar()
            print(f"Agregando a {name}...")
            jugadores[name] = 0
            print(f"{name} fue agregado con exito\n")
            continuar = input("Desea agregar otro participante? (s/n)\n").lower()
            if continuar == "s":
                n += 1
                continue
            else:
                guardar_participantes(jugadores)
                break
        else:
            continue

def configurar():
    set_name()
    global palabras
    palabras = set_palabras(jugadores)
    guardar_palabras(palabras)
    return jugadores, palabras

def iniciar():
    opcion = mostrar_bienvenida()
    if opcion == "0":
        limpiar()
        print("Saliendo del juego...")
        exit()
    elif opcion == "1":
        limpiar()
        print("Cargando partida guardada...")
        jugadores = cargar_participantes()
        palabras = cargar_palabras()
    elif opcion == "2":
        limpiar()
        print("Configurando nueva partida...")
        jugadores = {}
        palabras = []
        jugadores, palabras = configurar()
    elif opcion == "4":
        interfaz()
    else:
        limpiar()
        print("Configurando nuevas palabras...")
        palabras = set_palabras(cargar_participantes())
        guardar_palabras(palabras)
        jugadores = cargar_participantes()
    if opcion != "4":
        limpiar()
        input("\nPresione ENTER para continuar.")
        juego.play_game(jugadores, palabras, aux_palabras)

if __name__ == "__main__":
    interfaz()
    
    
    
