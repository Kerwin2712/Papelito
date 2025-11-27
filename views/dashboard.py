import ttkbootstrap as ttk

def dashboard_view(contenedor_principal, navegacion):
    for widget in contenedor_principal.winfo_children():
        widget.destroy()
    dashboard_frame = ttk.Frame(contenedor_principal, padding=10)
    dashboard_frame.pack(expand=True)
    
    ttk.Label(dashboard_frame, text="Bienvenido a Papelito").pack(pady=20)
    
    ttk.Separator(dashboard_frame).pack(fill="x", pady=10)
    
    ttk.Button(dashboard_frame, width=30, text="Jugar nueva partida", command=lambda: navegacion("pre_game")).pack(pady=10)
    ttk.Button(dashboard_frame, width=30, text="Preferences", command=lambda: navegacion("preferences")).pack(pady=10)
    ttk.Button(dashboard_frame, width=30, text="Salir", command=salir).pack(pady=10)
    

    return dashboard_frame

def salir():
    exit()