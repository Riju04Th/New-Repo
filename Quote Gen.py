import pyttsx3
engine = pyttsx3.init('sapi5')
# engine.getProperty('voices')
engine.setProperty('voices[1]')
import random
def generate_quote():
    quotes = [
        "The best way to predict the future is to create it.",
        "Life is 10% what happens to us and 90% how we react to it.",
        "The only way to do great work is to love what you do.",
        "You miss 100% of the shots you don’t take.",
        "Whether you think you can or you think you can’t, you’re right.",
        "The best revenge is massive success.",
        "The mind is everything. What you think you become.",
        "Your time is limited, don’t waste it living someone else’s life.",
        "You only live once, but if you do it right, once is enough.",
        "The journey of a thousand miles begins with one step.",
        "In our society, those who don't have many abilities tend to complain more.",
        "It's not the face that makes someone a monster; it's the choices they make with their lives.",
        "A lesson without pain is meaningless. For you cannot gain something without sacrificing something else in return.",
        "People’s lives don’t end when they die. It ends when they lose faith.",
        "If you don’t take risks, you can’t create a future.",
        "Whatever you lose, you’ll find it again. But what you throw away you’ll never get back.",
        "Fear is not evil. It tells you what your weakness is. And once you know your weakness, you can become stronger as well as kinder.",
        "The world isn’t perfect. But it’s there for us, doing the best it can….that’s what makes it so damn beautiful.",
        "A place where someone still thinks about you is a place you can call home.",
        "No matter how deep the night, it always turns to day, eventually."
    ]
    return random.choice(quotes)
if __name__ == "__main__":
    print("Here's your quote:")
    print(generate_quote())
