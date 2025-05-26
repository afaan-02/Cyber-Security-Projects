import pandas as pd

def analyze_traffic():
    df = pd.read_csv("data/traffic_data.csv")
    print("Traffic Summary:")
    print(df.describe())

if __name__ == "__main__":
    analyze_traffic()
