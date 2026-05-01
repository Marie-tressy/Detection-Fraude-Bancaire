# Detection-Fraude-Bancaire
Analyse comparative de modèles (Régression Logistique &amp; Random Forest) pour la détection de fraude bancaire sur 284000 transactions
# Détection de Fraude Bancaire - Analyse Comparative

### Objectif du Projet
Développer un système de détection de fraudes par carte bancaire capable de traiter des données massivement déséquilibrées (0,17% de fraudes). 

Ce projet a été réalisé dans le cadre d'un projet personnel pour démontrer ma capacité à manipuler des datasets réels (284 807 transactions) et à optimiser des modèles de Machine Learning.

### Méthodologie Technique
- **Preprocessing** : Normalisation des données (`StandardScaler`).
- **Équilibrage** : Technique de sous-échantillonnage (Under-sampling) pour l'entraînement.
- **Modèles testés** : Régression Logistique vs Random Forest.
- **Optimisation Métier** : Ajustement du seuil de décision à **0.3** pour maximiser le rappel (détection des fraudes).

### Résultats sur le Dataset Entier (Test Ultime)
| Modèle (Seuil 0.3) | Fraudes Capturées (Recall) | Clients Bloqués à tort |
| :--- | :---: | :---: |
| **Régression Logistique** | 93.8% (444/473) | 17 389 |
| **Random Forest** | **98.5% (466/473)** | **24 075** |

### Conclusion de l'Analyse
Le **Random Forest** est le modèle le plus performant pour la sécurité de la banque : il ne laisse passer que **7 fraudes sur 473**. Bien qu'il génère plus de faux positifs, le gain financier lié à la capture de 22 fraudes supplémentaires par rapport à la Régression Logistique justifie son utilisation en production.

## Démo en ligne
Application accessible: https://detection-fraude-bancaire-ycchtcrgduqb6shn85ezzg.streamlit.app/
---
*Projet réalisé en Python avec Scikit-Learn, Pandas et Seaborn.*
