import json
import os
import csv
from collections import defaultdict
from datetime import datetime

# Token decimal mapping (can be expanded)
TOKEN_DECIMALS = {
    "USDC": 6,
    "WMATIC": 18,
    "DAI": 18,
    "USDT": 6
}

def load_transactions(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def extract_wallet_features(transactions):
    wallet_data = defaultdict(lambda: {
        "total_deposit_usd": 0,
        "num_deposits": 0,
        "timestamps": set(),
        "unique_assets": set()
    })

    for tx in transactions:
        wallet = tx["userWallet"]
        action = tx["action"]
        ts = tx["timestamp"]

        if action == "deposit":
            data = tx["actionData"]
            amount = float(data["amount"])
            price = float(data["assetPriceUSD"])
            token = data["assetSymbol"]
            decimals = TOKEN_DECIMALS.get(token, 18)
            
            amount_usd = (amount / (10 ** decimals)) * price
            
            wallet_data[wallet]["total_deposit_usd"] += amount_usd
            wallet_data[wallet]["num_deposits"] += 1
            wallet_data[wallet]["timestamps"].add(ts)
            wallet_data[wallet]["unique_assets"].add(token)

    return wallet_data

def compute_scores(wallet_data):
    scores = []

    # Max values for normalization
    max_deposit = max(w["total_deposit_usd"] for w in wallet_data.values()) or 1
    max_deposits = max(w["num_deposits"] for w in wallet_data.values()) or 1
    max_days = 1

    # First calculate max active days
    for w in wallet_data.values():
        times = sorted(w["timestamps"])
        if len(times) >= 2:
            days = (max(times) - min(times)) / 86400  # seconds to days
            max_days = max(max_days, days)

    for wallet, data in wallet_data.items():
        times = sorted(data["timestamps"])
        active_days = (max(times) - min(times)) / 86400 if len(times) > 1 else 0

        score = (
            (data["total_deposit_usd"] / max_deposit) * 400 +
            (data["num_deposits"] / max_deposits) * 300 +
            (active_days / max_days) * 300
        )
        scores.append({
            "wallet": wallet,
            "score": round(min(score, 1000), 2)
        })

    return scores

def save_scores(scores, output_file):
    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["wallet", "score"])
        writer.writeheader()
        writer.writerows(scores)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "..", "data", "user-transactions.json")
    output_path = os.path.join(base_dir, "..", "output", "wallet_scores.csv")
    
    print("Loading data...")
    txns = load_transactions(input_path)

    print("Extracting wallet features...")
    wallet_data = extract_wallet_features(txns)

    print("Computing credit scores...")
    scores = compute_scores(wallet_data)

    print(f"Saving output to {output_path}")
    save_scores(scores, output_path)

    print("Done ✅")

if __name__ == "__main__":
    main()
