import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Configuration de la page
st.set_page_config(page_title="Simulateur de Fraude Bancaire", layout="wide")

st.title("Simulateur de Détection de Fraude")
st.write("Ajustez le seuil de décision pour voir l'impact sur la sécurité bancaire.")

# Barre latérale pour le réglage
st.sidebar.header("Paramètres du Modèle")
seuil = st.sidebar.slider("Seuil de détection", 0.0, 1.0, 0.3, 0.05)

st.subheader(f"Résultats pour un seuil de {seuil}")
fraudes_detectees = 0
faux_positifs = 0

# Simulation simplifiée basée sur les performances Random Forest
# On affiche la matrice de confusion en fonction du curseur
if seuil <= 0.3:
    fraudes_detectees=466
    faux_positifs=24075
else:
    fraudes_detectees = 420
    faux_positifs = 5000

col1, col2 = st.columns(2)

with col1:
    st.metric("Fraudes détectées", f"{fraudes_detectees} / 473", delta=f"{fraudes_detectees-444} vs LogReg")
    st.metric("Clients bloqués (Faux Positifs)", faux_positifs, delta=f"{faux_positifs-17389}", delta_color="inverse")

with col2:
    # Dessin de la matrice
    fig, ax = plt.subplots()
    # On crée une matrice fictive pour l'exemple visuel
    cm = [[250000, faux_positifs], [473-fraudes_detectees, fraudes_detectees]]
    sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', ax=ax)
    plt.xlabel('Prédiction')
    plt.ylabel('Réalité')
    st.pyplot(fig)

st.info("Plus le seuil est bas, plus on attrape de fraudeurs, mais plus on bloque de clients honnêtes.")