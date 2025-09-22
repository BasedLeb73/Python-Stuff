# frnd_chatbot.py
#Note this does not answer any questions.

def frnd_reply(user_input: str) -> str:
    text = user_input.lower()

    if any(greet in text for greet in ["hello", "hi", "hey"]):
        return "Hey! Glad you’re here 👋"
    elif "how are you" in text:
        return "I’m doing great, thanks for asking! How about you?"
    elif any(word in text for word in ["sad", "upset", "depressed"]):
        return "I’m sorry you’re feeling that way 💙 Want to talk about it?"
    elif "bye" in text:
        return "See you soon, friend 👋 Take care!"
    else:
        return "Got it 👍 Tell me more!"


def run_frnd():
    print("FRND 😊: Hey! I’m FRND. How’s it going?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("FRND 😊: See you soon, friend 👋 Take care!")
            break
        reply = frnd_reply(user_input)
        print(f"FRND 😊: {reply}")


if __name__ == "__main__":
    run_frnd()
