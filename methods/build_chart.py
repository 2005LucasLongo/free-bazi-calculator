# from lunarcalendar import Converter
import lunardate as ld
import datetime as dt
from datetime import timedelta

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
    '庚', '辛', # yang-yin metal 0 1
    '壬', '癸', # yang-yin water 2 3
    '甲', '乙', # yang-yin wood 4 5
    '丙', '丁', # yang-yin fire 6 7
    '戊', '己', # yang-yin earth 8 9
]
# if the year is 1998, then the element is '戊' because this is the index of the end of the year

HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM = [
    # hours elements indexes according to the element of the day
    
    # below are the indexes of the hour pillar's heavenly stems
    # from Rat hour to Pig hour
    # Rat - Ox - Tiger - Rabbit - Dragon - Snake - Horse - Goat - Monkey - Rooster - Dog - Pig
    # yang wood days
    [4,5,6,7,8,9,0,1,2,3,4,5],
    # yin wood days
    [6,7,8,9,0,1,2,3,4,5,6,7],
    # yang fire days
    [8,9,0,1,2,3,4,5,6,7,8,9],
    # yin fire days
    [0,1,2,3,4,5,6,7,8,9,0,1],
    # yang earth days
    [2,3,4,5,6,7,8,9,0,1,2,3],
    # yin earth days
    [4,5,6,7,8,9,0,1,2,3,4,5],
    # yang metal days
    [6,7,8,9,0,1,2,3,4,5,6,7],
    # yin metal days
    [8,9,0,1,2,3,4,5,6,7,8,9],
    # yang water days
    [0,1,2,3,4,5,6,7,8,9,0,1],
    # yin water days
    [2,3,4,5,6,7,8,9,0,1,2,3],
]

