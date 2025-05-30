import matplotlib.pyplot as plt

from config import FIGURES_DIR

# Define bins manually
labels = ["0–5 min", "5–15 min", "15–30 min", "30+ min"]
counts = [94210, 187432, 63845, 12073]  # Replace with your SQL output

plt.figure(figsize=(8, 5))
plt.bar(labels, counts, edgecolor="black")
plt.title("Trip Duration Distribution by Category")
plt.xlabel("Trip Duration (minutes)")
plt.ylabel("Number of Trips")
# plt.grid(axis='y')
plt.tight_layout()
plt.savefig(
    FIGURES_DIR / "trip_duration_distribution.png",
    dpi=300,
    bbox_inches="tight",
)
plt.show()
