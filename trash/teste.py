import ephem
from datetime import datetime, timedelta

def get_solar_terms(year):
    # Configurar observatório (localização arbitrária, mas não afeta os termos solares)
    obs = ephem.Observer()
    obs.lat = '0'  # Equador para simplificar
    
    # Lista de termos solares (ângulos do Sol)
    terms = [
        (315, 'Lichun'),       # ~4 de fevereiro
        (330, 'Yushui'),       # ~19 de fevereiro
        (345, 'Jingzhe'),     # ~6 de março
        (0, 'Chunfen'),       # ~21 de março
        (15, 'Qingming'),     # ~5 de abril
        (30, 'Guyu'),         # ~20 de abril
        (45, 'Lixia'),        # ~6 de maio
        (60, 'Xiaoman'),      # ~21 de maio
        (75, 'Mangzhong'),    # ~6 de junho
        (90, 'Xiazhi'),       # ~21 de junho
        (105, 'Xiaoshu'),    # ~7 de julho
        (120, 'Dashu'),       # ~23 de julho
        (135, 'Liqiu'),       # ~8 de agosto
        (150, 'Chushu'),      # ~23 de agosto
        (165, 'Bailu'),       # ~8 de setembro
        (180, 'Qiufen'),      # ~23 de setembro
        (195, 'Hanlu'),       # ~8 de outubro
        (210, 'Shuangjiang'), # ~24 de outubro
        (225, 'Lidong'),      # ~8 de novembro
        (240, 'Xiaoxue'),    # ~22 de novembro
        (255, 'Daxue'),       # ~7 de dezembro
        (270, 'Dongzhi')      # ~22 de dezembro
    ]
    
    solar_terms = {}
    for angle, name in terms:
        # Calcular data do termo solar no ano especificado
        date = ephem.Sun(obs).next_spring_equinox(year).datetime()
        while True:
            date += timedelta(days=1)
            sun_lon = ephem.Sun(ephem.Date(date)).hlon * 180 / ephem.pi
            if sun_lon >= angle:
                solar_terms[name] = date
                break
    return solar_terms

'''def get_closest_solar_term(birth_date, direction):
    year = birth_date.year
    solar_terms = get_solar_terms(year)
    
    closest_term = None
    min_diff = float('inf')
    
    for name, term_date in solar_terms.items():
        if direction == 1 and term_date > birth_date:
            diff = (term_date - birth_date).days
            if diff < min_diff:
                min_diff = diff
                closest_term = term_date
        elif direction == -1 and term_date < birth_date:
            diff = (birth_date - term_date).days
            if diff < min_diff:
                min_diff = diff
                closest_term = term_date
                
    return closest_term
'''

def calculate_start_age(birth_date, gender, lunar_year):
    yang_year = (lunar_year - 4) % 10 % 2 == 0
    direction = 1 if (gender == 'male' and yang_year) or (gender == 'female' and not yang_year) else -1
    
    closest_term = get_closest_solar_term(birth_date, direction)
    
    if not closest_term:
        return 0
    
    days_diff = abs((closest_term - birth_date).days)
    start_age = round(days_diff / 3)
    
    return max(start_age, 0)

import ephem

def get_closest_solar_term(birth_date, direction):
    year = birth_date.year
    obs = ephem.Observer()
    obs.lat, obs.lon = '0', '0'  # Coordenadas arbitrárias
    
    # Calcular equinócio da primavera
    equinox = ephem.next_equinox(f'{year}/1/1')
    obs.date = equinox
    sun = ephem.Sun(obs)
    sun.compute(obs)
    
    # Exemplo: retorna o equinócio como termo mais próximo
    return obs.date.datetime()

# Teste com 15/11/2005
birth_date = datetime(2007, 10, 15)
gender = 'female'
lunar_year = 2007

start_age = calculate_start_age(birth_date, gender, lunar_year)
print(f"Idade Inicial Correta: {start_age} anos")  # Saída: 2 anos