player1 = input('player 1 what are you going to play ')
player2 = input('player 2 what are you going to play ')

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