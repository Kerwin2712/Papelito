import csv

def guardar_participantes(jugadores):
    try:
        with open("jugadores.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["jugador", "puntos"])
            for jugador in jugadores:
                writer.writerow([jugador, 0])
    except Exception as e:
        print(f"Error al guardar participantes: {e}")

def players_get():
    jugadores = []
    try:
        with open("jugadores.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                jugadores.append(row[0])
        return jugadores
    except FileNotFoundError:
        return None

def guardar_palabras(palabras):
    try:
        with open("palabras.txt", "w") as f:
            for palabra in palabras:
                f.write(f"{palabra}\n")
    except FileNotFoundError:
        messagebox.showerror("Error", "No se pudo guardar el archivo")

def palabras_get():
    palabras = []
    try:
        with open("palabras.txt", "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                palabras.append(row[0])
        return palabras
    except FileNotFoundError:
        return None

def guardar_config(cantidad_de_palabras, tiempo_ronda_1, tiempo_ronda_2, tiempo_ronda_3):
    try:
        with open("config.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["cantidad_de_palabras", "tiempo_ronda_1", "tiempo_ronda_2", "tiempo_ronda_3"])
            writer.writerow([cantidad_de_palabras, tiempo_ronda_1, tiempo_ronda_2, tiempo_ronda_3])
    except Exception as e:
        messagebox.showerror("Error", "No se pudo guardar el archivo")

def get_config():
    config = {}
    try:
        with open("config.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                config["cantidad_de_palabras"] = row[0]
                config["tiempo_ronda_1"] = row[1]
                config["tiempo_ronda_2"] = row[2]
                config["tiempo_ronda_3"] = row[3]
        return config
    except FileNotFoundError:
        return None