restaurants = ["JP chawama", "Restaurant la lionne", "FSS"]
print(restaurants[0])
restaurants.append("Deux Ass Plus")
for nom in restaurants:
    print(nom)
nouveau = input("Nom du restaurant : ").strip()
if nouveau in restaurants:
    print("Ce restaurant existe déjà.")
else:
    restaurants.append(nom)
print(f"Il y a maintenant {len(restaurants)} restaurants.")