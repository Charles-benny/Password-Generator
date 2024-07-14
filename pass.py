import tkinter as tk
from tkinter import Label, ttk, messagebox
import random
import string
import pyperclip

def generate_password(username, length=12, exclude_similar=False, avoid_consecutive=False):
    if length < 8 or length > 15:
        raise ValueError("Password length must be between 8 and 15 characters")

    special_characters = "@#$%^*&!~"
    if exclude_similar:
        similar_characters = "im1Po0O"
        all_characters = ''.join(set(string.ascii_letters + string.digits + special_characters) - set(similar_characters))
    else:
        all_characters = string.ascii_letters + string.digits + special_characters

    while True:
        password = []
        password.append(random.choice(string.digits))
        password.append(random.choice(string.ascii_letters))
        password.append(random.choice(special_characters))
        password.extend(random.choice(all_characters)
                        for _ in range(length - len(password)))
        random.shuffle(password)
        password_str = ''.join(password)

        if avoid_consecutive and any(password_str[i] == password_str[i+1] for i in range(len(password_str) - 1)):
            continue

        if (len(set(password_str)) >= 4 and
            not any(char in username for char in password_str)):
            break

    return password_str

def on_generate():
    username = username_entry.get()
    try:
        length = int(length_entry.get())
        exclude_similar = exclude_similar_var.get()
        avoid_consecutive = avoid_consecutive_var.get()
        password = generate_password(username, length, exclude_similar, avoid_consecutive)
        result_var.set(password)
        check_password_strength(password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def check_password_strength(password):
    strength = 0
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char in "@#$%^*&!~" for char in password):
        strength += 1
    strength_bar['value'] = strength * 25

def copy_to_clipboard():
    password = result_var.get()
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg="#00AA80")

style = ttk.Style()
style.configure("TLabel", background="#00AA80", text="bold",font=("verdana", 13))
style.configure("TButton", background="#4CAF50", bg="#000000", font=("verdana", 12), padding=10)
style.configure("TCheckbutton", background="#00AA80", font=("verdana", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TProgressbar", troughcolor='#f5f5f5', background='#630330')

ttk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10, sticky="W")
username_entry = ttk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10, sticky="E")
ttk.Label(root, text="Password Length (8-15):").grid(row=1, column=0, padx=10, pady=10, sticky="W")
length_entry = ttk.Entry(root)
length_entry.grid(row=1, column=1, padx=10, pady=10, sticky="E")
exclude_similar_var = tk.BooleanVar()
exclude_similar_check = ttk.Checkbutton(root, text="Exclude similar characters (il1Lo0O)", variable=exclude_similar_var)
exclude_similar_check.grid(row=2, columnspan=2, padx=10, pady=5, sticky="W")

avoid_consecutive_var = tk.BooleanVar()
avoid_consecutive_check = ttk.Checkbutton(root, text="Avoid consecutive characters", variable=avoid_consecutive_var)
avoid_consecutive_check.grid(row=3, columnspan=2, padx=10, pady=5, sticky="W")

generate_button = ttk.Button(root, text="Generate Password", command=on_generate)
generate_button.grid(row=4, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, wraplength=300, font=('Helvetica', 12, 'bold'))
result_label.grid(row=5, columnspan=2, padx=10, pady=10)

ttk.Label(root, text="Password Strength:").grid(row=6, columnspan=2)
strength_bar = ttk.Progressbar(root, length=200, mode='determinate', maximum=100)
strength_bar.grid(row=7, columnspan=2, padx=10, pady=5)

copy_button = ttk.Button(root, text="COPY", command=copy_to_clipboard)
copy_button.grid(row=8, columnspan=2, pady=10)

Label(root, text="Developed by: Akash J", font=("verdana", 8), fg="white", bg="#000000").place(relx=1.0, rely=1.0, anchor='se')
root.mainloop()
