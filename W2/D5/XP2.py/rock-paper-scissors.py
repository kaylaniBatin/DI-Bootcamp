# rock-paper-scissors.py

from game import Game

def get_user_menu_choice():
    options = {
        '1': 'Play a new game',
        '2': 'Show scores',
        '3': 'Quit'
    }

    print("Rock-Paper-Scissors Menu:")
    for key, value in options.items():
        print(f"{key}. {value}")

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice in options:
            return choice
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

def print_results(results):
    print("\nGame Summary:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thanks for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == '1':
            game = Game()
            result = game.play()
            results[result] += 1

        elif choice == '2':
            print_results(results)

        elif choice == '3':
            print_results(results)
            break

if __name__ == "__main__":
    main()
