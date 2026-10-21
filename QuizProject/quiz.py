# quiz.py
# Contains the questions, quiz logic, and score calculation.

QUESTIONS = [
    {
        "question": "What is the output of print(type(5))?",
        "options": {"A": "<class 'str'>", "B": "<class 'int'>",
                    "C": "<class 'float'>", "D": "<class 'bool'>"},
        "answer": "B",
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {"A": "func", "B": "define", "C": "def", "D": "function"},
        "answer": "C",
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": {"A": "List", "B": "Dictionary", "C": "Set", "D": "Tuple"},
        "answer": "D",
    },
    {
        "question": "Which keyword is used to exit a loop immediately?",
        "options": {"A": "break", "B": "continue", "C": "exit", "D": "stop"},
        "answer": "A",
    },
    {
        "question": "Which function is used to read user input in Python?",
        "options": {"A": "scan()", "B": "input()", "C": "read()", "D": "get()"},
        "answer": "B",
    },
    {
        "question": "What does len([1, 2, 3, 4]) return?",
        "options": {"A": "3", "B": "5", "C": "4", "D": "2"},
        "answer": "C",
    },
]

VALID_OPTIONS = ("A", "B", "C", "D")


def get_student_name():
    """Keep asking until the student enters a non-empty name."""
    while True:
        name = input("\nEnter your name: ").strip()
        if not name:
            print("Error: Name cannot be empty. Please try again.")
            continue
        return name


def get_answer():
    """Keep asking until the student enters A, B, C, or D."""
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer not in VALID_OPTIONS:
            print("Error: Invalid input. Please enter A, B, C, or D.")
            continue  # skip the rest of this iteration and ask again
        return answer


def calculate_score(user_answers):
    """Compare user answers with correct answers. 1 mark per correct answer."""
    score = 0
    for index, question in enumerate(QUESTIONS):
        if user_answers[index] == question["answer"]:
            score += 1
    return score


def run_quiz():
    """Run the quiz and return (student_name, score, total_questions)."""
    name = get_student_name()
    user_answers = []

    print(f"\nWelcome, {name}! The quiz is starting.")
    print("=" * 40)

    for number, q in enumerate(QUESTIONS, start=1):
        print(f"\nQ{number}. {q['question']}")
        for key, value in q["options"].items():
            print(f"   {key}. {value}")
        user_answers.append(get_answer())

    score = calculate_score(user_answers)
    total = len(QUESTIONS)

    print("\n" + "=" * 40)
    print(f"Quiz complete! {name}, your score is {score} out of {total}.")
    print("=" * 40)

    return name, score, total