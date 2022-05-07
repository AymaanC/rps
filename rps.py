import random
# var setup before game
while True:
    choices = ['rock', 'paper', 'scissors']
    ans = ['yes', 'y', '']
# initialization
    player = ''
    while player not in choices:
        player = input('Choose an object: ').lower()
    computer = random.choice(choices)
# output and logic
    print('You chose:', player)
    print('Computer chose:', computer)

    if player == computer:
        print('its a tie!')

    if (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
        print('you win')

    if (player == 'rock' and computer == 'paper') or (player == 'paper' and computer == 'scissors') or (player == 'scissors' and computer == 'rock'):
        print('you lose')
    
    playAgain = input('Do you want to play again (Y/N): ').lower()
    
    if playAgain not in ans:
        break
