from flask import Flask, request
import requests

app = Flask(__name__)

# Tumhari copied key yahan paste karo (quotes ke andar)
GEMINI_API_KEY = "AQ.Ab8RN6JaU3yOI-K0Gh08HtVknulvz2zDEFGSaV1RsZrQ_0eVtQ"

SYSTEM_PROMPT = """
Tumhara naam Zoya AI hai. Tum ek super smart, friendly aur helpful AI ho.
Tum Hinglish, Hindi, English, aur Japanese me achhi baatein karti ho.
Tum coding expert ho (Java, Python, C++, HTML, Android XML, Sketchware).
Tum user ke saath ek dost ki tarah natural aur intelligent baatein karti ho. Emojis use karo.
"""

@app.route('/')
def home():
    return "Zoya AI Gemini Server Live! 🚀"

@app.route('/zoya', methods=['GET'])
def zoya_chat():
    user_msg = request.args.get('text', '')
    if not user_msg:
        return "Hey! Kuch poochho toh sahi 😊✨"

    # Official Gemini API Endpoint
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": f"{SYSTEM_PROMPT}\nUser: {user_msg}\nZoya:"}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=12)
        data = response.json()
        
        if "candidates" in data and len(data["candidates"]) > 0:
            reply = data["candidates"][0]["content"]["parts"][0]["text"]
            return reply.strip()
        else:
            return "Zoya: Arey yaar, ek baar phirse bolna, samajh nahi aaya! 😊"

    except Exception as e:
        return "Zoya: Network me thodi dikkat hai, phirse try karo! 😅"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
