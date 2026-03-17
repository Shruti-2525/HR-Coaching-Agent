import streamlit as st
from agent import analyze_consultation

st.markdown("""
<style>
    .stMetric {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Page config
st.set_page_config(page_title="HR Coaching Dashboard", layout="wide")

# Title
st.title("🧠 HR Coaching Intelligence Dashboard")
st.markdown("Analyze HR consultations and get AI-powered coaching insights.")

# Input section
st.subheader("📄 Enter Consultation Transcript")
transcript = st.text_area("Paste transcript here...", height=200)

# Analyze button
if st.button("🔍 Analyze Consultation"):

    if transcript:

        result = analyze_consultation(transcript)

        # Extract score (simple parsing)
        score = "N/A"
        for line in result.split("\n"):
            if "Score" in line:
                score = line.split(":")[-1].strip()

        # Dashboard layout
        st.markdown("---")

        col1, col2 = st.columns([1, 2])

        # LEFT SIDE → SCORE CARD
        with col1:
            st.markdown("### 📊 Performance Score")
            st.metric(label="Consultation Score", value=score)

        # RIGHT SIDE → INSIGHTS
        with col2:
            st.markdown("### 📋 Detailed Insights")
            st.markdown(result)

        # Highlight box
        st.markdown("---")
        st.success("✅ Analysis Complete! Use these insights to improve HR consultation quality.")

    else:
        st.warning("⚠️ Please enter a transcript.")


































# import streamlit as st
# from agent import analyze_consultation

# st.title("HR Coaching Intelligence Agent")

# st.write("Paste HR consultation transcript below to get AI coaching insights.")

# transcript = st.text_area("Consultation Transcript")

# if st.button("Analyze Consultation"):
    
#     if transcript:
#         result = analyze_consultation(transcript)
        
#         st.subheader("AI Coaching Insights")
#         st.write(result)
        
#     else:
#         st.warning("Please enter a transcript.")