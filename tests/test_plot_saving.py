import pandas as pd

from config import FIGURES_DIR
from python_scripts.plots import plot_weekday_trips


def test_plot_weekday_output_file():
    df = pd.DataFrame(
        {
            "weekday_name": [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ],
            "trip_count": [1000, 1200, 1100, 900, 800, 950, 870],
        }
    )

    plot_weekday_trips(df, filename="test_plot.png")
    output_path = FIGURES_DIR / "test_plot.png"

    assert output_path.exists(), "Plot was not saved in the figures/ folder"
    assert output_path.stat().st_size > 0, "Plot file is empty"
