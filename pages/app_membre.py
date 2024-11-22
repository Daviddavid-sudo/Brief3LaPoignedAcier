import streamlit as st
from utils import *

# Sidebar 
st.title("Interface Member")
menu = st.sidebar.selectbox(
    "Member",
    ["See available classes", "Join a Class", "Cancel Inscription", "Inscription History"]
)

if menu == "See available classes":
    st.sidebar.markdown('See available classes')
    st.title('See available classes')

    st.table(course_available())

if menu == "Join a Class":
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

        # st.table(course_available())

if menu == "Cancel Inscription":
    st.sidebar.markdown('Cancel inscription')
    st.title('Cancel inscription')

    member_id = st.number_input("Enter id", min_value=0, step=1)
    if member_id != 0:
        df = registration_history()
        df = df[["inscriptid", "nom", "horaire"]][df["member_id"] == member_id]
        st.table(df)

        t1 = st.text_input("id")
        if st.button("cancel inscription"):
            txt = Cancel_registration(t1)
            if txt:
                st.warning("Class canceled")
            else:
                st.error("No inscription exist")

if menu == "Inscription History":
    st.sidebar.markdown('History')
    st.title('History')

    st.table(registration_history())