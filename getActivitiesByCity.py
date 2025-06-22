import requests
import json
import os
from dotenv import load_dotenv

import os
from dotenv import load_dotenv

# Charger les variables du fichier .env
load_dotenv()


# --- Votre Clé API ---
# REMPLACEZ 'VOTRE_CLÉ_API_ICI' PAR VOTRE CLÉ API RÉELLE

api_key = os.environ.get("api_key")
if api_key is None:
    raise ValueError("La variable d'environnement 'api_key' n'est pas définie dans .env ou l'environnement.")



# --- URL de l'endpoint ---
url = "https://places.googleapis.com/v1/places:searchText"

# --- En-têtes de la requête ---
headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": api_key,
    # Spécifiez les champs exacts que vous voulez recevoir.
    # 'displayName' remplace 'name' dans la nouvelle API.
    # 'openingHours' remplace 'opening_hours'.
    "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.types"
}

# --- Corps de la requête (JSON) ---
data = {
    "textQuery": "activites los angeles", # Le texte de votre recherche
    "languageCode": "fr",             # Langue des résultats
    "maxResultCount": 50#,             # Nombre maximum de résultats à retourner
   # "includedTypes": ["museum", "aquarium", "tourist_attraction"] # Filtre par ces types spécifiques
}

try:
    # --- Envoi de la requête POST ---
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status() # Lève une exception pour les codes d'état HTTP d'erreur (4xx ou 5xx)

    # --- Traitement de la réponse JSON ---
    places_data = response.json()
    
    #print(places_data)

    if 'places' in places_data:
        print(f"Activités trouvées à Paris (types : musée, aquarium, attraction touristique) :")
        for place in places_data['places']:
            name = place.get('displayName', {}).get('text', 'N/A')
            address = place.get('formattedAddress', 'N/A')
            types = ', '.join(place.get('types', []))
            # opening_hours est plus complexe car il a un statut (ouvert/fermé) et des périodes
            opening_status = 'N/A'
            if place.get('openingHours'):
                if place['openingHours'].get('openNow') is not None:
                    opening_status = "Ouvert actuellement" if place['openingHours']['openNow'] else "Fermé actuellement"

            print(f"\nNom: {name}")
            print(f"Adresse: {address}")
            print(f"Types: {types}")
            print(f"Statut d'ouverture: {opening_status}")
            print("-" * 30)
    else:
        print("Aucune activité trouvée correspondant à vos critères.")
    
        

except requests.exceptions.HTTPError as err:
    print(f"Erreur HTTP: {err}")
    print(f"Code d'état: {response.status_code}")
    print(f"Réponse d'erreur: {response.text}")
except requests.exceptions.RequestException as err:
    print(f"Erreur de connexion ou de requête: {err}")
except json.JSONDecodeError:
    print(f"Erreur de décodage JSON. Réponse reçue: {response.text}")
except Exception as err:
    print(f"Une erreur inattendue s'est produite: {err}")