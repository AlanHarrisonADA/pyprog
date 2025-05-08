import random

def high_low():
    rand = random.randint(1,100)
    playing = True
    while playing:
        try:
            guess = int(input("guess a number! "))
            if guess == rand:
                print("congrats")
                playing = False
            else:
                message = "LOWER" if guess > rand else "HIGHER"
                raise RuntimeError(message)
        except ValueError as e:
            print(f"Invalid input: {e}")
        except RuntimeError as e:
            print(f"Not correct, {e}")


play = "y"
while play == "y":
    high_low()
    play = input("play again? (y/n)")

print("game over!")

            