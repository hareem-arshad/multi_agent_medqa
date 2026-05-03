# app.py

import streamlit as st
from pipeline import run_pipeline

st.title("🤖 Multi-Agent Clinical Reasoning System")

st.write("Solver → Critic → Refiner with evaluation")

question = st.text_area("Enter Medical Question")

if st.button("Run System"):

    initial, feedback, final = run_pipeline(question)

    st.subheader("🔵 Initial Answer (Solver)")
    st.write(initial)

    st.subheader("🟡 Critic Feedback")
    st.write(feedback)

    st.subheader("🟢 Final Improved Answer")
    st.write(final)