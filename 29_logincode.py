from random import randint

name = str(input("Ism kiriting: "))
phone = int(input("Telefon nomer kiriting: "))
def login(ism, nomer):
    cod = randint(1000, 9999)
    print(f"Kodingiz: {cod}")
    kod=int(input("Kodingizni kiriting: "))
    if kod==cod:
        with open("Toqsonlar.txt", "a") as f:
            f.write(f"\nIsm: {ism}\nTelefon raqam: {nomer}")
        print("Muvaffaqiyatli o'tdingiz!")
login(name, phone)

