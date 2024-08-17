from random import randint, choice


def get_response(usr_input: str) -> str:
    lowered: str = usr_input.lower()


    if lowered == "":
        return"Well well well"
    elif "hello" in lowered:
        return "hello there"
    elif "how are you" in lowered:
        return "Good, thanks for asking"
    elif "bye" in lowered:
        return "See you!"
    elif 'roll dice' in lowered:
        return f"You rolled {randint(1, 6)}"
    else:
        return choice(["Sorry I do not understand...",
               "What are you taling about?",
               "Do you mind rephrasing that"
               ])