MONTH_HEAVENLY_STEM_ACCORDING_TO_YEAR_HEAVENLY_STEM = [
    # months elements indexes according to the element of the year
    # from january to december
    # yang metal years 0
    [
        ELEMENTS[8], # January
        ELEMENTS[9], # February
        ELEMENTS[0], # March
        ELEMENTS[1], # April
        ELEMENTS[2], # May
        ELEMENTS[3], # June
        ELEMENTS[4], # July
        ELEMENTS[5], # August
        ELEMENTS[6], # September
        ELEMENTS[7], # October
        ELEMENTS[8], # November
        ELEMENTS[9], # December
    ],
    # yin metal years 1
    [
        ELEMENTS[0], # January
        ELEMENTS[1], # February
        ELEMENTS[2], # March
        ELEMENTS[3], # April
        ELEMENTS[4], # May
        ELEMENTS[5], # June
        ELEMENTS[6], # July
        ELEMENTS[7], # August
        ELEMENTS[8], # September
        ELEMENTS[9], # October
        ELEMENTS[0], # November
        ELEMENTS[1], # December
    ],
    # yang water years 2
    [
        ELEMENTS[2], # January
        ELEMENTS[3], # February
        ELEMENTS[4], # March
        ELEMENTS[5], # April
        ELEMENTS[6], # May
        ELEMENTS[7], # June
        ELEMENTS[8], # July
        ELEMENTS[9], # August
        ELEMENTS[0], # September
        ELEMENTS[1], # October
        ELEMENTS[2], # November
        ELEMENTS[3], # December
    ],
    # yin water years 3
    [
        ELEMENTS[4], # January
        ELEMENTS[5], # February
        ELEMENTS[6], # March
        ELEMENTS[7], # April
        ELEMENTS[8], # May
        ELEMENTS[9], # June 
        ELEMENTS[0], # July
        ELEMENTS[1], # August
        ELEMENTS[2], # September
        ELEMENTS[3], # October
        ELEMENTS[4], # November
        ELEMENTS[5], # December
    ],
    # yang wood years 4
    [
        ELEMENTS[6], # January
        ELEMENTS[7], # February
        ELEMENTS[8], # March
        ELEMENTS[9], # April
        ELEMENTS[0], # May
        ELEMENTS[1], # June
        ELEMENTS[2], # July
        ELEMENTS[3], # August
        ELEMENTS[4], # September
        ELEMENTS[5], # October
        ELEMENTS[6], # November
        ELEMENTS[7], # December
    ],
    # yin wood years 5
    [
        ELEMENTS[8], # January
        ELEMENTS[9], # February
        ELEMENTS[0], # March
        ELEMENTS[1], # April
        ELEMENTS[2], # May
        ELEMENTS[3], # June
        ELEMENTS[4], # July
        ELEMENTS[5], # August
        ELEMENTS[6], # September
        ELEMENTS[7], # October
        ELEMENTS[8], # November
        ELEMENTS[9], # December
    ],
    # yang fire years 6
    [
        ELEMENTS[0], # January
        ELEMENTS[1], # February
        ELEMENTS[2], # March        
        ELEMENTS[3], # April
        ELEMENTS[4], # May
        ELEMENTS[5], # June
        ELEMENTS[6], # July
        ELEMENTS[7], # August
        ELEMENTS[8], # September
        ELEMENTS[9], # October
        ELEMENTS[0], # November
        ELEMENTS[1], # December
    ],
    # yin fire years 7
    [
        ELEMENTS[2], # January
        ELEMENTS[3], # February
        ELEMENTS[4], # March
        ELEMENTS[5], # April
        ELEMENTS[6], # May
        ELEMENTS[7], # June
        ELEMENTS[8], # July
        ELEMENTS[9], # August
        ELEMENTS[0], # September
        ELEMENTS[1], # October
        ELEMENTS[2], # November
        ELEMENTS[3], # December
    ],
    # yang earth years 8
    [
        ELEMENTS[4], # January
        ELEMENTS[5], # February
        ELEMENTS[6], # March
        ELEMENTS[7], # April
        ELEMENTS[8], # May
        ELEMENTS[9], # June 
        ELEMENTS[0], # July
        ELEMENTS[1], # August
        ELEMENTS[2], # September
        ELEMENTS[3], # October
        ELEMENTS[4], # November
        ELEMENTS[5], # December
    ],
    # yin earth years 9
    [
        ELEMENTS[6], # January
        ELEMENTS[7], # February
        ELEMENTS[8], # March
        ELEMENTS[9], # April
        ELEMENTS[0], # May
        ELEMENTS[1], # June
        ELEMENTS[2], # July
        ELEMENTS[3], # August
        ELEMENTS[4], # September
        ELEMENTS[5], # October
        ELEMENTS[6], # November
        ELEMENTS[7], # December
    ]
]

'''def get_year_earthly_branch(solar_birthdate):
    lunar_birthdate = Converter.Solar2Lunar(solar_birthdate)
    while lunar_birthdate.year < 2010: # 2010 is the year of Metal Tiger
        lunar_birthdate.year += 12
    while lunar_birthdate.year > 2021: # 2021 is the year of Metal Ox
        lunar_birthdate.year -= 12
    return ZODIAC[lunar_birthdate.year-2010]'''

def get_year_earthly_branch(solar_year, solar_month, solar_day):
  fixed_date = ld.LunarDate.fromSolarDate(1900,1,31)
  solar_new_date = [solar_year, solar_month, solar_day] # solar
  fixed_date_dtformat = dt.date(fixed_date.year, fixed_date.month, fixed_date.day)

  if (solar_new_date[0] == 1900 and solar_new_date[1] == 1 and solar_new_date[2] < 31) or (solar_new_date[0] < 1900):
    day_diff = ld.LunarDate.fromSolarDate(solar_new_date[0],solar_new_date[1],solar_new_date[2]).day - 1
    lunar_new_date = fixed_date_dtformat + timedelta(day_diff)
  else:
    lunar_new_date = ld.LunarDate.fromSolarDate(solar_new_date[0], solar_new_date[1], solar_new_date[2])

  lunar_year = lunar_new_date.year
  
  while lunar_year < 2010: # 2010 is the year of Metal Tiger
    lunar_year += 12
  while lunar_year > 2021: # 2021 is the year of Metal Ox
    lunar_year -= 12
  return ZODIAC[lunar_year-2010]

