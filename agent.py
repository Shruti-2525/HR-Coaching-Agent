def analyze_consultation(transcript):

    text = transcript.lower()

    score = 50
    strengths = []
    improvements = []

    # Check if HR asked questions
    if "?" in text:
        score += 15
        strengths.append("HR asked relevant questions")

    # Check for skills/projects
    skills = ["python", "java", "sql", "react", "machine learning", "project"]
    if any(skill in text for skill in skills):
        score += 15
        strengths.append("Candidate skills/projects were discussed")

    # Multiple questions = better interaction
    if text.count("?") >= 2:
        score += 10
        strengths.append("HR asked multiple follow-up questions")

    # Very short conversation
    if len(text.split()) < 40:
        score -= 10
        improvements.append("Consultation was too short")

    # Weak HR responses
    weak_phrases = ["okay", "fine", "apply online"]
    if any(w in text for w in weak_phrases):
        score -= 5
        improvements.append("HR responses were generic")

    # Default improvement
    if not improvements:
        improvements.append("Ask deeper behavioral and technical questions")

    # Coaching suggestions
    coaching = [
        "Use STAR interview technique",
        "Ask open-ended questions",
        "Encourage detailed responses from candidates",
        "Provide clear next steps"
    ]

    # Convert lists to text
    strengths_text = "\n".join("- " + s for s in strengths)
    improvements_text = "\n".join("- " + i for i in improvements)
    coaching_text = "\n".join("- " + c for c in coaching)

    return f"""
HR Coaching Analysis (Prototype Mode)

Consultation Score: {score}/100

Strengths:
{strengths_text}

Areas for Improvement:
{improvements_text}

Coaching Suggestions:
{coaching_text}

(Note: This is a prototype AI model using rule-based analysis.)
"""


# API integration is commented out due to quota limits, but the function can be easily switched to use the Gemini API when available.
# from google import genai

# client = genai.Client(api_key="GEMINI_API_KEY")

# def analyze_consultation(transcript):

#     prompt = f"""
# You are an HR Coaching AI Agent.

# Analyze the HR consultation transcript and provide:
# 1. Consultation performance score (0-100)
# 2. Strengths
# 3. Areas for improvement
# 4. Coaching suggestions

# Transcript:
# {transcript}
# """

#     try:
#         response = client.models.generate_content(
#             model="gemini-2.0-flash",
#             contents=prompt,
#         )

#         return response.text

#     except Exception:

#         text = transcript.lower()

#         score = 50
#         strengths = []
#         improvements = []

#         if "?" in text:
#             score += 15
#             strengths.append("HR asked questions to understand the candidate")

#         skills = ["python", "java", "sql", "react", "machine learning", "project"]
#         if any(skill in text for skill in skills):
#             score += 15
#             strengths.append("Candidate skills or projects were discussed")

#         if text.count("?") >= 2:
#             score += 10
#             strengths.append("HR asked multiple follow-up questions")

#         if len(text.split()) < 40:
#             score -= 10
#             improvements.append("Interview was too short")

#         weak_phrases = ["okay", "fine", "apply online"]
#         if any(w in text for w in weak_phrases):
#             score -= 5
#             improvements.append("HR responses were somewhat generic")

#         if not improvements:
#             improvements.append("Ask deeper technical or behavioral questions")

#         coaching = [
#             "Use the STAR interview method",
#             "Ask open-ended follow-up questions",
#             "Encourage candidates to explain their projects"
#         ]

#         strengths_text = "\n".join("- " + s for s in strengths)
#         improvements_text = "\n".join("- " + i for i in improvements)
#         coaching_text = "\n".join("- " + c for c in coaching)

#         result = f"""
# HR Coaching Analysis (Prototype Mode)

# Consultation Score: {score}/100

# Strengths:
# {strengths_text}

# Areas for Improvement:
# {improvements_text}

# Coaching Suggestions:
# {coaching_text}

# (Note: Prototype analysis used because API quota for Gemini is exceeded.)
# """

#         return result