restaurants = ["JP chawama", "Restaurant la lionne", "FSS"]

while True:
    print("\n1. Voir la liste")
    print("2. Ajouter un restaurant")
    print("3. Quitter")
    choix = input("Ton choix : ").strip()

    if choix == "1":
        for nom in restaurants:
            print("-", nom)
    elif choix == "2":
        nom = input("Nom : ").strip()
        if nom in restaurants:
            print("Ce restaurant existe déjà.")
        else:
            restaurants.append(nom)
            print("Restaurant ajouté.")
    elif choix == "3":
        break
    else:
        print("Choix invalide.")