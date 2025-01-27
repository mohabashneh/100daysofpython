import tkinter as tk
from tkinter import messagebox

# Initialize scores
mohammad_score = 0
eda_score = 0
round_number = 1
current_turn = "Mohammad"  # Start with Mohammad
mohammad_choice = None

# Moves dictionary
moves = {"R": "Rock", "P": "Paper", "S": "Scissors"}

# Function to handle turns
def play_turn(choice):
    global mohammad_choice, current_turn

    if current_turn == "Mohammad":
        mohammad_choice = choice  # Store Mohammad's choice
        current_turn = "Eda"
        result_label.config(text="👑 Eda's Turn! Choose Your Move! 👑")
    else:
        play_game(mohammad_choice, choice)  # Eda plays, compare results

# Function to handle game logic
def play_game(mohammad_move, eda_move):
    global mohammad_score, eda_score, round_number, current_turn

    # Determine result
    if mohammad_move == eda_move:
        result = "💖✨ IT'S A TIE! ✨💖"
    elif (mohammad_move == "R" and eda_move == "S") or \
         (mohammad_move == "P" and eda_move == "R") or \
         (mohammad_move == "S" and eda_move == "P"):
        result = "🔥 Mohammad wins this round! 🔥"
        mohammad_score += 1
    else:
        result = "💅 Eda wins this round! 💅"
        eda_score += 1

    # Update UI
    round_number += 1
    current_turn = "Mohammad"  # Reset to Mohammad's turn
    round_label.config(text=f"✨ ROUND {round_number} ✨")
    score_label.config(text=f"👑 Mohammad: {mohammad_score} | Eda: {eda_score} 👑")
    result_label.config(text=f"💎 Mohammad chose {moves[mohammad_move]} | Eda chose {moves[eda_move]} 💎\n{result}")

    # Check for a winner
    if mohammad_score == 3:
        game_over("Mohammad")
    elif eda_score == 3:
        game_over("Eda")

# Function to handle game over
def game_over(winner):
    if winner == "Mohammad":
        root.config(bg="#111")  # Dark mode
        round_label.config(bg="#111", fg="red")
        score_label.config(bg="#111", fg="red")
        result_label.config(bg="#111", fg="red", text="👎👎👎 Mohammad Wins 👎👎👎\nSystem Error: Too much dislike detected.")
        messagebox.showinfo("Game Over", "Mohammad wins... but at what cost? 👎👎👎")
    else:
        root.config(bg="#ff69b4")  # Super pink
        round_label.config(bg="#ff69b4", fg="white")
        score_label.config(bg="#ff69b4", fg="white")
        result_label.config(bg="#ff69b4", fg="white", font=("Comic Sans MS", 24, "bold"),
                            text="💖✨ LAWYER WINS ✨💖\nGLITTER EXPLOSION!")
        messagebox.showinfo("🎉 GAME OVER 🎉", "🎀 LAWYER WINS! CELEBRATE! 🎀")
    
    root.after(2000, root.quit)  # Auto-close after 2 seconds

# Create the main window
root = tk.Tk()
root.title("💖✨ Mohammad vs. Eda ✨💖")
root.geometry("500x600")
root.config(bg="#ff69b4")  # Hot pink background

# Labels
title_label = tk.Label(root, text="💖 MOHAMMAD vs. EDA 💖", font=("Comic Sans MS", 18, "bold"), fg="white", bg="#ff1493")
title_label.pack(pady=10)

round_label = tk.Label(root, text=f"✨ ROUND {round_number} ✨", font=("Arial", 14, "bold"), fg="white", bg="#ff69b4")
round_label.pack()

score_label = tk.Label(root, text=f"👑 Mohammad: {mohammad_score} | Eda: {eda_score} 👑", font=("Arial", 14, "bold"),
                       fg="white", bg="#ff69b4")
score_label.pack(pady=10)

result_label = tk.Label(root, text="👑 Mohammad's Turn! Choose Your Move! 👑", font=("Arial", 12), fg="white",
                        bg="#ff69b4", wraplength=400, justify="center")
result_label.pack(pady=20)

# Button Frame
button_frame = tk.Frame(root, bg="#ff69b4")
button_frame.pack()

rock_button = tk.Button(button_frame, text="🪨 ROCK", font=("Comic Sans MS", 14, "bold"), fg="white", bg="#ff1493",
                        activebackground="#ff69b4", command=lambda: play_turn("R"))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = tk.Button(button_frame, text="📜 PAPER", font=("Comic Sans MS", 14, "bold"), fg="white", bg="#ff1493",
                         activebackground="#ff69b4", command=lambda: play_turn("P"))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = tk.Button(button_frame, text="✂️ SCISSORS", font=("Comic Sans MS", 14, "bold"), fg="white", bg="#ff1493",
                            activebackground="#ff69b4", command=lambda: play_turn("S"))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

# Run the app
root.mainloop()
