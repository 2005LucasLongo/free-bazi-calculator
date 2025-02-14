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

# sample
'''tayun = generate_tayun('m', '乙', '丁', '亥')
c = 1

print('-- TAYUN --')
for pillar in tayun:
    print(f'{c}th pillar: {pillar[0]}{pillar[1]}')
    c += 1'''