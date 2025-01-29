import datetime
from lunarcalendar import Converter, Solar, Lunar, DateNotExist

# variables
ZODIAC = [
    'Tiger', 'Rabbit',
    'Dragon', 'Snake',
    'Horse', 'Goat',
    'Monkey', 'Rooster',
    'Dog', 'Pig',
    'Rat', 'Ox'
]

ELEMENTS = [
    'Wood',
    'Fire',
    'Earth',
    'Metal',
    'Water'
]

YEARS_AND_ELEMENTS = [
    [1900, 3],
    [1901, 3],
    [1902, 4],
    [1903, 4],
    [1904, 0],
    [1905, 0],
    [1906, 1],
    [1907, 1],
    [1908, 2],
    [1909, 2]
]

MONTH_ELEMENT_INDEXES_ACCORDING_TO_YEAR_ELEMENT = [
    # months elements indexes according to the element of the year
    # from january to december
    
    # yang metal
    [2,2,3,3,4,4,0,0,1,1,2,2],
    # yin metal
    [3,3,4,4,0,0,1,1,2,2,3,3],
    # yang water
    [4,4,0,0,1,1,2,2,3,3,4,4],
    # yin water
    [0,0,1,1,2,2,3,3,4,4,0,0],
    # yang wood
    [1,1,2,2,3,3,4,4,0,0,1,1], 
    # yin wood
    [2,2,3,3,4,4,0,0,1,1,2,2],
    # yang fire
    [3,3,4,4,0,0,1,1,2,2,3,3],
    # yin fire
    [4,4,0,0,1,1,2,2,3,3,4,4],
    # yang earth
    [0,0,1,1,2,2,3,3,4,4,0,0],
    # yin earth
    [1,1,2,2,3,3,4,4,0,0,1,1]   
]

# methods
def getYearZodiac(year):
    while year < 2010:
        year += 12
    while year > 2021:
        year -= 12
    return ZODIAC[year-2010]

def getDayZodiac(year, month, day):
    base_date = datetime.date(1900, 1, 31)
    current_date = datetime.date(year, month, day)
    delta_days = (current_date - base_date).days
    index = (delta_days % 12)+2 
    if index == 12:
        index = 0
    if index == 13:
        index = 1
    return ZODIAC[index]

def getYearElementIndex(lunar_year):
    if lunar_year > 1909:
        while lunar_year > 1909:
            lunar_year -= 10
    if lunar_year < 1900:
        while lunar_year < 1900:
            lunar_year += 10
    return YEARS_AND_ELEMENTS[lunar_year - 1900][1]

def getMonthElementIndex(lunar_year, lunar_month):
    if lunar_year > 1909:
        while lunar_year > 1909:
            lunar_year -= 10
    if lunar_year < 1900:
        while lunar_year < 1900:
            lunar_year += 10
    lunar_year -= 1900
    return MONTH_ELEMENT_INDEXES_ACCORDING_TO_YEAR_ELEMENT[lunar_year][lunar_month-1]

def getDayElementIndex(year, month, day):
    base_date = datetime.date(1900, 1, 1)
    current_date = datetime.date(year, month, day)
    delta_days = (current_date - base_date).days
    if (delta_days % 10) % 2 != 0:
        return int(((delta_days % 10) - 1)/2)
    else:
        return int((delta_days % 10)/2)

# main code
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))

birthday = Solar(year,month,day)
birthday_in_lunar = Converter.Solar2Lunar(birthday)

year_zodiac = getYearZodiac(year)
month_zodiac = ZODIAC[birthday_in_lunar.month - 1]
day_zodiac = getDayZodiac(year, month, day)

year_element = ELEMENTS[getYearElementIndex(birthday_in_lunar.year)]
month_element = ELEMENTS[getMonthElementIndex(birthday_in_lunar.year, birthday_in_lunar.month)]
day_element = ELEMENTS[getDayElementIndex(year, month, day)]

# final result
print(f'Year pillar: {year_element} {year_zodiac}')
print(f'Month pillar: {month_element} {month_zodiac}')
print(f'Day pillar: {day_element} {day_zodiac}')