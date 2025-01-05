from datetime import datetime


def transformation_date(booked_dates, date_for_booking):
    b_d, d_f_b = [], []

    for date in booked_dates:
        if '-' in date:
            dt = date.split('-')
            b_d.append(list(map(lambda day: datetime.strptime(day, '%d.%m.%Y'), dt)))
            continue
        b_d.append(datetime.strptime(date, '%d.%m.%Y'))

    for date in date_for_booking:
        if '-' in date:
            dt = date.split('-')
            d_f_b.append(list(map(lambda day: datetime.strptime(day, '%d.%m.%Y'), dt)))
            continue
        d_f_b.append(datetime.strptime(date, '%d.%m.%Y'))

    return b_d, d_f_b


def is_available_date(booked_dates, date_for_booking):
    booked_dates, date_for_booking = transformation_date(booked_dates, date_for_booking)
    print(booked_dates, date_for_booking, sep='\n')

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))
