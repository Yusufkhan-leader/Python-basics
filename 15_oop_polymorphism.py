class NaqdTolov:
    def tolash(self, summa):
        return f"Naqd pul bilan {summa} to'landi!"
class UzcardTolov:
    def tolash(self, summa):
        umumiy=summa*1.01
        return f"Uzcard orqali {summa} so'm (komissiya bilan {umumiy} so'm) yechildi."
naqd = NaqdTolov()
uzcard = UzcardTolov()
tolov_usullari = [naqd, uzcard]
for usul in tolov_usullari:
    print(usul.tolash(50000))
