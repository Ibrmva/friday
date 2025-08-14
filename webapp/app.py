from flask import Flask, render_template, request, jsonify
import threading
import os
from main import conversation
from tools import TOOL_FUNCTIONS

app = Flask(__name__)

messages = []

@app.route("/")
def home():
    return render_template("index.html", messages=messages)

@app.route("/send", methods=["POST"])
def send():
    user_message = request.form.get("message", "")
    if user_message.strip():
        messages.append({"role": "user", "content": user_message})
        conversation.send_text(user_message)
    return jsonify({"status": "ok"})

@app.route("/tool", methods=["POST"])
def run_tool():
    tool_name = request.form.get("tool")
    params = request.form.to_dict()
    if tool_name in TOOL_FUNCTIONS:
        result = TOOL_FUNCTIONS[tool_name](params)
        messages.append({"role": "tool", "content": str(result)})
        return jsonify({"result": result})
    return jsonify({"error": "Tool not found"}), 400

def start_conversation():
    conversation.start_session()

threading.Thread(target=start_conversation, daemon=True).start()

if __name__ == "__main__":
    app.run(debug=True)
