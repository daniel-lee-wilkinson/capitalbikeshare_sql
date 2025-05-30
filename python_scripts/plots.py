import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

FIGURES_DIR = Path("figures")
FIGURES_DIR.mkdir(exist_ok=True)

def plot_weekday_trips(df: pd.DataFrame, filename: str = "trips_by_weekday.png"):
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['weekday_name'] = pd.Categorical(df['weekday_name'], categories=weekday_order, ordered=True)
    df = df.sort_values('weekday_name')

    plt.figure(figsize=(10, 6))
    plt.bar(df['weekday_name'], df['trip_count'], color='steelblue', edgecolor='black')
    plt.title('Number of Trips by Weekday (April 2025)')
    plt.xlabel('Day of Week')
    plt.ylabel('Number of Trips')
    plt.tight_layout()
    
    output_path = FIGURES_DIR / filename
    plt.savefig(output_path, dpi=300)
    plt.close()

def plot_hourly_trips(df: pd.DataFrame, filename: str = "trips_by_hour.png"):
    FIGURES_DIR.mkdir(exist_ok=True)
    output_path = FIGURES_DIR / filename

    plt.figure(figsize=(10, 6))
    plt.plot(df["Hour"], df["Trips"], marker='o', linestyle='-', color='steelblue')
    plt.title('Number of Trips by Hour of Day (April 2025)')
    plt.xlabel('Hour of Day (24h)')
    plt.ylabel('Number of Trips')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

def plot_duration_distribution(labels, counts, filename: str = "trip_duration_distribution.png"):
    FIGURES_DIR.mkdir(exist_ok=True)
    output_path = FIGURES_DIR / filename

    plt.figure(figsize=(8, 5))
    plt.bar(labels, counts, edgecolor='black')
    plt.title("Trip Duration Distribution by Category")
    plt.xlabel("Trip Duration (minutes)")
    plt.ylabel("Number of Trips")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

import folium

def save_top_stations_map(df: pd.DataFrame, filename: str = "top_stations_map.html"):
    FIGURES_DIR.mkdir(exist_ok=True)
    m = folium.Map(location=[38.9, -77.03], zoom_start=13)

    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=5 + (row['trip_count'] / 1000),
            popup=f"{row['station_name']} ({row['trip_count']} trips)",
            color='blue',
            fill=True,
            fill_opacity=0.7
        ).add_to(m)

    output_path = FIGURES_DIR / filename
    m.save(str(output_path))

