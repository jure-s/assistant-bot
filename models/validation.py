import re
from datetime import datetime

def validate_phone(phone):
    if not phone.isdigit() or len(phone) != 10:
        raise ValueError("Phone number must have exactly 10 digits.")
    return phone

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(pattern, email):
        raise ValueError("Invalid email format.")
    return email

def validate_birthday(birthday):
    try:
        return datetime.strptime(birthday, "%d.%m.%Y").date()
    except ValueError:
        raise ValueError("Invalid birthday format. Use DD.MM.YYYY.")
