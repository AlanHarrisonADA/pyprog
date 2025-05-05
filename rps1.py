
from rps_dict import beats2, beats, winner
#importing the dictionary containing RPS from rps_dict and function to check winner


def rock_paper_scissors(player1, player2):
    
    players = [player1, player2]
    choices = ["rock", "paper","scissors","spock","lizard"]
    
    
    for player in players:
        player = player.lower()
        if player not in choices:
            print("Not valid string argument for this game")
            return
    if player1 == player2:
        return "draw"
    

    winning_player = winner(beats, beats2, player1, player2)

    return winning_player
    

    
    
print(rock_paper_scissors("paper", "rock"))