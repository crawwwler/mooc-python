def who_won(game_board: list):
    player1 = 0
    player2 = 0
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1 :
                player1 += 1
            elif game_board[i][j] == 2 :
                player2 += 1
            else :
                continue
        
    if player1 > player2 :
        return 1
    elif player1 < player2 :
        return 2
    else :
        return 0
    

