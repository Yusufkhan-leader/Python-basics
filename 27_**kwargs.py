malumott={"sat":1600, "gpa":5.0, "ielts":9}
name=str(input("Ismingizni kiriting: "))
def profile_yarat(ism, **malumot):
    print(f"{ism}\n")
    for k, v in malumot.items():
        print(f"{k}={v}")
profile_yarat(name, **malumott)

