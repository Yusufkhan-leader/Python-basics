start= int(input("Boshlang'ich son: "))
end=int(input("Tugash soni:"))
def son(start, end):
    for i in range(start, end):
        if i%2==0:
            print(f"Juft son: {i}")
son(start, end)
