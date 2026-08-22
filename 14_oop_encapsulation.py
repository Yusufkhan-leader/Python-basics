class Kassa:
    def __init__(self, pul):
        self.__pul = pul

    def pulni_korish(self):
        return f"Kassada {self.__pul} so'm bor"

    def pul_qosh(self, miqdor):
        if miqdor > 0:
            self.__pul += miqdor
            print(f"Kassaga {miqdor} so'm qo'shildi.")
        else:
            print("Xato: Manfiy pul qo'shib bo'lmaydi!")

kassa1 = Kassa(500)

print(kassa1.pulni_korish())

kassa1.pul_qosh(200)
print(kassa1.pulni_korish())

kassa1.pul_qosh(-50)
