import random
def guess_me(x):
    var=random.randint(1,x)
    guess=0
    while guess!=var:
        guess=int(input(f"guess a number between 1 to {x}:->"))
        if guess<var:
            print("guessed too low,please guess again")
        elif guess>var:
            print('guessed too high,please guess again')

    else:
        print(f' you guessed exact number {var}\n'
              f'you are a #guess master')
guess_me(10)

