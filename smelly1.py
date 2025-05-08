'''This is a game, it's been written very badly and has a lot of
'code smells' - clean this code!
'''
def check_winner(dice_a, dice_b):
    return "player a" if dice_a % 2 == dice_b % 2 else "player b"
    
    
print(check_winner(3,5))  
print(check_winner(3,6))  


