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
        "The journey of a thousand miles begins with one step."
    ]
    return random.choice(quotes)
if __name__ == "__main__":
    print("Here's your quote:")
    print(generate_quote())
