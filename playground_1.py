import tkinter as tk


# Test if we have installed tkinter
#tk._test()

# Initialize our main window
root = tk.Tk()
root.title("My Calculator")


# Enty widget for the calculator display
entry = tk.Entry (root, width=30, font=('Arial', 30), borderwidth=5, justify='right')
entry.grid(row=0, column=0, columnspan=4)


# Function to handle button clicks
def button_click(value):
    # Get the current text in the entry widget
    current = entry.get()
    # Clear the current text in the entry widget
    entry.delete(0, tk.END)
    # Append the clicked button's value to the existing text
    entry.insert(tk.END, current + str(value))
 
# Function to evaluate the expression   
def evaluate():
    try:
        result = eval(entry.get()) # Evaluate the mathematical expression
        entry.delete(0, tk.END) # Clear the entry field
        entry.insert(tk.END, result) # Insert the calculated result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)


# Button layout

button_texts = [
   ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),  # First row: numbers and divide
   ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),  # Second row: numbers and multiply
   ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),  # Third row: numbers and subtract
   ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),  # Fourth row: 0, decimal, equals, and add
   ('C', 5, 0)  # Fifth row: clear button
]

# Loop through the buttons and create buttons dynamically 
for (text, row, col) in button_texts:
    if text == '=':
        button = tk.Button (
            root,
            text=text,
            padx=20, pady=20,
            font=('Arial', 18),
            command=evaluate
        )
    elif text == 'C':
        button = tk.Button (
            root,
            text=text,
            padx=20, pady=20,
            font=('Arial', 18),
            command=clear
        )
    else:
        button = tk.Button (
            root,
            text=text,
            padx=20, pady=20,
            font=('Arial', 18),
            command=lambda
            t=text: button_click(t)
        )
    
    # Place the buttons on the grid
    button.grid(row=row, column=col)
        



# Run the application
root.mainloop()