beats = {
        "rock":"scissors",
        "scissors":"paper",
        "paper":"rock",
        "lizard":"paper",
        "spock":"rock"
        }
beats2 = {
        "lizard":"spock",
        "spock":"scissors",
        "rock":"lizard",
        "paper":"spock",
        "scissors":"lizard",
        
    }

def winner(beats_rps1, beats_rps2, player1, player2):
    for x,y in beats_rps1.items():
        if player1 == x and player2 == y:
            return "player1"
        elif player1 == y and player2 == x:
            return "player2"
    
    for x,y in beats_rps2.items():
        if player1 == x and player2 == y:
            return "player1"
        elif player1 == y and player2 == x:
            return "player2"
        