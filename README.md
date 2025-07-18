# Aave V2 DeFi Credit Scoring

## 💡 Problem Statement

Assign a credit score (0–1000) to each wallet using raw transaction-level data from the Aave V2 protocol. The goal is to reflect responsible vs. risky user behavior using only historical transactions such as `deposit`, `borrow`, `repay`, `redeemunderlying`, and `liquidationcall`.

---

## 🔧 Approach Overview

### 1. Feature Engineering

From each wallet’s transaction history, we extract features like:
- Total `deposits` count and amount
- Total `borrows` count and amount
- `repay` to `borrow` ratio
- Liquidation frequency
- Duration active on the protocol
- Unique tokens interacted with

These features help determine user reliability, usage diversity, and risk profile.

---

### 2. Scoring Logic

Each wallet is scored on a scale of 0–1000 using a **scoring function** that weighs:
- Positive behavior: consistent deposits, timely repayments, low liquidation
- Negative behavior: excessive borrowing, frequent liquidations, low repayments

The scoring logic is implemented in `score_wallets.py`.

---

### 3. Output

The main script generates:
- 📄 `wallet_scores.csv`: wallet address & score
- 📊 `score_distribution.png`: credit score histogram
- 📘 `analysis.md`: behavioral analysis & graphs

---

## 📁 Project Structure

