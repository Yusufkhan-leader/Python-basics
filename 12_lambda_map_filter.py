kinolar = ["Inception", "Interstellar", "Dark Knight", "Avatar", "Tenet"]
baholar = [7.5, 8.8, 9.2, 6.5, 8.0]
saralangan_baholar=list(filter(lambda x: x>=8.0,baholar))
yangi_ballar=list(map(lambda x: x*10, saralangan_baholar))
katta_kinolar = list(map(lambda x: x.upper(), kinolar))
print(f"Saralangan baholar: {saralangan_baholar}")
print(f"10 ballik tizimda: {yangi_ballar}")
print(f"Katta harflarda: {katta_kinolar}")
