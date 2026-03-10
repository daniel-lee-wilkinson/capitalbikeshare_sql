import sys
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "trip_count": [1, 7, 20, 35, 60],
            "weekday": ["Monday", "Tuesday", "Wednesday", "Saturday", "Sunday"],
        }
    )
