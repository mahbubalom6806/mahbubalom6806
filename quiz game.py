
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

# List of quiz questions. Each question is a dictionary.
questions = [
    {
        "prompt": "Who is your lord?",
        "options": ["A. Allah", "B. Allah", "C. Allah", "D. Allah"],
        "answer": "A"
    },
    {
        "prompt": "Who is your prophet?",
        "options": ["A. Mohammed", "B. Muhammad", "C. Mahammad", "D. Mahammed"],
        "answer": "B"
    },
    {
        "prompt": "What is your religion?",
        "options": ["A. islam", "B. Islam", "C. Islaam", "D. islaam"],
        "answer": "B"
    },
    {
        "prompt": "when will these questions be asked?",
        "options": ["A. idk, when i die i guess", "B. NOW", "C. hi", "D. everytime"],
        "answer": "A"
    }
]

# Run the quiz
run_quiz(questions)