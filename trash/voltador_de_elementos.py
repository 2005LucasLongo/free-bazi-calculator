def get_day_heavenly_stem(solar_year, solar_month, solar_day):
    ELEMENTS = [
    '庚', '辛', # yang-yin metal 0 1
    '壬', '癸', # yang-yin water 2 3
    '甲', '乙', # yang-yin wood 4 5
    '丙', '丁', # yang-yin fire 6 7
    '戊', '己', # yang-yin earth 8 9
    ]
    
    import datetime as dt

    fixed_date = dt.date(2005,11,15) # yin water day
    new_date = dt.date(solar_year,solar_month,solar_day)
    difference_in_days = (new_date - fixed_date).days

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

def get_day_earthly_branch(solar_year, solar_month, solar_day):
    ZODIAC = [
    '寅', '卯', # Tiger, Rabbit 0 1
    '辰', '巳', # Dragon, Snake 2 3
    '午', '未', # Horse, Goat 4 5
    '申', '酉', # Monkey, Rooster 6 7
    '戌', '亥', # Dog, Pig 8 9
    '子', '丑' # Rat, Ox 10 11
    ]
    
    import datetime as dt

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
    
year = 1976
month = 10
day = 4
print(get_day_heavenly_stem(year, month, day))
print(get_day_earthly_branch(year, month, day))
