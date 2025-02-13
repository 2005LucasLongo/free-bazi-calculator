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


# Element percentage section

# Variables
wood_yang = 0
wood_yin = 0
fire_yang = 0
fire_yin = 0
earth_yang = 0
earth_yin = 0
metal_yang = 0
metal_yin = 0
water_yang = 0
water_yin = 0

# calculations

# heavenly stems

# year heavenly stem
if year_element == '甲':
    wood_yang += 1
elif year_element == '乙':
    wood_yin += 1
elif year_element == '丙':
    fire_yang += 1
elif year_element == '丁':
    fire_yin += 1
elif year_element == '戊':
    earth_yang += 1
elif year_element == '己':
    earth_yin += 1
elif year_element == '庚':
    metal_yang += 1
elif year_element == '辛':
    metal_yin += 1
elif year_element == '壬':
    water_yang += 1
else:
    water_yin += 1

# month heavenly stem
if month_element == '甲':
    wood_yang += 1
elif month_element == '乙':
    wood_yin += 1
elif month_element == '丙':
    fire_yang += 1
elif month_element == '丁':
    fire_yin += 1
elif month_element == '戊':
    earth_yang += 1
elif month_element == '己':
    earth_yin += 1
elif month_element == '庚':
    metal_yang += 1
elif month_element == '辛':
    metal_yin += 1
elif month_element == '壬':
    water_yang += 1
else:
    water_yin += 1

# day heavenly stem
if day_element == '甲':
    wood_yang += 1
elif day_element == '乙':
    wood_yin += 1
elif day_element == '丙':
    fire_yang += 1
elif day_element == '丁':
    fire_yin += 1
elif day_element == '戊':
    earth_yang += 1
elif day_element == '己':
    earth_yin += 1
elif day_element == '庚':
    metal_yang += 1
elif day_element == '辛':
    metal_yin += 1
elif day_element == '壬':
    water_yang += 1
else:
    water_yin += 1

# earthy branches

# year earthly branch
if year_zodiac == '子': # Rat
    water_yin += 1
elif year_zodiac == '丑': # Ox
    earth_yin += 0.6
    water_yin += 0.3
    metal_yin += 0.1
elif year_zodiac == '寅': # Tiger
    wood_yang += 0.6
    fire_yang += 0.3
    earth_yang += 0.1
elif year_zodiac == '卯': # Rabbit
    wood_yin += 1
elif year_zodiac == '辰': # Dragon
    earth_yang += 0.6
    wood_yin += 0.3
    water_yin += 0.1
elif year_zodiac == '巳': # Snake
    fire_yang += 0.6
    metal_yang += 0.3
    earth_yang += 0.1
elif year_zodiac == '午': # Horse
    fire_yin += 0.7
    earth_yin += 0.3
elif year_zodiac == '未': # Goat
    earth_yin += 0.6
    fire_yin += 0.3
    wood_yin += 0.1
elif year_zodiac == '申': # Monkey
    metal_yang += 0.6
    water_yang += 0.3
    earth_yang += 0.1
elif year_zodiac == '酉': # Rooster
    metal_yin += 1
elif year_zodiac == '戌': # Dog
    earth_yang += 0.6
    metal_yin += 0.3
    fire_yin += 0.1
else: # Pig
    water_yang += 0.7
    wood_yang += 0.3

# month earthly branch
if month_zodiac == '子': # Rat
    water_yin += 1
elif month_zodiac == '丑': # Ox
    earth_yin += 0.6
    water_yin += 0.3
    metal_yin += 0.1
elif month_zodiac == '寅': # Tiger
    wood_yang += 0.6
    fire_yang += 0.3
    earth_yang += 0.1
elif month_zodiac == '卯': # Rabbit
    wood_yin += 1
elif month_zodiac == '辰': # Dragon
    earth_yang += 0.6
    wood_yin += 0.3
    water_yin += 0.1
elif month_zodiac == '巳': # Snake
    fire_yang += 0.6
    metal_yang += 0.3
    earth_yang += 0.1
elif month_zodiac == '午': # Horse
    fire_yin += 0.7
    earth_yin += 0.3
elif month_zodiac == '未': # Goat
    earth_yin += 0.6
    fire_yin += 0.3
    wood_yin += 0.1
elif month_zodiac == '申': # Monkey
    metal_yang += 0.6
    water_yang += 0.3
    earth_yang += 0.1
