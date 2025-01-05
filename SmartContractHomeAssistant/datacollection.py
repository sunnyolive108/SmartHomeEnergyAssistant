import sqlite3
from datetime import datetime
import random
import os
from web3 import Web3
from blockchain_utils import get_web3_connection, get_contract
from dotenv import load_dotenv

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

load_dotenv()  # Dies sollte vor dem Aufruf von get_contract() stehen
# Blockchain-Integration
w3 = get_web3_connection()
contract = get_contract(w3)

# Funktion zum Hinzufügen der Daten zur Blockchain
def add_to_blockchain(timestamp, consumption):
    accounts = w3.eth.accounts  # Hier keine await notwendig
    tx_hash = contract.functions.addConsumption(
        int(datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").timestamp()),
        int(consumption * 1000)  # Umrechnung in Milliwatt für mehr Genauigkeit
    ).transact({'from': accounts[0]})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Verbrauch auf Blockchain gespeichert: {receipt.transactionHash.hex()}")

add_to_blockchain(timestamp, consumption)