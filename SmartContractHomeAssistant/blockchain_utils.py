import os
from web3 import Web3
from dotenv import load_dotenv

def get_web3_connection():
    w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
    if not w3.is_connected():
        raise ConnectionError("Konnte keine Verbindung zur Blockchain herstellen!")
    return w3

load_dotenv()
def get_contract(w3):
    contract_address = os.getenv('CONTRACT_ADDRESS')
    if not contract_address:
        raise ValueError("Contract address not set in environment variables.")
    
    contract_abi_path = os.getenv('CONTRACT_ABI_PATH')
    if not contract_abi_path:
        raise ValueError("Contract ABI path not set in environment variables.")
    
    with open(contract_abi_path, 'r') as file:
        contract_abi = json.load(file)
    
    return w3.eth.contract(address=contract_address, abi=contract_abi)

# Hinweis: Du brauchst auch das `json` Modul, um die ABI-Datei zu lesen
import json

# Beispielaufruf der Funktion (kommentiert aus, da nicht notwendig)
# print(fetch_from_blockchain(contract, 0))  # Ruft den ersten Verbrauch ab