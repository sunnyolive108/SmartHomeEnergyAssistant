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

print(df.head())  # überprüfen, ob die Daten geladen wurden

# Features erstellen
df['timestamp'] = pd.to_datetime(df['timestamp'])  # timestamp als datetime-Objekt
df['hour'] = df['timestamp'].dt.hour  # Stunde als Feature
df['day_of_week'] = df['timestamp'].dt.dayofweek  # Wochentag als Feature hinzufügen 

# Features und Labels definieren
X = df[['hour', 'day_of_week']]  # die Stunde als auch den Wochentag
y = df['consumption']  # Verbrauch als Label

# Aufteilen der Daten in Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Trainingsdaten: {len(X_train)}, Testdaten: {len(X_test)}")

# Modell erstellen und trainieren
model = LinearRegression()
model.fit(X_train, y_train)  # Kein Reshaping mehr nötig, da wir zwei Features haben

# Vorhersagen auf den Testdaten machen
y_pred = model.predict(X_test)

# Modell evaluieren
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean squared error: {mse}")
print(f"R^2: {r2}")
import pandas as pd

# Einfache Vorhersage machen 
vorhersage_df = pd.DataFrame({'hour': [14], 'day_of_week': [5]})
vorhersage = model.predict(vorhersage_df)
print(f"Vorhersage für {vorhersage_df['hour'][0]} Uhr am {vorhersage_df['day_of_week'][0]}: {vorhersage[0]} kW")
