# --- Define your functions below! ---
def intro():
    print("Hello, my name is Jacy.")
def say_greeting():
    print("Hello there!")

def say_default():
    print("Thats awesome!!")

def say_goodbye():
    print("Farewell!!")

def say_greeting2() :
    print("")




def process_input(solution):
        greetings = ["hi", "hello", "what's up", "wassup", "what's good",]
        goodbyes = ["bye, bye", "see you later", "until next time", "goodbye", "bye", "chao"]

        if is_valid_input(solution, greetings) :
            say_greeting()
        elif  is_valid_input(solution, goodbyes) :
            say_goodbye()

        else :
            say_default()



def is_valid_input(user_input, valid_responses):
    for item in valid_responses:
        if user_input == item:
            return True
    return False


def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        answer = answer.lower()
        process_input(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
