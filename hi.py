import tkinter as tk

def generate_greeting():
    first_name = entry_first.get()
    last_name = entry_last.get()
    
    # Creating greeting message
    greeting = f"Hello, {last_name} {first_name}!"
    
    # Extracting first 4 characters
    short_greeting = greeting[:4] * 3
    
    # Displaying output
    label_result.config(text=f"{greeting} {short_greeting}")

# Create main window
root = tk.Tk()
root.title("Greeting Generator")

# First Name Entry
tk.Label(root, text="Enter First Name:").pack()
entry_first = tk.Entry(root)
entry_first.pack()

# Last Name Entry
tk.Label(root, text="Enter Last Name:").pack()
entry_last = tk.Entry(root)
entry_last.pack()

# Button to generate greeting
button = tk.Button(root, text="Generate Greeting", command=generate_greeting)
button.pack()

# Label to display result
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack()

# Run the application
root.mainloop()
