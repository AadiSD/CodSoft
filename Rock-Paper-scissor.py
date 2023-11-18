import tkinter as tk
from tkinter import Label, Button, messagebox
import random


class RockPaperScissorsGame:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        self.root.configure(bg='light gray')

        # Set window dimensions and position it at the center of the screen
        window_width = 400
        window_height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Create and place GUI elements
        self.intro_label = Label(root, text="Welcome to Rock, Paper, Scissors!\nChoose your move:", bg='light gray')
        self.intro_label.pack(pady=10)

        self.rock_button = Button(root, text="Rock", command=lambda: self.play_game("rock"), bg='white')
        self.rock_button.place(x=115, y=50)

        self.paper_button = Button(root, text="Paper", command=lambda: self.play_game("paper"), bg='white')
        self.paper_button.place(x=175, y=50)

        self.scissors_button = Button(root, text="Scissors", command=lambda: self.play_game("scissors"), bg='white')
        self.scissors_button.place(x=235, y=50)

        self.restart_button = Button(root, text="Restart Game", command=self.restart_game, bg='white')
        self.restart_button.place(x=155, y=85)

        # Initialize scores
        self.user_score = 0
        self.computer_score = 0

        # Display scores
        self.score_label = Label(root, text=f"User Score: {self.user_score} | Computer Score: {self.computer_score}",
                                 bg='light gray')
        self.score_label.place(x=115, y=120)

    def play_game(self, user_choice):
        # Simulate computer's random choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        # Determine the winner and update scores
        result = self.determine_winner(user_choice, computer_choice)
        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1

        # Display result and scores in a pop-up window with "Play Again" button
        result_text = f"You chose {user_choice.capitalize()}\nThe computer chose {computer_choice.capitalize()}\n\n{result}\n\nUser Score: {self.user_score} | Computer Score: {self.computer_score}"
        play_again = messagebox.askyesno("Result", result_text + "\n\nDo you want to play again?")
        if play_again:
            # Reset the game for a new round
            self.clear_result()
        else:
            # Close the Tkinter window and exit the application
            self.root.destroy()

    def determine_winner(self, user_choice, computer_choice):
        # Determine the winner of the round
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                (user_choice == 'paper' and computer_choice == 'rock') or \
                (user_choice == 'scissors' and computer_choice == 'paper'):
            return "You win!"
        else:
            return "You lose!"

    def clear_result(self):
        # Clear the result and reset game state for a new round
        self.intro_label.config(text="Choose your move:")
        self.update_score_label()

    def restart_game(self):
        # Destroy the current window and create a new one for restarting the game
        self.root.destroy()
        new_root = tk.Tk()
        new_game = RockPaperScissorsGame(new_root)
        new_root.mainloop()

    def update_score_label(self):
        # Update the displayed scores
        self.score_label.config(text=f"User Score: {self.user_score} | Computer Score: {self.computer_score}")


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
