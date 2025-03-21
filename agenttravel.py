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

# Simulation d'activités nocturnes
def obtenir_activites_nocturnes(budget):
    activites_nocturnes = {
        "faible": ["Promenade nocturne sur les Champs-Élysées", "Concert dans un bar de jazz", "Cinéma en plein air"],
        "moyen": ["Spectacle de cabaret", "Dégustation de vins", "Visite nocturne d'un musée"],
        "élevé": ["Opéra à l'Opéra Garnier", "Dîner gastronomique avec vue", "Soirée privée dans un club exclusif"],
    }
    return activites_nocturnes[budget]

def creer_itineraire_paris(budget, duree):
    activites = obtenir_activites_getyourguide(budget)
    restaurants = obtenir_restaurants(budget)
    activites_nocturnes = obtenir_activites_nocturnes(budget)

    itineraires = []
    for jour in range(duree):
        jour_itineraire = {
            "jour": jour + 1,
            "matin": random.sample(activites, 1)[0],
            "midi": random.sample(restaurants, 1)[0],
            "apres_midi": random.sample(activites, 1)[0],
            "soir": random.sample(activites_nocturnes, 1)[0],
        }
        itineraires.append(jour_itineraire)

    return itineraires

def afficher_itineraire(itineraires):
    for jour in itineraires:
        print(f"Jour {jour['jour']}:")
        print(f"  9h00-12h00 : {jour['matin']['nom']} (Prix : {jour['matin']['prix']}€)")
        print(f"  12h00-13h30 : {jour['midi']['nom']} ({jour['midi']['type']})")
        print(f"  13h30-19h00 : {jour['apres_midi']['nom']} (Prix : {jour['apres_midi']['prix']}€)")
        print(f"  19h30-23h00 : {jour['soir']}")
        print("-" * 20)

# Exemple d'utilisation
budget = input("Quel est votre budget (faible, moyen, élevé) ? ")
duree = int(input("Combien de jours dure votre séjour ? "))

itineraires = creer_itineraire_paris(budget, duree)
afficher_itineraire(itineraires)