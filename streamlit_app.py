import streamlit as st
import random

st.title("study with you")

if st.button("let's study!!"):
    results = ["15minutes","30minutes","1hour","1.5hours","2hours","break time(~15minutes)"]
    result = random.choice(results)
    st.write(f"結果:{result}")