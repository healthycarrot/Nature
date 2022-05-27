pat = "パトカー"
taxi = "タクシー"

ans =""
for i,j in zip(pat,taxi):
    ans += i+j

print(ans)