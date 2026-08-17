parol="Python2026"
urinishlar=3
while urinishlar>0:
    kiritilgan_parol = input("Parolni kiriting: ")
    if kiritilgan_parol == "":
        print("Siz hech narsa kiritmadingiz!")
        continue
    if kiritilgan_parol==parol:
        print("Siz tizimga muvafaqqiyatli kirdingiz")
        break
    else:
        urinishlar-=1
        print(f"Parol xato! Qolgan urinishlar:{urinishlar}")
if urinishlar==0:
    print("Urinishlar tugadi! Afsuski hisob bloklandi😓")
