import tkinter as tk
from tkinter import messagebox

# Function to add a new task to the list
def add_task():
    task_text = task_entry.get()
    if task_text:
        task_listbox.insert(tk.END, task_text)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove the selected task from the list
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to remove.")

# Function to mark a task as completed
def complete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"{task} - Completed")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as completed.")

# Function to toggle the visibility of the popup window
def toggle_popup():
    if root.state() == 'normal':
        root.withdraw()  # Hide the window
    else:
        root.deiconify()  # Show the window

# Set up the main application window
root = tk.Tk()
root.title("Desktop To-Do List")
root.geometry("300x400")
root.config(bg="lightblue")

# Entry field to input tasks
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Button to add a new task
add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=25, height=10, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

# Button to remove a selected task
remove_task_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_task_button.pack(pady=5)

# Button to mark a selected task as completed
complete_task_button = tk.Button(root, text="Mark as Completed", command=complete_task)
complete_task_button.pack(pady=5)

# Button to hide the application (toggle visibility)
toggle_button = tk.Button(root, text="Hide / Show", command=toggle_popup)
toggle_button.pack(pady=5)

# Start the application
root.mainloop()