'''def get_month_earthly_branch(solar_birthdate):
    lunar_birthdate = Converter.Solar2Lunar(solar_birthdate)
    return ZODIAC[lunar_birthdate.month-1]'''

def get_month_earthly_branch(solar_year, solar_month, solar_day):
  fixed_date = ld.LunarDate.fromSolarDate(1900,1,31)
  solar_new_date = [solar_year, solar_month, solar_day] # solar
  fixed_date_dtformat = dt.date(fixed_date.year, fixed_date.month, fixed_date.day)

  if (solar_new_date[0] == 1900 and solar_new_date[1] == 1 and solar_new_date[2] < 31) or (solar_new_date[0] < 1900):
    day_diff = ld.LunarDate.fromSolarDate(solar_new_date[0],solar_new_date[1],solar_new_date[2]).day - 1
    lunar_new_date = fixed_date_dtformat + timedelta(day_diff)
  else:
    lunar_new_date = ld.LunarDate.fromSolarDate(solar_new_date[0], solar_new_date[1], solar_new_date[2])
  
  return ZODIAC[lunar_new_date.month - 1]

'''def get_day_earthly_branch(solar_birthdate):
    base_date = datetime.date(1900, 1, 31)
    current_date = datetime.date(solar_birthdate.year, solar_birthdate.month, solar_birthdate.day)
    delta_days = (current_date - base_date).days
    index = (delta_days % 12)+2 
    if index == 12:
        index = 0
    if index == 13:
        index = 1
    return ZODIAC[index]
'''

def get_day_earthly_branch(solar_year, solar_month, solar_day):
    fixed_date = dt.date(2005,11,15) # rabbit day
    new_date = dt.date(solar_year,solar_month,solar_day)
    difference_in_days = (new_date - fixed_date).days

    i = 1 + difference_in_days

    if i < 0:
        while i < 12:
            i += 12
        i -= 12
    if i > 11:
        while i > 11:
            i -= 12
        i -= 12
    
    return ZODIAC[i]

def get_hour_earthly_branch(hour, dst=False):
    if dst == True:
        hour -= 1
    if hour == -1:
        hour = 23
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

'''def get_year_heavenly_stem(solar_birthdate):
    lunar_birthdate = Converter.Solar2Lunar(solar_birthdate)
    while lunar_birthdate.year < 2010: # 2010 is the year of Metal Tiger
        lunar_birthdate.year += 10
    while lunar_birthdate.year > 2019: # 2019 is the year of Fire Pig
        lunar_birthdate.year -= 10
    year_string_arrayed = str(lunar_birthdate.year).strip('')
    return ELEMENTS[(int(year_string_arrayed[-1]))]'''
    
def get_year_heavenly_stem(solar_year, solar_month, solar_day):
  fixed_date = ld.LunarDate.fromSolarDate(1900,1,31)
  solar_new_date = [solar_year, solar_month, solar_day] # solar
  fixed_date_dtformat = dt.date(fixed_date.year, fixed_date.month, fixed_date.day)

  if (solar_new_date[0] == 1900 and solar_new_date[1] == 1 and solar_new_date[2] < 31) or (solar_new_date[0] < 1900):
    day_diff = ld.LunarDate.fromSolarDate(solar_new_date[0],solar_new_date[1],solar_new_date[2]).day - 1
    lunar_new_date = fixed_date_dtformat + timedelta(day_diff)
  else:
    lunar_new_date = ld.LunarDate.fromSolarDate(solar_new_date[0], solar_new_date[1], solar_new_date[2])

  year_heavenly_stem_index = int((str(lunar_new_date.year).strip(''))[-1])
  return ELEMENTS[year_heavenly_stem_index]

