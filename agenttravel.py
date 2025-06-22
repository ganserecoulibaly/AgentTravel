import random

# Simulation de données GetYourGuide (à remplacer par une API réelle)
def obtenir_activites_getyourguide(budget, activites_supplementaires=None):
    activites = {
        "faible": [
            {"ville":"paris","nom": "Promenade sur les quais de Seine","budget":"faible", "type_activite": "journee", "prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Visite du Sacré-Cœur", "budget":"faible","type_activite": "journee", "prix": 0, "duree": 90, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Flânerie dans le quartier Latin","budget":"faible", "type_activite": "journee", "prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Exploration du Marché des Enfants Rouges","budget":"faible", "type_activite": "journee", "prix": 0, "duree": 90, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Pique-nique au Jardin du Luxembourg","budget":"faible","type_activite": "journee","prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Balade sur la Coulée verte René-Dumont","budget":"faible","type_activite": "journee", "prix": 0, "duree": 150, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Visite du Parc des Buttes-Chaumont","budget":"faible","type_activite": "journee", "prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Découverte des passages couverts","budget":"faible","type_activite": "journee","prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Promenade au Canal Saint-Martin", "budget":"faible","type_activite": "journee","prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Balade au cimetière du Père-Lachaise", "budget":"faible","type_activite": "journee","prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
        ],
        "moyen": [
            {"ville":"paris","nom": "Billet coupe-file Musée du Louvre", "budget":"moyen","type_activite": "journee","prix": 17, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Tour Eiffel : billet sommet","budget":"moyen","type_activite": "journee", "prix": 26, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Croisière sur la Seine", "budget":"moyen","type_activite": "journee","prix": 15, "duree": 60, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Visite guidée du Musée d'Orsay","budget":"moyen","type_activite": "journee", "prix": 16, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Atelier de fabrication de macarons","budget":"moyen","type_activite": "journee", "prix": 45, "duree": 150, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Visite des Catacombes de Paris", "budget":"moyen","type_activite": "journee","prix": 29, "duree": 90, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Dégustation de vins et fromages", "budget":"moyen","type_activite": "journee","prix": 55, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Visite du Palais Garnier","budget":"moyen","type_activite": "journee", "prix": 14, "duree": 90, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Balade à vélo dans Paris","budget":"moyen","type_activite": "journee", "prix": 30, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Visite du Musée Rodin","budget":"moyen","type_activite": "journee", "prix": 12, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
        ],
        "élevé": [
            {"ville":"paris","nom": "Visite guidée privée du Louvre","budget":"eleve","type_activite": "journee", "prix": 250, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Dîner-croisière de luxe","budget":"eleve","type_activite": "journee", "prix": 150, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Spectacle Moulin Rouge (avec champagne)","budget":"eleve","type_activite": "journee", "prix": 120, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Cours de cuisine gastronomique", "budget":"eleve","type_activite": "journee","prix": 180, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Excursion en montgolfière au-dessus de Paris","budget":"eleve","type_activite": "journee", "prix": 300, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Séance photo privée à Paris", "budget":"eleve","type_activite": "journee","prix": 200, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Visite en hélicoptère de Paris", "budget":"eleve","type_activite": "journee","prix": 400, "duree": 60, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Dégustation de champagne dans une cave","budget":"eleve","type_activite": "journee", "prix": 100, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Shopping privé dans les boutiques de luxe","budget":"eleve","type_activite": "journee", "prix": 200, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Visite du Château de Versailles avec guide privé","budget":"eleve","type_activite": "journee", "prix": 280, "duree": 240, "tarifAdulte":0, "tarifEnfant":0},
        ],
    }
 
    # Ajout des activités supplémentaires
    if activites_supplementaires:
        activites[budget].extend(activites_supplementaires)  

    return activites[budget]

def obtenir_restaurants(budget):
    restaurants = {
        "faible": [
            {"ville":"paris","nom": "Crêperie Genia", "budget":"faible", "type_cuisine": "Crêperie", "duree": 25},
            {"ville":"paris","nom": "Le Bouillon Chartier", "budget":"faible","type_cuisine": "Bistrot", "duree": 45},
            {"ville":"paris","nom": "Five Guys", "budget":"faible","type_cuisine": "Burger", "duree": 25},
            {"ville":"paris","nom": "L'As du Fallafel","budget":"faible", "type_cuisine": "Cuisine du Moyen-Orient", "duree": 25},
            {"ville":"paris","nom": "La Droguerie", "budget":"faible","type_cuisine": "Sandwicherie", "duree": 25},
            {"ville":"paris","nom": "Le Petit Marcel","budget":"faible", "type_cuisine": "Bistrot", "duree": 45},
            {"ville":"paris","nom": "Breizh Café","budget":"faible", "type_cuisine": "Crêperie", "duree": 25},
            {"ville":"paris","nom": "Le Relais de l'Entrecôte","budget":"faible", "type_cuisine": "Steakhouse", "duree": 45},
            {"ville":"paris","nom": "Pizzeria Popolare","budget":"faible", "type_cuisine": "Pizzeria", "duree": 35},
            {"ville":"paris","nom": "La Crémaillère 1900", "budget":"faible","type_cuisine": "Bistrot", "duree": 45},
        ],
        "moyen": [
            {"nom": "Le Petit Marché", "budget":"moyen","type_cuisine": "Brasserie", "duree": 45},
            {"nom": "L'Arpège", "budget":"moyen","type_cuisine": "Gastronomique", "duree": 90},
            {"nom": "La Coupole", "budget":"moyen","type_cuisine": "Brasserie", "duree": 45},
            {"nom": "Le Comptoir du Relais", "budget":"moyen","type_cuisine": "Bistrot", "duree": 45},
            {"nom": "Les Cocottes de Christian Constant", "budget":"moyen","type_cuisine": "Bistrot", "duree": 45},
            {"nom": "Le Chateaubriand","budget":"moyen", "type_cuisine": "Gastronomique", "duree": 90},
            {"nom": "Septime", "budget":"moyen","type_cuisine": "Gastronomique", "duree": 90},
            {"nom": "Frenchie", "budget":"moyen","type_cuisine": "Gastronomique", "duree": 90},
            {"nom": "Le Jules Verne","budget":"moyen", "type_cuisine": "Gastronomique", "duree": 90},
            {"nom": "Guy Savoy", "budget":"moyen","type_cuisine": "Gastronomique", "duree": 90},
        ],
        "élevé": [
            {"ville":"paris","nom": "L'Ambroisie","budget":"eleve", "type_cuisine": "Gastronomique", "duree": 90},
            {"ville":"paris","nom": "Le Jules Verne","budget":"eleve", "type_cuisine": "Gastronomique", "duree": 90},
            {"ville":"paris","nom": "Guy Savoy","budget":"eleve", "type_cuisine": "Gastronomique", "duree": 90},
            {"ville":"paris","nom": "Pierre Gagnaire", "budget":"eleve","type_cuisine": "Gastronomique", "duree": 90},
            {"ville":"paris","nom": "Alain Ducasse au Plaza Athénée","budget":"eleve", "type_cuisine": "Gastronomique", "duree": 90},
            {"ville":"paris","nom": "Epicure", "budget":"eleve","type_cuisine": "Gastronomique", "duree": 90},
            {"ville":"paris","nom": "Le Cinq", "budget":"eleve","type_cuisine": "Gastronomique", "duree": 90},
            {"ville":"paris","nom": "L'Astrance", "budget":"eleve","type_cuisine": "Gastronomique", "duree": 90},
            {"ville":"paris","nom": "Yam'Tcha", "budget":"eleve","type_cuisine": "Gastronomique", "duree": 90},
            {"ville":"paris","nom": "Kei","budget":"eleve","type_cuisine": "Gastronomique", "duree": 90},
        ],
    }
    return restaurants[budget]

def obtenir_activites_nocturnes(budget):
    activites_nocturnes = {
        "faible": [
            {"ville":"paris","nom": "Promenade nocturne sur les Champs-Élysées","type_activite": "soiree", "prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Concert dans un bar de jazz","type_activite": "soiree",  "prix": 10, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Cinéma en plein air","type_activite": "soiree",  "prix": 12, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Soirée dans un bar étudiant", "type_activite": "soiree", "prix": 8, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Balade le long du Canal Saint-Martin","type_activite": "soiree",  "prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Visite nocturne du Quartier Latin", "type_activite": "soiree", "prix": 0, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Dégustation de bières artisanales","type_activite": "soiree",  "prix": 15, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Spectacle de rue","type_activite": "soiree",  "prix": 0, "duree": 60, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Soirée jeux de société dans un café","type_activite": "soiree",  "prix": 5, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Karaoké dans un bar","type_activite": "soiree",  "prix": 7, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
        ],
        "moyen": [
            {"ville":"paris","nom": "Spectacle de cabaret","type_activite": "soiree",  "prix": 50, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Dégustation de vins", "type_activite": "soiree", "prix": 40, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Visite nocturne d'un musée","type_activite": "soiree",  "prix": 25, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Dîner-spectacle","type_activite": "soiree",  "prix": 80, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Soirée dans un club de jazz","type_activite": "soiree",  "prix": 35, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Balade en bateau-mouche","type_activite": "soiree",  "prix": 20, "duree": 60, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Visite guidée nocturne de Paris","type_activite": "soiree",  "prix": 30, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Soirée dans un bar à cocktails","type_activite": "soiree",  "prix": 45, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Concert dans une salle de spectacle","type_activite": "soiree",  "prix": 60, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Match de football au Parc des Princes","type_activite": "soiree",  "prix": 70, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
        ],
        "élevé": [
            {"ville":"paris","nom": "Opéra à l'Opéra Garnier", "type_activite": "soiree", "prix": 150, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Dîner gastronomique avec vue","type_activite": "soiree",  "prix": 200, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Soirée privée dans un club exclusif","type_activite": "soiree",  "prix": 300, "duree": 180, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Spectacle au Lido","type_activite": "soiree",  "prix": 180, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Soirée dans un bar à champagne","type_activite": "soiree",  "prix": 120, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Dégustation de grands crus","type_activite": "soiree",  "prix": 250, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Ballet à l'Opéra Bastille", "type_activite": "soiree", "prix": 160, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Soirée dans un club de jazz privé","type_activite": "soiree",  "prix": 220, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Concert dans une salle de spectacle prestigieuse","type_activite": "soiree",  "prix": 280, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
            {"ville":"paris","nom": "Match de football VIP au Parc des Princes","type_activite": "soiree",  "prix": 350, "duree": 120, "tarifAdulte":0, "tarifEnfant":0},
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
        minutes = (duree_totale_jour - heures * 60) % 60

        print(f"Jour {jour['jour']}:")
        if lieu_depart != "": 
            print(f"Départ {lieu_depart}:")
        print(f"9h00-12h00 : {', '.join([a['nom'] + f' Durée : {a['duree']} minutes \n'
             +f'  Prix : {a['prix']}€\n'  
             +f'  Prix Adulte: {a['tarifAdulte']}€\nPrix Enfant : {a['tarifEnfant']}€\n ' for a in jour['matin']])}")
        
        print(f"12h00-13h30 : {jour['midi']['nom']} ({jour['midi']['type']})")
        
                
        print(f"13h30-19h00 : {''.join([a['nom'] + f' Durée : {a['duree']} minutes \n'
             +f'  Prix : {a['prix']}€\n'  
             +f'  Prix Adulte: {a['tarifAdulte']}€\n  Prix Enfant : {a['tarifEnfant']}€\n\n' for a in jour['apres_midi']])}")
        
        print(f"19h30-23h00 : {jour['soir']['nom']} (Prix : {jour['soir']['prix']}€  Durée : {jour['soir']['duree']} minutes)\n")
        print(f"Prix total de la journée (hors repas) : {prix_total_jour}€")
        if minutes == 0:
            print(f"Durée totale des activités : {heures} heures")
        else:
            print(f"Durée totale des activités : {heures} heures et {minutes} minutes")
            
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