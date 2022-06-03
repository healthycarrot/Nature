import pandas as pd

df = pd.read_table("resource/popular-names.txt",header=None,sep="\t",names=["name","sex","number","year"])

df.to_csv("resource/col1.txt",columns=["name"],index=False)
df.to_csv("resource/col2.txt",columns=["sex"],index=False)
