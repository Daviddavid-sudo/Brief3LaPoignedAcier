import streamlit as st
from utils import *

st.title("Interface Administrateur")

# Sidebar 
menu = st.sidebar.selectbox(
    "Menu",
    ["Modifier The Coaches", "Modifier Classes", "Members subscribed", "Cancel Inscription or Class"]
)
#  Gestion des Coachs
if menu == "Modifier The Coaches":
    st.header("Coaches")
    d = Coach_dataframe()
    st.table(d)
    # Ajouter un coach
    st.subheader("Add Coach")
    name = st.text_input("Coach name")
    specialty = st.text_input("Specality")
    if st.button("Add Coach"):
        if name and specialty:
            add_coach(name, specialty)
            st.success(f"Coach {name} added.")
        else:
            st.error("Please enter all neccessary information.")

    # Modifier un coach
    st.subheader("Modifier Coach")
    coach_id = st.number_input("ID du Coach à modifier", min_value=1, step=1)
    new_name = st.text_input("New name")
    new_specialty = st.text_input("New Speciality")
    if st.button("Modifier Coach"):
        if new_name and new_specialty:
            update_coach(coach_id, new_name, new_specialty)
            st.success(f"Coach {coach_id} updated.")
        else:
            st.error("Please enter all neccessary information.")

    # Supprimer un coach
    st.subheader("Delete Coach")
    delete_coach_id = st.number_input("Coach id deleted", min_value=1, step=1)
    if st.button("Delete Coach"):
        r = delete_coach(delete_coach_id)
        if r == "No coach":
            st.error("No coach with this id")
        else:
            st.success(f"Coach {delete_coach_id} deleted.")

#  Gestion des Cours
if menu == "Modifier Classes":
    st.header("Classes")
    k = Class_dataframe()
    st.table(k)
    st.header("Modifier Classes")
    
    # Ajouter un cours
    st.subheader("Add Class")
    course_name = st.selectbox(
    "Choose a sport",
    ("","Boxe", "Yoga", "Musculation", "Crossfit"),
)
    if course_name != "":
        hours = st.number_input("Time", min_value=9, max_value=16, step=1)
        max_capacity = st.number_input("Max capacity", min_value=1, step=1)
        coach_id = st.number_input("Coachid", min_value=1, step=1)
        if st.button("Add Class"):
            t = add_class(name=course_name, hours=hours, max_capacity=max_capacity, coach_id=coach_id)
            if t == "not possible":
                st.error("Not possible")
            else:
                st.success(f"{course_name} class added.")

      # Modifier un cours
    st.subheader("Modifier Class")
    update_course_id = st.number_input("Class id modified", min_value=1, step=1)
    new_course_name = st.text_input("New sport")
    new_hours = st.number_input("New Time", min_value=9, max_value=16, step=1)
    new_capacity = st.number_input("New Max Capacity", min_value=1, step=1)
    new_coach_id = st.number_input("NNew Coach id", min_value=1, step=1)
    if st.button("Modifier Class"):
        q = update_class(update_course_id, new_course_name, new_hours, new_capacity, new_coach_id)
        if q == "not possible":
                st.error("Not possible")
        else:
            st.success(f"{course_name} class modified.")


    # Supprimer un cours
    st.subheader("Delete Class")
    delete_course_id = st.number_input("Classid to delete", min_value=1, step=1)
    if st.button("Delete Class"):
        z = delete_class(delete_course_id)
        if z == "No class":
            st.error("No class with this id exist")
        else:
            st.success(f"{delete_course_id} class deleted.")



elif menu == "Members subscribed":
    st.header("Members subscribed")
    course_id = st.number_input("Course id", min_value=1, step=1)
    if st.button("See members subscribed"):
        df = registration_history()
        df = df["member_id"][df["cours_id"] == course_id]
        st.table(df)
        


# Annuler une Inscription ou un Cours
elif menu == "Cancel Inscription or Class":
    st.header("Cancel Inscription or Class")

    # Annuler une inscription
    st.subheader("Cancel Inscription")
    inscription_id = st.number_input("ID of Inscription", min_value=1, step=1)
    if st.button("Cancel Inscription"):
        p = Cancel_registration(inscription_id)
        if p:
            st.success("Inscription canceled.")
        else:
            st.error("Inscription does not exist")

    # Annuler un cours
    st.subheader("Class Cancel")
    delete_course_id = st.number_input("Course id", min_value=1, step=1)
    if st.button("Cancel Class"):
        delete_class(delete_course_id)
        st.success(f"{delete_course_id} class canceled.")




