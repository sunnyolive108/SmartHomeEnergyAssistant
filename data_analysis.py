import sqlite3
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# h = Stunde | w = Wochentag (0 = Montag bis 6 = Sonntag)
tag = {0: 'Montag', 1: 'Dienstag', 2: 'Mittwoch', 3: 'Donnerstag', 4: 'Freitag', 5: 'Samstag', 6: 'Sonntag'}
h = 14
w = 5

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
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)  # Kein Reshaping mehr nötig, da wir zwei Features haben

# Vorhersagen auf den Testdaten machen
y_pred = model.predict(X_test)

# Modell evaluieren
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean squared error: {mse}")
print(f"R^2: {r2}")

# Einfache Vorhersage machen 
vorhersage_df = pd.DataFrame({'hour': [h], 'day_of_week': [w]})
vorhersage = model.predict(vorhersage_df)
print(f"Vorhersage für {h} Uhr am {tag[w]}: {vorhersage[0]:.2f} kW")