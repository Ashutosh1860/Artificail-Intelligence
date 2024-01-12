import re

def simple_chatbot(user_input):
    # Define rules and responses
    rules = {
        r'hello|hi|hey': 'Hello! How can I help you?',
        r'how are you': 'I am a chatbot. I don\'t have feelings, but thanks for asking!',
        r'your name': 'I\'m just a simple chatbot.',
        r'bye|goodbye': 'Goodbye! Have a great day!'
    }

    # Check user input against rules
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    # If no match found
    return "I'm sorry, I didn't understand that."

# Main loop for the chatbot
while True:
    # Get user input
    user_input = input("You: ")

    # Exit the loop if the user types 'exit'
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Get chatbot response and print it
    response = simple_chatbot(user_input)
    print("Bot:", response)
