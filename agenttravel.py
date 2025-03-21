import random

# Simulation de données GetYourGuide (à remplacer par une API réelle)
def obtenir_activites_getyourguide(budget):
    activites = {
        "faible": [
            {"nom": "Promenade sur les quais de Seine", "prix": 0},
            {"nom": "Visite du Sacré-Cœur", "prix": 0},
            {"nom": "Flânerie dans le quartier Latin", "prix": 0},
        ],
        "moyen": [
            {"nom": "Billet coupe-file Musée du Louvre", "prix": 17},
            {"nom": "Tour Eiffel : billet sommet", "prix": 26},
            {"nom": "Croisière sur la Seine", "prix": 15},
        ],
        "élevé": [
            {"nom": "Visite guidée Musée d'Orsay", "prix": 30},
            {"nom": "Dîner-croisière de luxe", "prix": 150},
            {"nom": "Spectacle Moulin Rouge (avec champagne)", "prix": 120},
        ],
    }
    return activites[budget]

# Simulation de données de restaurants (à remplacer par une API réelle)
def obtenir_restaurants(budget):
    restaurants = {
        "faible": [
            {"nom": "Crêperie Genia", "type": "Crêperie"},
            {"nom": "Le Bouillon Chartier", "type": "Bistrot"},
            {"nom": "Five Guys", "type": "Burger"},
        ],
        "moyen": [
            {"nom": "Le Petit Marché", "type": "Brasserie"},
            {"nom": "L'Arpège", "type": "Gastronomique"},
            {"nom": "La Coupole", "type": "Brasserie"},
        ],
        "élevé": [
            {"nom": "L'Ambroisie", "type": "Gastronomique"},
            {"nom": "Le Jules Verne", "type": "Gastronomique"},
            {"nom": "Guy Savoy", "type": "Gastronomique"},
        ],
    }
    return restaurants[budget]

def creer_itineraire_paris(budget, duree):
    activites = obtenir_activites_getyourguide(budget)
    restaurants = obtenir_restaurants(budget)

    itineraires = []
    for jour in range(duree):
        jour_itineraire = {
            "jour": jour + 1,
            "activites": random.sample(activites, min(3, len(activites))),
            "restaurants": random.sample(restaurants, 2),
        }
        itineraires.append(jour_itineraire)

    return itineraires

def afficher_itineraire(itineraires):
    for jour in itineraires:
        print(f"Jour {jour['jour']}:")
        print("  Activités :")
        for activite in jour["activites"]:
            print(f"    - {activite['nom']} (Prix : {activite['prix']}€)")
        print("  Restaurants :")
        for restaurant in jour["restaurants"]:
            print(f"    - {restaurant['nom']} ({restaurant['type']})")
        print("-" * 20)

# Exemple d'utilisation
budget = input("Quel est votre budget (faible, moyen, élevé) ? ")
duree = int(input("Combien de jours dure votre séjour ? "))

itineraires = creer_itineraire_paris(budget, duree)
afficher_itineraire(itineraires)