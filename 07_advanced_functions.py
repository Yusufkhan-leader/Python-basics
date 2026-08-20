kinolar_royxati = [
    {"nomi": "Inception", "baho": 8.8},
    {"nomi": "Interstellar", "baho": 8.7},
    {"nomi": "Shutter Island", "baho": 8.2},
    {"nomi": "The Prestige", "baho": 8.5}
]

def kinolarni_chiqar(kinolar, minimal_baho=8.5):
    for kino in kinolar:
        if kino["baho"] >= minimal_baho:
            print(f"Kino: {kino['nomi']} — Baho: {kino['baho']}")

print("Standard (8.5) bo'yicha")
kinolarni_chiqar(kinolar_royxati)

print("\nYuqoriroq baho bo'yicha")
kinolarni_chiqar(kinolar_royxati, 8.7)
