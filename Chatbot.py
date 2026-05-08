# Function for chatbot response
def chatbot_response(user_input):

    # Convert input to lowercase
    user_input = user_input.lower()

    # Predefined responses
    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "bye":
        return "Goodbye!"

    elif user_input == "what is your name":
        return "I am a simple Python chatbot."

    elif user_input == "help":
        return "You can say: hello, how are you, bye"

    else:
        return "Sorry, I don't understand that."

# Main Program

print("===================================")
print("        BASIC PYTHON CHATBOT      ")
print("===================================")
print("Type 'bye' to exit the chatbot.")

# Chat loop
while True:

    # Take user input
    user_message = input("\nYou: ")

    # Get chatbot reply
    reply = chatbot_response(user_message)

    # Print chatbot response
    print("Bot:", reply)

    # Exit condition
    if user_message.lower() == "bye":
        print("\nChatbot Closed Successfully!")
        break