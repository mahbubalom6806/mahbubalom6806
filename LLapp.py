import random

# edit this list - get more from Chat GPT

words = [
    {"arabic": "الـ", "english": "the"},
    {"arabic": "من", "english": "of/from"},
    {"arabic": "الذي", "english": "that/which"},
    {"arabic": "و", "english": "and"},
    {"arabic": "إلى", "english": "to/at"},
    {"arabic": "في", "english": "in/on"},
    {"arabic": "واحد", "english": "a/an"},
    {"arabic": "أن يكون", "english": "to be"},
    {"arabic": "نفسه", "english": "oneself/itself"},
    {"arabic": "لا", "english": "no/not"},
    {"arabic": "لديه", "english": "to have (auxiliary)"},
    {"arabic": "لأجل/بواسطة", "english": "for/by"},
    {"arabic": "مع", "english": "with"},
    {"arabic": "له/لها/لك/لهم", "english": "his/her/your/their"},
    {"arabic": "من أجل/إلى", "english": "for/to"},
    {"arabic": "كما", "english": "like/as"},
    {"arabic": "أن يكون", "english": "to be"},
    {"arabic": "أن يملك", "english": "to have"},
    {"arabic": "له/لها/لك", "english": "him/her/you (indirect object)"},
    {"arabic": "هو/هي/أنت", "english": "it/him/you (direct object)"},
]


def quiz_user(words):
    """Quiz the user with words."""
    random.shuffle(words)  # Shuffle the list of words
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['arabic']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['english']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()
    


