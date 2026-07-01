import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
from datetime import datetime

# Configuration de la page
st.set_page_config(page_title="Location de Voitures - CRUD", layout="wide")
st.title("🚗 Gestion des Locations de Voitures")
st.markdown("---")

# Initialiser Firebase (une seule fois)
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Menu latéral
menu = st.sidebar.radio(
    "📋 Menu Principal",
    ["➕ Ajouter une location", "📋 Liste des locations", "✏️ Modifier", "🗑️ Supprimer"]
)

st.sidebar.markdown("---")
st.sidebar.info("Projet NoSQL - Location de voitures\n\nBase de données : Firestore\nType : Document")

# ==================== CREATE ====================
if menu == "➕ Ajouter une location":
    st.header("➕ Ajouter une nouvelle location")
    
    col1, col2 = st.columns(2)
    
    with col1:
        id_customer = st.text_input("ID Client", placeholder="ex: customer_100")
        id_vehicle = st.text_input("ID Véhicule", placeholder="ex: vehicle_50")
        desc_vehicle = st.text_input("Description du véhicule", placeholder="ex: RENAULT CLIO")
        segment = st.selectbox("Segment", ["mining", "engineering", "agribusiness", "energy", "other"])
    
    with col2:
        purchase_value = st.number_input("Prix d'achat", min_value=0, value=30000)
        selling_value = st.number_input("Prix de vente", min_value=0, value=15000)
        contract_duration = st.number_input("Durée du contrat (mois)", min_value=1, max_value=60, value=12)
    
    if st.button(" Ajouter la location", type="primary"):
        if id_customer and id_vehicle:
            # Compter les documents existants
            docs = db.collection("car_rentals").get()
            new_id = len(docs) + 1
            
            new_rental = {
                "id_customer": id_customer,
                "id_vehicle": id_vehicle,
                "desc_vehicle": desc_vehicle,
                "segment": segment,
                "purchase_value": purchase_value,
                "selling_value": selling_value,
                "contract_duration": contract_duration
            }
            
            db.collection("car_rentals").document(f"rental_{new_id}").set(new_rental)
            st.success(f" Location ajoutée avec succès ! ID: rental_{new_id}")
        else:
            st.error(" Veuillez remplir au moins l'ID Client et l'ID Véhicule")

# ==================== READ ====================
elif menu == "📋 Liste des locations":
    st.header("📋 Liste des locations")
    
    # Recherche
    search = st.text_input("🔍 Rechercher par ID Client", placeholder="ex: customer_1")
    
    # Récupérer les données
    docs = db.collection("car_rentals").get()
    
    data = []
    for doc in docs:
        doc_data = doc.to_dict()
        doc_data["id_document"] = doc.id
        data.append(doc_data)
    
    df = pd.DataFrame(data)
    
    if not df.empty:
        if search:
            df = df[df["id_customer"].str.contains(search, case=False, na=False)]
            st.info(f"{len(df)} résultat(s) trouvé(s)")
        
        st.dataframe(df, use_container_width=True)
        
        # Voir un document en détail
        st.markdown("---")
        st.subheader(" Voir un document en détail")
        doc_id = st.selectbox("Choisir un document", df["id_document"].tolist())
        if doc_id:
            doc_ref = db.collection("car_rentals").document(doc_id).get()
            if doc_ref.exists:
                st.json(doc_ref.to_dict())
    else:
        st.warning("Aucune donnée trouvée")

# ==================== UPDATE ====================
elif menu == "✏️ Modifier":
    st.header("✏️ Modifier une location")
    
    # Liste des documents
    docs = db.collection("car_rentals").get()
    doc_ids = [doc.id for doc in docs]
    
    selected_id = st.selectbox("Sélectionner le document à modifier", doc_ids)
    
    if selected_id:
        doc_ref = db.collection("car_rentals").document(selected_id)
        doc_data = doc_ref.get().to_dict()
        
        if doc_data:
            st.subheader(f"Modification de {selected_id}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                new_desc = st.text_input("Description véhicule", value=doc_data.get("desc_vehicle", ""))
                new_segment = st.selectbox("Segment", 
                                           ["mining", "engineering", "agribusiness", "energy", "other"],
                                           index=["mining", "engineering", "agribusiness", "energy", "other"].index(doc_data.get("segment", "other")))
                new_duration = st.number_input("Durée contrat (mois)", value=doc_data.get("contract_duration", 12))
            
            with col2:
                new_purchase = st.number_input("Prix achat", value=doc_data.get("purchase_value", 0))
                new_selling = st.number_input("Prix vente", value=doc_data.get("selling_value", 0))
            
            if st.button("💾 Enregistrer les modifications", type="primary"):
                updates = {
                    "desc_vehicle": new_desc,
                    "segment": new_segment,
                    "contract_duration": new_duration,
                    "purchase_value": new_purchase,
                    "selling_value": new_selling
                }
                doc_ref.update(updates)
                st.success(f"✅ Document {selected_id} modifié avec succès !")
                st.rerun()

# ==================== DELETE ====================
elif menu == "🗑️ Supprimer":
    st.header("🗑️ Supprimer une location")
    
    # Liste des documents
    docs = db.collection("car_rentals").get()
    doc_ids = [doc.id for doc in docs]
    
    selected_id = st.selectbox("Sélectionner le document à supprimer", doc_ids)
    
    if selected_id:
        doc_ref = db.collection("car_rentals").document(selected_id)
        doc_data = doc_ref.get().to_dict()
        
        if doc_data:
            st.warning(f"⚠️ Vous allez supprimer le document : **{selected_id}**")
            st.json(doc_data)
            
            confirm = st.checkbox("✅ Je confirme la suppression")
            
            if confirm and st.button("🗑️ Supprimer définitivement", type="primary"):
                doc_ref.delete()
                st.success(f"✅ Document {selected_id} supprimé avec succès !")
                st.rerun()