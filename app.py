# app.py
from flask import Flask, request, jsonify
from chatbot import chatbot

app = Flask(__name__)

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

    response = {
        "bot_response": result["answer"],
        "chat_history": chat_history
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
