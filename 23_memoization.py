kesh={}
def climb_stairs(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n in kesh:
        return kesh[n]
    
    kesh[n] = climb_stairs(n - 1) + climb_stairs(n - 2)
    return kesh[n]
n=int(input("Zinaning hadini kiriting: "))
usullar=climb_stairs(n)   
print(f"Zinaning {n}inchi hadiga chiqishning {usullar}ta usuli bor")