elif month_zodiac == '酉': # Rooster
    metal_yin += 1
elif month_zodiac == '戌': # Dog
    earth_yang += 0.6
    metal_yin += 0.3
    fire_yin += 0.1
else: # Pig
    water_yang += 0.7
    wood_yang += 0.3

# day earthly branch
if day_zodiac == '子': # Rat
    water_yin += 1
elif day_zodiac == '丑': # Ox
    earth_yin += 0.6
    water_yin += 0.3
    metal_yin += 0.1
elif day_zodiac == '寅': # Tiger
    wood_yang += 0.6
    fire_yang += 0.3
    earth_yang += 0.1
elif day_zodiac == '卯': # Rabbit
    wood_yin += 1
elif day_zodiac == '辰': # Dragon
    earth_yang += 0.6
    wood_yin += 0.3
    water_yin += 0.1
elif day_zodiac == '巳': # Snake
    fire_yang += 0.6
    metal_yang += 0.3
    earth_yang += 0.1
elif day_zodiac == '午': # Horse
    fire_yin += 0.7
    earth_yin += 0.3
elif day_zodiac == '未': # Goat
    earth_yin += 0.6
    fire_yin += 0.3
    wood_yin += 0.1
elif day_zodiac == '申': # Monkey
    metal_yang += 0.6
    water_yang += 0.3
    earth_yang += 0.1
elif day_zodiac == '酉': # Rooster
    metal_yin += 1
elif day_zodiac == '戌': # Dog
    earth_yang += 0.6
    metal_yin += 0.3
    fire_yin += 0.1
else: # Pig
    water_yang += 0.7
    wood_yang += 0.3
    

# considers hour pillar
if option == 'y':
    # hour heavenly stem
    if hour_element == '甲':
        wood_yang += 1
    elif hour_element == '乙':
        wood_yin += 1
    elif hour_element == '丙':
        fire_yang += 1
    elif hour_element == '丁':
        fire_yin += 1
    elif hour_element == '戊':
        earth_yang += 1
    elif hour_element == '己':
        earth_yin += 1
    elif hour_element == '庚':
        metal_yang += 1
    elif hour_element == '辛':
        metal_yin += 1
    elif hour_element == '壬':
        water_yang += 1
    else:
        water_yin += 1
    
    # hour earthly branch
    if hour_zodiac == '子': # Rat
        water_yin += 1
    elif hour_zodiac == '丑': # Ox
        earth_yin += 0.6
        water_yin += 0.3
        metal_yin += 0.1
    elif hour_zodiac == '寅': # Tiger
        wood_yang += 0.6
        fire_yang += 0.3
        earth_yang += 0.1
    elif hour_zodiac == '卯': # Rabbit
        wood_yin += 1
    elif hour_zodiac == '辰': # Dragon
        earth_yang += 0.6
        wood_yin += 0.3
        water_yin += 0.1
    elif hour_zodiac == '巳': # Snake
        fire_yang += 0.6
        metal_yang += 0.3
        earth_yang += 0.1
    elif hour_zodiac == '午': # Horse
        fire_yin += 0.7
        earth_yin += 0.3
    elif hour_zodiac == '未': # Goat
        earth_yin += 0.6
        fire_yin += 0.3
        wood_yin += 0.1
    elif hour_zodiac == '申': # Monkey
        metal_yang += 0.6
        water_yang += 0.3
        earth_yang += 0.1
    elif hour_zodiac == '酉': # Rooster
        metal_yin += 1
    elif hour_zodiac == '戌': # Dog
        earth_yang += 0.6
        metal_yin += 0.3
        fire_yin += 0.1
    else: # Pig
        water_yang += 0.7
        wood_yang += 0.3
    
    # divides per 8
    wood_yang /= 8
    wood_yin /= 8
    fire_yang /= 8
    fire_yin /= 8
    earth_yang /= 8 
    earth_yin /= 8
    metal_yang /= 8
    metal_yin /= 8
    water_yang /= 8
    water_yin /= 8
# doesn't considers hour pillar
else:
    wood_yang /= 6
    wood_yin /= 6
    fire_yang /= 6
    fire_yin /= 6
    earth_yang /= 6
    earth_yin /= 6
    metal_yang /= 6
    metal_yin /= 6
    water_yang /= 6
    water_yin /= 6

