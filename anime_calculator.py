import tkinter as tk
from tkinter import messagebox, font
import math

# Functions for calculations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def power(x, y):
    return x ** y

def logarithm(x, base):
    if x <= 0 or base <= 0 or base == 1:
        return "Error: Invalid input for logarithm!"
    return math.log(x, base)

# Function to handle button clicks
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        elif operation == "Division":
            result = divide(num1, num2)
        elif operation == "Power":
            result = power(num1, num2)
        elif operation == "Logarithm":
            result = logarithm(num1, num2)
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to handle numpad input
def add_to_entry(value):
    focused_entry = root.focus_get()
    if focused_entry in [entry_num1, entry_num2]:
        focused_entry.insert(tk.END, value)

# Create the main window
root = tk.Tk()
root.title("Anime Calculator")
root.geometry("800x500")  # Larger window size
root.configure(bg="#f0f0f0")

# Anime-style font
try:
    anime_font = font.Font(family="Comic Sans MS", size=14, weight="bold")  # Increased font size
except:
    anime_font = font.Font(size=14, weight="bold")  # Fallback font

# Header
header = tk.Label(root, text="Anime Calculator", font=(anime_font, 24), bg="#f0f0f0", fg="#ff6f61")
header.pack(pady=10)

# Main container frame
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack()

# Left frame (input fields)
left_frame = tk.Frame(main_frame, bg="#f0f0f0")
left_frame.grid(row=0, column=0, padx=20)

# Input fields with larger size
tk.Label(left_frame, text="Number 1:", font=anime_font, bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(left_frame, font=anime_font, bg="#ffffff", fg="#333333", relief="flat", width=15)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(left_frame, text="Number 2:", font=anime_font, bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(left_frame, font=anime_font, bg="#ffffff", fg="#333333", relief="flat", width=15)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Operation selection
tk.Label(left_frame, text="Operation:", font=anime_font, bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10)
operations = ["Addition", "Subtraction", "Multiplication", "Division", "Power", "Logarithm"]
operation_var = tk.StringVar(value=operations[0])
operation_menu = tk.OptionMenu(left_frame, operation_var, *operations)
operation_menu.config(font=anime_font, bg="#ff6f61", fg="#ffffff", relief="flat")
operation_menu.grid(row=2, column=1, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(left_frame, text="Calculate", font=anime_font, 
                            bg="#ff6f61", fg="#ffffff", relief="flat", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Result display
result_label = tk.Label(left_frame, text="Result: ", font=anime_font, bg="#f0f0f0", fg="#333333")
result_label.grid(row=4, column=0, columnspan=2)

# Right frame (numpad)
right_frame = tk.Frame(main_frame, bg="#f0f0f0")
right_frame.grid(row=0, column=1, padx=20)

# Numpad buttons
numpad_buttons = [
    ('7', '8', '9'),
    ('4', '5', '6'),
    ('1', '2', '3'),
    ('0', '.', '⌫')
]

for i, row in enumerate(numpad_buttons):
    for j, btn in enumerate(row):
        btn_color = "#ff6f61" if btn == '⌫' else "#a1c9f1"
        tk.Button(right_frame, text=btn, font=anime_font, width=4, height=2,
                 bg=btn_color, fg="#333333", relief="flat",
                 command=lambda v=btn: add_to_entry(v) if v != '⌫' else delete_last_char()).grid(row=i, column=j, padx=2, pady=2)

def delete_last_char():
    focused_entry = root.focus_get()
    if focused_entry in [entry_num1, entry_num2]:
        focused_entry.delete(len(focused_entry.get())-1, tk.END)

# Run the application
root.mainloop()