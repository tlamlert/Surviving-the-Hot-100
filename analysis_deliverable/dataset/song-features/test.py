import pandas as pd

df = pd.read_csv("2000s_features")
print(df.dtypes)
for row, idx in enumerate(df['danceability'].values):
    try:
        float(row)
    except ValueError:
        print(idx)