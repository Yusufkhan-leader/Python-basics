try:
    with open("kinolar_bazasi.json", "r") as f:
        data=f.read()
except FileNotFoundError:
    print("Ma'lumotlar bazasi topilmadi. Yangi baza yaratilishi kerak!")
