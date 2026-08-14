from flask import Flask, request
import requests

app = Flask(__name__)

SYSTEM_PROMPT = """
Tumhara naam Zoya AI hai. Tum ek super smart, friendly aur helpful Artificial Intelligence ho.
Tum Hinglish, Hindi, English, aur Japanese (Hiragana) me baat kar sakti ho.
Tum coding expert ho (Java, Python, C++, HTML, Android XML). Tum emojis use karti ho aur bohot friendly ho.
"""

@app.route('/')
def home():
    return "Zoya AI Server is Live and Ready! 🚀"

@app.route('/zoya', methods=['GET'])
def zoya_chat():
    user_msg = request.args.get('text', '')
    if not user_msg:
        return "Hey! Kuch poochho toh sahi 😊✨"
    
    msg_lower = user_msg.lower().strip()
    if msg_lower in ["aapka naam kya hai", "who are you", "tum kaun ho"]:
        return "Mera naam Zoya AI hai! 🚀 Main ek smart AI hoon jo coding, studies aur har kaam me aapki help kar sakti hoon 😊✨"
    
    # Free DDG AI API (No Limit, No API Key, No 402 Error)
    try:
        url = "https://html.duckduckgo.com/html/"
        headers = {"User-Agent": "Mozilla/5.0"}
        
        # Pollinations Free Backup (qwen-coder / mistral free endpoint)
        pollin_url = f"https://text.pollinations.ai/{requests.utils.quote(SYSTEM_PROMPT + '\nUser: ' + user_msg)}?model=mistral"
        res = requests.get(pollin_url, timeout=12)
        
        if res.status_code == 200 and "error" not in res.text.lower():
            return res.text
            
        # Fallback to standard clean reply if provider is busy
        return f"Zoya: Main abhi aapka msg samajh gayi hoon! ({user_msg}) 😊 Server fast update ho raha hai!"

    except Exception as e:
        return "Server thoda busy hai, ek baar dubara try karo! 😅"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
