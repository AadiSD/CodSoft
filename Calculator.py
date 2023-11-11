import tkinter as tk
from tkinter import Label, Entry, Button, StringVar, messagebox

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculate_result():
    num1 = num1_entry.get()
    num2 = num2_entry.get()
    operation = operation_var.get()

    if operation == "Operation" or not operation:
        messagebox.showwarning("Error", "Please select a valid operation.")
        return

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")
        return

    if operation == "Addition (+)":
        result = add(num1, num2)
    elif operation == "Subtraction (-)":
        result = subtract(num1, num2)
    elif operation == "Multiplication (*)":
        result = multiply(num1, num2)
    elif operation == "Division (/)":
        result = divide(num1, num2)

    result_label.config(text=f"The result of {operation.lower()} is: {result}")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

window_width = 325
window_height = 275

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.configure(bg='light gray')

# Create and place the widgets
Label(window, text="Enter the first number:", bg='light gray').grid(row=0, column=0, padx=10, pady=5)
num1_entry = Entry(window, validate='key', validatecommand=(window.register(is_float), '%P'))
num1_entry.grid(row=0, column=1, padx=10, pady=5)
num1_entry.configure(bg='white')

Label(window, text="Enter the second number:", bg='light gray').grid(row=1, column=0, padx=10, pady=5)
num2_entry = Entry(window, validate='key', validatecommand=(window.register(is_float), '%P'))
num2_entry.grid(row=1, column=1, padx=10, pady=5)
num2_entry.configure(bg='white')

Label(window, text="Select operation:", bg='light gray').grid(row=2, column=0, padx=10, pady=5)
operations = ["Operation", "Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]
operation_var = StringVar(window)
operation_var.set(operations[0])  # Default value

operation_menu = tk.OptionMenu(window, operation_var, *operations)
operation_menu.grid(row=2, column=1, padx=10, pady=5)
operation_menu.configure(bg='white')

calculate_button = Button(window, text="Calculate", command=calculate_result, bg='white')
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = Label(window, text="", bg='light gray')
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Start the main event loop
window.mainloop()
