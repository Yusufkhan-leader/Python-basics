try:
    baho=float(input("Balingizni kiriting: "))
    ball=baho*10
    print(f"10 ballik tizimda balingiz: {ball}")
except ValueError:
    print("Format xato! Faqat son kiriting!")
