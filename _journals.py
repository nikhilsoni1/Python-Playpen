import pandas as pd

df = pd.DataFrame({'Journal': [], "Volume": [], "Contents": []})
a = ["a", "b", "c"]
b = ["d", "e", "f"]
c = ["g", "h", "i"]
for i in range(10):
    df_append = pd.DataFrame({'Journal': a, "Volume": b, "Contents": c})
    df = df.append(df_append)
    del df_append
df.reset_index(inplace=True, drop=True)
print(df)
