age = input("Quel est votre âge ? ").strip()
age = int(age)
if age < 13:
    print("Tu es un enfant.")
elif age < 18:
    print("Tu es adolescent.")
else:
    print("Tu es adulte.")