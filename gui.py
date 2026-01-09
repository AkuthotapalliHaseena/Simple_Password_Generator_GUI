import tkinter as tk
from tkinter import messagebox
from password_generator import PasswordGenerator

class PasswordGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("300x300")

        tk.Label(root, text="Password Length").grid(row=0, column=0, pady=10, padx=10, sticky="w")
        self.length_entry = tk.Entry(root,width=10)
        self.length_entry.grid(row=0,column=1,pady=10)

        self.letters_var = tk.BooleanVar()
        self.numbers_var = tk.BooleanVar()
        self.symbols_var = tk.BooleanVar()

        tk.Checkbutton(root, text="Include Letters", variable=self.letters_var).grid(row=1, column=0, columnspan=2, sticky="w", padx=20)
        tk.Checkbutton(root, text="Include Numbers", variable=self.numbers_var).grid(row=2, column=0, columnspan=2, sticky="w", padx=20)
        tk.Checkbutton(root, text="Include Symbols", variable=self.symbols_var).grid(row=3, column=0, columnspan=2, sticky="w", padx=20)

        tk.Button(root, text="Generate Password", command=self.generate_password).grid(row=4, column=0, columnspan=2, pady=15)

        self.result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())

            generator = PasswordGenerator(
                length,
                self.letters_var.get(),
                self.numbers_var.get(),
                self.symbols_var.get()
            )

            password = generator.generate()
            self.result_label.config(text=password)

        except ValueError as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGUI(root)
    root.mainloop()
