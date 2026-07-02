from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "Electric_Vehicle_Population_Data.csv"
CHARTS_DIR = BASE_DIR / "visuals" / "charts"


def main():
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_PATH)

    df.columns = df.columns.str.strip().str.lower()

    print("Missing values:")
    print(df.isnull().sum())

    df = df.dropna(subset=["county", "city", "electric range"])

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nDataset shape:")
    print(df.shape)

    print("\nDataset info:")
    print(df.info())

    print("\nSummary statistics:")
    print(df.describe())

    top_makes = df["make"].value_counts().head(10)
    print("\nTop EV manufacturers:")
    print(top_makes)

    plt.figure()
    top_makes.plot(kind="bar")
    plt.title("Top 10 EV Manufacturers")
    plt.xlabel("Manufacturer")
    plt.ylabel("Number of Vehicles")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "top_manufacturers.png")
    plt.show()

    year_counts = df["model year"].value_counts().sort_index()
    plt.figure()
    year_counts.plot(kind="line")
    plt.title("EV Adoption Growth Over Time")
    plt.xlabel("Year")
    plt.ylabel("Number of Vehicles")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "ev_growth.png")
    plt.show()

    county_counts = df["county"].value_counts().head(10)
    plt.figure()
    county_counts.plot(kind="bar")
    plt.title("Top 10 Counties by EV Adoption")
    plt.xlabel("County")
    plt.ylabel("Number of Vehicles")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "top_counties.png")
    plt.show()

    city_counts = df["city"].value_counts().head(10)
    plt.figure()
    city_counts.plot(kind="bar")
    plt.title("Top Cities for EV Adoption")
    plt.xlabel("City")
    plt.ylabel("Number of Vehicles")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "top_cities.png")
    plt.show()

    type_counts = df["electric vehicle type"].value_counts()
    plt.figure()
    type_counts.plot(kind="pie", autopct="%1.1f%%")
    plt.title("EV Type Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "ev_type.png")
    plt.show()


if __name__ == "__main__":
    main()