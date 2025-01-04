import sqlite3
from datetime import datetime
import random

# Funktion zur Simulation von Energieverbrauchsdaten
def simulate_consumption():
    return random.uniform(1.0, 5.0)  # Simulierter Verbrauch zwischen 1 und 5 kW

# Verbinden oder erstellen der Datenbank
conn = sqlite3.connect('energy_consumption.db')
c = conn.cursor()

# Tabelle erstellen, falls sie nicht existiert
c.execute('''CREATE TABLE IF NOT EXISTS energy_data
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              timestamp TEXT,
              consumption FLOAT)''')

# Daten in die Datenbank einfügen
consumption = simulate_consumption()
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
c.execute("INSERT INTO energy_data (timestamp, consumption) VALUES (?, ?)", (timestamp, consumption))

# Speichern und Verbindung schließen
conn.commit()
conn.close()

print(f"[Simulierter] Verbrauch {consumption} kW um {timestamp} gespeichert.")
