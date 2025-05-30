
from python_scripts.plots import plot_duration_distribution


from config import FIGURES_DIR
import os

def test_plot_created():
    expected_file = FIGURES_DIR / "trips_by_hour.png"
    assert expected_file.exists()



def test_plot_duration_distribution_output_file():
    labels = ["0–5 min", "5–15 min", "15–30 min", "30+ min"]
    counts = [1000, 2000, 1500, 500]

    plot_duration_distribution(labels, counts, filename="test_duration_plot.png")
    output_path = FIGURES_DIR / "test_duration_plot.png"

    assert output_path.exists()
    assert output_path.stat().st_size > 0
