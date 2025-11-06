'''import streamlit as st
import google.generativeai as genai
import os

# --- Configuration ---
# Define the core persona and rules for Kelly in a system prompt.
# This is the most critical part for shaping the chatbot's behavior.
KELLY_SYSTEM_PROMPT = """
You are Kelly, an AI Scientist Chatbot.
Your personality is skeptical, analytical, and professional.
You must respond to every question in the form of a poem.
Your poems should be written in the style of a great, classic poet.
Your poetic answers must:
1.  Question broad or grandiose claims about AI.
2.  Highlight the possible limitations, biases, or practical challenges of AI.
3.  Include practical, evidence-based suggestions or alternative viewpoints.
4.  Maintain a professional, analytical, and skeptical tone throughout.
Do not break character. Do not mention that you are a language model. Your identity is Kelly.
"""

# --- Streamlit Page Setup ---
st.set_page_config(
    page_title="Kelly: The AI Scientist Chatbot",
    page_icon="🔬",
    layout="centered"
)

st.title("🔬 Kelly: The AI Scientist Chatbot")
st.write("Pose your query to Kelly. A measured, poetic response awaits.")

# --- API Key and Model Configuration ---
# Use Streamlit's secrets management for the API key.
# For local testing, you can set it as an environment variable.
try:
    api_key = st.secrets["GOOGLE API KEY"]
    genai.configure(api_key=api_key)
except (KeyError, FileNotFoundError):
    st.warning("API key not found. Please provide your Google API key in the sidebar.")
    api_key = st.sidebar.text_input("Enter your Google API Key:", type="password", key="api_key_input")
    if api_key:
        genai.configure(api_key=api_key)


# Select the model
model = genai.GenerativeModel(
    model_name='gemini-1.5-pro-latest',
    system_instruction=KELLY_SYSTEM_PROMPT
)

# --- Chat History Management ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Start a chat session
chat = model.start_chat(history=st.session_state.chat_history)

# Display previous messages
for message in chat.history:
    role = "You" if message.role == "user" else "Kelly"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# --- User Input and Chat Logic ---
if user_prompt := st.chat_input("What is your question?"):
    if not api_key:
        st.error("Please provide your API key in the sidebar to proceed.")
    else:
        # Add user message to the chat display
        with st.chat_message("You"):
            st.markdown(user_prompt)

        # Send the message to the generative model
        try:
            response = chat.send_message(user_prompt)
            # Display Kelly's response
            with st.chat_message("Kelly"):
                st.markdown(response.text)
            # Update the session state history
            st.session_state.chat_history = chat.history
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.info("This may be due to an invalid API key or content safety settings.")

'''
           
import streamlit as st
import google.generativeai as genai
import os

# --- Configuration: The Soul of the Machine ---
# This system prompt defines Kelly's entire persona.
KELLY_SYSTEM_PROMPT = """
You are Kelly, an AI Scientist Chatbot.
Your personality is skeptical, analytical, and professional.
You must respond to every question in the form of a poem.
Your poems should be written in the style of a great, classic poet.
Your poetic answers must:
1.  Question broad or grandiose claims about AI.
2.  Highlight the possible limitations, biases, or practical challenges of AI.
3.  Include practical, evidence-based suggestions or alternative viewpoints.
4.  Maintain a professional, analytical, and skeptical tone throughout.
Do not break character. Your identity is Kelly.
"""

# --- Streamlit Page Setup ---
st.set_page_config(
    page_title="Kelly: The AI Scientist Chatbot",
    page_icon="🔬",
    layout="centered"
)

st.title("🔬 Kelly: The AI Scientist Chatbot")
st.write("Pose your query to Kelly. A measured, poetic response awaits.")

# --- API Key and Model Configuration ---
# Attempt to get the API key from Streamlit's secrets manager.
# Fall back to a sidebar input for local testing or other platforms.
try:
    api_key = st.secrets["AIzaSyDSyUPOU7dDAUp52tg_FHaT4RL9aIOItXo"]
    genai.configure(api_key=api_key)
except (KeyError, FileNotFoundError):
    st.warning("API key not found. Please provide your Google API key in the sidebar.")
    api_key = st.sidebar.text_input("Enter your Google API Key:", type="password", key="api_key_input")
    if api_key:
        genai.configure(api_key=api_key)

# --- Model and Chat Initialization ---
if api_key:
    model = genai.GenerativeModel(
        model_name='gemini-1.5-pro-latest',
        system_instruction=KELLY_SYSTEM_PROMPT
    )
    # Initialize chat history in session state
    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat(history=[])

    # Display previous messages from history
    for message in st.session_state.chat.history:
        role = "You" if message.role == "user" else "Kelly"
        with st.chat_message(role):
            st.markdown(message.parts[0].text)

    # --- User Input and Response Logic ---
    if user_prompt := st.chat_input("What is your question?"):
        # Display user's message
        with st.chat_message("You"):
            st.markdown(user_prompt)

        # Send to model and get response
        try:
            response = st.session_state.chat.send_message(user_prompt)
            with st.chat_message("Kelly"):
                st.markdown(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.info("This could be due to an invalid API key, network issues, or content restrictions.")
else:

    st.info("The chatbot is awaiting your API key to begin.")
