import streamlit as st
from utils import *

st.sidebar.markdown('Cancel class')
st.title('Cancel class')

t1 = st.text_input("id")
if st.button("cancel inscription"):
    Cancel_registration(t1)
    st.error("Class canceled")