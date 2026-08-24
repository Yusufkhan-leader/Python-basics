import requests
url="https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
response=requests.get(url)
data=response.json()
for valyuta in data:
    if valyuta["Ccy"] == "USD":
        kurs=float(valyuta["Rate"])
        dollar=int(input("Dollaringizni kiriting: "))
        som=kurs*dollar
        print(f"Dollaringiz: {som} USD")
