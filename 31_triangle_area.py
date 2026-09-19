import math

print("Uchburchak yuzini hisoblash!\n")
usul1="3ta tomon"
usul2="Tomon va balandlik"
usul3="2tomon va orasidagi burchak"
print(f"A) {usul1}\nB) {usul2}\nC) {usul3}")
yuzacha = str(input("Variantni tanlang: "))

if yuzacha in ["A", "a"]:
    def yuz(x, y, z):
        p = (x + y + z) / 2
        yuza = p * (p - x) * (p - y) * (p - z)
        return math.sqrt(yuza)

    a = float(input("1-tomon: "))
    b = float(input("2-tomon: "))
    c = float(input("3-tomon: "))
    print(f"Uchburchak yuzi: {yuz(a, b, c)}")

elif yuzacha in["B" , "b"]:
    def yuz(x, y):
        return (x * y) / 2

    t = float(input("Tomon: "))
    z = float(input("Balandlik: "))
    print(f"Uchburchak yuzi: {yuz(t, z)}")

elif yuzacha in ["C",  "c"]:
    def yuz(x, y, z):
        p = (x * y) / 2
        k = math.sin(math.radians(z))
        return p * k

    a = float(input("1-tomon: "))
    b = float(input("2-tomon: "))
    c = int(input("Ular orasidagi burchak: "))
    print(f"Uchburchak yuzi: {yuz(a, b, c)}")

else:
    print("Noto'g'ri tanlov kiritildi!")
