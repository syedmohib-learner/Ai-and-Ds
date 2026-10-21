# file_handler.py
# Handles saving and reading quiz results.

import os

# Always use results.txt located in the same folder as this file
FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.txt")


def save_result(name, score, total):
    """Append a result to results.txt (old records are preserved)."""
    try:
        with open(FILE_NAME, "a") as file:
            file.write(f"{name} | {score} | {total}\n")
        print("Result saved successfully.")
    except OSError as error:
        print(f"Error: Could not save the result. ({error})")


def display_results():
    """Read results.txt and display all previous results."""
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No results file found yet. Take a quiz first!")
        return
    except OSError as error:
        print(f"Error: Could not read the results file. ({error})")
        return

    if not lines:
        print("No previous results available.")
        return

    print("\n" + "=" * 40)
    print("PREVIOUS RESULTS")
    print("=" * 40)

    for number, line in enumerate(lines, start=1):
        parts = line.strip().split(" | ")
        if len(parts) != 3:
            continue  # skip corrupted lines
        name, score, total = parts
        print(f"{number}. Name: {name:<15} Score: {score}/{total}")