import streamlit as st
from utils import *
from app_membre import *

st.sidebar.markdown('History')
st.title('History')

st.table(registration_history())