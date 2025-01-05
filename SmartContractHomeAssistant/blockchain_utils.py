import os
from web3 import Web3

def get_web3_connection():
    w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
    if not w3.is_connected():
        raise ConnectionError("Konnte keine Verbindung zur Blockchain herstellen!")
    return w3

def get_contract(w3):
    contract_abi = [
        {
          "inputs": [
            {
              "internalType": "uint256",
              "name": "",
              "type": "uint256"
            }
          ],
          "name": "consumptions",
          "outputs": [
            {
              "internalType": "uint256",
              "name": "timestamp",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "value",
              "type": "uint256"
            }
          ],
          "stateMutability": "view",
          "type": "function"
        },
        {
          "inputs": [
            {
              "internalType": "uint256",
              "name": "_timestamp",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "_value",
              "type": "uint256"
            }
          ],
          "name": "addConsumption",
          "outputs": [],
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "inputs": [],
          "name": "getConsumptionCount",
          "outputs": [
            {
              "internalType": "uint256",
              "name": "",
              "type": "uint256"
            }
          ],
          "stateMutability": "view",
          "type": "function"
        },
        {
          "inputs": [
            {
              "internalType": "uint256",
              "name": "_index",
              "type": "uint256"
            }
          ],
          "name": "getConsumption",
          "outputs": [
            {
              "internalType": "uint256",
              "name": "",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "",
              "type": "uint256"
            }
          ],
          "stateMutability": "view",
          "type": "function"
        }
    ]
    contract_address = 'YOUR_CONTRACT_ADDRESS'  # Adresse deines Smart Contracts
    return w3.eth.contract(address=contract_address, abi=contract_abi)

# Hinweis: Der ABI und die Contract-Adresse werden hier hartcodiert. 
# In der Praxis möchtest du diese vielleicht aus einer Konfigurationsdatei oder Umweltvariablen lesen.
# Außerdem solltest du 'YOUR_CONTRACT_ADDRESS' durch die echte Adresse ersetzen, sobald du sie hast.

# Beispielaufruf der Funktion (kommentiert aus, da nicht notwendig)
# print(fetch_from_blockchain(contract, 0))  # Ruft den ersten Verbrauch ab