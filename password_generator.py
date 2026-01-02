
import random
import string

class PasswordGenerator:
    def __init__(self, length):
        self.length = length

    def generate(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password
