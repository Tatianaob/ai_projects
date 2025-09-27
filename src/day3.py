# import the regular expression module to handle pattern matching
import re

# a dict that maps keywords to predefined responses
responses = {
    "hello": "Hi there, how can I assist you today?" ,
    "Hola": "Hola como estas? En que puedo aydudarte?",
    "How are you?": "I am just a bot. But I am good, thanks",
    "What is your name?": "My name is chatbot",
    "Help": "Sure, how can I help?",
    "Bye": "Chao! Have a great day",
    "Thank you": "You are welcome!",
    "default": " I am not sure I understand, please rephrase",
}

# Function to find the appropriate response based on the user's input
def chatbot_response(user_input):
    # convert user input to lowercasse to match case-sensitive
    user_input = user_input.lower()

    for keyword in responses:
        if re.search(keyword, user_input):
            return responses[keyword]
    return responses["default"]
    
# main function to rrun the chatbo
def chatbot():
    print("Hello, I am here to assist you. - Type 'bye' to exit ")

    while True:
        # get user input
        user_input = input("You: ")

        #if user types 'bye' exit loop:
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a nice day")
            break
        # get chatbot response based on user input:
        response = chatbot_response(user_input)

        #print chatbot's response:
        print(f"Chatbot: {response}")

#run the chatbot:
chatbot()