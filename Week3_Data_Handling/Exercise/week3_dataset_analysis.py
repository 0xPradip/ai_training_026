"""
Week 3 Final Project — Titanic Dataset Analysis
================================================
Load → Clean → Analyze → Visualize.

Uses the public Titanic dataset (free, no auth needed).
Produces a 4-panel chart saved as titanic_analysis.png.

Concepts demonstrated:
- Loading data from a public URL with pandas
- Handling missing values (fillna)
- Removing duplicates
- Filtering, groupby, aggregation
- Multi-panel charts with matplotlib

Run:
    pip install pandas matplotlib
    python week3_dataset_analysis.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# Free public dataset — no auth required
DATA_URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"


def load_and_clean() -> pd.DataFrame:
    """Load the Titanic CSV and clean it for analysis."""
    print("📊  Loading Titanic dataset from public URL...")
    df = pd.read_csv(DATA_URL)
    print(f"   Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print()

    print("🧹  Cleaning missing values...")
    print(f"   Before — Age missing: {df['Age'].isna().sum()}, "
          f"Embarked missing: {df['Embarked'].isna().sum()}")
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    df = df.drop_duplicates()
    print(f"   After  — Age missing: {df['Age'].isna().sum()}, "
          f"Embarked missing: {df['Embarked'].isna().sum()}")
    print(f"   Final shape: {df.shape}")
    print()

    return df


def headline_stats(df: pd.DataFrame):
    """Print key survival statistics."""
    print("=" * 50)
    print("📈  HEADLINE NUMBERS")
    print("=" * 50)

    overall = df["Survived"].mean() * 100
    print(f"\nOverall survival rate: {overall:.1f}%  "
          f"({df['Survived'].sum()} of {len(df)} passengers)")

    print("\nSurvival rate by passenger class:")
    by_class = df.groupby("Pclass")["Survived"].mean().mul(100).round(1)
    for cls, rate in by_class.items():
        bar = "█" * int(rate / 2)
        print(f"   Class {cls}:  {bar:<25}  {rate}%")

    print("\nSurvival rate by sex:")
    by_sex = df.groupby("Sex")["Survived"].mean().mul(100).round(1)
    for sex, rate in by_sex.items():
        bar = "█" * int(rate / 2)
        print(f"   {sex.capitalize():<8} {bar:<40}  {rate}%")

    print("\nCross-tab: survival % by (class × sex)")
    crosstab = (
        df.groupby(["Pclass", "Sex"])["Survived"]
        .mean()
        .mul(100)
        .round(1)
        .unstack()
    )
    print(crosstab)
    print()


def plot_charts(df: pd.DataFrame, outfile: str = "titanic_analysis.png"):
    """Build a 4-panel summary chart and save it."""
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    fig.suptitle("Titanic — Who Survived?", fontsize=16, fontweight="bold")

    # 1. Survival by class
    df.groupby("Pclass")["Survived"].mean().mul(100).plot(
        kind="bar", ax=axes[0, 0], color="steelblue", edgecolor="black"
    )
    axes[0, 0].set_title("Survival % by Class")
    axes[0, 0].set_ylabel("Survival %")
    axes[0, 0].set_xlabel("Class")
    axes[0, 0].tick_params(axis="x", rotation=0)
    axes[0, 0].grid(axis="y", alpha=0.3)

    # 2. Survival by sex
    df.groupby("Sex")["Survived"].mean().mul(100).plot(
        kind="bar", ax=axes[0, 1], color=["coral", "steelblue"], edgecolor="black"
    )
    axes[0, 1].set_title("Survival % by Sex")
    axes[0, 1].set_ylabel("Survival %")
    axes[0, 1].set_xlabel("")
    axes[0, 1].tick_params(axis="x", rotation=0)
    axes[0, 1].grid(axis="y", alpha=0.3)

    # 3. Age distribution
    axes[1, 0].hist(
        [df.loc[df["Survived"] == 0, "Age"], df.loc[df["Survived"] == 1, "Age"]],
        bins=25, label=["Died", "Survived"], color=["#c0392b", "#27ae60"],
        edgecolor="black", alpha=0.85,
    )
    axes[1, 0].set_title("Age Distribution by Outcome")
    axes[1, 0].set_xlabel("Age")
    axes[1, 0].set_ylabel("Count")
    axes[1, 0].legend()
    axes[1, 0].grid(axis="y", alpha=0.3)

    # 4. Class × Sex heatmap-style
    crosstab = (
        df.groupby(["Pclass", "Sex"])["Survived"]
        .mean()
        .mul(100)
        .unstack()
    )
    crosstab.plot(
        kind="bar", ax=axes[1, 1], color=["coral", "steelblue"], edgecolor="black"
    )
    axes[1, 1].set_title("Survival % by Class × Sex")
    axes[1, 1].set_ylabel("Survival %")
    axes[1, 1].set_xlabel("Class")
    axes[1, 1].tick_params(axis="x", rotation=0)
    axes[1, 1].legend(title="Sex")
    axes[1, 1].grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig(outfile, dpi=120, bbox_inches="tight")
    print(f"✅  Saved chart: {outfile}")
    plt.show()


def main():
    df = load_and_clean()
    headline_stats(df)
    plot_charts(df)

    print()
    print("=" * 50)
    print("💡  KEY INSIGHT")
    print("=" * 50)
    print(
        "Class and sex were the strongest predictors of survival.\n"
        "  • A first-class woman had ~97% chance of surviving.\n"
        "  • A third-class man had ~14% chance.\n"
        "Real disasters reveal social hierarchies hidden in normal times.\n"
    )


if __name__ == "__main__":
    main()
