# Name - Jaylen Schelb
# Program - Chat Bot

from random import choice

print("")

def get_week_report_bot_response(user_response):

    bot_response_positive = ["Great to hear! Hope things stay this good! :)", "Aye! That's what I like to hear!",
                             "Awesome! Keep it up!", "Hearing good things from you makes me happy! Keep spreading the positive vibes! :)"]
    
    bot_response_negative = ["It will get better. Keep your head up", "Sorry to hear that, better days are on the horizon",
                             "Dang. I hope next week treats you better", "My condolences, you'll get 'em next week!"]
  
    bot_response_neutral = ["Sounds Interesting", "Thanks for sharing!", "Interesting..."]

    positive_key_words = ["great", "good", "awesome", "amazing", "nice", "fantastic", "lit", "dope", "wasn't bad", "wonderful"]
    negative_key_words = ["bad", "horrible", "okay", "boring", "crappy", "depressing", "wasn't great", "wasn't good"]

    user_response = user_response.replace(".", " ").casefold()

    if any(i in positive_key_words for i in user_response.split()):
        return choice (bot_response_positive)
    elif any(i in negative_key_words for i in user_response.split()):
        return choice (bot_response_negative)
    else:
        return choice (bot_response_neutral)

print("Hey! How was your week? Feel free to go into as much detail as you would like.")
print("You can run this bot for as many times as you would like. When you are done, simply type 'stop'")
print("")

user_response = ""

while True:
    print("")
    user_response = input("Tell me about your week here: ")

    if user_response == "stop" or user_response == "Stop":
        print("Goodbye")
        break

    bot_response = get_week_report_bot_response(user_response)
    print(bot_response)
