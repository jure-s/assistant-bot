def parse_input(user_input):
    """
    Розбиває введення користувача на команду та аргументи.
    """
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args