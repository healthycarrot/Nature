def n_gram(target,n):
    return [target[idx:idx+n] for idx in range(len(target)-n+1)]