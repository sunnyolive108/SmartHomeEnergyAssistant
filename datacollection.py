import sqlite3
from datetime import datetime
import random
import os

# Funktion zur Simulation von Energieverbrauchsdaten
def simulate_consumption():
    return random.uniform(1.0, 5.0)  # Simulierter Verbrauch zwischen 1 und 5 kW

# Ordnerpfad der aktuellen Datei ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'energy_consumption.db')

# Verbinden oder erstellen der Datenbank
conn = sqlite3.connect(db_path)
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