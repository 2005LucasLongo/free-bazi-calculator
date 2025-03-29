import lunardate as ld
import datetime as dt
import math

ELEMENTS = [
    '庚', '辛', # yang-yin metal 0 1
    '壬', '癸', # yang-yin water 2 3
    '甲', '乙', # yang-yin wood 4 5
    '丙', '丁', # yang-yin fire 6 7
    '戊', '己', # yang-yin earth 8 9
]

def get_tayun_start (solar_year, solar_month, solar_day, day_stem, gender):
    
    JIEQI = [
        [solar_year, 1, 6], # Xiaohan 0
        [solar_year, 1, 21], # Dahan 1
        [solar_year, 2, 5], # Lichun 2
        [solar_year, 2, 19], # Yushui  3
        [solar_year, 3, 6], # Jingzhe  4
        [solar_year, 3, 21], # Chunfen  5
        [solar_year, 4, 5], # Qingming 6
        [solar_year, 4, 21], # Guyu 7
        [solar_year, 5, 6], # Lixia 8
        [solar_year, 5, 22], # Xiaoma 9 
        [solar_year, 6, 6], # Mangzhong 10
        [solar_year, 6, 22], # Xiazhi 11
        [solar_year, 7, 8], # Xiaoshu 12
        [solar_year, 7, 23], # Dashu 13
        [solar_year, 8, 8], # Liqiu 14
        [solar_year, 8, 24], # Chushu 15
        [solar_year, 9, 8], # Bailu 16
        [solar_year, 9, 24], # Qiufen 17
        [solar_year, 10, 9], # Hanlu 18
        [solar_year, 10, 24], # Shuangjiang 19
        [solar_year, 11, 8], # Lidong  20
        [solar_year, 11, 23], # Xiaoxue 21
        [solar_year, 12, 8], # Daxue 22
        [solar_year, 12, 22], # Dongzhi 23
        [solar_year+1, 1, 6], # Xiaohan 24
        [solar_year+1, 1, 21], # Dahan 25
    ]
    
    solar_date = dt.date(solar_year, solar_month, solar_day)
    lunar_date = ld.LunarDate.fromSolarDate(solar_date.year, solar_date.month, solar_date.day)
    chosen_jieqi_to_solar = None
    
    if gender == 'm':
        if day_stem in ['庚', '壬', '甲', '丙', '戊']: # yang day stem
            # gets the closest jieqi after the given date
            for jieqi in JIEQI:
                jieqi_to_solar = ld.LunarDate(jieqi[0], jieqi[1], jieqi[2]).toSolarDate()
                if jieqi_to_solar >= solar_date:
                    chosen_jieqi_to_solar = jieqi_to_solar
                    break
        elif day_stem in ['辛', '癸', '乙', '丁', '己']: # in day stem
            # gets the closest jieqi before the given date
            for jieqi in JIEQI:
                jieqi_to_solar = ld.LunarDate(jieqi[0], jieqi[1], jieqi[2]).toSolarDate()
                if jieqi_to_solar <= solar_date:
                    chosen_jieqi_to_solar = jieqi_to_solar
                else:
                    break
        else:
            raise Exception("Invalid element for day heavenly stem!")
    elif gender == 'f':
        if day_stem in ['庚', '壬', '甲', '丙', '戊']: # yang day stem
            # gets the closest jieqi before the given date
            for jieqi in JIEQI:
                jieqi_to_solar = ld.LunarDate(jieqi[0], jieqi[1], jieqi[2]).toSolarDate()
                if jieqi_to_solar <= solar_date:
                    chosen_jieqi_to_solar = jieqi_to_solar
                else:
                    break
        elif day_stem in ['辛', '癸', '乙', '丁', '己']: # in day stem
            # gets the closest jieqi after the given date
            for jieqi in JIEQI:
                jieqi_to_solar = ld.LunarDate(jieqi[0], jieqi[1], jieqi[2]).toSolarDate()
                if jieqi_to_solar >= solar_date:
                    chosen_jieqi_to_solar = jieqi_to_solar
                    break
        else:
            raise Exception("Invalid element for day heavenly stem!")
    else:
        if (day_stem in ELEMENTS) == False:
            raise Exception("Invalid element and gender (must be 'm' or 'f')!")
        raise Exception("Gender must be 'm' or 'f'!")
    
    difference_in_days = math.floor((solar_date - chosen_jieqi_to_solar).total_seconds()/float(86400))
    if difference_in_days < 0:
        difference_in_days = -(difference_in_days)
    initial_tayun = math.ceil(difference_in_days/3)
    return initial_tayun + solar_year

