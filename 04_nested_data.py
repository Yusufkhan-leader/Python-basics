kinolar = [
    {"nomi": "Inception", "rejissyor": "Christopher Nolan", "baho": 8.8},
    {"nomi": "Interstellar", "rejissyor": "Christopher Nolan", "baho": 8.7},
    {"nomi": "Shutter Island", "rejissyor": "Martin Scorsese", "baho": 8.2},
    {"nomi": "The Prestige", "rejissyor": "Christopher Nolan", "baho": 8.5},
    {"nomi": "The Matrix", "rejissyor": "Lana Wachowski, Lilly Wachowski", "baho": 8.7}
]
for kino in kinolar:
    if kino["baho"]>=8.5:
        print(f"kino nomi: {kino['nomi']}, rejissyor: {kino['rejissyor']}, baho: {kino['baho']}")
