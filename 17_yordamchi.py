class Kino:
    def __init__(self, nomi, narxi):
        self.nomi=nomi
        self.narxi=narxi
    def malumot(self):
        return f"Kino nomi: {self.nomi} Narxi: {self.narxi}"   
class Kassa:
    def __init__(self, boshlangich_balans):
        self.__balans = boshlangich_balans
    def balansni_korish(self):
        return f"Balansda {self.__balans} so'm bor"
    def chipta_sot(self, kino_obyekti):
        self.__balans += kino_obyekti.narxi  
        return f"'{kino_obyekti.nomi}' filmi uchun chipta sotildi! Narxi: {kino_obyekti.narxi} so'm"        
        
