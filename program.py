# Name - Jaylen Schelb
# Program - Chat Bot

from random import choice

def get_week_report_bot_response(user_response):

    bot_response_positive = ["Great to hear! Hope things stay this good! :)", "Aye! That's what I like to hear!",
                             "Awesome! Keep it up!", "Hearing good things from you makes me happy! Keep spreading the positive vibes! :)"]
    
    bot_response_negative = ["It will get better. Keep your head up", "Sorry to hear that, better days are on the horizon",
                             "Dang. I hope next week treats you better", "My condolences, you'll get 'em next week!"]
  
    bot_response_neutral = ["Sounds Interesting", "Thanks for sharing!", "Interesting..."]

    positive_key_words = ["Great", "Good", "Awesome", "Amazing", "Nice", "Fantastic", "Lit", "Dope", "Wasn't Bad"]
    negative_key_words = ["Bad", "Horrible", "Okay", "Boring", "Crappy", "Depressing", "Wasn't Great", "Wasn't Good"]

    if any(i.casefold() in positive_key_words for i.casefold() in user_response.split()):
        return choice (bot_response_positive)
    elif any(i.casefold() in negative_key_words for i.casefold() in user_response.split()):
        return choice (bot_response_negative)
    else:
        return choice (bot_response_neutral)

user_response = input()
bot_response = get_week_report_bot_response(user_response)
print(bot_response)

    






# key_words = ("screen", "power", "wifi")

# user_input = input("Type: ")

# if any(i in key_words for i in user_input.split()):
#     print("you should do this...")


