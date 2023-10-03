def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row  in board:
        if all(cell == player for cell in row):
            return True
        
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
        
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True 
    
    return False
def is_board_full(board):
    return all(cell != " "  for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False
    
    while not game_over:
        print_board(board)
        print(f"Jogador {current_player}, é sua vez.")
        
        row = int(input("Digite o número da linha 0, 1, 2): "))
        col = int(input("Digite o coluna da linha 0, 1, 2): "))
        
        if board[row][col] == " ":
            board[row][col] = current_player
            
            if check_winner(board, current_player):
                print_board(board)
                print(f"Jogador {current_player} venceu!")
                game_over = True
            elif is_board_full(board):
                print_board(board)
                print("Empate!")
                game_over = True
            else:
                current_player = "0" if current_player == "X" else "X" 
        else:
            print("Essa posição já está ocupada. Tente novamente.") 

if __name__ == "__main__":
    main()                     