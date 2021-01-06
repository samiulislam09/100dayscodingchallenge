import random
p = ['rock', 'paper', 'scissor']
computer = p[random.randint(0, 2)]
game_running = True


while game_running:
    player = input('rock, paper, scissor?').lower()
    print(f'--------Your choice {player}-------')
    if player == 'rock':
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif player == 'paper':
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    elif player == 'scissor':
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)
    print(f'-----Computer choice {computer} -----')
    if computer == 'rock':
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif computer == 'paper':
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    elif computer == 'scissor':
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)
    if computer == player:
        print('-------tie-------')
    elif player == 'paper':
        if computer == 'scissor':
            print(f'you lose! {computer} cuts the {player}')
        else:
            print(f'Yay you won 😎 {player} covers {computer}')
    elif player == 'rock':
        if computer == 'paper':
            print(f'you lose {computer} covers {player}')
        else:
            print(f'Yay you won 😎 {player} smashes {computer}')
    elif player == 'scissor':
        if computer == 'rock':
            print(f'you lose! {computer} smashes {player}')
        else:
            print(f'Yay you won 😎 {player} cut {computer}')
    else:
        print('this is not a valid play! try a valid keyword')
    print('GΛMΣ-ӨVΣЯ')

    game_running = False




