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
