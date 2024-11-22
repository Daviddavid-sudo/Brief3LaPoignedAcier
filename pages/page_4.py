import streamlit as st
from utils import *

st.sidebar.markdown('Cancel inscription')
st.title('Cancel inscription')

t1 = st.text_input("id")
if st.button("cancel inscription"):
    txt = Cancel_registration(t1)
    if txt:
        st.warning("Class canceled")
    else:
        st.error("No inscription exist")
