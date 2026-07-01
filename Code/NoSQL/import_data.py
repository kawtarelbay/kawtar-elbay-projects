import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import os

# 1. Chemin vers  fichier CSV
csv_file = "car_rental_data.csv"  

# 2. Vérifier que le fichier existe
if not os.path.exists(csv_file):
    print(f"Fichier {csv_file} introuvable !")
    exit()

# 3. Lire le CSV avec pandas
df = pd.read_csv(csv_file)
print(f"{len(df)} lignes chargées")

# 4. Initialiser Firebase avec la clé de service
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# 5. Connexion à Firestore
db = firestore.client()

# 6. Nom de la collection dans Firestore
collection_name = "car_rentals"

# 7. Importer chaque ligne comme un document
count = 0
for index, row in df.iterrows():
    # Convertir la ligne en dictionnaire
    doc_data = row.to_dict()
    
    # Nettoyer les valeurs NaN (remplacer par None)
    for key, value in doc_data.items():
        if pd.isna(value):
            doc_data[key] = None
    
    # Ajouter un ID unique (optionnel)
    doc_id = f"rental_{index+1}"
    
    # Ajouter le document à Firestore
    db.collection(collection_name).document(doc_id).set(doc_data)
    count += 1
    if count % 100 == 0:
        print(f"{count} documents importés...")

print(f" Import terminé ! {count} documents dans la collection '{collection_name}'")