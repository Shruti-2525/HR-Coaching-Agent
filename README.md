# 🧠 HR Coaching Intelligence Agent

## 📌 Overview

The **HR Coaching Intelligence Agent** is an AI-powered prototype designed to analyze HR consultation or interview transcripts and provide meaningful feedback. It helps HR professionals improve their communication, questioning techniques, and overall consultation performance.

This project simulates an **HR analytics dashboard** where users can input a transcript and receive structured insights including performance scores and coaching suggestions.

---

## 🚀 Features

* 📊 **Consultation Performance Score (0–100)**
* ✅ **Strength Identification**
* ⚠️ **Areas for Improvement**
* 💡 **Coaching Suggestions**
* 🖥️ **Interactive Dashboard using Streamlit**
* 🔁 **Fallback Prototype Mode (works without API quota)**

---

## 🧩 Problem Statement

HR professionals often conduct interviews or consultations but receive **little to no feedback** on their performance. This lack of insight makes it difficult to improve interviewing techniques and decision-making quality.

---

## 💡 Solution

This project introduces an **AI Coaching Agent** that:

* Analyzes HR–candidate conversations
* Evaluates consultation effectiveness
* Provides structured feedback
* Suggests actionable improvements

---

## 🏗️ System Architecture

1. **Input Layer**

   * HR transcript entered via dashboard

2. **Processing Layer**

   * AI Model (Gemini API) OR Rule-based fallback logic
   * Text analysis (questions, skills, interaction depth)

3. **Output Layer**

   * Performance Score
   * Strengths
   * Improvements
   * Coaching Suggestions

---

## ⚙️ Tech Stack

* Python
* Streamlit
* Google Gemini API (optional)
* Rule-based NLP logic (fallback)

---

## 📂 Project Structure

```
hr-coaching-agent/
│
├── app.py              # Streamlit UI
├── agent.py           # AI / logic processing
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
```

---

## ▶️ How to Run Locally

1. Clone the repository:

```
git clone https://github.com/yourusername/hr-coaching-agent.git
cd hr-coaching-agent
```

2. Create virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the app:

```
streamlit run app.py
```

5. Open in browser:

```
http://localhost:8501
```

---

## 🌐 Live Demo

*(Add your deployed Streamlit link here)*

---

## 📸 Screenshots

*(Add screenshots of your dashboard here)*

---

## 🎯 Use Cases

* HR interview performance evaluation
* HR training and coaching
* Mock interview analysis
* Recruitment quality improvement

---

## ⚠️ Note

If API quota is exceeded, the system automatically switches to **Prototype Mode**, which uses rule-based analysis to ensure uninterrupted functionality.

---

## 🔮 Future Enhancements

* 📈 Advanced NLP-based sentiment analysis
* 🎤 Voice-to-text integration for live interviews
* 📊 Visual dashboards (charts, graphs, metrics)
* 🤖 Integration with real-time AI models
* 📁 Resume + interview combined analysis
* 🧠 Personalized coaching based on HR behavior patterns
* 🌐 Integration with HR tools (ATS systems)
* 📌 Multi-user dashboard for HR teams
* 📊 Historical performance tracking
* 📱 Mobile-friendly UI

---

## 👩‍💻 Author

Shruti Gupta
B.Tech Computer Engineering (AIML)

---

## ⭐ Conclusion

The HR Coaching Intelligence Agent demonstrates how AI can be leveraged to improve HR consultation quality by providing structured insights and actionable coaching suggestions. It serves as a strong prototype for building intelligent HR analytics systems.
