import ngaram

paradise = "paraparaparadise"
paragraph = "paragraph"

X =  ngaram.n_gram(paradise,2)

Y =  ngaram.n_gram(paragraph,2)

print(X)
print(Y)

X = set(X)
Y = set(Y)

XorY = X|Y
XandY = X&Y
XminusY = X-Y

print("和集合：",XorY)
print("積集合：",XandY)
print("差集合：",XminusY)

print("se" in X)
print("se" in Y)