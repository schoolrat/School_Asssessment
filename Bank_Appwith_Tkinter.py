from tkinter import *

# Create the main window
root = Tk()
root.title("Simple Bank App")
root.geometry("300x250")

# Global balance variable
balance = 0

# Function to update balance display
def update_balance():
    balance_label.config(text=f"Balance: £{balance}")

# Deposit function
def deposit():
    global balance
    try:
        amount = int(entry.get())
        balance += amount
        update_balance()
        message_label.config(text=f"Deposited £{amount}")
    except ValueError:
        message_label.config(text="Please enter a valid number")

# Withdraw function
def withdraw():
    global balance
    try:
        amount = int(entry.get())
        balance -= amount
        update_balance()
        message_label.config(text=f"Withdrew £{amount}")
    except ValueError:
        message_label.config(text="Please enter a valid number")

# Exit function
def exit_app():
    root.destroy()

# Widgets
Label(root, text="Enter amount:").pack(pady=5)
entry = Entry(root)
entry.pack(pady=5)

Button(root, text="Deposit", command=deposit).pack(pady=5)
Button(root, text="Withdraw", command=withdraw).pack(pady=5)
Button(root, text="Exit", command=exit_app).pack(pady=5)

balance_label = Label(root, text=f"Balance: £{balance}", font=("Arial", 12, "bold"))
balance_label.pack(pady=10)

message_label = Label(root, text="", fg="blue")
message_label.pack(pady=5)

# Start the GUI loop
root.mainloop()