import random

# Simulation de données GetYourGuide (à remplacer par une API réelle)
def obtenir_activites_getyourguide(budget, activites_supplementaires=None):
    activites = {
        "faible": [
            {"nom": "Promenade sur les quais de Seine", "prix": 0, "duree": 120},
            {"nom": "Visite du Sacré-Cœur", "prix": 0, "duree": 90},
            {"nom": "Flânerie dans le quartier Latin", "prix": 0, "duree": 120},
            {"nom": "Exploration du Marché des Enfants Rouges", "prix": 0, "duree": 90},
            {"nom": "Pique-nique au Jardin du Luxembourg", "prix": 0, "duree": 120},
            {"nom": "Balade sur la Coulée verte René-Dumont", "prix": 0, "duree": 150},
            {"nom": "Visite du Parc des Buttes-Chaumont", "prix": 0, "duree": 120},
            {"nom": "Découverte des passages couverts", "prix": 0, "duree": 120},
            {"nom": "Promenade au Canal Saint-Martin", "prix": 0, "duree": 120},
            {"nom": "Balade au cimetière du Père-Lachaise", "prix": 0, "duree": 120},
        ],
        "moyen": [
            {"nom": "Billet coupe-file Musée du Louvre", "prix": 17, "duree": 180},
            {"nom": "Tour Eiffel : billet sommet", "prix": 26, "duree": 120},
            {"nom": "Croisière sur la Seine", "prix": 15, "duree": 60},
            {"nom": "Visite guidée du Musée d'Orsay", "prix": 16, "duree": 120},
            {"nom": "Atelier de fabrication de macarons", "prix": 45, "duree": 150},
            {"nom": "Visite des Catacombes de Paris", "prix": 29, "duree": 90},
            {"nom": "Dégustation de vins et fromages", "prix": 55, "duree": 120},
            {"nom": "Visite du Palais Garnier", "prix": 14, "duree": 90},
            {"nom": "Balade à vélo dans Paris", "prix": 30, "duree": 180},
            {"nom": "Visite du Musée Rodin", "prix": 12, "duree": 120},
        ],
        "élevé": [
            {"nom": "Visite guidée privée du Louvre", "prix": 250, "duree": 180},
            {"nom": "Dîner-croisière de luxe", "prix": 150, "duree": 180},
            {"nom": "Spectacle Moulin Rouge (avec champagne)", "prix": 120, "duree": 120},
            {"nom": "Cours de cuisine gastronomique", "prix": 180, "duree": 180},
            {"nom": "Excursion en montgolfière au-dessus de Paris", "prix": 300, "duree": 120},
            {"nom": "Séance photo privée à Paris", "prix": 200, "duree": 120},
            {"nom": "Visite en hélicoptère de Paris", "prix": 400, "duree": 60},
            {"nom": "Dégustation de champagne dans une cave", "prix": 100, "duree": 120},
            {"nom": "Shopping privé dans les boutiques de luxe", "prix": 200, "duree": 180},
            {"nom": "Visite du Château de Versailles avec guide privé", "prix": 280, "duree": 240},
        ],
    }
 
    # Ajout des activités supplémentaires
    if activites_supplementaires:
        activites[budget].extend(activites_supplementaires)  

    return activites[budget]

def obtenir_restaurants(budget):
    restaurants = {
        "faible": [
            {"nom": "Crêperie Genia", "type": "Crêperie"},
            {"nom": "Le Bouillon Chartier", "type": "Bistrot"},
            {"nom": "Five Guys", "type": "Burger"},
            {"nom": "L'As du Fallafel", "type": "Cuisine du Moyen-Orient"},
            {"nom": "La Droguerie", "type": "Sandwicherie"},
            {"nom": "Le Petit Marcel", "type": "Bistrot"},
            {"nom": "Breizh Café", "type": "Crêperie"},
            {"nom": "Le Relais de l'Entrecôte", "type": "Steakhouse"},
            {"nom": "Pizzeria Popolare", "type": "Pizzeria"},
            {"nom": "La Crémaillère 1900", "type": "Bistrot"},
        ],
        "moyen": [
            {"nom": "Le Petit Marché", "type": "Brasserie"},
            {"nom": "L'Arpège", "type": "Gastronomique"},
            {"nom": "La Coupole", "type": "Brasserie"},
            {"nom": "Le Comptoir du Relais", "type": "Bistrot"},
            {"nom": "Les Cocottes de Christian Constant", "type": "Bistrot"},
            {"nom": "Le Chateaubriand", "type": "Gastronomique"},
            {"nom": "Septime", "type": "Gastronomique"},
            {"nom": "Frenchie", "type": "Gastronomique"},
            {"nom": "Le Jules Verne", "type": "Gastronomique"},
            {"nom": "Guy Savoy", "type": "Gastronomique"},
        ],
        "élevé": [
            {"nom": "L'Ambroisie", "type": "Gastronomique"},
            {"nom": "Le Jules Verne", "type": "Gastronomique"},
            {"nom": "Guy Savoy", "type": "Gastronomique"},
            {"nom": "Pierre Gagnaire", "type": "Gastronomique"},
            {"nom": "Alain Ducasse au Plaza Athénée", "type": "Gastronomique"},
            {"nom": "Epicure", "type": "Gastronomique"},
            {"nom": "Le Cinq", "type": "Gastronomique"},
            {"nom": "L'Astrance", "type": "Gastronomique"},
            {"nom": "Yam'Tcha", "type": "Gastronomique"},
            {"nom": "Kei", "type": "Gastronomique"},
        ],
    }
    return restaurants[budget]

