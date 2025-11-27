from utils.utils import limpiar

separador = "-" * 50

bienvenida = '''
    Bienvenido al juego de Papelito.
'''

opciones = '''
    Opciones: 
        0. Salir
        1. Jugar partida guardada
        2. Configurar nueva partida
        3. Configurar nuevas palabras
        4. Mostrar interfaz
'''

def mostrar_bienvenida():
    limpiar()
    print(separador)
    print(bienvenida)
    print(separador)
    print(opciones)
    print(separador)
    return input("Ingrese una opcion: ")

