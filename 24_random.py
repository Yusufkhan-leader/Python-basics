from random import randint
name=str(input("Ismingizni kiriting: "))
phone=int(input("Telefon raqamingizni kiriting: "))
email=input("Emailingizni kiriting: ")
son=randint(100000, 999999)
def login(kod):
    return f'Kodingiz: {kod}'

print(f"{login(son)}")
