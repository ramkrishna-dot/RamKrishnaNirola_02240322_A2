
import random
from RamkrishnaNirola_02240322_A2_PB import run_game
class MultiGameProgram:
    def _init_(self):
        scores = {"guess_number": 0,"rock_paper_scissors": 0,"trivia_quiz": 0,"pokemon binder":0}

    def guess_number_game(self):
        print("\nGuess Number Game")
        min_num = int(input("Enter minimum number: "))
        max_num = int(input("Enter maximum number: "))

        target = random.randint(min_num, max_num)
        guesses = 0
  
        while True:
            guess = int(input("Your guess (or 0 to quit): "))
            if guess == 0:     
                print(f"Game ended. The number was {target}.")
                break

            guesses += 1

            if guess < target:   
                print("Too low!")
            elif guess > target:
                print("Too high!")
            else:
                print(f"Correct! The number was {target}. You took {guesses} guesses.")
                self.scores["guess_number"] += (10 - guesses)
                break

    def rock_paper_scissors(self):
        print("\nRock Paper Scissors Game")
        choices = ['rock', 'paper', 'scissors']
        wins = 0
        rounds = 0

        while True:
            user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
            if user_choice == 'quit':
                print(f"Game ended. You won {wins} out of {rounds} rounds.")
                self.scores["rock_paper_scissors"] += wins
                break

            computer_choice = random.choice(choices)
            print(f"Computer chose: {computer_choice}")

            if user_choice == computer_choice:
                print("It's a tie!")
            elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                 (user_choice == 'paper' and computer_choice == 'rock') or \
                 (user_choice == 'scissors' and computer_choice == 'paper'):
                print("You win this round!")
                wins += 1
            else:
                print("Computer wins!")

            rounds += 1

    def trivia_quiz(self):
        print("\nTrivia Pursuit Quiz")
        questions = {
            "Science": [
                {"question": "What is the symbol for gold?", "options": ["Go", "Au", "Gd", "Ag"], "answer": "Au"},
                {"question": "How many bones in the human body?", "options": ["106", "206", "306", "406"], "answer": "206"}
            ],
            "History": [
                {"question": "Year WWII ended?", "options": ["1943", "1944", "1945", "1946"], "answer": "1945"},
                {"question": "First king of bhutan?", "options": ["sonam dorji", "kinga wangchuck", "jigme wangchuk", "ugyen wangchuk"], "answer": "ugyen wangchuk"}
            ]
        }

        correct_answers = 0
        total_questions = 0

        for category, qs in questions.items():
            print(f"\n{category} Quiz:")
            for q in qs:
                total_questions += 1
                print("\n" + q["question"])
                for opt in q["options"]:
                    print(opt)

                user_answer = input("Your answer: ").title()

                if user_answer == q["answer"]:
                    print("Correct!")
                    correct_answers += 1
                else:
                    print(f"Incorrect. The correct answer was {q['answer']}.")

        self.scores["trivia_quiz"] += correct_answers
        print(f"\nTrivia Quiz Complete! Score: {correct_answers}/{total_questions}")

  

    def check_scores(self):
        print("\nOverall Scores")
        for game, score in self.scores.items():
            print(f"{game.replace('_', ' ').title()}: {score}")

    def run(self):
        print("Multi-Game Program")

        while True:
            print("\nSelect a function (1-6):")
            print("1. Guess Number Game")
            print("2. Rock Paper Scissors Game")
            print("3. Trivia Pursuit Quiz Game")
           
            print("4. Check Current Overall Scores")
            print("5. Pokemonbindergame")
            print("6. Exit Program")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.guess_number_game()
            elif choice == '2':
                self.rock_paper_scissors()
            elif choice == '3':
                self.trivia_quiz()
            elif choice == '4':
                self.check_scores()
            elif choice == '5':
                run_game()
            elif choice == '6':
                print("Exiting program. Goodbye!")
                break  
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    game = MultiGameProgram()
    game.run()