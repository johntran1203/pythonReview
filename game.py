import random

random_nim = random.randint(0,2)

player1 = input('player 1 what are you going to play ')

if random_nim == 0:
    player2 = 'rock'
elif random_nim ==1:
    player2 = 'paper'
else:
    player2 = 'scissor'

if player1 == 'rock' and player2 == 'paper':
    print("player 2 won the game")
elif player1 == 'rock' and player2 == 'rock':
    print("the game is a draw")
elif player1 == 'rock' and player2 == 'scissor':
    print('player 1 won the game')
elif player1 == 'paper' and player2 == 'paper':
    print('game is a draw')
elif player1 == 'paper' and player2 == 'rock':
    print('player 1 won the game')
elif player1 == 'paper' and player2 == 'scissor':
    print('player 2 won the game')
elif player1 == 'scissor' and player2 == 'scissor':
    print('player 1 won the game')
elif player1 == 'scissor' and player2 == 'rock':
    print('player 2 won the game')
elif player1 == 'scissor' and player2 == 'paper':
    print('player 1 won the game')
else:
    print('something went wrong')