import os
import pandas as pd
import matplotlib.pyplot as plt

# --- Setup paths ---
# Dynamically get the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the CSV file
csv_path = os.path.join(script_dir, "..", "output", "wallet_scores.csv")

# Check if the CSV file exists
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"CSV file not found at path: {csv_path}")

# --- Load CSV data ---
df = pd.read_csv(csv_path)

# --- Print and calculate basic summary statistics ---
summary_stats = df.describe()
print("Wallet Score Summary Statistics:")
print(summary_stats)

# --- Create bins for the scores (every 50 points) ---
bins = list(range(0, 1050, 50))  # Creates bins: 0-50, 50-100, …, 950-1000
labels = [f'{i}-{i+50}' for i in bins[:-1]]
df['score_range'] = pd.cut(df['score'], bins=bins, labels=labels, right=False)

# Count the number of wallets in each bin
score_dist = df['score_range'].value_counts().sort_index()

# --- Plot the histogram ---
plt.figure(figsize=(12, 6))
bars = plt.bar(score_dist.index, score_dist.values, color='lightgreen', edgecolor='black')

# Add count labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 2, str(int(height)),
             ha='center', va='bottom', fontsize=9)

plt.title('Wallet Credit Score Distribution', fontsize=14)
plt.xlabel('Score Range', fontsize=12)
plt.ylabel('Number of Wallets', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

# Save the histogram to the output folder with high resolution
output_img_path = os.path.join(script_dir, "..", "output", "score_distribution.png")
plt.savefig(output_img_path, dpi=300, bbox_inches='tight')
plt.show()

# --- Get Top 10 Wallets by Score ---
df_sorted = df.sort_values(by="score", ascending=False)
top_10_wallets = df_sorted.head(10)
print("\nTop 10 Wallets by Score:")
print(top_10_wallets[['wallet', 'score']])

# --- Write analysis results to a Markdown file ---
analysis_text = "# Wallet Credit Score Analysis\n\n"
analysis_text += "## Summary Statistics\n\n"
analysis_text += summary_stats.to_markdown() + "\n\n"
analysis_text += "## Score Distribution (Counts per Range)\n\n"
analysis_text += score_dist.to_markdown() + "\n\n"
analysis_text += "## Top 10 Wallets by Score\n\n"
analysis_text += top_10_wallets[['wallet', 'score']].to_markdown() + "\n"

analysis_file = os.path.join(script_dir, "..", "output", "analysis.md")
with open(analysis_file, "w") as f:
    f.write(analysis_text)

print(f"\nAnalysis written to {analysis_file}")
