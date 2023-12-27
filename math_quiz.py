import time
import os
from assignments_lvl1_add import set1
from assignments_lvl2_add import set2


class MathQuiz:
    def __init__(self):
        # Output data
        self.correct_answers = 0
        self.incorrect_answers = []
        self.percentage_answers = ""
        self.time_taken = ""

    def run_quiz(self, df):
        try:
            # Start timer
            start_time = time.time()

            # Print out assignments and take user answers
            for key, value in df.items():
                user_answer = int(input(f"{key}+{value}= "))

                # If answer is correct, add "1" to the counter
                if user_answer == key+value:
                    self.correct_answers += 1

                # If answer is wrong, add full assignment to incorrect answers
                else:
                    self.incorrect_answers.append(
                        f"Incorret answer: {key}+{value}={user_answer} Correct answer: {key+value}")

            # Stop timer
            end_time = time.time()

            # How many time does it take
            self.time_taken = end_time - start_time
            # % of the all answers
            self.percentage_answers = \
                self.correct_answers / len(df.keys()) * 100

        # If user make mistake, don't stop the game
        except(ValueError, TypeError): 
            pass


        return "You did it!"

    def show_results(self):
        try:
            print(f"\n-------Results-------")
            print(
                f"You have: {self.correct_answers} from {len(set1.keys())} correct answers!")
            for answer in self.incorrect_answers:
                print(answer)
            print(f"{round(self.percentage_answers, 2)}% from 100%")
            return f"It takes: {round(self.time_taken, 2)} Sek."
        except TypeError as e:
            pass

    def export_results(self):
        try:
            export = input("Do you want to export your Progress?[y/n]:")

            if export == "y":
                name = input("Input name for your file please: ").strip()
                print("File is automatically saved to desktop")

                directory = os.path.expanduser(f"~/Desktop/{name}+.txt")

                with open(directory, "w") as file:
                    file.write(f"-------Results-------")
                    file.write(
                        f"\n{self.correct_answers} from {len(set1.keys())} correct answers!")
                    for answer in self.incorrect_answers:
                        file.write(f"\n{answer}")
                    file.write(
                        f"\n{round(self.percentage_answers, 2)}% from 100%")
                    file.write(f"\nIt takes: {round(self.time_taken, 2)} Sek.")

            elif export == "n":
                return "See you :)!"
            else:
                raise IndexError("You can only choose between y/n")

        except IndexError as e:
            print(f"Error occured! {e}")
        except TypeError as e:
            print(f"Error occured! {e}")

        return "Successfuly exported!\n"


def main():
    while True:
        try:
            print("Main Menu:\
                \n[1] First Level of Difficulty Addition\
                \n[2] Second Level of Difficulty Addition\
                \n[3] Exit")
            category = int(input())

            # Create a quiz
            math_quiz = MathQuiz()

            if category == 1:
                start = input(
                    "It can take from 2 to 10 minutes, are you sure you want to start?[y/n]: ").strip().lower()
                if start == "y":
                    print(math_quiz.run_quiz(set1))
                    print(math_quiz.show_results())
                    print(math_quiz.export_results())
                elif start == "n":
                    print(":(")
                else:
                    print("You can only choose between y/n!")

            elif category == 2:
                start = input(
                    "It can take from 2 to 10 minutes, are you sure you want to start?[y/n]: ").strip().lower()
                if start == "y":
                    print(math_quiz.run_quiz(set2))
                    print(math_quiz.show_results())
                    print(math_quiz.export_results())
                elif start == "n":
                    print(":(")
                else:
                    print("You can only choose between y/n!")

            elif category == 3:
                print("See you :)!")
                break

            elif start == "n":
                print(":(")

            else:
                raise ValueError("You can only choose between y/n!")

        except ValueError as e:
            print(f"Error occured: {e}")


if __name__ == "__main__":
    main()
