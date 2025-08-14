class Question:
    """
    Represents a single question with its text and correct answer.
    """
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def check_answer(self, user_answer):
        """
        Checks if the user's answer matches the correct answer.
        Case-insensitive comparison.
        """
        return user_answer.lower() == self.answer.lower()

class Quiz:
    """
    Manages the quiz, including the list of questions,
    running the game, and tracking the score.
    """
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def get_current_question(self):
        """
        Returns the current question object.
        """
        return self.questions[self.question_index]

    def has_more_questions(self):
        """
        Checks if there are more questions in the quiz.
        """
        return self.question_index < len(self.questions)

    def next_question(self):
        """
        Moves to the next question.
        """
        self.question_index += 1

    def run(self):
        """
        The main loop for running the quiz.
        """
        print("--- Welcome to the Python Quiz Game! ---")

        for question in self.questions:
            print(f"\\nQuestion {self.question_index + 1}: {question.text}")
            user_answer = input("Your answer: ")

            if question.check_answer(user_answer):
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {question.answer}")

            self.next_question()

        self.show_final_score()

    def show_final_score(self):
        """
        Displays the final score to the user.
        """
        print("\\n--- Quiz Complete ---")
        print(f"Your final score is: {self.score}/{len(self.questions)}")
        print("---------------------\\n")


def main():
    # Define a list of Question objects
    question_data = [
        Question("What keyword is used to define a function in Python?", "def"),
        Question("Which data structure in Python is an ordered, immutable collection of items?", "tuple"),
        Question("What is the name of the package installer for Python?", "pip"),
        Question("Which OOP principle refers to bundling data and methods within a single unit?", "Encapsulation")
    ]

    # Create a Quiz instance and run it
    quiz = Quiz(question_data)
    quiz.run()


if __name__ == "__main__":
    main()
