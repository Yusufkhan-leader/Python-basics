import json
amaliyot = {
    "foydalanuvchi": "Ali",
    "almashtirildi_usd": 100,
    "olinadigan_som": 1280000
}
with open("tarix.json", "w") as fayl:
    json.dump(amaliyot, fayl, indent=4)
with open("tarix.json", "r") as fayl:
    data=json.load(fayl)
for k,v in data.items():
    print(f"{k.title()}: {v}")

