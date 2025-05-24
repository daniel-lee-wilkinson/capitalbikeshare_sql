import matplotlib.pyplot as plt
import pandas as pd

# Data
hours = [f"{i:02}" for i in range(24)]
trip_counts = [
    6843, 3917, 2309, 1244, 1503, 4060,
    11229, 24557, 38741, 27932, 24870, 28307,
    33686, 36630, 39841, 49183, 56424, 69796,
    61183, 48413, 35156, 26566, 19341, 12468
]

# Create DataFrame (optional, but useful for clarity)
df = pd.DataFrame({
    'Hour': hours,
    'Trips': trip_counts
})

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df['Hour'], df['Trips'], marker='o', linestyle='-', color='steelblue')
plt.title('Number of Trips by Hour of Day (April 2025)')
plt.xlabel('Hour of Day (24h)')
plt.ylabel('Number of Trips')
#plt.grid(True)
#plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("C:/Users/danie/sql_projects/bikeshare/trips_by_hour.png", dpi=300)
plt.show()
