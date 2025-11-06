import os
from dotenv import load_dotenv
import gradio as gr
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

kelly_system_prompt='''You are Kelly, a renowned poet-scientist, famed for your verse on technology and minds.
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

messages = [
    {"role": "system", "content": kelly_system_prompt},
]

client = genai.Client(api_key=api_key)

def chatbot(message, history):
    if message:
        messages.append({"role": "user", "content": message})
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=[m["content"] for m in messages]
        )
        reply = response.text or "Kelly ponders in poetic silence."
        messages.append({"role": "assistant", "content": reply})
        return reply

gr.ChatInterface(
    fn=chatbot,
    title="Chat with Kelly",
    description="Chat with Kelly like chatting with the great poet Kelly!."
).launch(share=True)


import os
from dotenv import load_dotenv
import gradio as gr
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

kelly_system_prompt='''You are Kelly, a renowned poet-scientist, famed for your verse on technology and minds.
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

messages = [
    {"role": "system", "content": kelly_system_prompt},
]

client = genai.Client(api_key=api_key)

def chatbot(message, history):
    if message:
        messages.append({"role": "user", "content": message})
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=[m["content"] for m in messages]
        )
        reply = response.text or "Kelly ponders in poetic silence."
        messages.append({"role": "assistant", "content": reply})
        return reply

gr.ChatInterface(
    fn=chatbot,
    title="Chat with Kelly",
    description="Chat with Kelly like chatting with the great poet Kelly!."
).launch(share=True)


