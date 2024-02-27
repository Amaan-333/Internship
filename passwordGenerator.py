import random
import string
import tkinter as tk
from tkinter import messagebox

def condition_random_password():
    length = length_entry.get()
    alpha_count = alpha_count_entry.get()
    digits_count = digits_count_entry.get()
    special_count = special_count_entry.get()

    if length.isdigit() and alpha_count.isdigit() and digits_count.isdigit() and special_count.isdigit():
        characters_count = int(alpha_count) + int(digits_count) + int(special_count)
        if characters_count > int(length):
            messagebox.showerror("Error", "The entered Character Count is Greater than the total Password Length")
            return

        password = []
        for i in range(int(alpha_count)):
            password.append(random.choice(string.ascii_letters))
        for i in range(int(digits_count)):
            password.append(random.choice(string.digits))
        for i in range(int(special_count)):
            password.append(random.choice(string.punctuation))
        if characters_count < int(length):
            password += random.choices(string.ascii_letters + string.digits + string.punctuation, k=int(length) - characters_count)

        password_str = ''.join(password)
        messagebox.showinfo("Generated Password", password_str)
    else:
        messagebox.showerror("Error", "Please enter valid numeric values")

def random_password():
    length = length_entry.get()
    if length.isdigit():
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=int(length)))
        messagebox.showinfo("Generated Password", password)
    else:
        messagebox.showerror("Error", "Please enter a valid length")

# GUI setup
root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

alpha_count_label = tk.Label(root, text="Alphabets Count:")
alpha_count_label.grid(row=1, column=0)
alpha_count_entry = tk.Entry(root)
alpha_count_entry.grid(row=1, column=1)

digits_count_label = tk.Label(root, text="Digits Count:")
digits_count_label.grid(row=2, column=0)
digits_count_entry = tk.Entry(root)
digits_count_entry.grid(row=2, column=1)

special_count_label = tk.Label(root, text="Special Characters Count:")
special_count_label.grid(row=3, column=0)
special_count_entry = tk.Entry(root)
special_count_entry.grid(row=3, column=1)

condition_button = tk.Button(root, text="Generate Password (Condition Based)", command=condition_random_password)
condition_button.grid(row=4, column=0, columnspan=2)

random_button = tk.Button(root, text="Generate Random Password", command=random_password)
random_button.grid(row=5, column=0, columnspan=2)

root.mainloop()
