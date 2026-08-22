class Kino:
    def __init__(self, nomi, bahosi):
        self.nomi=nomi
        self.bahosi=bahosi
    def malumot_ber(self):
        return(f"Kino: {self.nomi}, Bahosi: {self.bahosi}")
class Serial(Kino):
    def __init__(self, nomi, bahosi, qismlar_soni):
        super().__init__(nomi, bahosi)
        self.qismlar_soni=qismlar_soni
    def malumot_ber(self):
        ota_matn = super().malumot_ber()  # "Kino: Ichkarida, Bahosi: 9.8" ni oladi
        return f"{ota_matn}, Qismlari: {self.qismlar_soni}"
kino1=Kino("Interstellar", 9.0)
Serial2=Serial("Ichkarida", 9.8, 354)
print(kino1.malumot_ber())
print(Serial2.malumot_ber())