'''def get_month_heavenly_stem(solar_birthdate):
    lunar_birthdate = Converter.Solar2Lunar(solar_birthdate)
    while lunar_birthdate.year < 2010: # 2010 is the year of Metal Tiger
        lunar_birthdate.year += 10
    while lunar_birthdate.year > 2019: # 2019 is the year of Fire Pig
        lunar_birthdate.year -= 10
    year_string_arrayed = str(lunar_birthdate.year).strip('')
    year_element_index = (int(year_string_arrayed[-1]))
    return MONTH_HEAVENLY_STEM_ACCORDING_TO_YEAR_HEAVENLY_STEM[year_element_index][lunar_birthdate.month-1]
'''
def get_month_heavenly_stem(solar_year, solar_month, solar_day):
  fixed_date = ld.LunarDate.fromSolarDate(1900,1,31)
  solar_new_date = [solar_year, solar_month, solar_day] # solar
  fixed_date_dtformat = dt.date(fixed_date.year, fixed_date.month, fixed_date.day)

  if (solar_new_date[0] == 1900 and solar_new_date[1] == 1 and solar_new_date[2] < 31) or (solar_new_date[0] < 1900):
    day_diff = ld.LunarDate.fromSolarDate(solar_new_date[0],solar_new_date[1],solar_new_date[2]).day - 1
    lunar_new_date = fixed_date_dtformat + timedelta(day_diff)
  else:
    lunar_new_date = ld.LunarDate.fromSolarDate(solar_new_date[0], solar_new_date[1], solar_new_date[2])

  year_heavenly_stem_index = int((str(lunar_new_date.year).strip(''))[-1])
  return MONTH_HEAVENLY_STEM_ACCORDING_TO_YEAR_HEAVENLY_STEM[year_heavenly_stem_index][lunar_new_date.month - 1]

'''def get_day_heavenly_stem(solar_birthdate):
    base_date = datetime.date(1900, 1, 1)
    current_date = datetime.date(solar_birthdate.year, solar_birthdate.month, solar_birthdate.day)
    delta_days = (current_date - base_date).days
    return ELEMENTS[(delta_days % 10)-6]
'''

def get_day_heavenly_stem(solar_year, solar_month, solar_day):
    fixed_date = dt.date(2005,11,15) # yin water day
    solar_new_date = dt.date(solar_year,solar_month,solar_day)
    difference_in_days = (solar_new_date - fixed_date).days

    i = 3 + difference_in_days

    if i < 0:
        while i < 10:
            i += 10
        i -= 10
    if i > 9:
        while i > 9:
            i -= 10
        i -= 10
    
    return ELEMENTS[i]

