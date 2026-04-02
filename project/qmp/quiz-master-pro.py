import random


def run_quiz():
    score = 0
    questions = []

    # Load Questions from File (Week 6 Concept)
    try:
        with open("questions.txt", "r") as f:
            questions = [line.strip().split(",") for line in f]
    except FileNotFoundError:
        print("Error: questions.txt not found.")
        return

    random.shuffle(questions)  # Shuffle logic

    for q in questions:
        print(f"\n{q[0]}")
        print(f"{q[1]} | {q[2]} | {q[3]}")
        ans = input("Your Answer (A/B/C): ").upper()

        if ans == q[4]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer was {q[4]}")

    percent = (score / len(questions)) * 100
    print(f"\nFinal Score: {score}/{len(questions)} ({percent}%)")

    # Save High Score
    with open("high_scores.txt", "a") as h:
        name = input("Enter name for leaderboard: ")
        h.write(f"{name}: {percent}%\n")


if __name__ == "__main__":
    run_quiz()