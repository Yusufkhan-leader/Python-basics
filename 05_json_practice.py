import json
kinolar = [
    {"nomi": "Inception", "baho": 8.8},
    {"nomi": "Interstellar", "baho": 8.7},
    {"nomi": "The Matrix", "baho": 8.7}
]
with open("kinolar.json", "w") as fayl:
    json.dump(kinolar, fayl, indent=4)

print("Ma'lumotlar JSON fayliga saqlandi!")
