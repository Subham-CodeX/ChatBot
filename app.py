from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

texts = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! 😊",
    "how are you": "I am fine bro, What about you?",
    "bye": "Goodbye! love you.",
    "who are you?": "I am Subham.",
    "name": "I am Subham. What's your name?",
    "madhure": "bol re",
    "madhure ki korchis": "kichu na.",
    "madhure vlo lagche na.": "ore krishna , kno re ?",
    "madhure tui jibone ki korte chas ?": "I want to self-depended woman",
    "love": "Krishna, Ma, Baba. they are my love my world."
}

def chatbot_text(user_input):
    user_input = user_input.lower()
    return texts.get(user_input, "I don't understand that. tui ki aber bolte parbi ?")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get('msg')
    return chatbot_text(user_input)

if __name__ == "__main__":
    app.run(debug=True)
