
import random
responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "how are you": ["I'm doing great!", "All good, thanks for asking!", "Fantastic!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I didn't understand that. Can you rephrase?"
print("🤖 Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("🤖 Chatbot: Goodbye!")
        break
    print("🤖 Chatbot:", chatbot_response(user_input))
