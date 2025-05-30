import pandas as pd
from config import FIGURES_DIR
from python_scripts.plots import save_top_stations_map


def test_save_top_stations_map_output_file():
    df = pd.DataFrame(
        {
            "station_name": ["A", "B"],
            "trip_count": [1000, 1500],
            "latitude": [38.9, 38.91],
            "longitude": [-77.03, -77.04],
        }
    )

    # Create the plot
    save_top_stations_map(df, filename="test_top_stations_map.html")

    # Assert output file exists and is not empty
    output_path = FIGURES_DIR / "test_top_stations_map.html"
    assert output_path.exists(), "Expected HTML file was not created"
    assert output_path.stat().st_size > 0, "Generated file is empty"
