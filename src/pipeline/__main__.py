from pathlib import Path

from pipeline.ingest import load_csv


def main() -> None:
    df = load_csv(Path("data/raw/incidents.csv"))

    print(df)


if __name__ == "__main__":
    main()