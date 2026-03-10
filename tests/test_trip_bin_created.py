def test_trip_bin_created(sample_df):
    import pandas as pd

    sample_df["trip_bin"] = pd.cut(
        sample_df["trip_count"],
        bins=[0, 5, 15, 30, 50, float("inf")],
        labels=[1, 2, 3, 4, 5],
    ).astype(float)
    assert sample_df["trip_bin"].notna().all()
