from datetime import *
import datetime
import math
from lunarcalendar import *

# it can only support down until year 437 BC
year = 1661
original_year = year
month = 12
day = 31

base_year = 1662

if year <= 0:
    base_year += ((year * -1) + 1)
    year = 1

solar_date_A = datetime.date(year, month, day)
solar_date_B = datetime.date(base_year, 1, 1) # base date

print(solar_date_A)
print(solar_date_B)

diff_days = math.floor((solar_date_B - solar_date_A).total_seconds()/float(86400))
diff_days = (solar_date_B - solar_date_A).days 

if diff_days < 0:
    print(f'{day}.{month}.{original_year} está {diff_days * -1} dias depois de 1.1.1662')
else:
    print(f'{day}.{month}.{original_year} está {diff_days} dias antes de 1.1.1662')


lunar_date_B = Converter.Solar2Lunar(Solar(1662, 1, 1))
print(lunar_date_B)

print((datetime.date(1662,1,1)) - timedelta(diff_days))

lunar_date_A = lunar_date_B 
lunar_date_A.day -= diff_days

print(lunar_date_A)
# datetime_lunar_date_B = datetime.date(lunar_date_B.year, lunar_date_B.month, lunar_date_B.day)
# datetime_lunar_date_A = datetime_lunar_date_B - timedelta(diff_days)
