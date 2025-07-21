texts ={
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! 😊",
    "how are you": "I am fine bro,  What about you?",
    "bye": "Goodbye! love you.",
    "who are you?":"I am Subham.",
    "name": "I am Subham. What's your name?",
    "madhure":"bol re",
    "madhure ki korchis":"kichu na.",
    "madhure vlo lagche na.":"ore krishna , kno re ?",
    "madhure tui jibone ki korte chas ?":"I want to self-depended woman",
    "love":"Krishna,Ma,Baba. they are my love my world.",

}

def chatbot_text(user_input):
    user_input=user_input.lower()
    return texts.get(user_input, "I don't understand that. tui ki aber bolte parbi ?")


print("ChatBot: Hello! Type 'bye' to exit.")
while True:
    user_txt= input("you: ")
    if user_txt.lower() == "bye":
        print("ChatBot: Goodbye!")
        break
    print("ChatBot:", chatbot_text(user_txt))
