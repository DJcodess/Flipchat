# app.py
from flask import Flask, render_template, request, jsonify
from chatbot import chatbot

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

# Create a dictionary to store chat histories
chat_histories = {}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_id = data.get('user_id')
    question = data.get('question')

    if user_id not in chat_histories:
        chat_histories[user_id] = []

    chat_history = chat_histories[user_id]
    result = chatbot({"question": question, "chat_history": chat_history})

    chat_history.append((result["question"], result["answer"]))

    # # Extract product and image URLs from bot's response using regular expressions
    import re

    product_url_match = re.search(r'(https?://[^\s]+)', result["answer"])
    if product_url_match:
        product_url = product_url_match.group(0)
        result["answer"] = re.sub(re.escape(product_url), '', result["answer"])
    else:
        product_url = None

    response = {
        "bot_response": result["answer"],
        "product_info": {
            "product_url": product_url
            # "image_url": image_url
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
