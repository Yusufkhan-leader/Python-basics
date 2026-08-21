kinolar = ["Inception", "Interstellar", "Dark Knight", "Avatar", "Tenet"]

while True:
    try:
        baho=float(input("Kino bahosini kiriting: "))
        ball=baho*10
        if ball>=80:
            kinolar.append("Oppenheimer")
            print(f"Sizning balingizga mos bir kino: {kinolar[-1]}")
        elif ball>=70:
            print(f"Bu bahoga mos kino: {kinolar[0]}")
        elif ball>=60:
            print(f"Bu bahoga mos kino: {kinolar[1]}")
        elif ball>=50:
            print(f"Bu bahoga mos kino: {kinolar[2]}")
        elif ball>=40:
            print(f"Bu bahoga mos kino: {kinolar[3]}")
        elif ball>=30:
            print(f"Bu bahoga mos kino: {kinolar[4]}")
        else:
            print("Ro'yxatdan bu bahoga mos kino topilmadi!")    
    except ValueError:
        print("Format xato! Faqat son kiriting!")



