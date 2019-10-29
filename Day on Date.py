import calendar


def check_leap(y):
    if y % 100 == 0:
        if y % 400 == 0:
            return True
        else:
            return False
    else:
        if y % 4 == 0:
            return True
        else:
            return False


def check_valid_date(dt, m, l):
    if l:
        if m == 2:
            if dt < 30:
                return True
            else:
                return False
        else:
            if m < 8:
                if m % 2 == 1:
                    if dt < 32:
                        return True
                    else:
                        return False
                else:
                    if dt < 31:
                        return True
                    else:
                        return False
            else:
                if m % 2 == 0:
                    if dt < 32:
                        return True
                    else:
                        return False
                else:
                    if dt < 31:
                        return True
                    else:
                        return False
    else:
        if m == 2:
            if dt < 29:
                return True
            else:
                return False
        else:
            if m < 8:
                if m % 2 == 1:
                    if dt < 32:
                        return True
                    else:
                        return False
                else:
                    if dt < 31:
                        return True
                    else:
                        return False
            else:
                if m % 2 == 0:
                    if dt < 32:
                        return True
                    else:
                        return False
                else:
                    if dt < 31:
                        return True
                    else:
                        return False


def get_day(day_in):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[day_in]

while 1:
    year = int(input("Enter year (from 1970): "))
    if year < 1970:
        print('Enter an year starting from 1970.')
        print()
    else:
        break

while 1:
    month = int(input("Enter month number: "))
    if 0 < month <= 12:
        break
    else:
        print('Enter a valid month number.')
        print()

leap = check_leap(year)

while 1:
    date = int(input("Enter date: "))
    if date > 0 and check_valid_date(date, month, leap):
        break
    else:
        print('Enter a valid date.')
        print()

day_index = calendar.weekday(year, month, date)
day = get_day(day_index)
print(date, "/", month, "/", year, "falls on", day, ".")
