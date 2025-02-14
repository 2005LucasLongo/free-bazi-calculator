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

def check_nobleman_star(day_heavenly_stem, any_earthly_branch):
    nobleman_star = False
    if day_heavenly_stem == ELEMENTS[0] or day_heavenly_stem == ELEMENTS[4] or day_heavenly_stem == ELEMENTS[8]: # yang metal, yang wood, yang earth
        if any_earthly_branch in [ZODIAC[11], ZODIAC[5]]: # ox , goat
            nobleman_star = True
    elif day_heavenly_stem == ELEMENTS[6] or day_heavenly_stem == ELEMENTS[7]: # yang fire, yin fire
        if any_earthly_branch in [ZODIAC[7], ZODIAC[9]]: # rooster, pig
            nobleman_star = True
    elif day_heavenly_stem == ELEMENTS[5] or day_heavenly_stem == ELEMENTS[9]: # yin wood, yin earth
        if any_earthly_branch in [ZODIAC[6], ZODIAC[10]]: # monkey, rat
            nobleman_star = True
    elif day_heavenly_stem == ELEMENTS[1]: # yin metal
        if any_earthly_branch in [ZODIAC[0], ZODIAC[4]]: # tiger, horse
            nobleman_star = True
    elif day_heavenly_stem == ELEMENTS[2] or day_heavenly_stem == ELEMENTS[3]: # yang water, yin water
        if any_earthly_branch in [ZODIAC[1], ZODIAC[3]]: # rabbit, snake
            nobleman_star = True
    return nobleman_star

def check_succes_star(day_heavenly_stem, any_earthly_branch):
    success_star = False
    if day_heavenly_stem == ELEMENTS[0] or day_heavenly_stem == ELEMENTS[4] or day_heavenly_stem == ELEMENTS[8]: # yang metal, yang wood, yang earth
        if any_earthly_branch in [ZODIAC[10], ZODIAC[11]]: # rat, ox
            success_star = True
    elif day_heavenly_stem == ELEMENTS[6] or day_heavenly_stem == ELEMENTS[7]: # yang fire, yin fire
        if any_earthly_branch in [ZODIAC[2], ZODIAC[0]]: # tiger, dragon
            success_star = True
    elif day_heavenly_stem == ELEMENTS[5] or day_heavenly_stem == ELEMENTS[9]: # yin wood, yin earth
        if any_earthly_branch in [ZODIAC[6], ZODIAC[11]]: # monkey, ox
            success_star = True
    elif day_heavenly_stem == ELEMENTS[1]: # yin metal
        if any_earthly_branch in [ZODIAC[9], ZODIAC[5]]: # pig, goat
            success_star = True
    elif day_heavenly_stem == ELEMENTS[2] or day_heavenly_stem == ELEMENTS[3]: # yang water, yin water
        if any_earthly_branch in [ZODIAC[6], ZODIAC[8]]: # monkey, dog
            success_star = True
    return success_star

# sample 
print(check_nobleman_star('甲', '子'))
print(check_succes_star('甲', '子'))