# print percentages
print()
# the code below used pure brute force to work
# and i hated every single second coding this
if day_element == '甲': # means daymaster is yang wood
    print(f'Resource - water / Shui / 水 : {format(((water_yang * 100) + (water_yin * 100)), ".2f")}%')
    print(f'Parallel (DM) - wood / Mu / 木 : {format(((wood_yang * 100) + (wood_yin * 100)), ".2f")}%')
    print(f'Output - fire / Huo / 火 : {format(((fire_yang * 100) + (fire_yin * 100)), ".2f")}%')
    print(f'Wealth - earth / Tu / 土 : {format(((earth_yang * 100) + (earth_yin * 100)), ".2f")}%')
    print(f'Power - metal / Jin / 金 : {format(((metal_yang * 100) + (metal_yin * 100)), ".2f")}%')
elif day_element == '乙': # means daymaster is yin wood
    print(f'Resource - water / Shui / 水 : {format(((water_yang * 100) + (water_yin * 100)), ".2f")}%')
    print(f'Parallel - (DM) wood / Mu / 木 : {format(((wood_yang * 100) + (wood_yin * 100)), ".2f")}%')
    print(f'Output - fire / Huo / 火 : {format(((fire_yang * 100) + (fire_yin * 100)), ".2f")}%')
    print(f'Wealth - earth / Tu / 土 : {format(((earth_yang * 100) + (earth_yin * 100)), ".2f")}%')
    print(f'Power - metal / Jin / 金 : {format(((metal_yang * 100) + (metal_yin * 100)), ".2f")}%')
elif day_element == '丙': # means daymaster is yang fire
    print(f'Resource - wood / Mu / 木 : {format(((wood_yang * 100) + (wood_yin * 100)), ".2f")}%')
    print(f'Parallel - (DM) fire / Huo / 火 : {format(((fire_yang * 100) + (fire_yin * 100)), ".2f")}%')
    print(f'Output - earth / Tu / 土 : {format(((earth_yang * 100) + (earth_yin * 100)), ".2f")}%')
    print(f'Wealth - metal / Jin / 金 : {format(((metal_yang * 100) + (metal_yin * 100)), ".2f")}%')
    print(f'Power - water / Shui / 水 : {format(((water_yang * 100) + (water_yin * 100)), ".2f")}%')
elif day_element == '丁': # means daymaster is yin fire
    print(f'Resource - wood / Mu / 木 : {format(((wood_yang * 100) + (wood_yin * 100)), ".2f")}%')
    print(f'Parallel - (DM) fire / Huo / 火: {format(((fire_yang * 100) + (fire_yin * 100)), ".2f")}%')
    print(f'Output - earth / Tu / 土 : {format(((earth_yang * 100) + (earth_yin * 100)), ".2f")}%')
    print(f'Wealth - metal / Jin / 金 : {format(((metal_yang * 100) + (metal_yin * 100)), ".2f")}%')
    print(f'Power - water / Shui / 水 : {format(((water_yang * 100) + (water_yin * 100)), ".2f")}%')
elif day_element == '戊': # means daymaster is yang earth
    print(f'Resource - fire / Huo / 火 : {format(((fire_yang * 100) + (fire_yin * 100)), ".2f")}%')
    print(f'Parallel - (DM) earth / Tu / 土 : {format(((earth_yang * 100) + (earth_yin * 100)), ".2f")}%')
    print(f'Output - metal / Jin / 金 : {format(((metal_yang * 100) + (metal_yin * 100)), ".2f")}%')
    print(f'Wealth - water / Shui / 水 : {format(((water_yang * 100) + (water_yin * 100)), ".2f")}%')
    print(f'Power - wood / Mu / 木 : {format(((wood_yang * 100) + (wood_yin * 100)), ".2f")}%')
elif day_element == '己': # means daymaster is yin earth
    print(f'Resource - fire / Huo / 火 : {format(((fire_yang * 100) + (fire_yin * 100)), ".2f")}%')
    print(f'Parallel - (DM) earth / Tu / 土 : {format(((earth_yang * 100) + (earth_yin * 100)), ".2f")}%')
    print(f'Output - metal / Jin / 金 : {format(((metal_yang * 100) + (metal_yin * 100)), ".2f")}%')
    print(f'Wealth - water / Shui / 水 : {format(((water_yang * 100) + (water_yin * 100)), ".2f")}%')
    print(f'Power - wood / Mu / 木 : {format(((wood_yang * 100) + (wood_yin * 100)), ".2f")}%')
