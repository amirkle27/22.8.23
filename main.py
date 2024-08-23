import game

def play_game ():
    print("Hello, and welcome to our version of 'Rock, Paper, Scissors!")
    ans: str = input("Would you like to give it a go??"). lower().strip()
    while True:
        if ans in ["yes","y"]:
            print("Lets go then!")
            print("Player no. 1,")
            num1 = game.check_validity()
            print("Player no. 2,")
            num2 = game.check_validity()
            (game.check_winner(num1,num2))
            if game.check_winner(num1,num2) == 0:
                print("OH! It's a Draw!")
            elif game.check_winner(num1,num2) == 1:
                print("Player no. 1 won! Congratulations!")
            else:
                print("Player no. 2 won! Congratulations!")
            ans = input("Play Again?")
        elif ans in ["no", "n"]:
            print("Never mind. Some other time perhaps...")
            break
        else:
            ans = input("I didn't quite get your answer. Could you repeat that?").lower().strip()




play_game()