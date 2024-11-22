# **La Poigne d'Acier - Application Web**

**Contexte :**  
**La Poigne d’Acier**, la salle de sport emblématique, modernise sa gestion avec une application web interactive. Ce projet vise à améliorer la gestion des coachs, des cours et des inscriptions, tout en offrant une expérience utilisateur fluide pour les membres.

---

## **Fonctionnalités principales**

### **Interface Membre :**
- Consulter les cours disponibles.
- S'inscrire à des cours en fonction des places disponibles.
- Annuler une inscription.
- Consulter l'historique des inscriptions.

### **Interface Administrateur :**
- Ajouter, modifier ou supprimer des coachs et des cours.
- Voir la liste des membres inscrits à chaque cours.
- Annuler une inscription ou un cours.

---

## **Organisation du projet**

### **Structure des fichiers :**

| Fichier/Dossier       | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `main.py`            | Point d'entrée principal de l'application.                                 |
| `pages/app_admin.py` | Interface Streamlit dédiée aux administrateurs.                            |
| `pages/app_membre.py`| Interface Streamlit dédiée aux membres.                                    |
| `model.py`           | Modélisation des données avec SQLModel.                                    |
| `init_db.py`         | Initialisation de la base de données SQLModel et création des tables.       |
| `populate_db.py`     | Script pour insérer des données fictives dans la base de données.           |
| `utils.py`           | Fonctions utilitaires pour la gestion et manipulation des données.          |
| `database.db`        | Base de données générée par SQLModel contenant les informations nécessaires.|
| `requirements.txt`   | Liste des dépendances nécessaires au projet.                               |
| `sports.jpg`         | Image illustrant le projet.                                                |

---

## **Technologies utilisées**

1. **Base de données :**  
   - SQLModel : pour la modélisation et la manipulation de la base de données.
   - Fichier SQLite généré automatiquement avec SQLModel.

2. **Framework Web :**  
   - Streamlit : création d'une application web interactive.

3. **Génération de données :**  
   - Faker : pour la génération de données fictives (membres, coachs, cours, inscriptions).

---

## **Installation et utilisation**

### **Prérequis :**
- Python 3.9 ou supérieur.
- Pip installé.

### **Étapes d'installation :**

1. **Clonez le projet :**
   ```bash
   git clone <URL_DU_REPOSITORY>
   cd <NOM_DU_REPOSITORY>

### **Étapes d'installation :**

1. **Installez les dépendances :**
   ```bash
   pip install -r requirements.txt

2. **Initialisez la base de données :**
    ```bash
   python init_db.py

3. **Ajoutez des données fictives :**
    ```bash
    python populate_db.py

4. **Lancez l'application :**
    ```bash
    streamlit run main.py


## **Roadmap du développement**

### **Phase 1 : Modélisation des données**
- Création du schéma relationnel avec SQLModel.
- Initialisation et population de la base de données.

### **Phase 2 : Développement des interfaces**
- **Interface membre** :
  - Gestion des inscriptions et des participations.
  - Consultation de l’historique.
- **Interface administrateur** :
  - Gestion des coachs et des cours.
  - Consultation et annulation des inscriptions.

### **Phase 3 : Tests et démonstration**
- Validation des fonctionnalités développées.
- Préparation et réalisation de la démonstration finale.



## **AUTEURS**

- **Khadija Abdelmalek** 
- **David Scott**