def obtenir_activites_nocturnes(budget):
    activites_nocturnes = {
        "faible": [
            {"nom": "Promenade nocturne sur les Champs-Élysées", "prix": 0, "duree": 120},
            {"nom": "Concert dans un bar de jazz", "prix": 10, "duree": 120},
            {"nom": "Cinéma en plein air", "prix": 12, "duree": 120},
            {"nom": "Soirée dans un bar étudiant", "prix": 8, "duree": 180},
            {"nom": "Balade le long du Canal Saint-Martin", "prix": 0, "duree": 120},
            {"nom": "Visite nocturne du Quartier Latin", "prix": 0, "duree": 120},
            {"nom": "Dégustation de bières artisanales", "prix": 15, "duree": 120},
            {"nom": "Spectacle de rue", "prix": 0, "duree": 60},
            {"nom": "Soirée jeux de société dans un café", "prix": 5, "duree": 120},
            {"nom": "Karaoké dans un bar", "prix": 7, "duree": 180},
        ],
        "moyen": [
            {"nom": "Spectacle de cabaret", "prix": 50, "duree": 120},
            {"nom": "Dégustation de vins", "prix": 40, "duree": 120},
            {"nom": "Visite nocturne d'un musée", "prix": 25, "duree": 120},
            {"nom": "Dîner-spectacle", "prix": 80, "duree": 180},
            {"nom": "Soirée dans un club de jazz", "prix": 35, "duree": 120},
            {"nom": "Balade en bateau-mouche", "prix": 20, "duree": 60},
            {"nom": "Visite guidée nocturne de Paris", "prix": 30, "duree": 120},
            {"nom": "Soirée dans un bar à cocktails", "prix": 45, "duree": 120},
            {"nom": "Concert dans une salle de spectacle", "prix": 60, "duree": 120},
            {"nom": "Match de football au Parc des Princes", "prix": 70, "duree": 120},
        ],
        "élevé": [
            {"nom": "Opéra à l'Opéra Garnier", "prix": 150, "duree": 180},
            {"nom": "Dîner gastronomique avec vue", "prix": 200, "duree": 180},
            {"nom": "Soirée privée dans un club exclusif", "prix": 300, "duree": 180},
            {"nom": "Spectacle au Lido", "prix": 180, "duree": 120},
            {"nom": "Soirée dans un bar à champagne", "prix": 120, "duree": 120},
            {"nom": "Dégustation de grands crus", "prix": 250, "duree": 120},
            {"nom": "Ballet à l'Opéra Bastille", "prix": 160, "duree": 120},
            {"nom": "Soirée dans un club de jazz privé", "prix": 220, "duree": 120},
            {"nom": "Concert dans une salle de spectacle prestigieuse", "prix": 280, "duree": 120},
            {"nom": "Match de football VIP au Parc des Princes", "prix": 350, "duree": 120},
        ],
    }
    return activites_nocturnes[budget]

