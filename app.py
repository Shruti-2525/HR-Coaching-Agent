import streamlit as st
from agent import analyze_consultation

st.title("HR Coaching Intelligence Agent")

st.write("Paste HR consultation transcript below to get AI coaching insights.")

transcript = st.text_area("Consultation Transcript")

if st.button("Analyze Consultation"):
    
    if transcript:
        result = analyze_consultation(transcript)
        
        st.subheader("AI Coaching Insights")
        st.write(result)
        
    else:
        st.warning("Please enter a transcript.")