def rps(player1, player2):
    if player1 == "scissors" and player2 == "paper":
        return "Player 1 won!"
    if player1 == "paper" and player2 == "scissors":
        return "Player 2 won!"

    if player1 == "rock" and player2 == "scissors":
        return "Player 1 won!"
    if player1 == "scissors" and player2 == "rock":
        return "Player 2 won!"

    if player1 == "paper" and player2 == "rock":
        return "Player 1 won!"
    if player1 == "rock" and player2 == "paper":
        return "Player 2 won!"

    else:
        return "Draw!"