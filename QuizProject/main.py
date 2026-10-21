# main.py
# Entry point of the Quiz Management System.

import quiz
import file_handler


def show_menu():
    print("\n" + "=" * 40)
    print("      QUIZ MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Start Quiz")
    print("2. View Previous Results")
    print("3. Exit Program")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice not in ("1", "2", "3"):
            print("Error: Invalid choice. Please enter 1, 2, or 3.")
            continue  # skip and show the menu again

        if choice == "1":
            name, score, total = quiz.run_quiz()
            file_handler.save_result(name, score, total)
        elif choice == "2":
            file_handler.display_results()
        elif choice == "3":
            print("Thank you for using the Quiz Management System. Goodbye!")
            break  # exit the menu loop


if __name__ == "__main__":
    main()