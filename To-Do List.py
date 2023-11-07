import tkinter as tk

# Initialize a list to store tasks with their completion status
tasks = []

# Initialize a variable to track the visibility of task status
status_visible = False

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        tasks.append((task, False))

# Function to remove a task
def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        task, _ = tasks[task_index]
        listbox.delete(task_index)
        tasks.pop(task_index)

# Function to update a task
def update_task():
    selected_task = listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        updated_task = entry.get()
        listbox.delete(task_index)
        listbox.insert(task_index, updated_task)
        tasks[task_index] = (updated_task, tasks[task_index][1])
        entry.delete(0, tk.END)

# Function to toggle the completion status of a task
def toggle_completion():
    selected_task = listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        task, completed = tasks[task_index]
        tasks[task_index] = (task, not completed)
        list_tasks()
        list_tasks()
# Function to list tasks and toggle status visibility
def list_tasks():
    global status_visible
    listbox.delete(0, tk.END)
    for task, completed in tasks:
        task_status = "✓" if completed else "✗"
        if status_visible:
            listbox.insert(tk.END, f"{task_status} {task}")
        else:
            listbox.insert(tk.END, task)
    status_visible = not status_visible

# Function to clear all input fields
def clear_all():
    entry.delete(0, tk.END)
    listbox.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("To-Do List")
root.configure(bg='light gray')

# Set window dimensions and position
window_width = 600
window_height = 450

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a listbox to display tasks
listbox = tk.Listbox(root, width=90, height=18)
listbox.pack(pady=10)

# Create an entry widget for adding and updating tasks
entry = tk.Entry(root, width=90)
entry.pack(pady=5)

# Create buttons for various actions
add_button = tk.Button(root, text="Add Task", command=add_task, width=24)
add_button.place(x=25, y=350)
add_button.configure(bg='white')

remove_button = tk.Button(root, text="Remove Task", command=remove_task, width=24)
remove_button.place(x=210, y=350)
remove_button.configure(bg='white')

update_button = tk.Button(root, text="Update Task", command=update_task, width=24)
update_button.place(x=395, y=350)
update_button.configure(bg='white')

toggle_completion_button = tk.Button(root, text="Toggle Completion", command=toggle_completion, width=24)
toggle_completion_button.place(x=25, y=380)
toggle_completion_button.configure(bg='white')

status_button = tk.Button(root, text="Status", command=list_tasks, width=24)
status_button.place(x=210, y=380)
status_button.configure(bg='white')

clear_button = tk.Button(root, text="Clear", command=clear_all, width=24)
clear_button.place(x=395, y=380)
clear_button.configure(bg='white')

# Start the main event loop
root.mainloop()
