import pandas as pd

def split_file(df,N):
    df_cut = pd.qcut(df,N,label=[i for i in range(N)])

