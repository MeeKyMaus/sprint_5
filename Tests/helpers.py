import random

def generate_unique_email():
    random_number = random.randint(100, 999)  # Случайное трехзначное число
    return f"testuser_{random_number}@yandex.com"
