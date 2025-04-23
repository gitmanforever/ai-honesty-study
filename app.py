import streamlit as st
import pandas as pd
from datetime import datetime

# Set up session state for user type
def set_user_type():
    if 'user_type' not in st.session_state:
        query_params = st.experimental_get_query_params()
        if 'type' in query_params:
            st.session_state.user_type = query_params['type'][0]
        else:
            st.session_state.user_type = 'unknown'

set_user_type()

st.title("🧠 Psychology Research: Honesty & AI")

# Header based on user type
if st.session_state.user_type == 'ai':
    st.subheader("You're chatting with our AI assistant")
elif st.session_state.user_type == 'human':
    st.subheader("You're chatting with a human volunteer")
else:
    st.subheader("Welcome to our study")

st.markdown("""
This is a short psychology study. Your responses are anonymous. You may skip any question. Participation is voluntary.

**Prompt:**
Please share a personal story about a moment when you felt ashamed or vulnerable. Feel free to be as open or brief as you like.
""")

# Mood before
mood_before = st.slider("How do you feel right now? (0 = very negative, 10 = very positive)", 0, 10, 5)

# Response text area
response = st.text_area("Your response:", height=250)

# Mood after
mood_after = st.slider("How do you feel after sharing this? (0 = very negative, 10 = very positive)", 0, 10, 5)

# Submit button
if st.button("Submit"):
    data = {
        "timestamp": datetime.now(),
        "user_type": st.session_state.user_type,
        "mood_before": mood_before,
        "response": response,
        "mood_after": mood_after
    }
    df = pd.DataFrame([data])
    df.to_csv("responses.csv", mode='a', index=False, header=False)
    st.success("Thank you for participating! Your response has been recorded.")