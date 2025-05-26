import pandas as pd
import matplotlib.pyplot as plt

def visualize_traffic():
    df = pd.read_csv("data/traffic_data.csv")
    plt.figure(figsize=(10, 6))
    df['length'].plot(kind='hist', bins=50, alpha=0.7)
    plt.title("Packet Size Distribution")
    plt.xlabel("Packet Size (bytes)")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    visualize_traffic()
