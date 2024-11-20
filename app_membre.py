import streamlit as st
import utils

st.title('Member Login in')

t1 = st.text_input("Enter id")
st.button("submit")
# Consulter les cours disponibles.
if st.button("See available classes", use_container_width=True):
    results = utils.course_available()
    for result in results:
        st.write(result)
# S'inscrire à un cours (vérification des places restantes et des conflits d'horaires).
if st.button("Subscribe to class", use_container_width=True):
    st.write("call function")
# Annuler une inscription.
if st.button("Cancel inscription", use_container_width=True):
    st.write("cancel inscription")
# Consulter l’historique des inscriptions.
if st.button("History", use_container_width=True):
    st.write("call function")