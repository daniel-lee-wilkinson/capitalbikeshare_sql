import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def day_group(day):
    if day in ["Monday", "Tuesday", "Wednesday", "Thursday"]:
        return "1. Weekday (Mon–Thu)"
    elif day == "Friday":
        return "2. Friday"
    elif day == "Saturday":
        return "3. Saturday"
    else:
        return "4. Sunday"


def build_heatmap_figure(df: pd.DataFrame) -> go.Figure:
    df = df.copy()
    df["day_group"] = df["weekday"].apply(day_group)

    grouped = (
        df.groupby(["day_group", "start_lat", "start_lng", "member_casual"])[
            "trip_count"
        ]
        .mean()
        .reset_index()
    )

    grouped["trip_bin"] = pd.cut(
        grouped["trip_count"],
        bins=[0, 5, 15, 30, 50, float("inf")],
        labels=[1, 2, 3, 4, 5],
    ).astype(float)

    groups = ["1. Weekday (Mon–Thu)", "2. Friday", "3. Saturday", "4. Sunday"]

    colorscale = [
        [0.0, "lightyellow"],
        [0.25, "yellow"],
        [0.5, "orange"],
        [0.75, "orangered"],
        [1.0, "darkred"],
    ]
    bin_labels = ["0-5", "5-15", "15-30", "30-50", "50+"]

    def chart_title(group_name: str) -> str:
        return (
            f"Capital Bikeshare - {group_name}"
            "<br><sup>Color scale = mean trips per location: "
            "1: 0-5, 2: 5-15, 3: 15-30, 4: 30-50, 5: 50+</sup>"
        )

    center_lat = df["start_lat"].mean()
    center_lon = df["start_lng"].mean()

    fig = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=("Members", "Casual"),
        specs=[[{"type": "mapbox"}, {"type": "mapbox"}]],
    )

    for group in groups:
        for col, rider_type in enumerate(["member", "casual"], start=1):
            day_data = grouped[
                (grouped["day_group"] == group)
                & (grouped["member_casual"] == rider_type)
            ]
            trace = go.Densitymapbox(
                lat=day_data["start_lat"],
                lon=day_data["start_lng"],
                z=day_data["trip_bin"],
                customdata=day_data[["trip_count"]],
                radius=15,
                name=f"{group} - {rider_type}",
                visible=(group == "1. Weekday (Mon–Thu)"),
                colorscale=colorscale,
                zmin=1,
                zmax=5,
                showscale=(col == 2),
                colorbar=(
                    dict(
                        title="Mean trips",
                        tickvals=[1, 2, 3, 4, 5],
                        ticktext=bin_labels,
                    )
                    if col == 2
                    else None
                ),
                hovertemplate=(
                    "Lat: %{lat:.4f}<br>Lon: %{lon:.4f}<br>"
                    "Mean trips: %{customdata[0]:.1f}<br>"
                    "Trip bin: %{z:.0f}<extra></extra>"
                ),
            )
            fig.add_trace(trace, row=1, col=col)

    # 2 traces per group (member + casual)
    buttons = []
    for i, group in enumerate(groups):
        visibility = [False] * len(groups) * 2
        visibility[i * 2] = True  # member trace
        visibility[i * 2 + 1] = True  # casual trace
        buttons.append(
            dict(
                label=group,
                method="update",
                args=[
                    {"visible": visibility},
                    {"title": chart_title(group)},
                ],
            )
        )

    fig.update_layout(
        mapbox=dict(
            style="carto-positron", zoom=11, center=dict(lat=center_lat, lon=center_lon)
        ),
        mapbox2=dict(
            style="carto-positron", zoom=11, center=dict(lat=center_lat, lon=center_lon)
        ),
        updatemenus=[
            dict(
                type="buttons",
                direction="right",
                buttons=buttons,
                x=0.5,
                xanchor="center",
                y=1.08,
            )
        ],
        title=chart_title("Weekday (Mon-Thu)"),
        height=600,
    )
    return fig


def generate_heatmap_html(
    input_csv: str = "tripdata.csv", output_html: str = "heatmap.html"
):
    df = pd.read_csv(input_csv)
    fig = build_heatmap_figure(df)
    fig.write_html(output_html)


if __name__ == "__main__":
    generate_heatmap_html()
