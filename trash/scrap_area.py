from lunarcalendar import Converter, Solar
import lunardate as ld
import datetime as dt
from datetime import timedelta

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


def get_month_earthly_branch(solar_year, solar_month, solar_day):
  data_limite = ld.LunarDate.fromSolarDate(1900,1,31)
  data_nova = [solar_year, solar_month, solar_day] # solar
  data_limite_dtformat = dt.date(data_limite.year, data_limite.month, data_limite.day)

  if (data_nova[0] == 1900 and data_nova[1] == 1 and data_nova[2] < 31) or (data_nova[0] < 1900):
    diferenca_de_dias = ld.LunarDate.fromSolarDate(data_nova[0],data_nova[1],data_nova[2]).day - 1
    data_nova_lunar = data_limite_dtformat + timedelta(diferenca_de_dias)
  else:
    data_nova_lunar = ld.LunarDate.fromSolarDate(data_nova[0], data_nova[1], data_nova[2])

  # 31/01/1900 solar foi o 01/01/1900 lunar que é o limite de lunardate
  # logo, 30/01/1900 solar seria a véspera do ano novo lunar de 1899 para 1900

  # get the animal of the month
  return ZODIAC[data_nova_lunar.month - 1]

def get_month_heavenly_stem(solar_year, solar_month, solar_day):
  data_limite = ld.LunarDate.fromSolarDate(1900,1,31)
  data_nova = [solar_year, solar_month, solar_day] # solar
  data_limite_dtformat = dt.date(data_limite.year, data_limite.month, data_limite.day)

  if (data_nova[0] == 1900 and data_nova[1] == 1 and data_nova[2] < 31) or (data_nova[0] < 1900):
    diferenca_de_dias = ld.LunarDate.fromSolarDate(data_nova[0],data_nova[1],data_nova[2]).day - 1
    data_nova_lunar = data_limite_dtformat + timedelta(diferenca_de_dias)
  else:
    data_nova_lunar = ld.LunarDate.fromSolarDate(data_nova[0], data_nova[1], data_nova[2])

  # 31/01/1900 solar foi o 01/01/1900 lunar que é o limite de lunardate
  # logo, 30/01/1900 solar seria a véspera do ano novo lunar de 1899 para 1900

  # get the animal of the month
  month_earthly_branch = ZODIAC[data_nova_lunar.month - 1]

  # get the element of the month

  # # to get that we need the year element

  year_heavenly_stem_index = int((str(data_nova_lunar.year).strip(''))[-1])

  return MONTH_HEAVENLY_STEM_ACCORDING_TO_YEAR_HEAVENLY_STEM[year_heavenly_stem_index][data_nova_lunar.month - 1]
  

def get_month_heavenly_stem(solar_year, solar_month, solar_day):
  fixed_date = ld.LunarDate.fromSolarDate(1900,1,31)
  solar_new_date = [solar_year, solar_month, solar_day] # solar
  fixed_date_dtformat = dt.date(fixed_date.year, fixed_date.month, fixed_date.day)

  if (solar_new_date[0] == 1900 and solar_new_date[1] == 1 and solar_new_date[2] < 31) or (solar_new_date[0] < 1900):
    day_diff = ld.LunarDate.fromSolarDate(solar_new_date[0],solar_new_date[1],solar_new_date[2]).day - 1
    lunar_new_date = fixed_date_dtformat + timedelta(day_diff)
  else:
    lunar_new_date = ld.LunarDate.fromSolarDate(solar_new_date[0], solar_new_date[1], solar_new_date[2])

  # 31/01/1900 solar foi o 01/01/1900 lunar que é o limite de lunardate
  # logo, 30/01/1900 solar seria a véspera do ano novo lunar de 1899 para 1900

  # get the animal of the month
  month_earthly_branch = ZODIAC[lunar_new_date.month - 1]

  # get the element of the month

  # # to get that we need the year element

  year_heavenly_stem_index = int((str(lunar_new_date.year).strip(''))[-1])

  return MONTH_HEAVENLY_STEM_ACCORDING_TO_YEAR_HEAVENLY_STEM[year_heavenly_stem_index][lunar_new_date.month - 1]


def get_year_earthly_branch(solar_year, solar_month, solar_day):
  fixed_date = ld.LunarDate.fromSolarDate(1900,1,31)
  solar_new_date = [solar_year, solar_month, solar_day] # solar
  fixed_date_dtformat = dt.date(fixed_date.year, fixed_date.month, fixed_date.day)

  if (solar_new_date[0] == 1900 and solar_new_date[1] == 1 and solar_new_date[2] < 31) or (solar_new_date[0] < 1900):
    day_diff = ld.LunarDate.fromSolarDate(solar_new_date[0],solar_new_date[1],solar_new_date[2]).day - 1
    lunar_new_date = fixed_date_dtformat + timedelta(day_diff)
  else:
    lunar_new_date = ld.LunarDate.fromSolarDate(solar_new_date[0], solar_new_date[1], solar_new_date[2])

  # 31/01/1900 solar foi o 01/01/1900 lunar que é o limite de lunardate
  # logo, 30/01/1900 solar seria a véspera do ano novo lunar de 1899 para 1900
  
  lunar_year = lunar_new_date.year
  
  while lunar_year < 2010: # 2010 is the year of Metal Tiger
    lunar_year += 12
  while lunar_year > 2021: # 2021 is the year of Metal Ox
    lunar_year -= 12
  return ZODIAC[lunar_year-2010]

def get_year_heavenly_stem(solar_year, solar_month, solar_day):
  fixed_date = ld.LunarDate.fromSolarDate(1900,1,31)
  solar_new_date = [solar_year, solar_month, solar_day] # solar
  fixed_date_dtformat = dt.date(fixed_date.year, fixed_date.month, fixed_date.day)

  if (solar_new_date[0] == 1900 and solar_new_date[1] == 1 and solar_new_date[2] < 31) or (solar_new_date[0] < 1900):
    day_diff = ld.LunarDate.fromSolarDate(solar_new_date[0],solar_new_date[1],solar_new_date[2]).day - 1
    lunar_new_date = fixed_date_dtformat + timedelta(day_diff)
  else:
    lunar_new_date = ld.LunarDate.fromSolarDate(solar_new_date[0], solar_new_date[1], solar_new_date[2])

  # 31/01/1900 solar foi o 01/01/1900 lunar que é o limite de lunardate
  # logo, 30/01/1900 solar seria a véspera do ano novo lunar de 1899 para 1900

  year_heavenly_stem_index = int((str(lunar_new_date.year).strip(''))[-1])
  return ELEMENTS[year_heavenly_stem_index]

  
  
# sample
ano = 1899
mes = 10
dia = 4

print('Year pillar')
print(get_year_heavenly_stem(ano, mes, dia))
print(get_year_earthly_branch(ano, mes, dia))

print('Month pillar')
print(get_month_heavenly_stem(ano, mes, dia))
print(get_month_earthly_branch(ano, mes, dia))


