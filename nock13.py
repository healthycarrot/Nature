import pandas as pd

df1 = pd.read_table("resource/col1.txt",sep="\t",header=0)
df2 = pd.read_table("resource/col2.txt",sep="\t",header=0)

df_merge = pd.concat([df1,df2],axis=1)

print(df_merge)