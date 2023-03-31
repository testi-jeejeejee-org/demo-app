import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My App", page_icon=":smiley:", layout="wide", initial_sidebar_state="expanded")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_automation = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_DVSwGQ.json")
lottie_learning = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_DMgKk1.json")
lottie_working = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_iv4dsx3q.json")


with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Hi, I am Evgenii :wave:")
        st.subheader("I am a DevOps Consultant :computer:")
        st.write("I am passionate in helping companies to integrate people, processes, and technology together in order to provide uninterrupted value to their customers :rocket:")
        st.write("Also, I am happy to share my knowledge with people! :smiley:")
    with right_column:
        st_lottie(lottie_working, height=400, width=500, key="working")


with st.container():
    st.write("## What I do :thinking_face:")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Automation 🤖 ")
        st.write("I am a big fan of DevOps culture, and I am always looking for ways to improve the way we work :wrench:")
        st.write("I love to automate 🤖 processes and build reliable CI/CD pipelines :nerd_face:")
        st_lottie(lottie_automation, height=200, width=300, key="automation")
        

    with right_column:
        st.header("Continuous Learning :books:")
        st.write("I am a big fan of continuous learning :books: and I am always looking for ways to improve my skills :nerd_face:")
        st.write("The most recent book I read is [The DevOps Handbook](https://www.amazon.com/DevOps-Handbook-World-Class-Reliability-Organizations/dp/1942788002) :book:")
        st_lottie(lottie_learning, height=200, width=300, key="learning")
    