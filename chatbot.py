import random
import datetime

print("🤖 Chatbot Started! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()  # convert input to lowercase
    hour = datetime.datetime.now().hour  # for time-based greetings

    # Greetings based on time
    if "hi" in user_input or "hello" in user_input:
        if 5 <= hour < 12:
            print("Bot:", random.choice(["Good morning!", "Hi there!", "Hello!"]))
        elif 12 <= hour < 18:
            print("Bot:", random.choice(["Good afternoon!", "Hi!", "Hello!"]))
        else:
            print("Bot:", random.choice(["Good evening!", "Hi!", "Hello!"]))

    elif "how are you" in user_input:
        print("Bot:", random.choice(["I'm doing great!", "Fantastic, thanks!", "All good!"]))

    elif "your name" in user_input:
        print("Bot: I'm a simple rule-based chatbot created by Kusum 🙂")

    elif "favorite color" in user_input or "favourite color" in user_input:
        print("Bot:", random.choice(["I like blue!", "Green is my favorite!", "I love all colors!"]))

    elif "mood" in user_input:
        print("Bot:", random.choice(["Feeling happy!", "Excited to chat!", "Chill and relaxed."]))

    elif "time" in user_input:
        print("Bot:", datetime.datetime.now().strftime("%H:%M:%S"))

    elif "date" in user_input or "today" in user_input:
        print("Bot: Today's date is", datetime.date.today())

    elif "joke" in user_input:
        print("Bot:", random.choice([
            "Why did the computer go to the doctor? It caught a virus 😄",
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the smartphone go to school? It wanted to be smarter!"
        ]))

    elif "thanks" in user_input or "thank you" in user_input:
        print("Bot: You're welcome!")

    elif "who created you" in user_input:
        print("Bot: I was created by Kusum Kurdekar 🙂")

    elif "bye" in user_input:
        print("Bot: Goodbye! Have a great day!")
        break

    else:
        print("Bot: I don't understand. Try saying hi, time, date, joke, or bye.")
