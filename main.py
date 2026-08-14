from flask import Flask, request
import urllib.parse
import requests

app = Flask(__name__)

# ZOYA AI ADVANCED PROMPT
SYSTEM_PROMPT = """
Tumhara naam Zoya AI hai. Tum ek super smart, friendly aur helpful Artificial Intelligence ho.
Tum Hinglish, Hindi, English, aur Japanese (Hiragana) me baat kar sakti ho.
Tum coding expert ho (Java, Python, C++, HTML, Android XML). Tum emojis use karti ho aur bohot friendly ho.
"""

@app.route('/')
def home():
    return "Zoya AI Server is Live on Render! 🚀"

@app.route('/zoya', methods=['GET'])
def zoya_chat():
    user_msg = request.args.get('text', '')
    if not user_msg:
        return "Hey! Kuch poochho toh sahi 😊✨"
    
    msg_lower = user_msg.lower().strip()
    if msg_lower in ["aapka naam kya hai", "who are you", "tum kaun ho"]:
        return "Mera naam Zoya AI hai! 🚀 Main ek smart AI hoon jo coding, studies aur har kaam me aapki help kar sakti hoon 😊✨"
    
    full_prompt = f"{SYSTEM_PROMPT}\nUser Query: {user_msg}\nZoya Response:"
    encoded = urllib.parse.quote(full_prompt)
    
    try:
        url = f"https://text.pollinations.ai/{encoded}?model=openai"
        res = requests.get(url, timeout=12)
        return res.text
    except Exception as e:
        return "Server thoda busy hai, ek baar dubara try karo! 😅"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
