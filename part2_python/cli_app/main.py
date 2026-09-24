import argparse
import pandas as pd


def query_traffic(data_path, hour_filter):
    df = pd.read_csv(data_path)
    df["date_time"] = pd.to_datetime(df["date_time"])
    df["hour"] = df["date_time"].dt.hour

    filtered = df[df["hour"] == hour_filter]
    avg_vol = filtered["traffic_volume"].mean()
    print(f"--- Traffic Report for Hour {hour_filter}:00 ---")
    print(f"Total Records: {len(filtered)}")
    print(f"Average Traffic Volume: {avg_vol:.2f} vehicles")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Smart City Traffic CLI Query"
    )
    parser.add_argument(
        "--hour", type=int, default=8, help="Hour of the day (0-23)"
    )
    args = parser.parse_args()

    query_traffic("processed_traffic.csv", args.hour)
