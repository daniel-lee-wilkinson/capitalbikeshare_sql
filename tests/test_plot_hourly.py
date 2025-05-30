import pandas as pd

from config import FIGURES_DIR
from python_scripts.plots import plot_hourly_trips


def test_plot_hourly_output_file():
    df = pd.DataFrame(
        {
            "Hour": [f"{i:02}" for i in range(24)],
            "Trips": [1000 + i * 100 for i in range(24)],
        }
    )

    plot_hourly_trips(df, filename="test_hourly_plot.png")
    output_path = FIGURES_DIR / "test_hourly_plot.png"

    assert output_path.exists()
    assert output_path.stat().st_size > 0
