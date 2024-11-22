import streamlit as st
from utils import (
    add_coach, update_coach, delete_coach,
    add_class, update_class, delete_class,
    registration_history, Cancel_registration,
    course_available
)

st.title("Interface Administrateur")

# Sidebar 
menu = st.sidebar.selectbox(
    "Menu",
    ["Gérer les Coachs", "Gérer les Cours", "Voir les Membres Inscrits", "Annuler une Inscription ou un Cours"]
)
#  Gestion des Coachs
if menu == "Gérer les Coachs":
    st.header("Gestion des Coachs")
    
    # Ajouter un coach
    st.subheader("Ajouter un Coach")
    name = st.text_input("Nom du Coach")
    specialty = st.text_input("Spécialité")
    if st.button("Ajouter le Coach"):
        if name and specialty:
            add_coach(name, specialty)
            st.success(f"Coach {name} ajouté avec succès.")
        else:
            st.error("Veuillez remplir tous les champs.")

    # Modifier un coach
    st.subheader("Modifier un Coach")
    coach_id = st.number_input("ID du Coach à modifier", min_value=1, step=1)
    new_name = st.text_input("Nouveau Nom")
    new_specialty = st.text_input("Nouvelle Spécialité")
    if st.button("Modifier le Coach"):
        if new_name and new_specialty:
            update_coach(coach_id, new_name, new_specialty)
            st.success(f"Coach {coach_id} mis à jour avec succès.")
        else:
            st.error("Veuillez remplir tous les champs.")

    # Supprimer un coach
    st.subheader("Supprimer un Coach")
    delete_coach_id = st.number_input("ID du Coach à supprimer", min_value=1, step=1)
    if st.button("Supprimer le Coach"):
        delete_coach(delete_coach_id)
        st.success(f"Coach {delete_coach_id} supprimé.")

#  Gestion des Cours
if menu == "Gérer les Cours":
    st.header("Gestion des Cours")
    
    # Ajouter un cours
    st.subheader("Ajouter un Cours")
    course_name = st.text_input("Nom du Cours")
    hours = st.number_input("Horaire", min_value=0, max_value=16, step=1)
    max_capacity = st.number_input("Capacité Maximale", min_value=1, step=1)
    coach_id = st.number_input("ID du Coach Responsable", min_value=1, step=1)
    if st.button("Ajouter le Cours"):
        add_class(course_id, course_name, hours, max_capacity, coach_id)
        st.success(f"Cours {course_name} ajouté avec succès.")

      # Modifier un cours
    st.subheader("Modifier un Cours")
    update_course_id = st.number_input("ID du Cours à Modifier", min_value=1, step=1)
    new_course_name = st.text_input("Nouveau Nom du Cours")
    new_hours = st.number_input("Nouvel Horaire", min_value=0, max_value=16, step=1)
    new_capacity = st.number_input("Nouvelle Capacité", min_value=1, step=1)
    new_coach_id = st.number_input("Nouveau ID Coach Responsable", min_value=1, step=1)
    if st.button("Modifier le Cours"):
        update_class(update_course_id, new_course_name, new_hours, new_capacity, new_coach_id)
        st.success(f"Cours {update_course_id} mis à jour avec succès.")
    # else:
    #     st.error("Veuillez remplir tous les champs.")

    # Supprimer un cours
    st.subheader("Supprimer un Cours")
    delete_course_id = st.number_input("ID du Cours à supprimer", min_value=1, step=1)
    if st.button("Supprimer le Cours"):
        delete_coach(delete_course_id)
        st.success(f"Cours {delete_course_id} supprimé.")


# Voir les Membres Inscrits
# elif menu == "Voir les Membres Inscrits":
#     st.header("Membres Inscrits")
    
#     course_id = st.number_input("ID du Cours pour voir les Membres", min_value=1, step=1)
#     if st.button("Voir les Membres"):
#         history = registration_history()
#         members_in_course = [entry for entry in history if entry["course_id"] == course_id]
#         if members_in_course:
#             for member in members_in_course:
#                 st.write(f"ID Membre: {member['member_id']}, Date d'Inscription: {member['date_inscription']}")
#         else:
#             st.write("Aucun membre inscrit à ce cours.")

elif menu == "Voir les Membres Inscrits":
    st.header("Membres Inscrits")
    
    # Entrée pour l'ID du cours
    course_id = st.number_input("ID du Cours pour voir les Membres", min_value=1, step=1)
    
    if st.button("Voir les Membres"):
        try:
            # Récupération de l'historique des inscriptions
            history = registration_history()
            
            # Validation des données : vérifier que `history` est une liste de dictionnaires
            if isinstance(history, list) and all(isinstance(entry, dict) for entry in history):
                # Filtrer les membres inscrits pour le cours demandé
                members_in_course = [entry for entry in history if entry.get("course_id") == course_id]
                
                if members_in_course:
                    st.write("Membres inscrits à ce cours :")
                    for member in members_in_course:
                        st.write(f"ID Membre: {member.get('member_id')}, Date d'Inscription: {member.get('date_inscription')}")
                else:
                    st.write("Aucun membre inscrit à ce cours.")
            else:
                st.error("Les données des inscriptions ne sont pas valides. Veuillez vérifier.")
        except Exception as e:
            st.error(f"Une erreur s'est produite : {str(e)}")

# Annuler une Inscription ou un Cours
elif menu == "Annuler une Inscription ou un Cours":
    st.header("Annulation")

    # Annuler une inscription
    st.subheader("Annuler une Inscription")
    inscription_id = st.number_input("ID de l'Inscription à Annuler", min_value=1, step=1)
    if st.button("Annuler l'Inscription"):
        try:
            Cancel_registration(inscription_id)
            st.success("Inscription annulée avec succès.")
        except Exception as e:
            st.error(f"Erreur : {e}")

    # Annuler un cours
    st.subheader("Annuler un Cours")
    delete_course_id = st.number_input("ID du Cours à Annuler", min_value=1, step=1)
    if st.button("Annuler le Cours"):
        delete_class(delete_course_id)
        st.success(f"Cours {delete_course_id} annulé avec succès.")




