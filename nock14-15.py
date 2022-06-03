import pandas

def output_head(df,N):
    print(df.head(N))

def output_tail(df,N):
    print(df.tail(N))
df = pandas.read_table("resource/popular-names.txt",header=None,sep="\t",names=["name","sex","numner","year"])

output_tail(df,5)

