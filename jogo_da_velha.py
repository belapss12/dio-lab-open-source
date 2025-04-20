import tkinter as tk
from tkinter import messagebox

# Configuração da janela
root = tk.Tk()
root.title("Jogo da Velha")

# Variáveis de controle
current_player = "X"
board = [""] * 9

# Função para verificar vencedor
def check_winner():
    winning_positions = [(0,1,2), (3,4,5), (6,7,8),  # Linhas
                         (0,3,6), (1,4,7), (2,5,8),  # Colunas
                         (0,4,8), (2,4,6)]  # Diagonais
    
    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] and board[pos[0]] != "":
            return board[pos[0]]
    
    if "" not in board:
        return "Empate"
    
    return None

# Função chamada ao clicar em um botão
def on_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index]["text"] = current_player
        winner = check_winner()

        if winner:
            if winner == "Empate":
                messagebox.showinfo("Resultado", "O jogo terminou em empate!")
            else:
                messagebox.showinfo("Resultado", f"O jogador {winner} venceu!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

# Função para reiniciar o jogo
def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    
    for button in buttons:
        button["text"] = ""

# Criando botões
buttons = []
for i in range(9):
    btn = tk.Button(root, text="", width=10, height=4, font=("Arial", 20),
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Executa a interface gráfica
print("O jogo está rodando...")
root.mainloop()
