def start_game():
    game_cells = []
    possible_user_inputs = range(0, 9)
    win_possibilities = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8)]
    player_turn = 'X'

    def clean_board():
        return ['' for x in possible_user_inputs]

    def print_board():
        print(f'{game_cells[0]} | {game_cells[1]} | {game_cells[2]}')
        print(f'{game_cells[3]} | {game_cells[4]} | {game_cells[5]}')
        print(f'{game_cells[6]} | {game_cells[7]} | {game_cells[8]}')

    def change_turn():
        nonlocal player_turn
        if player_turn == 'X':
            player_turn = "O"
        else:
            player_turn = 'X'

    def check_winner():
        for possibility in win_possibilities:
            if game_cells[possibility[0]] == game_cells[possibility[1]] == game_cells[possibility[2]] != '':
                return game_cells[possibility[0]]
        return ''

    def get_user_input():
        while True:
            try:
                user_input = int(
                    input('please choose a number between 1 to 9'))
                if user_input not in range(0, 10):
                    print("input is invalid")
                    continue
                return user_input
            except ValueError:
                print("invalid value")

    def run_game():
        nonlocal game_cells
        game_cells = clean_board()
        print(game_cells)
        winner = ''
        while True:
            print_board()
            user_input = get_user_input()
            game_cells[user_input - 1] = player_turn
            winner = check_winner()
            if winner:
                print_board()
                print(f'the winner is {player_turn}')
                break
            elif '' not in game_cells:
                print_board()
                print("the game is a draw")
            else:
                change_turn()
                continue
    run_game()


start_game()
