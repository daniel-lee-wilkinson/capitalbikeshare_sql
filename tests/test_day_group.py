def test_day_group(sample_df):
    from bigquery_queries.plotting import day_group

    assert day_group("Monday") == "1. Weekday (Mon–Thu)"
    assert day_group("Saturday") == "3. Saturday"
