from flask import Flask, request
from g4f.client import Client

app = Flask(__name__)
client = Client()

SYSTEM_PROMPT = """
Tumhara naam Zoya AI hai. Tum ek super smart, friendly aur helpful AI ho.
Tum Hinglish, Hindi, English, aur Japanese me achhi baatein karti ho.
Tum coding expert ho (Java, Python, C++, HTML, Android XML, Sketchware).
Tum user ke saath ek dost ki tarah natural aur intelligent baatein karti ho. Emojis use karo.
"""

@app.route('/')
def home():
    return "Zoya AI Backend is Live! 🚀"

@app.route('/zoya', methods=['GET'])
def zoya_chat():
    user_msg = request.args.get('text', '')
    if not user_msg:
        return "Hey! Kuch poochho toh sahi 😊✨"

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_msg}
            ]
        )
        reply = response.choices[0].message.content
        return reply.strip()

    except Exception as e:
        # Fallback to alternate fast engine
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_msg}
                ]
            )
            return response.choices[0].message.content.strip()
        except:
            return "Zoya: Network issue hai, ek baar phirse try karo! 😅"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
