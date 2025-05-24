import pandas as pd
import matplotlib.pyplot as plt

# Data mapped from weekday number (0=Sunday, ..., 6=Saturday)
data = {
    'weekday_name': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'trip_count': [79663, 112499, 115016, 93269, 83013, 93044, 87695]
}
df = pd.DataFrame(data)

# Ensure correct weekday order
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['weekday_name'] = pd.Categorical(df['weekday_name'], categories=weekday_order, ordered=True)
df = df.sort_values('weekday_name')

# Plot
plt.figure(figsize=(10, 6))
plt.bar(df['weekday_name'], df['trip_count'], color='steelblue', edgecolor='black')
plt.title('Number of Trips by Weekday (April 2025)')
plt.xlabel('Day of Week')
plt.ylabel('Number of Trips')
#plt.grid(axis='y')
plt.tight_layout()
plt.savefig("C:\\Users\\danie\\sql_projects\\bikeshare\\trips_by_weekday.png", dpi=300)
plt.show()
