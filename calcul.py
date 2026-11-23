a = int(input("Premier nombre : "))
b = int(input("Deuxième nombre : "))
print(f"La somme est {a+b}")
print(f"La différence est {a-b}")
print(f"Le produit est {a*b}")
if  b == 0:
    print("Division impossible par zéro ")
else:
    print(f"Le quotient est {round(a/b, 5)}")       