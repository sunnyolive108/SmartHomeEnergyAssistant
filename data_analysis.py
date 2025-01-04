import sqlite3
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Ordnerpfad der aktuellen Datei ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'energy_consumption.db')

# Datenbank öffnen und Daten laden
conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * from energy_data", conn)
conn.close()

print(df.head())  # Ausgabe der ersten paar Zeilen, um zu überprüfen, ob die Daten geladen wurden

# Annahme: Wir wollen den Energieverbrauch basierend auf der Zeit vorhersagen
X = df['timestamp'].apply(lambda x: pd.to_datetime(x).hour)  # Stunde als Feature
y = df['consumption']  # Verbrauch als Label

# Aufteilen der Daten in Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Trainingsdaten: {len(X_train)}, Testdaten: {len(X_test)}")

# Modell erstellen und trainieren
# model = LinearRegression()
# model.fit(X_train.values.reshape(-1, 1), y_train)  # Reshaping, da LinearRegression 2D-Array erwartet       
