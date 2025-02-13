import methods.build_chart as buildChart
import methods.calc_elements as calcElements

# main code
year = -1
while year == -1:
    year = input("Enter a year: ")
    try:
        year = int(year)
        if year < 0:
            print("Year must be a positive number")
            year = -1
    except:
        print("Year must be a number")
        year = -1
        
month = -1
while month == -1:
    print('January - 1\nFebruary - 2\nMarch - 3\nApril - 4\nMay - 5\nJune - 6\nJuly - 7\nAugust - 8\nSeptember - 9\nOctober - 10\nNovember - 11\nDecember - 12')
    month = input("Enter a month: ")
    try:
        month = int(month)
        if month < 1 or month > 12:
            print('You must insert a valid month (1-12)')
            month = -1
    except:
        print("Month must be a number")
        month = -1

day = -1
while day == -1:
    day = input("Enter a day: ")
    try:
        day = int(day)
        if day < 1 or day > 31:
            print("You must insert a valid day")
            day = -1
    except:
        print("Day must be a number")
        day = -1

option = ''
while option != 'y' and option != 'n':
    option = input("Show hour pillar? (y/n): ").lower().strip()
    if option != 'y' and option != 'n':
        print("You must insert a valid option!")
if option == 'y':
    hour = -1
    while hour == -1:
        hour = input("Enter an hour (0-23): ")
        try:
            hour = int(hour)
            if hour < 0 or hour > 23:
                print("You must insert a valid hour (0-23)")
                hour = -1
        except:
            print("Hour must be a number")
            hour = -1

    daylight_saving_time = ''
    while daylight_saving_time != 'y' and daylight_saving_time != 'n':
        daylight_saving_time = input("There was DST when you were born? (y/n): ").lower().strip()
        if daylight_saving_time != 'y' and daylight_saving_time != 'n':
            print("You must insert a valid option!")
    if daylight_saving_time == 'y':
        daylight_saving_time = True
    elif daylight_saving_time == 'n':
        daylight_saving_time = False

year_zodiac = buildChart.get_year_earthly_branch(year, month, day)
month_zodiac = buildChart.get_month_earthly_branch(year, month, day)
day_zodiac = buildChart.get_day_earthly_branch(year, month, day)

year_element = buildChart.get_year_heavenly_stem(year, month, day)
month_element = buildChart.get_month_heavenly_stem(year, month, day)
day_element = buildChart.get_day_heavenly_stem(year, month, day)

if option == 'y':
    hour_zodiac = buildChart.get_hour_earthly_branch(hour, daylight_saving_time)
    hour_element = buildChart.get_hour_heavenly_stem(year, month, day, hour, daylight_saving_time)
    print('                  H  D  M  Y')
    print('Heavenly Stem    ', hour_element, day_element, month_element, year_element)
    print('Earthly Branches ', hour_zodiac, day_zodiac, month_zodiac, year_zodiac)
    elements = calcElements.calc_element_percentage_fullchart(year_element, year_zodiac, month_element, month_zodiac, day_element, day_zodiac, hour_element, hour_zodiac)
else:
    print('                  D  M  Y')
    print('Heavenly Stem    ', day_element, month_element, year_element)
    print('Earthly Branches ', day_zodiac, month_zodiac, year_zodiac)
    elements = calcElements.calc_element_percentage_unknown_hour(year_element, year_zodiac, month_element, month_zodiac, day_element, day_zodiac)

print('\nElements: ')
print(f'Wood: {format(elements["wood"], ".2f")}% ({calcElements.get_element_status(elements["wood"])})')
print(f'Fire: {format(elements["fire"], ".2f")}% ({calcElements.get_element_status(elements["fire"])})')
print(f'Earth: {format(elements["earth"], ".2f")}% ({calcElements.get_element_status(elements["earth"])})')
print(f'Metal: {format(elements["metal"], ".2f")}% ({calcElements.get_element_status(elements["metal"])})')
print(f'Water: {format(elements["water"], ".2f")}% ({calcElements.get_element_status(elements["water"])})')
