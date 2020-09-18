# Name - Jaylen Schelb
# Program - Chat Bot

# Importing the random library to get access to the choice() function. This will allow me to randomly select an item from a 
# chosen list
from random import choice

# Newline to make the program read cleaner
print("")

# Function to get the bot's response from whatever the user inputs
def get_week_report_bot_response(user_response):

    # List of possible bot responses grouped by positive, negative, and neutral. Neutral responses are in case the bot is
    # unable to determine whether or not the user's response is a good or bad one
    bot_response_positive = ["Great to hear! Hope things stay this good! :)", "Aye! That's what I like to hear!",
                             "Awesome! Keep it up!", "Hearing good things from you makes me happy! Keep spreading the positive vibes! :)"]
    
    bot_response_negative = ["It will get better. Keep your head up", "Sorry to hear that, better days are on the horizon",
                             "Dang. I hope next week treats you better", "My condolences, you'll get 'em next week!"]
  
    bot_response_neutral = ["Sounds Interesting", "Thanks for sharing!", "Interesting..."]

    # Words and phrases the bot will look for in the user's response to determine whether it was a good or bad one
    positive_key_words = ["great", "good", "awesome", "amazing", "nice", "fantastic", "lit", "dope", "wonderful"]
    positive_key_phrases = ["wasnt bad"]
    negative_key_words = ["bad", "horrible", "okay", "boring", "crappy", "depressing", "wasn't great"]
    negative_key_phrases = ["wasnt good"]

    # Stripping the user's response of punctuation and capitilization so the bot can read the response no matter what 
    # punctuation and/or capitilization methods were used
    user_word_response = user_response.replace(".", " ").casefold()
    user_phrase_response = user_response.replace("'", "").casefold()

    # These two if statements are checking to see if any of the key words or phrases were used. The bot will give an 
    # appropriate response based on the type of words and/or phrases it detects. If no words or phrases are detected, 
    # the bot will default to a neutral response
    if any(i in user_phrase_response for i in positive_key_phrases):
        return choice(bot_response_positive)
    elif any(i in user_phrase_response for i in negative_key_phrases):
        return choice(bot_response_negative)
    else:
        None

    if any(i in positive_key_words for i in user_word_response.split()):
        return choice (bot_response_positive)
    elif any(i in negative_key_words for i in user_word_response.split()):
        return choice(bot_response_negative)
    else:
        return choice(bot_response_neutral)

# Introduction message
print("Hey! How was your week? Feel free to go into as much detail as you would like.")
print("You can run this bot for as many times as you would like. When you are done, simply type 'stop'")
print("")

# Asking the user for the input. The bot will keep asking for input and outputting a response until the user types 'stop'
while True:
    print("")
    user_response = input("Tell me about your week here: ")

    if user_response == "stop" or user_response == "Stop":
        print("Goodbye")
        break

    bot_response = get_week_report_bot_response(user_response)
    print(bot_response)
