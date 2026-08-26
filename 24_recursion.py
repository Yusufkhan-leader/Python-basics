def reverse_string(matn):
    if len(matn)<=1:
        return matn
    else:
        return matn[-1] + reverse_string(matn[:-1])

matn=input("Ismingizni kiriting: ")
matn=matn.lower()
natija=reverse_string(matn)
print(f"Ismingizning teskarisi: {natija}")
