from flask import Flask, request, jsonify
from g4f.client import Client
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
client = Client()

@app.route('/')
def main():
    return "Reach API Docs - https://github.com/arcaaane/reach-ai/ \nAI Messaging - https://flask-reach.vercel.app/chat?message=YOUR_MESSAGE"

@app.route('/chat') # methods=['GET'])
def chat():
    user_message = request.args.get("message")
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_message}],
        web_search=False
    )
    return jsonify({"response": response.choices[0].message.content})
    
