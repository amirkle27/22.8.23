def check_validity (choice: str = "") -> int:
    match choice.lower().strip():
        case "rock":
            return  2
        case "scissors":
            return  1
        case "paper":
            return  0
        case _:
            raise ValueError ("Illegal Game Option")

def check_winner (player1_choice: int, player2_choice: int) -> int:
    verdict: int =  1 if player1_choice-1 == player2_choice or player1_choice+2 == player2_choice else 2 if player2_choice-1 == player1_choice or player2_choice+2 == player1_choice else 0 if player1_choice==player2_choice else None
    if player1_choice > 2 or player1_choice < 0 or player2_choice > 2 or player2_choice < 0:
        raise ValueError("Illegal Game Option")
    return verdict