def get_hour_heavenly_stem(year, month, day, hour, dst=False):
    hour_earthly_branch = get_hour_earthly_branch(hour, dst)
    if (hour == 0) and (dst == True):
        datetime_date = dt.date(year, month, day) - timedelta(days=1)
        year = datetime_date.year
        month = datetime_date.month
        day = datetime_date.day
    day_heavenly_stem = get_day_heavenly_stem(year, month, day)
    if day_heavenly_stem == '甲': # means daymaster is yang wood
        if hour_earthly_branch == '子': # Rat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[0][0]]
        elif hour_earthly_branch == '丑': # Ox hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[0][1]]
        elif hour_earthly_branch == '寅': # Tiger hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[0][2]]
        elif hour_earthly_branch == '卯': # Rabbit hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[0][3]]
        elif hour_earthly_branch == '辰': # Dragon hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[0][4]]
        elif hour_earthly_branch == '巳': # Snake hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[0][5]]
        elif hour_earthly_branch == '午': # Horse hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[0][6]]
        elif hour_earthly_branch == '未': # Goat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[0][7]]
        elif hour_earthly_branch == '申': # Monkey hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[0][8]]
        elif hour_earthly_branch == '酉': # Rooster hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[0][9]]
        elif hour_earthly_branch == '戌': # Dog hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[0][10]]
        else: # Pig hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[0][11]]
    elif day_heavenly_stem == '乙': # means daymaster is yin wood
        if hour_earthly_branch == '子': # Rat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[1][0]]
        elif hour_earthly_branch == '丑': # Ox hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[1][1]]
        elif hour_earthly_branch == '寅': # Tiger hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[1][2]]
        elif hour_earthly_branch == '卯': # Rabbit hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[1][3]]
        elif hour_earthly_branch == '辰': # Dragon hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[1][4]]
        elif hour_earthly_branch == '巳': # Snake hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[1][5]]
        elif hour_earthly_branch == '午': # Horse hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[1][6]]
        elif hour_earthly_branch == '未': # Goat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[1][7]]
        elif hour_earthly_branch == '申': # Monkey hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[1][8]]
        elif hour_earthly_branch == '酉': # Rooster hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[1][9]]
        elif hour_earthly_branch == '戌': # Dog hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[1][10]]
        else: # Pig hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[1][11]]
    elif day_heavenly_stem == '丙': # means daymaster is yang fire
        if hour_earthly_branch == '子': # Rat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[2][0]]
        elif hour_earthly_branch == '丑': # Ox hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[2][1]]
        elif hour_earthly_branch == '寅': # Tiger hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[2][2]]
        elif hour_earthly_branch == '卯': # Rabbit hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[2][3]]
        elif hour_earthly_branch == '辰': # Dragon hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[2][4]]
        elif hour_earthly_branch == '巳': # Snake hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[2][5]]
        elif hour_earthly_branch == '午': # Horse hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[2][6]]
        elif hour_earthly_branch == '未': # Goat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[2][7]]
        elif hour_earthly_branch == '申': # Monkey hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[2][8]]
        elif hour_earthly_branch == '酉': # Rooster hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[2][9]]
        elif hour_earthly_branch == '戌': # Dog hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[2][10]]
        else: # Pig hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[2][11]]
    elif day_heavenly_stem == '丁': # means daymaster is yin fire
        if hour_earthly_branch == '子': # Rat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[3][0]]
        elif hour_earthly_branch == '丑': # Ox hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[3][1]]
        elif hour_earthly_branch == '寅': # Tiger hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[3][2]]
        elif hour_earthly_branch == '卯': # Rabbit hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[3][3]]
        elif hour_earthly_branch == '辰': # Dragon hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[3][4]]
        elif hour_earthly_branch == '巳': # Snake hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[3][5]]
        elif hour_earthly_branch == '午': # Horse hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[3][6]]
        elif hour_earthly_branch == '未': # Goat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[3][7]]
        elif hour_earthly_branch == '申': # Monkey hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[3][8]]
        elif hour_earthly_branch == '酉': # Rooster hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[3][9]]
        elif hour_earthly_branch == '戌': # Dog hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[3][10]]
        else: # Pig hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[3][11]]
    elif day_heavenly_stem == '戊': # means daymaster is yang earth
        if hour_earthly_branch == '子': # Rat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[4][0]]
        elif hour_earthly_branch == '丑': # Ox hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[4][1]]
        elif hour_earthly_branch == '寅': # Tiger hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[4][2]]
        elif hour_earthly_branch == '卯': # Rabbit hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[4][3]]
        elif hour_earthly_branch == '辰': # Dragon hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[4][4]]
        elif hour_earthly_branch == '巳': # Snake hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[4][5]]
        elif hour_earthly_branch == '午': # Horse hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[4][6]]
        elif hour_earthly_branch == '未': # Goat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[4][7]]
        elif hour_earthly_branch == '申': # Monkey hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[4][8]]
        elif hour_earthly_branch == '酉': # Rooster hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[4][9]]
        elif hour_earthly_branch == '戌': # Dog hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[4][10]]
        else: # Pig hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[4][11]]
    elif day_heavenly_stem == '己': # means daymaster is yin earth
        if hour_earthly_branch == '子': # Rat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[5][0]]
        elif hour_earthly_branch == '丑': # Ox hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[5][1]]
        elif hour_earthly_branch == '寅': # Tiger hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[5][2]]
        elif hour_earthly_branch == '卯': # Rabbit hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[5][3]]
        elif hour_earthly_branch == '辰': # Dragon hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[5][4]]
        elif hour_earthly_branch == '巳': # Snake hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[5][5]]
        elif hour_earthly_branch == '午': # Horse hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[5][6]]
        elif hour_earthly_branch == '未': # Goat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[5][7]]
        elif hour_earthly_branch == '申': # Monkey hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[5][8]]
        elif hour_earthly_branch == '酉': # Rooster hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[5][9]]
        elif hour_earthly_branch == '戌': # Dog hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[5][10]]
        else: # Pig hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[5][11]]
    elif day_heavenly_stem == '庚': # means daymaster is yang metal
        if hour_earthly_branch == '子': # Rat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[6][0]]
        elif hour_earthly_branch == '丑': # Ox hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[6][1]]
        elif hour_earthly_branch == '寅': # Tiger hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[6][2]]
        elif hour_earthly_branch == '卯': # Rabbit hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[6][3]]
        elif hour_earthly_branch == '辰': # Dragon hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[6][4]]
        elif hour_earthly_branch == '巳': # Snake hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[6][5]]
        elif hour_earthly_branch == '午': # Horse hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[6][6]]
        elif hour_earthly_branch == '未': # Goat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[6][7]]
        elif hour_earthly_branch == '申': # Monkey hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[6][8]]
        elif hour_earthly_branch == '酉': # Rooster hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[6][9]]
        elif hour_earthly_branch == '戌': # Dog hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[6][10]]
        else: # Pig hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[6][11]]
    elif day_heavenly_stem == '辛': # means daymaster is yin metal
        if hour_earthly_branch == '子': # Rat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[7][0]]
        elif hour_earthly_branch == '丑': # Ox hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[7][1]]
        elif hour_earthly_branch == '寅': # Tiger hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[7][2]]
        elif hour_earthly_branch == '卯': # Rabbit hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[7][3]]
        elif hour_earthly_branch == '辰': # Dragon hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[7][4]]
        elif hour_earthly_branch == '巳': # Snake hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[7][5]]
        elif hour_earthly_branch == '午': # Horse hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[7][6]]
        elif hour_earthly_branch == '未': # Goat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[7][7]]
        elif hour_earthly_branch == '申': # Monkey hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[7][8]]
        elif hour_earthly_branch == '酉': # Rooster hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[7][9]]
        elif hour_earthly_branch == '戌': # Dog hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[7][10]]
        else: # Pig hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[7][11]]
    elif day_heavenly_stem == '壬': # means daymaster is yang water:
        if hour_earthly_branch == '子': # Rat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[8][0]]
        elif hour_earthly_branch == '丑': # Ox hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[8][1]]
        elif hour_earthly_branch == '寅': # Tiger hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[8][2]]
        elif hour_earthly_branch == '卯': # Rabbit hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[8][3]]
        elif hour_earthly_branch == '辰': # Dragon hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[8][4]]
        elif hour_earthly_branch == '巳': # Snake hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[8][5]]
        elif hour_earthly_branch == '午': # Horse hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[8][6]]
        elif hour_earthly_branch == '未': # Goat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[8][7]]
        elif hour_earthly_branch == '申': # Monkey hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[8][8]]
        elif hour_earthly_branch == '酉': # Rooster hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[8][9]]
        elif hour_earthly_branch == '戌': # Dog hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[8][10]]
        else: # Pig hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[8][11]]
    else: # elif day_heavenly_stem == '癸': # means daymaster is yin water
        if hour_earthly_branch == '子': # Rat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[9][0]]
        elif hour_earthly_branch == '丑': # Ox hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[9][1]]
        elif hour_earthly_branch == '寅': # Tiger hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[9][2]]
        elif hour_earthly_branch == '卯': # Rabbit hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[9][3]]
        elif hour_earthly_branch == '辰': # Dragon hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[9][4]]
        elif hour_earthly_branch == '巳': # Snake hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[9][5]]
        elif hour_earthly_branch == '午': # Horse hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[9][6]]
        elif hour_earthly_branch == '未': # Goat hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[9][7]]
        elif hour_earthly_branch == '申': # Monkey hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[9][8]]
        elif hour_earthly_branch == '酉': # Rooster hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[9][9]]
        elif hour_earthly_branch == '戌': # Dog hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[9][10]]
        else: # Pig hour
            return ELEMENTS[HOUR_HEAVENLY_STEM_ACCORDING_TO_DAY_HEAVENLY_STEM[9][11]]
    
    



