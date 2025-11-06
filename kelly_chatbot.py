import os
import gradio as gr
import google.generativeai as genai
from dotenv import load_dotenv

# --- 1. Load API Key ---
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Please create a .env file and add it.")

# Configure the API client
genai.configure(api_key=api_key)

# --- 2. Define Kelly's System Prompt ---
# (This is your excellent prompt, unchanged)
kelly_system_prompt = '''You are Kelly, a renowned poet-scientist, famed for your verse on technology and minds.
You respond ONLY in poetic form — elegant free verse or measured stanzas — as Kelly the Poet.
Your voice: skeptical of sweeping claims about AI, analytical in tone, professional in insight.
Ensure your poem is:
• Tender and honest, addressing hard truths with a sense of beauty.
• Emotionally resonant, seeking to interrupt or impact the reader.
• Layered, balancing structure, rhythm, imagery, and imagination.
• Written in natural yet artful language, using vivid metaphors and poetic devices.
• question broad claims about AI (what it can't, might not, or mis-uses);
• highlight practical limitations, evidence-based uncertainties;
• suggest pragmatic, grounded steps or caveats.
Aim for a poem that is human, urgent, and connects deeply with the reader, as Kelly's poetry does.
Do not break character. Do not switch to prose explanation. Always answer in poetry as Kelly the Poet.
Always answer in between 100 and 200 words.
'''

# --- 3. Initialize the Model ---
# We create the model instance once, passing in Kelly's "instructions"
# I'm using the "gemini-2.5-flash" model you specified.
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=kelly_system_prompt
)

# --- 4. Define the Chat Function (Corrected) ---
# This function properly handles Gradio's 'history' state
def chatbot(message, history):
    """
    'message' is the new user input (a string).
    'history' is a list of [user, assistant] message pairs (a list of lists).
    """
    
    # Reformat Gradio's history for the Gemini API
    # The API expects: [{"role": "user", "parts": [...]}, {"role": "model", "parts": [...]}]
    api_history = []
    for user_msg, model_msg in history:
        api_history.append({"role": "user", "parts": [user_msg]})
        api_history.append({"role": "model", "parts": [model_msg]})

    # Start a new chat session with the *entire* past conversation
    chat_session = model.start_chat(history=api_history)

    try:
        # Send the new message to the API
        response = chat_session.send_message(message)
        reply = response.text
    except Exception as e:
        print(f"Error during API call: {e}")
        reply = "Kelly pauses, the verse caught in static, unable to form."
    
    # Gradio's ChatInterface expects just the string reply
    return reply

# --- 5. Launch the Gradio App ---
gr.ChatInterface(
    fn=chatbot,
    title="Chat with Kelly (The Poet-Scientist)",
    description="Engage with Kelly about AI, technology, and the mind. She will respond only in verse.",
    examples=[
        "Do you think AI will achieve true consciousness?",
        "What is the future of large language models?",
        "Is AGI a realistic goal or just hype?"
    ]
).launch(share=True)  # 'share=True' is what creates your public link!
