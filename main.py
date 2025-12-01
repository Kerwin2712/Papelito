from views.dashboard import dashboard_view
from views.preferences import preferences_view
from views.pre_game import pre_game_view
from views.words import words_view
from views.game import play_game_view
from tkinter import messagebox
import ttkbootstrap as ttk

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

if __name__ == "__main__":
    interfaz()