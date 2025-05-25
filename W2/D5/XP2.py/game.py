#rock paper scissors 
# game.py
import random

class Game:
    def get_user_item(self):
        valid_items = ['rock', 'paper', 'scissors']
        while True:
            user_input = input("Choose rock, paper, or scissors: ").lower().strip()
            if user_input in valid_items:
                return user_input
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")

    def get_computer_item(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (
            (user_item == "rock" and computer_item == "scissors") or
            (user_item == "scissors" and computer_item == "paper") or
            (user_item == "paper" and computer_item == "rock")
        ):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"\nYou chose: {user_item}")
        print(f"Computer chose: {computer_item}")
        print(f"Result: You {result.upper()}!\n")

        return result
