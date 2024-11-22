import streamlit as st
from utils import *

st.sidebar.markdown('Subscribe to class')
st.title('Subscribe to class')

option = st.selectbox(
    "Which class",
    ("","Boxe", "Yoga", "Musculation", "Crossfit"),
)
if option != "":
    st.write("You selected:", option)
    df = course_available()
    time_avaliable = df["Time"][df["name"] == option]
    times = [""]
    for time in time_avaliable:
        times.append(f"{time}")
    option_time = st.selectbox(
        "Time",
        tuple(times),
    )
    if option_time != "":
        coach_avaliable = df["coach_id"][(df["name"] == option) & (df["Time"] == option_time)]
        coachs = [""]
        for coach in coach_avaliable:
            coachs.append(f"{coach}")
        
        option_coach = st.selectbox(
            "Coach",
            tuple(coachs),
        )
        if option_coach != "":
            option_time = option_time[:-1]
            id_member = st.text_input("id member")
            if st.button("Subscribe to class"):
                text = register_course(option_coach, int(option_time), option, int(id_member))
                if text == "no class available":
                    st.error(text)
                
                elif text == "already another class at this time":
                    st.warning(text)
                
                elif text == "sent":
                    st.success(text)