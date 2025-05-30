import pandas as pd
import folium


# Load data
df = pd.read_csv(
    "C:/Users/danie/PycharmProjects/capitalbikeshare_sql/processed_data/top_stations.csv"
)

# Create base map centered on DC
m = folium.Map(location=[38.9, -77.03], zoom_start=13)

# Add each station to the map
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=5 + (row["trip_count"] / 1000),
        popup=f"{row['station_name']} ({row['trip_count']} trips)",
        color="blue",
        fill=True,
        fill_opacity=0.7,
    ).add_to(m)

# Save as HTML map
m.save("top_stations_map.html")