def creer_itineraire(budget, duree, lieu_depart=None, activites_supplementaires=None, jours_visites=None):
    activites = obtenir_activites_getyourguide(budget, activites_supplementaires)
    restaurants = obtenir_restaurants(budget)
    activites_nocturnes = obtenir_activites_nocturnes(budget)

    # Ajout des lieux spécifiés par l'utilisateur à la liste des activités
    if activites_supplementaires:
        for lieu in activites_supplementaires:
            
            activites.append({"nom": f"Visite de {lieu}", "prix": 0, "duree": 0})

    itineraires = []
    activites_utilisees = []
    activites_nocturnes_utilisees = []

    for jour in range(duree):
        #activite_supplementaire = {"nom": f"Visite de {lieu}", "prix": 0, "duree": 0} Ajout des lieux spécifiés par l'utilisateur à la liste des activités du jour
        if activites_supplementaires and jours_visites and (jour + 1) in jours_visites:
            for lieu in activites_supplementaires:
                act = {"nom": f"Visite de {lieu}", "prix": 0, "duree": 0} 
                #activite_supplementaire = act
                activites.append(act)

        activites_disponibles = [a for a in activites if a not in activites_utilisees]
        if not activites_disponibles:
            activites_utilisees = []
            activites_disponibles = [a for a in activites if a not in activites_utilisees]

        # Sélection des activités du matin en respectant la limite de 3 heures
        matin = []
        duree_matin = 0
        while duree_matin < 180 and activites_disponibles:
            activite_candidate = random.choice(activites_disponibles)
            if duree_matin + activite_candidate['duree'] <= 180:
                matin.append(activite_candidate)
                duree_matin += activite_candidate['duree']
                activites_disponibles.remove(activite_candidate)
                activites_utilisees.append(activite_candidate)
            else:
                break
        if not matin:
            matin.append(random.choice(activites_disponibles))
            activites_utilisees.append(matin[0])

        midi = random.choice(restaurants)

        activites_disponibles = [a for a in activites if a not in activites_utilisees]
        if not activites_disponibles:
            activites_utilisees = []
            activites_disponibles = [a for a in activites if a not in activites_utilisees]

        # Sélection des activités de l'après-midi en respectant la limite de 5h30
        apres_midi = []
        duree_apres_midi = 0
        while duree_apres_midi < 330 and activites_disponibles:
            activite_candidate = random.choice(activites_disponibles)
            if duree_apres_midi + activite_candidate['duree'] <= 330:
                apres_midi.append(activite_candidate)
                duree_apres_midi += activite_candidate['duree']
                activites_disponibles.remove(activite_candidate)
                activites_utilisees.append(activite_candidate)
            else:
                break
        if not apres_midi:
            apres_midi.append(random.choice(activites_disponibles))
            activites_utilisees.append(apres_midi[0])

        activites_nocturnes_disponibles = [a for a in activites_nocturnes if a not in activites_nocturnes_utilisees]
        if not activites_nocturnes_disponibles:
            activites_nocturnes_utilisees = []
            activites_nocturnes_disponibles = [a for a in activites_nocturnes if a not in activites_nocturnes_utilisees]

        soir = random.choice(activites_nocturnes_disponibles)
        activites_nocturnes_utilisees.append(soir)

        jour_itineraire = {
            "jour": jour + 1,
            "matin": matin,
            "midi": midi,
            "apres_midi": apres_midi,
            "soir": soir,
        }
        itineraires.append(jour_itineraire)
    return itineraires

        
def afficher_itineraire(itineraires, lieu_depart=None):
    if lieu_depart:
        print(f"Itinéraire depuis {lieu_depart}:")
    else:
        print("Pas de lieu de départ indiqué")
        
    for jour in itineraires:
        prix_total_jour = sum(a['prix'] for a in jour['matin']) + sum(a['prix'] for a in jour['apres_midi']) + jour['soir']['prix']
        duree_totale_jour = sum(a['duree'] for a in jour['matin']) + sum(a['duree'] for a in jour['apres_midi']) + jour['soir']['duree']

        heures = duree_totale_jour // 60
        minutes = duree_totale_jour % 60

        print(f"Jour {jour['jour']}:")
        if lieu_depart != "": 
            print(f"Départ {lieu_depart}:")
        print(f"  9h00-12h00 : {', '.join([a['nom'] + f' (Prix : {a['prix']}€, Durée : {a['duree']} minutes)' for a in jour['matin']])}")
        print(f"  12h00-13h30 : {jour['midi']['nom']} ({jour['midi']['type']})")
        print(f"  13h30-19h00 : {', '.join([a['nom'] + f' (Prix : {a['prix']}€, Durée : {a['duree']} minutes)' for a in jour['apres_midi']])}")
        print(f"  19h30-23h00 : {jour['soir']['nom']} (Prix : {jour['soir']['prix']}€, Durée : {jour['soir']['duree']} minutes)")
        print(f"  Prix total de la journée (hors repas) : {prix_total_jour}€")
        if minutes == 0:
            print(f"  Durée totale des activités : {heures} heures")
        else:
            print(f"  Durée totale des activités : {heures} heures et {minutes} minutes")
            
        print("-" * 20)        

# Exemple d'utilisation
ville = input("Quel est votre ville à découvrir ? ")
lieu_depart = input("Quel est votre lieu de départ ? (laisser vide si inconnu) ")
budget = input("Quel est votre budget (faible, moyen, élevé) ? ")
duree = int(input("Combien de jours dure votre séjour ? "))

# Demande des activités supplémentaires
activites_supplementaires_input = input("Quelles activités supplémentaires souhaitez-vous ajouter ? (séparées par une virgule, laisser vide si aucune) ")
activites_supplementaires = [{"nom": activite.strip(), "prix": 0, "duree": 0} for activite in activites_supplementaires_input.split(',')] if activites_supplementaires_input else None


jours_visites = input("Quels jours souhaitez-vous visiter ces lieux ? (séparés par une virgule, laisser vide si aucun) ")
jours_visites = [int(jour.strip()) for jour in jours_visites.split(',')] if jours_visites else None


itineraires = creer_itineraire(budget, duree, lieu_depart, activites_supplementaires, jours_visites)
afficher_itineraire(itineraires,lieu_depart)