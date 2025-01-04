import sqlite3
import pandas as pd
import os

# Ordnerpfad der aktuellen Datei ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'energy_consumption.db')

# Datenbank öffnen und Daten laden
conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * from energy_data", conn)
conn.close()

print(df.head())  # Ausgabe der ersten paar Zeilen, um zu überprüfen, ob die Daten geladen wurden
