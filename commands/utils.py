def validate_field(prompt, validation_func=None, required=False):
    """
    Універсальна функція для запиту значення поля з валідацією.
    """
    while True:
        value = input(prompt).strip()
        if not value and not required:
            return None  # Пусте значення дозволене для необов'язкових полів
        if not validation_func:
            return value  # Якщо валідації немає, повертаємо значення одразу
        try:
            return validation_func(value)
        except ValueError as e:
            print(f"Error: {e}. Please try again.")