elif day_element == '庚': # means daymaster is yang metal
    print(f'Resource - earth / Tu / 土 : {format(((earth_yang * 100) + (earth_yin * 100)), ".2f")}%')
    print(f'Parallel - (DM) metal / Jin / 金 : {format(((metal_yang * 100) + (metal_yin * 100)), ".2f")}%')
    print(f'Output - water / Shui / 水 : {format(((water_yang * 100) + (water_yin * 100)), ".2f")}%')
    print(f'Wealth - wood / Mu / 木 : {format(((wood_yang * 100) + (wood_yin * 100)), ".2f")}%')
    print(f'Power - fire / Huo / 火 : {format(((fire_yang * 100) + (fire_yin * 100)), ".2f")}%')
elif day_element == '辛': # means daymaster is yin metal
    print(f'Resource - earth / Tu / 土 : {format(((earth_yang * 100) + (earth_yin * 100)), ".2f")}%')
    print(f'Parallel - (DM) metal / Jin / 金 : {format(((metal_yang * 100) + (metal_yin * 100)), ".2f")}%')
    print(f'Output - water / Shui / 水 : {format(((water_yang * 100) + (water_yin * 100)), ".2f")}%')
    print(f'Wealth - wood / Mu / 木 : {format(((wood_yang * 100) + (wood_yin * 100)), ".2f")}%')
    print(f'Power - fire / Huo / 火 : {format(((fire_yang * 100) + (fire_yin * 100)), ".2f")}%')
elif day_element == '壬': # means daymaster is yang water
    print(f'Resource - metal / Jin / 金 : {format(((metal_yang * 100) + (metal_yin * 100)), ".2f")}%')
    print(f'Parallel - (DM) water / Shui / 水 : {format(((water_yang * 100) + (water_yin * 100)), ".2f")}%')
    print(f'Output - wood / Mu / 木 : {format(((wood_yang * 100) + (wood_yin * 100)), ".2f")}%')
    print(f'Wealth - fire / Huo / 火 : {format(((fire_yang * 100) + (fire_yin * 100)), ".2f")}%')
    print(f'Power - earth / Tu / 土 : {format(((earth_yang * 100) + (earth_yin * 100)), ".2f")}%')
else: # means daymaster is yin water
    print(f'Resource - metal / Jin / 金 : {format(((metal_yang * 100) + (metal_yin * 100)), ".2f")}%')
    print(f'Parallel - (DM) water / Shui / 水 : {format(((water_yang * 100) + (water_yin * 100)), ".2f")}%')
    print(f'Output - wood / Mu / 木 : {format(((wood_yang * 100) + (wood_yin * 100)), ".2f")}%')
    print(f'Wealth - fire / Huo / 火 : {format(((fire_yang * 100) + (fire_yin * 100)), ".2f")}%')
    print(f'Power - earth / Tu / 土 : {format(((earth_yang * 100) + (earth_yin * 100)), ".2f")}%')

has_hour_pillar = option
option = input("Show 10 Gods? (y/n): ").lower().strip()    

