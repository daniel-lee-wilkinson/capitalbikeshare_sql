import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd
from pathlib import Path
from python_scripts.plots import save_top_stations_map, FIGURES_DIR

def test_save_top_stations_map_output_file():
    df = pd.DataFrame({
        "station_name": ["A", "B"],
        "trip_count": [1000, 1500],
        "latitude": [38.9, 38.91],
        "longitude": [-77.03, -77.04]
    })

    save_top_stations_map(df, filename="test_top_stations_map.html")
    output_path = FIGURES_DIR / "test_top_stations_map.html"

    assert output_path.exists()
    assert output_path.stat().st_size > 0