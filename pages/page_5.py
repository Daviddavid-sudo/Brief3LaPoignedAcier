import streamlit as st
from utils import *

st.sidebar.markdown('Join class')
st.title('Join class')

option = st.selectbox(
    "Choose a sport",
    ("","Boxe", "Yoga", "Musculation", "Crossfit"),
)
if option != "":
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
            if st.button("Join class"):
                text = register_course(option_coach, int(option_time), option, int(id_member))
                if text == "no class available":
                    st.error(text)

                elif text =='already subscribed':
                    st.warning(text)

                elif text == "sent":
                    st.success(text)