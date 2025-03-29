import lunardate as ld
import datetime as dt
import math

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

yang_elements = [
    ELEMENTS[0], # yang metal
    ELEMENTS[2], # yang water
    ELEMENTS[4], # yang wood
    ELEMENTS[6], # yang fire
    ELEMENTS[8] # yang earth
]

yin_elements = [
    ELEMENTS[1], # yin metal
    ELEMENTS[3], # yin water
    ELEMENTS[5], # yin wood
    ELEMENTS[7], # yin fire
    ELEMENTS[9] # yin earth
]

def generate_tayun(gender, year_heavenly_stem, month_heavenly_stem, month_earthly_branch, pillars_amount=10): 
    tayun_pillars = []

    if gender == 'm':
        if year_heavenly_stem in yang_elements:
            index_of_month_heavenly_stem = ELEMENTS.index(month_heavenly_stem)
            index_of_month_earthly_branch = ZODIAC.index(month_earthly_branch)
            
            for c in range(0, pillars_amount):
                if (index_of_month_heavenly_stem+1) >= 10:
                    index_of_month_heavenly_stem -= 10
                if (index_of_month_earthly_branch+1) >= 12:
                    index_of_month_earthly_branch -= 12
                # print(f'Pillar {c+1}: {ELEMENTS[index_of_month_heavenly_stem+1]}{ZODIAC[index_of_month_earthly_branch+1]}')
                tayun_pillars.append([ELEMENTS[index_of_month_heavenly_stem+1], ZODIAC[index_of_month_earthly_branch+1]])
                index_of_month_heavenly_stem += 1
                index_of_month_earthly_branch += 1
        elif year_heavenly_stem in yin_elements:
            index_of_month_heavenly_stem = ELEMENTS.index(month_heavenly_stem)
            index_of_month_earthly_branch = ZODIAC.index(month_earthly_branch)
            
            for c in range(0, pillars_amount):
                if (index_of_month_heavenly_stem-1) <= -11:
                    index_of_month_heavenly_stem += 10
                if (index_of_month_earthly_branch-1) <= -13:
                    index_of_month_earthly_branch += 12
                # print(f'Pillar {c+1}: {ELEMENTS[index_of_month_heavenly_stem-1]}{ZODIAC[index_of_month_earthly_branch-1]}')
                tayun_pillars.append([ELEMENTS[index_of_month_heavenly_stem-1], ZODIAC[index_of_month_earthly_branch-1]])
                index_of_month_heavenly_stem -= 1
                index_of_month_earthly_branch -= 1
    elif gender == 'f':
        if year_heavenly_stem in yang_elements:
            index_of_month_heavenly_stem = ELEMENTS.index(month_heavenly_stem)
            index_of_month_earthly_branch = ZODIAC.index(month_earthly_branch)
            
            for c in range(0, pillars_amount):
                if (index_of_month_heavenly_stem-1) <= -11:
                    index_of_month_heavenly_stem += 10
                if (index_of_month_earthly_branch-1) <= -13:
                    index_of_month_earthly_branch += 12
                # print(f'Pillar {c+1}: {ELEMENTS[index_of_month_heavenly_stem-1]}{ZODIAC[index_of_month_earthly_branch-1]}')
                tayun_pillars.append([ELEMENTS[index_of_month_heavenly_stem-1], ZODIAC[index_of_month_earthly_branch-1]])
                index_of_month_heavenly_stem -= 1
                index_of_month_earthly_branch -= 1
        elif year_heavenly_stem in yin_elements:
            index_of_month_heavenly_stem = ELEMENTS.index(month_heavenly_stem)
            index_of_month_earthly_branch = ZODIAC.index(month_earthly_branch)
            
            for c in range(0, pillars_amount):
                if (index_of_month_heavenly_stem+1) >= 10:
                    index_of_month_heavenly_stem -= 10
                if (index_of_month_earthly_branch+1) >= 12:
                    index_of_month_earthly_branch -= 12
                # print(f'Pillar {c+1}: {ELEMENTS[index_of_month_heavenly_stem+1]}{ZODIAC[index_of_month_earthly_branch+1]}')
                tayun_pillars.append([ELEMENTS[index_of_month_heavenly_stem+1], ZODIAC[index_of_month_earthly_branch+1]])
                index_of_month_heavenly_stem += 1
                index_of_month_earthly_branch += 1
    else:
        print('You must insert a valid gender!')
    return tayun_pillars

