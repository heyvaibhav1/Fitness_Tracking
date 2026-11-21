import numpy as np
import pandas as pd
from tabulate import tabulate
from crud_operations import load_data, FILE


def _print_table(title, rows, headers):
    """Prints a titled grid table with the supplied rows and column headers."""
    print(f"\n{title}")
    print(tabulate(rows, headers=headers, tablefmt="grid", showindex=False))


def data_structures_demo():
    """Demonstrates 5 Python data structure concepts."""
    rows = load_data()
    mins_list = [int(r["Duration"]) for r in rows]
    mins_list.append(45)
    hr_tuple = (60, 120, 160)
    workouts_set = {r["Workout"] for r in rows}
    summary_dict = {"Count": len(rows), "Zones": hr_tuple}
    _print_table("Data Structures", [
        ["Workouts", ", ".join(sorted(workouts_set))],
        ["Heart-rate zones", ", ".join(map(str, hr_tuple))],
        ["Record count", summary_dict.get("Count")]
    ], ["Concept", "Value"])

def numpy_analysis():
    """Demonstrates 1D/2D NumPy arrays, indexing, slicing, and stats."""
    df = pd.read_csv(FILE).dropna(subset=["Calories"])
    arr_1d = df["Calories"].to_numpy(dtype=float)
    arr_2d = df[["Duration", "Calories"]].to_numpy(dtype=float)
    _print_table("1D Array (Calories)", [
        [index, value] for index, value in enumerate(arr_1d[:3])
    ], ["Index", "Calories"])
    _print_table("2D Array (Duration and Calories)", arr_2d[:2, :].tolist(),
                 ["Duration", "Calories"])
    _print_table("Calories Statistics", [
        ["Sum", f"{np.sum(arr_1d):.1f}"],
        ["Mean", f"{np.mean(arr_1d):.1f}"],
        ["Max", f"{np.max(arr_1d):.1f}"],
        ["Min", f"{np.min(arr_1d):.1f}"],
        ["Std", f"{np.std(arr_1d):.1f}"]
    ], ["Statistic", "Value"])

def pandas_report():
    """Handles missing values, filters, sorts, groups, describes, and prints insights."""
    df = pd.read_csv(FILE)
    df["Calories"] = df["Calories"].fillna(df["Calories"].median())
    df["HR"] = df["HR"].fillna(df["HR"].median())

    selected = df[["ID", "Name", "Workout", "Calories"]].head(3)
    _print_table("Selected Columns (Top 3)", selected.to_numpy().tolist(), selected.columns.tolist())
    filtered = df[df["Calories"] > 400].sort_values("Calories", ascending=False)
    high_burn = filtered[["ID", "Workout", "Calories"]].head(3)
    _print_table("High-Burn (>400 kcal) Top 3", high_burn.to_numpy().tolist(),
                 high_burn.columns.tolist())
    workout_averages = df.groupby("Workout", as_index=False)["Calories"].mean().round(1)
    _print_table("GroupBy Workout Avg Calories", workout_averages.to_numpy().tolist(),
                 workout_averages.columns.tolist())
    stats = df[["Duration", "Calories", "Steps"]].describe().round(1).rename_axis("Statistic").reset_index()
    _print_table("Stats Summary", stats.to_numpy().tolist(), stats.columns.tolist())

    top_w = df.groupby("Workout")["Calories"].mean().idxmax()
    _print_table("Summary Report", [
        ["Records", len(df)],
        ["Top Calorie Workout", top_w],
        ["Average Steps", f"{df['Steps'].mean():.0f}"]
    ], ["Metric", "Value"])