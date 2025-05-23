import random
from config import FIRST_NAMES, DOMAINS

def generate_gmail():
    first = random.choice(FIRST_NAMES)
    number = random.randint(1000, 9999)
    email = f"{first.lower()}{number}{random.choice(DOMAINS)}"
    password = f"{first.lower()}@{number}"
    recovery = f"{first.lower()}.recovery@gmail.com"
    return first, email, password, recovery