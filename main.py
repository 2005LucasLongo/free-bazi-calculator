import datetime
from lunarcalendar import Converter, Solar

# variables
ZODIAC = [
    '寅', '卯', # Tiger, Rabbit 0 1
    '辰', '巳', # Dragon, Snake 2 3
    '午', '未', # Horse, Goat 4 5
    '申', '酉', # Monkey, Rooster 6 7
    '戌', '亥', # Dog, Pig 8 9
    '子', '丑' # Rat, Ox 10 11
]

ELEMENTS = [
    '甲', '乙', # yang-yin wood 0 1
    '丙', '丁', # yang-yin fire 2 3
    '戊', '己', # yang-yin earth 4 5
    '庚', '辛', # yang-yin metal 6 7
    '壬', '癸', # yang-yin water 8 9
]

YEARS_AND_ELEMENTS = [
    [1900, 6],
    [1901, 7],
    [1902, 8],
    [1903, 9],
    [1904, 0],
    [1905, 1],
    [1906, 2],
    [1907, 3],
    [1908, 4],
    [1909, 5]
]

MONTH_ELEMENT_INDEXES_ACCORDING_TO_YEAR_ELEMENT = [
    # months elements indexes according to the element of the year
    # from january to december
    
    # yang metal
    [4,5,6,7,8,9,0,1,2,3,4,5],
    # yin metal
    [6,7,8,9,0,1,2,3,4,5,6,7],
    # yang water
    [8,9,0,1,2,3,4,5,6,7,8,9],
    # yin water
    [0,1,2,3,4,5,6,7,8,9,0,1],
    # yang wood
    [2,3,4,5,6,7,8,9,0,1,2,3], 
    # yin wood
    [4,5,6,7,8,9,0,1,2,3,4,5],
    # yang fire
    [6,7,8,9,0,1,2,3,4,5,6,7],
    # yin fire
    [8,9,0,1,2,3,4,5,6,7,8,9],
    # yang earth
    [0,1,2,3,4,5,6,7,8,9,0,1],
    # yin earth
    [2,3,4,5,6,7,8,9,0,1,2,3],   
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

def getHourZodiac(hour, dst):
    if dst == 'y':
        hour -= 1
    if hour < 0 or hour > 23:
        raise 'Invalid hour'
    elif hour == 0 or hour == 23:
        return ZODIAC[10] # Rat
    elif hour == 1 or hour == 2:
        return ZODIAC[11] # Ox
    elif hour == 3 or hour == 4:
        return ZODIAC[0] # Tiger
    elif hour == 5 or hour == 6:
        return ZODIAC[1] # Rabbit
    elif hour == 7 or hour == 8:
        return ZODIAC[2] # Dragon
    elif hour == 9 or hour == 10:
        return ZODIAC[3] # Snake
    elif hour == 11 or hour == 12:
        return ZODIAC[4] # Horse
    elif hour == 13 or hour == 14:
        return ZODIAC[5] # Goat
    elif hour == 15 or hour == 16:
        return ZODIAC[6] # Monkey
    elif hour == 17 or hour == 18:
        return ZODIAC[7] # Rooster
    elif hour == 19 or hour == 20:
        return ZODIAC[8] # Dog
    else:
        return ZODIAC[9] # Pig

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
    return delta_days % 10

def getHourElementIndex(hour_zodiac, day_element):
    
    HOUR_ELEMENT_INDEX_LIST = [
        # Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, Pig
        [0,1,2,3,4,5,6,7,8,9,0,1], # madeira yang
        [2,3,4,5,6,7,8,9,0,1,2,3], # maderia yin
        [4,5,6,7,8,9,0,1,2,3,4,5], # fogo yang
        [6,7,8,9,0,1,2,3,4,5,6,7], # fogo yin
        [8,9,0,1,2,3,4,5,6,7,8,9], # terra yang
        [0,1,2,3,4,5,6,7,8,9,0,1], # terra yin
        [2,3,4,5,6,7,8,9,0,1,2,3], # metal yang
        [4,5,6,7,8,9,0,1,2,3,4,5], # metal yin
        [6,7,8,9,0,1,2,3,4,5,6,7], # água yang
        [8,9,0,1,2,3,4,5,6,7,8,9] # água yin
    ]
    
    if day_element == '甲':
        if hour_zodiac == '子':
            return HOUR_ELEMENT_INDEX_LIST[0][0]
        if hour_zodiac == '丑':
            return HOUR_ELEMENT_INDEX_LIST[0][1]
        if hour_zodiac == '寅':
            return HOUR_ELEMENT_INDEX_LIST[0][2]
        if hour_zodiac == '卯':
            return HOUR_ELEMENT_INDEX_LIST[0][3]
        if hour_zodiac == '辰':
            return HOUR_ELEMENT_INDEX_LIST[0][4]
        if hour_zodiac == '巳':
            return HOUR_ELEMENT_INDEX_LIST[0][5]
        if hour_zodiac == '午':
            return HOUR_ELEMENT_INDEX_LIST[0][6]
        if hour_zodiac == '未':
            return HOUR_ELEMENT_INDEX_LIST[0][7]
        if hour_zodiac == '申':
            return HOUR_ELEMENT_INDEX_LIST[0][8]
        if hour_zodiac == '酉':
            return HOUR_ELEMENT_INDEX_LIST[0][9]
        if hour_zodiac == '戌':
            return HOUR_ELEMENT_INDEX_LIST[0][10]
        if hour_zodiac == '亥':
            return HOUR_ELEMENT_INDEX_LIST[0][11]
    if day_element == '乙':
        if hour_zodiac == '子':
            return HOUR_ELEMENT_INDEX_LIST[1][0]
        if hour_zodiac == '丑':
            return HOUR_ELEMENT_INDEX_LIST[1][1]
        if hour_zodiac == '寅':
            return HOUR_ELEMENT_INDEX_LIST[1][2]
        if hour_zodiac == '卯':
            return HOUR_ELEMENT_INDEX_LIST[1][3]
        if hour_zodiac == '辰':
            return HOUR_ELEMENT_INDEX_LIST[1][4]
        if hour_zodiac == '巳':
            return HOUR_ELEMENT_INDEX_LIST[1][5]
        if hour_zodiac == '午':
            return HOUR_ELEMENT_INDEX_LIST[1][6]
        if hour_zodiac == '未':
            return HOUR_ELEMENT_INDEX_LIST[1][7]
        if hour_zodiac == '申':
            return HOUR_ELEMENT_INDEX_LIST[1][8]
        if hour_zodiac == '酉':
            return HOUR_ELEMENT_INDEX_LIST[1][9]
        if hour_zodiac == '戌':
            return HOUR_ELEMENT_INDEX_LIST[1][10]
        if hour_zodiac == '亥':
            return HOUR_ELEMENT_INDEX_LIST[1][11]
    if day_element == '丙':
        if hour_zodiac == '子':
            return HOUR_ELEMENT_INDEX_LIST[2][0]
        if hour_zodiac == '丑':
            return HOUR_ELEMENT_INDEX_LIST[2][1]
        if hour_zodiac == '寅':
            return HOUR_ELEMENT_INDEX_LIST[2][2]
        if hour_zodiac == '卯':
            return HOUR_ELEMENT_INDEX_LIST[2][3]
        if hour_zodiac == '辰':
            return HOUR_ELEMENT_INDEX_LIST[2][4]
        if hour_zodiac == '巳':
            return HOUR_ELEMENT_INDEX_LIST[2][5]
        if hour_zodiac == '午':
            return HOUR_ELEMENT_INDEX_LIST[2][6]
        if hour_zodiac == '未':
            return HOUR_ELEMENT_INDEX_LIST[2][7]
        if hour_zodiac == '申':
            return HOUR_ELEMENT_INDEX_LIST[2][8]
        if hour_zodiac == '酉':
            return HOUR_ELEMENT_INDEX_LIST[2][9]
        if hour_zodiac == '戌':
            return HOUR_ELEMENT_INDEX_LIST[2][10]
        if hour_zodiac == '亥':
            return HOUR_ELEMENT_INDEX_LIST[2][11]
    if day_element == '丁':
        if hour_zodiac == '子':
            return HOUR_ELEMENT_INDEX_LIST[3][0]
        if hour_zodiac == '丑':
            return HOUR_ELEMENT_INDEX_LIST[3][1]
        if hour_zodiac == '寅':
            return HOUR_ELEMENT_INDEX_LIST[3][2]
        if hour_zodiac == '卯':
            return HOUR_ELEMENT_INDEX_LIST[3][3]
        if hour_zodiac == '辰':
            return HOUR_ELEMENT_INDEX_LIST[3][4]
        if hour_zodiac == '巳':
            return HOUR_ELEMENT_INDEX_LIST[3][5]
        if hour_zodiac == '午':
            return HOUR_ELEMENT_INDEX_LIST[3][6]
        if hour_zodiac == '未':
            return HOUR_ELEMENT_INDEX_LIST[3][7]
        if hour_zodiac == '申':
            return HOUR_ELEMENT_INDEX_LIST[3][8]
        if hour_zodiac == '酉':
            return HOUR_ELEMENT_INDEX_LIST[3][9]
        if hour_zodiac == '戌':
            return HOUR_ELEMENT_INDEX_LIST[3][10]
        if hour_zodiac == '亥':
            return HOUR_ELEMENT_INDEX_LIST[3][11]
    if day_element == '戊':
        if hour_zodiac == '子':
            return HOUR_ELEMENT_INDEX_LIST[4][0]
        if hour_zodiac == '丑':
            return HOUR_ELEMENT_INDEX_LIST[4][1]
        if hour_zodiac == '寅':
            return HOUR_ELEMENT_INDEX_LIST[4][2]
        if hour_zodiac == '卯':
            return HOUR_ELEMENT_INDEX_LIST[4][3]
        if hour_zodiac == '辰':
            return HOUR_ELEMENT_INDEX_LIST[4][4]
        if hour_zodiac == '巳':
            return HOUR_ELEMENT_INDEX_LIST[4][5]
        if hour_zodiac == '午':
            return HOUR_ELEMENT_INDEX_LIST[4][6]
        if hour_zodiac == '未':
            return HOUR_ELEMENT_INDEX_LIST[4][7]
        if hour_zodiac == '申':
            return HOUR_ELEMENT_INDEX_LIST[4][8]
        if hour_zodiac == '酉':
            return HOUR_ELEMENT_INDEX_LIST[4][9]
        if hour_zodiac == '戌':
            return HOUR_ELEMENT_INDEX_LIST[4][10]
        if hour_zodiac == '亥':
            return HOUR_ELEMENT_INDEX_LIST[4][11]
    if day_element == '己':
        if hour_zodiac == '子':
            return HOUR_ELEMENT_INDEX_LIST[5][0]
        if hour_zodiac == '丑':
            return HOUR_ELEMENT_INDEX_LIST[5][1]
        if hour_zodiac == '寅':
            return HOUR_ELEMENT_INDEX_LIST[5][2]
        if hour_zodiac == '卯':
            return HOUR_ELEMENT_INDEX_LIST[5][3]
        if hour_zodiac == '辰':
            return HOUR_ELEMENT_INDEX_LIST[5][4]
        if hour_zodiac == '巳':
            return HOUR_ELEMENT_INDEX_LIST[5][5]
        if hour_zodiac == '午':
            return HOUR_ELEMENT_INDEX_LIST[5][6]
        if hour_zodiac == '未':
            return HOUR_ELEMENT_INDEX_LIST[5][7]
        if hour_zodiac == '申':
            return HOUR_ELEMENT_INDEX_LIST[5][8]
        if hour_zodiac == '酉':
            return HOUR_ELEMENT_INDEX_LIST[5][9]
        if hour_zodiac == '戌':
            return HOUR_ELEMENT_INDEX_LIST[5][10]
        if hour_zodiac == '亥':
            return HOUR_ELEMENT_INDEX_LIST[5][11]
    if day_element == '庚':
        if hour_zodiac == '子':
            return HOUR_ELEMENT_INDEX_LIST[6][0]
        if hour_zodiac == '丑':
            return HOUR_ELEMENT_INDEX_LIST[6][1]
        if hour_zodiac == '寅':
            return HOUR_ELEMENT_INDEX_LIST[6][2]
        if hour_zodiac == '卯':
            return HOUR_ELEMENT_INDEX_LIST[6][3]
        if hour_zodiac == '辰':
            return HOUR_ELEMENT_INDEX_LIST[6][4]
        if hour_zodiac == '巳':
            return HOUR_ELEMENT_INDEX_LIST[6][5]
        if hour_zodiac == '午':
            return HOUR_ELEMENT_INDEX_LIST[6][6]
        if hour_zodiac == '未':
            return HOUR_ELEMENT_INDEX_LIST[6][7]
        if hour_zodiac == '申':
            return HOUR_ELEMENT_INDEX_LIST[6][8]
        if hour_zodiac == '酉':
            return HOUR_ELEMENT_INDEX_LIST[6][9]
        if hour_zodiac == '戌':
            return HOUR_ELEMENT_INDEX_LIST[6][10]
        if hour_zodiac == '亥':
            return HOUR_ELEMENT_INDEX_LIST[6][11]
    if day_element == '辛':
        if hour_zodiac == '子':
            return HOUR_ELEMENT_INDEX_LIST[7][0]
        if hour_zodiac == '丑':
            return HOUR_ELEMENT_INDEX_LIST[7][1]
        if hour_zodiac == '寅':
            return HOUR_ELEMENT_INDEX_LIST[7][2]
        if hour_zodiac == '卯':
            return HOUR_ELEMENT_INDEX_LIST[7][3]
        if hour_zodiac == '辰':
            return HOUR_ELEMENT_INDEX_LIST[7][4]
        if hour_zodiac == '巳':
            return HOUR_ELEMENT_INDEX_LIST[7][5]
        if hour_zodiac == '午':
            return HOUR_ELEMENT_INDEX_LIST[7][6]
        if hour_zodiac == '未':
            return HOUR_ELEMENT_INDEX_LIST[7][7]
        if hour_zodiac == '申':
            return HOUR_ELEMENT_INDEX_LIST[7][8]
        if hour_zodiac == '酉':
            return HOUR_ELEMENT_INDEX_LIST[7][9]
        if hour_zodiac == '戌':
            return HOUR_ELEMENT_INDEX_LIST[7][10]
        if hour_zodiac == '亥':
            return HOUR_ELEMENT_INDEX_LIST[7][11]
    if day_element == '壬':
        if hour_zodiac == '子':
            return HOUR_ELEMENT_INDEX_LIST[8][0]
        if hour_zodiac == '丑':
            return HOUR_ELEMENT_INDEX_LIST[8][1]
        if hour_zodiac == '寅':
            return HOUR_ELEMENT_INDEX_LIST[8][2]
        if hour_zodiac == '卯':
            return HOUR_ELEMENT_INDEX_LIST[8][3]
        if hour_zodiac == '辰':
            return HOUR_ELEMENT_INDEX_LIST[8][4]
        if hour_zodiac == '巳':
            return HOUR_ELEMENT_INDEX_LIST[8][5]
        if hour_zodiac == '午':
            return HOUR_ELEMENT_INDEX_LIST[8][6]
        if hour_zodiac == '未':
            return HOUR_ELEMENT_INDEX_LIST[8][7]
        if hour_zodiac == '申':
            return HOUR_ELEMENT_INDEX_LIST[8][8]
        if hour_zodiac == '酉':
            return HOUR_ELEMENT_INDEX_LIST[8][9]
        if hour_zodiac == '戌':
            return HOUR_ELEMENT_INDEX_LIST[8][10]
        if hour_zodiac == '亥':
            return HOUR_ELEMENT_INDEX_LIST[8][11]
    if day_element == '癸':
        if hour_zodiac == '子':
            return HOUR_ELEMENT_INDEX_LIST[9][0]
        if hour_zodiac == '丑':
            return HOUR_ELEMENT_INDEX_LIST[9][1]
        if hour_zodiac == '寅':
            return HOUR_ELEMENT_INDEX_LIST[9][2]
        if hour_zodiac == '卯':
            return HOUR_ELEMENT_INDEX_LIST[9][3]
        if hour_zodiac == '辰':
            return HOUR_ELEMENT_INDEX_LIST[9][4]
        if hour_zodiac == '巳':
            return HOUR_ELEMENT_INDEX_LIST[9][5]
        if hour_zodiac == '午':
            return HOUR_ELEMENT_INDEX_LIST[9][6]
        if hour_zodiac == '未':
            return HOUR_ELEMENT_INDEX_LIST[9][7]
        if hour_zodiac == '申':
            return HOUR_ELEMENT_INDEX_LIST[9][8]
        if hour_zodiac == '酉':
            return HOUR_ELEMENT_INDEX_LIST[9][9]
        if hour_zodiac == '戌':
            return HOUR_ELEMENT_INDEX_LIST[9][10]
        if hour_zodiac == '亥':
            return HOUR_ELEMENT_INDEX_LIST[9][11]

# main code
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))
option = input("Show hour pillar? (y/n): ").lower().strip()
if option == 'y':
    hour = int(input("Enter a hour: "))
    daylight_saving_time = input("There was DST when you were born? (y/n): ").lower().strip()
    hour_zodiac = getHourZodiac(hour, daylight_saving_time)
    hour_element = ELEMENTS[getHourElementIndex(hour_zodiac, ELEMENTS[getDayElementIndex(year, month, day)])]

birthday = Solar(year,month,day)
birthday_in_lunar = Converter.Solar2Lunar(birthday)

year_zodiac = getYearZodiac(year)
month_zodiac = ZODIAC[birthday_in_lunar.month - 1]
day_zodiac = getDayZodiac(year, month, day)

year_element = ELEMENTS[getYearElementIndex(birthday_in_lunar.year)]
month_element = ELEMENTS[getMonthElementIndex(birthday_in_lunar.year, birthday_in_lunar.month)]
day_element = ELEMENTS[getDayElementIndex(year, month, day)]

if option == 'y':
    print('                  H  D  M  Y')
    print('Heavenly Stem    ', hour_element, day_element, month_element, year_element)
    print('Earthly Branches ', hour_zodiac, day_zodiac, month_zodiac, year_zodiac)
else:
    print('                  D  M  Y')
    print('Heavenly Stem    ', day_element, month_element, year_element)
    print('Earthly Branches ', day_zodiac, month_zodiac, year_zodiac)