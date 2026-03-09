import streamlit as st
import pandas as pd
import geopandas as gp
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium


# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("tripdata.csv")
    return df


gdf = gp.GeoDataFrame(
    load_data(),
    geometry=gp.points_from_xy(load_data().start_lng, load_data().start_lat),
).set_crs("EPSG:4326")

# UI
st.title("Capital Bikeshare Trip Heatmap")
st.markdown("Starting locations by day of the week — February 2026")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = st.selectbox("Select a day", days)

# Filter and plot
day_data = gdf[gdf["weekday"] == day][
    ["start_lat", "start_lng", "trip_count"]
].values.tolist()

m = folium.Map(location=[gdf.geometry.y.mean(), gdf.geometry.x.mean()], zoom_start=12)
HeatMap(data=day_data, radius=15, blur=10).add_to(m)

st_folium(m, width=900, height=600)
