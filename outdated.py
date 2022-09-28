from sys import argv

while True:
    months = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }

    AD = input("Date: ")

    try:
        month, day, year = AD.split("/")
        if (int(month)) >= 1 and int((month)) <= 12 and (int(day)) >= 1 and (int(day)) <= 31:
            break

    except:
        try:
            old_month, old_day, old_year = AD.split()
            for month in months:
                month = months[month]
            print(f"{year}/{month}/{day}")
        except:

            # format date into index
            # Months
            # Sort months
