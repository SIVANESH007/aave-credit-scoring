# 📊 Wallet Credit Score Analysis

This file presents the analysis of credit scores assigned to Ethereum wallets based on their DeFi behavior from Aave V2 protocol transactions.

---

## 🧮 Score Summary Statistics

| Metric        | Value       |
|---------------|-------------|
| Count         | 3,328 wallets |
| Mean Score    | 42.27        |
| Std Dev       | 74.30        |
| Min Score     | 0.59         |
| 25th Percentile | 0.59       |
| Median (50%)  | 2.09         |
| 75th Percentile | 49.44      |
| Max Score     | 633.70       |

> 🧠 **Insight**: The distribution is highly right-skewed — most wallets score very low (near 0), with only a few showing strong behavior and scoring above 400.

---

## 🔝 Top 10 Wallets by Score

These wallets exhibited the most reliable on-chain behavior across key metrics such as regular repayments, fewer liquidations, and healthy deposits:

| Rank | Wallet Address | Score  |
|------|----------------|--------|
| 1    | 0x058b10cbe1872ad139b00326686ee8ccef274c58 | 633.70 |
| 2    | 0x0476f3ee277eb20568ee2369b337f3ce55bc558a | 586.81 |
| 3    | 0x005f16f017aa933bb41965b52848ceb8ee48b171 | 492.77 |
| 4    | 0x0034baeeb160a5f1032b6d124d3e87cc94d74e62 | 473.39 |
| 5    | 0x05c18ffc1c74cb67cb26bb5222aaf3355b74bbc3 | 469.52 |
| 6    | 0x04ee10fd378f7cad5ac5751d7cd0f42b13ee3b76 | 444.62 |
| 7    | 0x000000003ce0cf2c037493b1dc087204bd7f713e | 426.69 |
| 8    | 0x04fb136989106430e56f24c3d6a473488235480e | 419.63 |
| 9    | 0x02eca8cc78b7d30c1ac5e16988ed2c8a9da658d6 | 411.22 |
| 10   | 0x05404b6f8990a4108150366adb572a870b137edc | 400.08 |

---

## 📉 Score Distribution Chart

Most wallets have a very low score, indicating either:
- New/inactive wallets,
- Limited diversity in interaction,
- Risky behavior (liquidations, lack of repayment),
- Or bot-like activity.

![Score Histogram](output/score_distribution.png)

---

## 🔴 Low-Scoring Wallet Behaviors (0–50)

Wallets in this range exhibit:
- High liquidation-to-borrow ratio
- Very low or no repayments
- Few transactions or single token usage
- Short interaction period

> ⚠️ *These wallets are likely exploitative, inactive, or bots.*

---

## 🟢 High-Scoring Wallet Behaviors (400+)

These are among the most reliable and responsible users:
- Consistent repayments
- High borrow-to-repay ratio
- Fewer or no liquidations
- Use of multiple tokens and protocol actions
- Longer duration of activity

> ✅ *Likely safe users for credit extension, farming rewards, or protocol incentives.*

---

## 📌 Takeaways

- The scoring model successfully separates risky vs responsible behavior.
- Most users score low, indicating high risk or inactivity.
- Only a small elite group scores above 400.
- This model can be used in real-world dApps to flag suspicious wallets or prioritize trusted ones.

---

## 🔮 Future Work

- Add on-chain KYC or ENS data to enrich wallet profiles
- Use clustering to auto-classify wallet types (farmer, borrower, bot, etc.)
- Build dashboard to live-score wallets from Aave or other protocols

