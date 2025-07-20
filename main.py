import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Hardcoded credentials
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Main window
root = tk.Tk()
root.title("Login Form")
root.geometry("350x250")
root.configure(bg="white")

# Header
tk.Label(root, text="Login", font=("Helvetica", 20, "bold"), fg="blue", bg="white").pack(pady=10)

# Username
tk.Label(root, text="Username:", fg="blue", bg="white", anchor="w").pack(fill="x", padx=30)
entry_username = tk.Entry(root, bg="lightblue")
entry_username.pack(padx=30, fill="x")

# Password
tk.Label(root, text="Password:", fg="blue", bg="white", anchor="w").pack(fill="x", padx=30, pady=(10, 0))
entry_password = tk.Entry(root, show="*", bg="lightblue")
entry_password.pack(padx=30, fill="x")

# Login button
tk.Button(root, text="Login", bg="blue", fg="white", command=login).pack(pady=20)

root.mainloop()