if option == 'y':
    # power element
    direct_officer = [] # same polarity as dm
    qi_sha = [] # opposite polarity of dm
    # resource element
    direct_resource = [] # same polarity as dm
    indirect_resource = [] # opposite polarity of dm
    # parallel element
    friends = [] # same polarity as dm
    rob_wealth = [] # opposite polarity of dm
    # output element
    eating_god = [] # same polarity as dm
    hurting_officer = [] # opposite polarity of dm
    # wealth element
    direct_wealth = [] # same polarity as dm
    indirect_wealth = [] # opposite polarity of dm
    
    # Yang Wood
    if day_element == '甲':
        direct_officer = ['Yin Metal', metal_yin*100]
        qi_sha = ['Yang Metal', metal_yang*100]
        direct_resource = ['Yin Water', water_yin*100]
        indirect_resource = ['Yang Water', water_yang*100]
        friends = ['Yang Wood', wood_yang*100]
        rob_wealth = ['Yin Wood', wood_yin*100]
        eating_god = ['Yang Fire', fire_yang*100]
        hurting_officer = ['Yin Fire', fire_yin*100]
        direct_wealth = ['Yin Earth', earth_yin*100]
        indirect_wealth = ['Yang Earth', earth_yang*100]
    # Yin Wood
    elif day_element == '乙':
        direct_officer = ['Yang Metal', metal_yang*100]
        qi_sha = ['Yin Metal', metal_yin*100]
        direct_resource = ['Yang Water', water_yang*100]
        indirect_resource = ['Yin Water', water_yin*100]
        friends = ['Yin Wood', wood_yin*100]
        rob_wealth = ['Yang Wood', wood_yang*100]
        eating_god = ['Yin Fire', fire_yin*100]
        hurting_officer = ['Yang Fire', fire_yang*100]
        direct_wealth = ['Yang Earth', earth_yang*100]
        indirect_wealth = ['Yin Earth', earth_yin*100]
    # Yang Fire
    elif day_element == '丙':
        direct_officer = ['Yin Water', water_yin*100]
        qi_sha = ['Yang Water', water_yang*100]
        direct_resource = ['Yin Wood', wood_yin*100]
        indirect_resource = ['Yang Wood', wood_yang*100]
        friends = ['Yang Fire', fire_yang*100]
        rob_wealth = ['Yin Fire', fire_yin*100]
        eating_god = ['Yang Earth', earth_yang*100]
        hurting_officer = ['Yin Earth', earth_yin*100]
        direct_wealth = ['Yin Metal', metal_yin*100]
        indirect_wealth = ['Yang Metal', metal_yang*100]
    # Yin Fire
    elif day_element == '丁':
        direct_officer = ['Yang Water', water_yang*100]
        qi_sha = ['Yin Water', water_yin*100]
        direct_resource = ['Yang Wood', wood_yang*100]
        indirect_resource = ['Yin Wood', wood_yin*100]
        friends = ['Yin Fire', fire_yin*100]
        rob_wealth = ['Yang Fire', fire_yang*100]
        eating_god = ['Yin Earth', earth_yin*100]
        hurting_officer = ['Yang Earth', earth_yang*100]
        direct_wealth = ['Yang Metal', metal_yang*100]
        indirect_wealth = ['Yin Metal', metal_yin*100]
    # Yang Earth
    elif day_element == '戊':
        direct_officer = ['Yin Wood', wood_yin*100]
        qi_sha = ['Yang Wood', wood_yang*100]
        direct_resource = ['Yin Fire', fire_yin*100]
        indirect_resource = ['Yang Fire', fire_yang*100]
        friends = ['Yang Earth', earth_yang*100]
        rob_wealth = ['Yin Earth', earth_yin*100]
        eating_god = ['Yang Metal', metal_yang*100]
        hurting_officer = ['Yin Metal', metal_yin*100]
        direct_wealth = ['Yin Water', water_yin*100]
        indirect_wealth = ['Yang Water', water_yang*100]
    # Yin Earth
    elif day_element == '己':
        direct_officer = ['Yang Wood', wood_yang*100]
        qi_sha = ['Yin Wood', wood_yin*100]
        direct_resource = ['Yang Fire', fire_yang*100]
        indirect_resource = ['Yin Fire', fire_yin*100]
        friends = ['Yin Earth', earth_yin*100]
        rob_wealth = ['Yang Earth', earth_yang*100]
        eating_god = ['Yin Metal', metal_yin*100]
        hurting_officer = ['Yang Metal', metal_yang*100]
        direct_wealth = ['Yang Water', water_yang*100]
        indirect_wealth = ['Yin Water', water_yin*100]
    # Yang Metal
    elif day_element == '庚':
        direct_officer = ['Yin Fire', fire_yin*100]
        qi_sha = ['Yang Fire', fire_yang*100]
        direct_resource = ['Yin Earth', earth_yin*100]
        indirect_resource = ['Yang Earth', earth_yang*100]
        friends = ['Yang Metal', metal_yang*100]
        rob_wealth = ['Yin Metal', metal_yin*100]
        eating_god = ['Yang Water', water_yang*100]
        hurting_officer = ['Yin Water', water_yin*100]
        direct_wealth = ['Yin Wood', wood_yin*100]
        indirect_wealth = ['Yang Wood', wood_yang*100]
    # Yin Metal
    elif day_element == '辛':
        direct_officer = ['Yang Fire', fire_yang*100]
        qi_sha = ['Yin Fire', fire_yin*100]
        direct_resource = ['Yang Earth', earth_yang*100]
        indirect_resource = ['Yin Earth', earth_yin*100]
        friends = ['Yin Metal', metal_yin*100]
        rob_wealth = ['Yang Metal', metal_yang*100]
        eating_god = ['Yin Water', water_yin*100]
        hurting_officer = ['Yang Water', water_yang*100]
        direct_wealth = ['Yang Wood', wood_yang*100]        
        indirect_wealth = ['Yin Wood', wood_yin*100]
    # Yang Water
    elif day_element == '壬':
        direct_officer = ['Yin Earth', earth_yin*100]
        qi_sha = ['Yang Earth', earth_yang*100]
        direct_resource = ['Yin Metal', metal_yin*100]
        indirect_resource = ['Yang Metal', metal_yang*100]
        friends = ['Yang Water', water_yang*100]
        rob_wealth = ['Yin Water', water_yin*100]
        eating_god = ['Yang Wood', wood_yang*100]
        hurting_officer = ['Yin Wood', wood_yin*100]
        direct_wealth = ['Yin Fire', fire_yin*100]
        indirect_wealth = ['Yang Fire', fire_yang*100]
    # Yin Water
    elif day_element == '癸':
        direct_officer = ['Yang Earth', earth_yang*100]
        qi_sha = ['Yin Earth', earth_yin*100]
        direct_resource = ['Yin Metal', metal_yin*100]
        indirect_resource = ['Yang Metal', metal_yang*100]
        friends = ['Yin Water', water_yin*100]
        rob_wealth = ['Yang Water', water_yang*100]
        eating_god = ['Yin Wood', wood_yin*100]
        hurting_officer = ['Yang Wood', wood_yang*100]
        direct_wealth = ['Yang Fire', fire_yang*100]
        indirect_wealth = ['Yin Fire', fire_yin*100]
    else:
        raise Exception('Error: Day element is not valid')
    print()
    print(f'Direct officer 正官 (Zheng Guang): {direct_officer[0]} {format(direct_officer[1], ".2f")}%')
    print(f'Seven killings 七杀 (Qi Sha): {qi_sha[0]} {format(qi_sha[1], ".2f")}%')
    print(f'Direct resource 正印 (Zheng Yin): {direct_resource[0]} {format(direct_resource[1], ".2f")}%')
    print(f'Indirect resource 偏印 (Pian Yin): {indirect_resource[0]} {format(indirect_resource[1], ".2f")}%')
    print(f'Friends 比肩 (Bi Jian): {friends[0]} {format(friends[1], ".2f")}%')
    print(f'Rob wealth 劫财 (Jie Cai): {rob_wealth[0]} {format(rob_wealth[1], ".2f")}%')
    print(f'Eating god 食神 (Shi Shen): {eating_god[0]} {format(eating_god[1], ".2f")}%')
    print(f'Hurting officer 伤官 (Shang Guan): {hurting_officer[0]} {format(hurting_officer[1], ".2f")}%')
    print(f'Direct wealth 正财 (Zheng Cai): {direct_wealth[0]} {format(direct_wealth[1], ".2f")}%')
    print(f'Indirect wealth 偏财 (Pian Cai): {indirect_wealth[0]} {format(indirect_wealth[1], ".2f")}%')
    
    print('\nThanks for using our little script!')
else:
    print('\nThanks for using our little script!') 

if has_hour_pillar.lower().strip() == 'y':
    import methods.calc_elements as calc_elements
    element_percentage = calc_elements.calc_element_percentage_fullchart(year_element, year_zodiac, month_element, month_zodiac, day_element, day_zodiac, hour_element, hour_zodiac)
    print(f'Wood: {format(element_percentage["wood"], ".2f")}% ({calc_elements.get_element_status(element_percentage["wood"])})')
    print(f'Fire: {format(element_percentage["fire"], ".2f")}% ({calc_elements.get_element_status(element_percentage["fire"])})')
    print(f'Earth: {format(element_percentage["earth"], ".2f")}% ({calc_elements.get_element_status(element_percentage["earth"])})')
    print(f'Metal: {format(element_percentage["metal"], ".2f")}% ({calc_elements.get_element_status(element_percentage["metal"])})')
    print(f'Water: {format(element_percentage["water"], ".2f")}% ({calc_elements.get_element_status(element_percentage["water"])})')

print(birthday)
print(birthday_in_lunar)