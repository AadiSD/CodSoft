import random
import string
import tkinter as tk
from tkinter import Label, Entry, Button

# Made By @AadiSD

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    length = max(8, length)
    return ''.join(random.choice(all_characters) for _ in range(length))

def on_validate(P):
    if P.isdigit():
        return True
    else:
        return False

def generate_and_display_password():
    length = length_entry.get()
    try:
        length = int(length)
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return

    password = generate_password(length)
    result_label.config(text=f"Generated Password: {password}")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

window_width = 300
window_height = 200

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.configure(bg='light gray')

# Create and place the widgets
Label(window, text="Enter the desired length of the password:", bg='light gray').pack(pady=10)
length_entry = Entry(window, validate='key')
length_entry.configure(validatecommand=(length_entry.register(on_validate), '%P'))
length_entry.pack(pady=10)
length_entry.configure(bg='white')

generate_button = Button(window, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=10)
generate_button.configure(background='white')

result_label = Label(window, text="")
result_label.pack(pady=10)
result_label.configure(bg='light gray')

# Start the main event loop
window.mainloop()
