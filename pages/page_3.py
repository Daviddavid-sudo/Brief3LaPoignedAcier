import streamlit as st
from utils import *

st.sidebar.markdown('See available classes')
st.title('See available classes')

st.table(course_available())