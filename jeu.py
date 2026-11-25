import random
secret = random.randint(1, 100)
essais = 0
proposition = 0

while proposition != secret:
    proposition = int(input("Ton nombre : "))
    if proposition < 1 or proposition > 100:
        print("Choisis un nombre entre 1 et 100.")
        continue
    essais = essais + 1
    if proposition < secret:
        print("C'est plus !")
    elif proposition > secret:
        print("C'est moins !")
    else:
        print(f"Bravo ! Tu as trouvé en {essais} essais.")