def get_tayun_start (solar_year, solar_month, solar_day, day_stem, gender):
    
    solar_date = dt.date(solar_year, solar_month, solar_day)
    lunar_date = ld.LunarDate.fromSolarDate(solar_date.year, solar_date.month, solar_date.day)
    
    JIEQI = [
        [lunar_date.year, 1, 6], # Xiaohan 0
        [lunar_date.year, 1, 21], # Dahan 1
        [lunar_date.year, 2, 5], # Lichun 2
        [lunar_date.year, 2, 19], # Yushui  3
        [lunar_date.year, 3, 6], # Jingzhe  4
        [lunar_date.year, 3, 21], # Chunfen  5
        [lunar_date.year, 4, 5], # Qingming 6
        [lunar_date.year, 4, 21], # Guyu 7
        [lunar_date.year, 5, 6], # Lixia 8
        [lunar_date.year, 5, 22], # Xiaoma 9 
        [lunar_date.year, 6, 6], # Mangzhong 10
        [lunar_date.year, 6, 22], # Xiazhi 11
        [lunar_date.year, 7, 8], # Xiaoshu 12
        [lunar_date.year, 7, 23], # Dashu 13
        [lunar_date.year, 8, 8], # Liqiu 14
        [lunar_date.year, 8, 24], # Chushu 15
        [lunar_date.year, 9, 8], # Bailu 16
        [lunar_date.year, 9, 24], # Qiufen 17
        [lunar_date.year, 10, 9], # Hanlu 18
        [lunar_date.year, 10, 24], # Shuangjiang 19
        [lunar_date.year, 11, 8], # Lidong  20
        [lunar_date.year, 11, 23], # Xiaoxue 21
        [lunar_date.year, 12, 8], # Daxue 22
        [lunar_date.year, 12, 22], # Dongzhi 23
        [lunar_date.year+1, 1, 6], # Xiaohan 24
        [lunar_date.year+1, 1, 21], # Dahan 25
    ]
    
    print(lunar_date)
    chosen_jieqi = None # lunar
    chosen_jieqi_to_solar = None
    
    if gender == 'm':
        if day_stem in ['庚', '壬', '甲', '丙', '戊']: # yang day stem
            return 0
        elif day_stem in ['辛', '癸', '乙', '丁', '己']: # in day stem
            # gets the closest jieqi before the given date
            for jieqi in JIEQI:
                # new getter of the closest jieqi before the given date
                if jieqi[0] > lunar_date.year:
                    break
                elif jieqi[0] == lunar_date.year and jieqi[1] > lunar_date.month:
                    break
                elif jieqi[1] == lunar_date.month and jieqi[2] > lunar_date.day:
                    break
                else:
                    chosen_jieqi = jieqi
        else:
            raise Exception("Invalid element for day heavenly stem!")
    elif gender == 'f':
        if day_stem in ['庚', '壬', '甲', '丙', '戊']: # yang day stem
            return 0
        elif day_stem in ['辛', '癸', '乙', '丁', '己']: # in day stem
            return 0
        else:
            raise Exception("Invalid element for day heavenly stem!")
    else:
        if (day_stem in ELEMENTS) == False:
            raise Exception("Invalid element and gender (must be 'm' or 'f')!")
        raise Exception("Gender must be 'm' or 'f'!")
    
    print(chosen_jieqi)
    difference_in_days = math.floor((dt.date(lunar_date.year, lunar_date.month, lunar_date.day) - dt.date(chosen_jieqi[0], chosen_jieqi[1], chosen_jieqi[2])).total_seconds()/float(86400)) # (lunar_date - ld.LunarDate(chosen_jieqi[0], chosen_jieqi[1], chosen_jieqi[2])).days
    print(difference_in_days)
    if difference_in_days < 0:
        difference_in_days = -(difference_in_days)
    initial_tayun = math.ceil(difference_in_days/3)
    return initial_tayun + solar_year


# sample
'''tayun = generate_tayun('m', '己', '丁', '酉')
init_year = get_tayun_start(2009,3,4,'己','m')

print('-- TAYUN --')
for pillar in tayun:
    print(f'{init_year-2009} years ({init_year}): {pillar[0]}{pillar[1]}')
    init_year += 10'''