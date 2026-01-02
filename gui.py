
import tkinter as tk
from tkinter import messagebox
from password_generator import PasswordGenerator

class PasswordGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Password Generator")

        self.label = tk.Label(root, text="Enter Password Length")
        self.label.pack(pady=5)

        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=5)

        self.generate_btn = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_btn.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            generator = PasswordGenerator(length)
            password = generator.generate()
            self.result_label.config(text=password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGUI(root)
    root.mainloop()
