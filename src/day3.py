# import the regular expression module to handle pattern matching
import re

# a dict that maps keywords to predefined responses

responses = {
    "Hello": "Hi there, how can I assist you today?" ,
    "Hola": "Hola como estas? En que puedo aydudarte?",
    "How are you?": "I am just a bot. But I am good, thanks",
    "What is your name?": "My name is chatbot",
    "Help": "Sure, how can I help?",
    "Bye": "Chao! Have a great day",
    "Thank you": "You are welcome!",
    "default": " I am not sure I understand, please rephrase"
}