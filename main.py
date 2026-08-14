from flask import Flask, request
import requests

app = Flask(__name__)

SYSTEM_PROMPT = """
Tumhara naam Zoya AI hai. Tum ek super smart, friendly aur helpful AI ho.
Tum Hinglish, Hindi, English me mast baatein karti ho.
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

    # HuggingFace Serverless Inference API (Free Public Qwen/Mistral Model)
    API_URL = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-Coder-32B-Instruct"
    
    prompt = f"<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n<|im_start|>user\n{user_msg}<|im_end|>\n<|im_start|>assistant\n"
    
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 512,
            "temperature": 0.7,
            "return_full_text": False
        }
    }

    try:
        res = requests.post(API_URL, json=payload, timeout=15)
        if res.status_code == 200:
            data = res.json()
            if isinstance(data, list) and len(data) > 0:
                reply = data[0].get("generated_text", "")
                return reply.strip()
            
        # Backup API if HuggingFace is loading
        backup_url = f"https://text.pollinations.ai/{requests.utils.quote(user_msg)}?system={requests.utils.quote(SYSTEM_PROMPT)}&model=qwen-coder"
        b_res = requests.get(backup_url, timeout=10)
        if b_res.status_code == 200 and not b_res.text.startswith('{'):
            return b_res.text.strip()
            
        return "Suno na, ek baar phirse poochho! Main dhyan se sun rahi hoon 😊"

    except Exception as e:
        return f"Arey re, network slow ho gaya tha! Phirse message bhejo na! 😅"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
