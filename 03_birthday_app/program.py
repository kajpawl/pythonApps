import datetime


def print_header():
    print('------------------------------')
    print('         BIRTHDAY APP')
    print('------------------------------')
    print()


def get_birthday_information():
    print('When were you born?')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    # this_year_date = datetime.date(target_date.year, original_date.month, original_date.day)
    this_year_date = datetime.date(year=target_date.year, month=original_date.month, day=original_date.day)

    dt = this_year_date - target_date
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print('Your birthday was {} days ago.'.format(abs(days)))
    elif days == 0:
        print('Your birthday is today. Happy Birthday!')
    else:
        print('Your birthday is in {} days.'.format(days))


def main():
    print_header()
    bday = get_birthday_information()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)


main()
