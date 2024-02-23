import requests
import pandas as pd

def get_ethereum_transactions(address):
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&sort=asc&apikey=YourApiKeyToken"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['result']
    else:
        print("Failed to fetch transactions.")
        return []

def analyze_whale_wallet(address, threshold):
    transactions = get_ethereum_transactions(address)
    if transactions:
        df = pd.DataFrame(transactions)
        df['value'] = df['value'].astype(float) / 1e18  # Convert wei to ether
        whale_transactions = df[df['value'] > threshold]
        if not whale_transactions.empty:
            print("Whale transactions found:")
            print(whale_transactions)
        else:
            print("No whale transactions found.")
    else:
        print("No transactions found for the specified address.")

if __name__ == "__main__":
    whale_address = "0x0000000000000000000000000000000000000000"  # Replace with the address to analyze
    threshold_eth = 1000  # Set the threshold in ether
    analyze_whale_wallet(whale_address, threshold_eth)
