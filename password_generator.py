
import random
import string

class PasswordGenerator:
    def __init__(self, length, use_letters, use_numbers, use_symbols):
        self.length = length
        self.use_letters = use_letters
        self.use_numbers = use_numbers
        self.use_symbols = use_symbols

    def generate(self):
        characters = ""

        if self.use_letters:
            characters += string.ascii_letters
        if self.use_numbers:
            characters += string.digits
        if self.use_symbols:
            characters += string.punctuation

        if not characters:
            raise ValueError("Select at least one character type")

        return ''.join(random.choice(characters) for _ in range(self.length))
