import resource
import pandas as pd

df = pd.read_table(
    "resource/popular-names.txt",
    header=None,
    sep="\t",
    names=["name","sex","number","year"])

print(len(df))
print(df.head)