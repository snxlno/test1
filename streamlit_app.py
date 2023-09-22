import streamlit as st
import random

st.title("study with you")

if st.button("let's study !!"):
    results = ["15minutes","30minutes","1hour","1.5hours","2hours","             breaktime !"]
    result = random.choice(results)
    st.write(f"結果:{result}")

    subject = random.choice(["英語", "数学", "プログラミング", "歴史", "地理", "国語", "理科", "社会", "その他"])
    place = random.choice(["自宅", "図書館", "カフェ", "公園", "学校", "その他"])
    st.write(f"結果:{result}")
    st.write(f"勉強する内容:{subject}")
    st.write(f"勉強する場所:{place}")