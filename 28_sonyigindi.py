def yigindi(n):
    if n==1:
        return 1
    return n+yigindi(n-1)

n=int(input("Son kiriting: "))
print(f"1dan {n}gacha bo'lgan sonlar yig'indisi: {yigindi(n)}")
