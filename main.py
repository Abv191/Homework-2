from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    today = datetime.now().date()
    next_week = today + timedelta(days=7)
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    birthdays_by_day = {weekday: [] for weekday in weekdays}

    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        if today <= birthday < next_week:
            weekday = weekdays[birthday.weekday()]
            birthdays_by_day[weekday].append(name)

    for weekday, names in birthdays_by_day.items():
        if names:
            print(f"{weekday}: {', '.join(names)}")

# Приклад використання
users = [
    {'name': 'John', 'birthday': datetime(2023, 6, 28)},
    {'name': 'Alice', 'birthday': datetime(2023, 6, 30)},
    {'name': 'Bob', 'birthday': datetime(2023, 7, 2)},
    {'name': 'Kate', 'birthday': datetime(2023, 7, 3)},
    {'name': 'Mike', 'birthday': datetime(2023, 7, 5)}
]

get_birthdays_per_week(users)