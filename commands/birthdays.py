from datetime import datetime, timedelta

def get_upcoming_birthdays(contacts, days):
    today = datetime.today().date()
    end_date = today + timedelta(days=days)
    upcoming_birthdays = []

    for contact in contacts.values():
        if contact.birthday:
            birthday_this_year = contact.birthday.replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = contact.birthday.replace(year=today.year + 1)

            if today <= birthday_this_year <= end_date:
                upcoming_birthdays.append(contact)

    return "\n".join(str(contact) for contact in upcoming_birthdays) if upcoming_birthdays else f"No birthdays in the next {days} days."
