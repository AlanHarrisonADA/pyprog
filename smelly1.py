'''This is a game, it's been written very badly and has a lot of
'code smells' - clean this code!
'''
def f1(a,b):
    if   a == 1 and (b == 1 or b == 3 or b == 5):
         return "a"
    elif a == 3 and (b == 1 or b == 3 or b == 5):
         return "a"
    elif a == 5 and (b == 1 or b == 3 or b == 5):
         return "a"
    elif a == 2 and (b == 2 or b == 4 or b == 6):
         return "a"
    elif a == 4 and (b == 2 or b == 4 or b == 6):
         return "a"
    elif a == 6 and (b == 2 or b == 4 or b == 6):
         return "a"
    else:
         return "b"
    
    
print(f1(3,5))  
print(f1(3,6))  


