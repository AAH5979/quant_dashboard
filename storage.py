import pandas as pd

def load_data():
    try:
        return pd.read_csv("data/ticks.csv", parse_dates=["timestamp"])
    except:
        return pd.DataFrame()
