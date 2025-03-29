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

def check_success_star(day_heavenly_stem, any_earthly_branch):
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

def check_yang_heavenly_noble_star(day_heavenly_stem, any_earthly_branch):
    yang_heavenly_noble = False
    if day_heavenly_stem == ELEMENTS[4] and any_earthly_branch == ZODIAC[5]: # yang wood, goat
        yang_heavenly_noble == True
    elif day_heavenly_stem == ELEMENTS[5] and any_earthly_branch == ZODIAC[6]: # yin wood, monkey
        yang_heavenly_noble == True
    elif day_heavenly_stem == ELEMENTS[6] and any_earthly_branch == ZODIAC[7]: # yang fire, rooster
        yang_heavenly_noble == True
    elif day_heavenly_stem == ELEMENTS[7] and any_earthly_branch == ZODIAC[9]: # yin fire, pig
        yang_heavenly_noble == True
    elif day_heavenly_stem == ELEMENTS[8] and any_earthly_branch == ZODIAC[11]: # yang earth, ox
        yang_heavenly_noble == True
    elif day_heavenly_stem == ELEMENTS[9] and any_earthly_branch == ZODIAC[10]: # yin earth, rat
        yang_heavenly_noble == True
    elif day_heavenly_stem == ELEMENTS[0] and any_earthly_branch == ZODIAC[11]: # yang metal, ox
        yang_heavenly_noble == True
    elif day_heavenly_stem == ELEMENTS[1] and any_earthly_branch == ZODIAC[0]: # yin metal, tiger
        yang_heavenly_noble == True
    elif day_heavenly_stem == ELEMENTS[2] and any_earthly_branch == ZODIAC[1]: # yang water, rabbit
        yang_heavenly_noble == True
    elif day_heavenly_stem == ELEMENTS[3] and any_earthly_branch == ZODIAC[3]: # yin water, snake
        yang_heavenly_noble == True
    return yang_heavenly_noble

def check_yin_heavenly_noble_star(day_heavenly_stem, any_earthly_branch):
    yin_heavenly_noble_star = False
    if day_heavenly_stem == ELEMENTS[4] and any_earthly_branch == ZODIAC[11]:
        yin_heavenly_noble_star = True # yang wood, ox
    elif day_heavenly_stem == ELEMENTS[5] and any_earthly_branch == ZODIAC[10]:
        yin_heavenly_noble_star = True # yin wood, rat
    elif day_heavenly_stem == ELEMENTS[6] and any_earthly_branch == ZODIAC[9]:
        yin_heavenly_noble_star = True # yang fire, pig
    elif day_heavenly_stem == ELEMENTS[7] and any_earthly_branch == ZODIAC[7]:
        yin_heavenly_noble_star = True # yin fire, rooster
    elif day_heavenly_stem == ELEMENTS[8] and any_earthly_branch == ZODIAC[5]:
        yin_heavenly_noble_star = True # yang earth, goat
    elif day_heavenly_stem == ELEMENTS[9] and any_earthly_branch == ZODIAC[6]:
        yin_heavenly_noble_star = True # yin earth, monkey
    elif day_heavenly_stem == ELEMENTS[0] and any_earthly_branch == ZODIAC[5]:
        yin_heavenly_noble_star = True # yang metal, goat
    elif day_heavenly_stem == ELEMENTS[1] and any_earthly_branch == ZODIAC[4]:
        yin_heavenly_noble_star = True # yin metal, horse
    elif day_heavenly_stem == ELEMENTS[2] and any_earthly_branch == ZODIAC[3]:
        yin_heavenly_noble_star = True # yang water, snake
    elif day_heavenly_stem == ELEMENTS[3] and any_earthly_branch == ZODIAC[1]:
        yin_heavenly_noble_star = True # yin water, rabbit
    return yin_heavenly_noble_star

def check_prosperity_star (day_heavenly_stem, any_earthly_branch):
    prosperity_star = False
    if day_heavenly_stem == ELEMENTS[4] and any_earthly_branch == ZODIAC[0]:
        prosperity_star = True # yang wood, tiger
    elif day_heavenly_stem == ELEMENTS[5] and any_earthly_branch == ZODIAC[1]:
        prosperity_star = True # yin wood, rabbit
    elif day_heavenly_stem == ELEMENTS[6] and any_earthly_branch == ZODIAC[3]:
        prosperity_star = True # yang fire, snake
    elif day_heavenly_stem == ELEMENTS[7] and any_earthly_branch == ZODIAC[4]:
        prosperity_star = True # yin fire, horse
    elif day_heavenly_stem == ELEMENTS[8] and any_earthly_branch == ZODIAC[3]:
        prosperity_star = True # yang earth, snake
    elif day_heavenly_stem == ELEMENTS[9] and any_earthly_branch == ZODIAC[4]:
        prosperity_star = True # yin earth, horse
    elif day_heavenly_stem == ELEMENTS[0] and any_earthly_branch == ZODIAC[6]:
        prosperity_star = True # yang metal, monkey 
    elif day_heavenly_stem == ELEMENTS[1] and any_earthly_branch == ZODIAC[7]:
        prosperity_star = True # yin metal, rooster
    elif day_heavenly_stem == ELEMENTS[2] and any_earthly_branch == ZODIAC[9]:
        prosperity_star = True # yang water, pig
    elif day_heavenly_stem == ELEMENTS[3] and any_earthly_branch == ZODIAC[10]:
        prosperity_star = True # yin water, rat
    return prosperity_star

def check_sword_star (day_heavenly_stem, any_earthly_branch):
    sword_star = False
    if day_heavenly_stem == ELEMENTS[4] and any_earthly_branch == ZODIAC[1]:
        sword_star = True # yang wood, rabbit
    elif day_heavenly_stem == ELEMENTS[5] and any_earthly_branch == ZODIAC[0]:
        sword_star = True # yin wood, tiger
    elif day_heavenly_stem == ELEMENTS[6] and any_earthly_branch == ZODIAC[4]:
        sword_star = True # yang fire, horse
    elif day_heavenly_stem == ELEMENTS[7] and any_earthly_branch == ZODIAC[3]:
        sword_star = True # yin fire, snake
    elif day_heavenly_stem == ELEMENTS[8] and any_earthly_branch == ZODIAC[4]:
        sword_star = True # yang earth, horse
    elif day_heavenly_stem == ELEMENTS[9] and any_earthly_branch == ZODIAC[3]:
        sword_star = True # yin earth, snake
    elif day_heavenly_stem == ELEMENTS[0] and any_earthly_branch == ZODIAC[7]:
        sword_star = True # yang metal, rooster
    elif day_heavenly_stem == ELEMENTS[1] and any_earthly_branch == ZODIAC[6]:
        sword_star = True # yin metal, monkey
    elif day_heavenly_stem == ELEMENTS[2] and any_earthly_branch == ZODIAC[10]:
        sword_star = True # yang water, rat
    elif day_heavenly_stem == ELEMENTS[3] and any_earthly_branch == ZODIAC[9]:
        sword_star = True # yin water, pig
    return sword_star

def check_golden_carriage_star (day_heavenly_stem, any_earthly_branch):
    golden_carriage_star = False
    if day_heavenly_stem == ELEMENTS[4] and any_earthly_branch == ZODIAC[2]:
        golden_carriage_star = True # yang wood, dragon
    elif day_heavenly_stem == ELEMENTS[5] and any_earthly_branch == ZODIAC[3]:
        golden_carriage_star = True # yin wood, snake
    elif day_heavenly_stem == ELEMENTS[6] and any_earthly_branch == ZODIAC[5]:
        golden_carriage_star = True # yang fire, goat
    elif day_heavenly_stem == ELEMENTS[7] and any_earthly_branch == ZODIAC[6]:
        golden_carriage_star = True # yin fire, monkey
    elif day_heavenly_stem == ELEMENTS[8] and any_earthly_branch == ZODIAC[5]:
        golden_carriage_star = True # yang earth, goat
    elif day_heavenly_stem == ELEMENTS[9] and any_earthly_branch == ZODIAC[6]:
        golden_carriage_star = True # yin earth, monkey
    elif day_heavenly_stem == ELEMENTS[0] and any_earthly_branch == ZODIAC[8]:
        golden_carriage_star = True # yang metal, dog
    elif day_heavenly_stem == ELEMENTS[1] and any_earthly_branch == ZODIAC[9]:
        golden_carriage_star = True # yin metal, pig
    elif day_heavenly_stem == ELEMENTS[2] and any_earthly_branch == ZODIAC[11]:
        golden_carriage_star = True # yang water, ox
    elif day_heavenly_stem == ELEMENTS[3] and any_earthly_branch == ZODIAC[0]:
        golden_carriage_star = True # yin water, tiger
    return golden_carriage_star

def check_red_peach_blossom_star (day_heavenly_stem, any_earthly_branch):
    red_peach_blossom_star = False
    if day_heavenly_stem == ELEMENTS[4] and any_earthly_branch == ZODIAC[4]:
        red_peach_blossom_star = True # yang wood, horse
    elif day_heavenly_stem == ELEMENTS[5] and any_earthly_branch == ZODIAC[4]:
        red_peach_blossom_star = True # yin wood, horse
    elif day_heavenly_stem == ELEMENTS[6] and any_earthly_branch == ZODIAC[0]:
        red_peach_blossom_star = True # yang fire, tiger
    elif day_heavenly_stem == ELEMENTS[7] and any_earthly_branch == ZODIAC[5]:
        red_peach_blossom_star = True # yin fire, goat
    elif day_heavenly_stem == ELEMENTS[8] and any_earthly_branch == ZODIAC[2]:
        red_peach_blossom_star = True # yang earth, dragon
    elif day_heavenly_stem == ELEMENTS[9] and any_earthly_branch == ZODIAC[2]:
        red_peach_blossom_star = True # yin earth, dragon
    elif day_heavenly_stem == ELEMENTS[0] and any_earthly_branch == ZODIAC[8]:
        red_peach_blossom_star = True # yang metal, dog 
    elif day_heavenly_stem == ELEMENTS[1] and any_earthly_branch == ZODIAC[7]:
        red_peach_blossom_star = True # yin metal, rooster
    elif day_heavenly_stem == ELEMENTS[2] and any_earthly_branch == ZODIAC[10]:
        red_peach_blossom_star = True # yang water, rat
    elif day_heavenly_stem == ELEMENTS[3] and any_earthly_branch == ZODIAC[6]:
        red_peach_blossom_star = True # yin water, monkey
    return red_peach_blossom_star

def check_academic_star (day_heavenly_stem, any_earthly_branch):
    academic_star = False
    if day_heavenly_stem == ELEMENTS[4] and any_earthly_branch == ZODIAC[3]:
        academic_star = True # yang wood, snake
    elif day_heavenly_stem == ELEMENTS[5] and any_earthly_branch == ZODIAC[4]:
        academic_star = True # yin wood, horse
    elif day_heavenly_stem == ELEMENTS[6] and any_earthly_branch == ZODIAC[6]:
        academic_star = True # yang fire, monkey
    elif day_heavenly_stem == ELEMENTS[7] and any_earthly_branch == ZODIAC[7]:
        academic_star = True # yin fire, rooster
    elif day_heavenly_stem == ELEMENTS[8] and any_earthly_branch == ZODIAC[6]:
        academic_star = True # yang earth, monkey
    elif day_heavenly_stem == ELEMENTS[9] and any_earthly_branch == ZODIAC[7]:
        academic_star = True # yin earth, rooster
    elif day_heavenly_stem == ELEMENTS[0] and any_earthly_branch == ZODIAC[9]:
        academic_star = True # yang metal, pig
    elif day_heavenly_stem == ELEMENTS[1] and any_earthly_branch == ZODIAC[10]:
        academic_star = True # yin metal, rat
    elif day_heavenly_stem == ELEMENTS[2] and any_earthly_branch == ZODIAC[0]:
        academic_star = True # yang water, tiger
    elif day_heavenly_stem == ELEMENTS[3] and any_earthly_branch == ZODIAC[1]:
        academic_star = True # yin water, rabbit
    return academic_star

def check_literacy_star (day_heavenly_stem, any_earthly_branch):
    literacy_star = False
    if day_heavenly_stem == ELEMENTS[4] and any_earthly_branch == ZODIAC[9]:
        literacy_star = True # yang wood, pig
    elif day_heavenly_stem == ELEMENTS[5] and any_earthly_branch == ZODIAC[4]:
        literacy_star = True # yin wood, horse
    elif day_heavenly_stem == ELEMENTS[6] and any_earthly_branch == ZODIAC[0]:
        literacy_star = True # yang fire, tiger
    elif day_heavenly_stem == ELEMENTS[7] and any_earthly_branch == ZODIAC[7]:
        literacy_star = True # yin fire, rooster
    elif day_heavenly_stem == ELEMENTS[8] and any_earthly_branch == ZODIAC[0]:
        literacy_star = True # yang earth, tiger
    elif day_heavenly_stem == ELEMENTS[9] and any_earthly_branch == ZODIAC[7]:
        literacy_star = True # yin earth, rooster
    elif day_heavenly_stem == ELEMENTS[0] and any_earthly_branch == ZODIAC[3]:
        literacy_star = True # yang metal, snake
    elif day_heavenly_stem == ELEMENTS[1] and any_earthly_branch == ZODIAC[11]:
        literacy_star = True # yin metal, rat
    elif day_heavenly_stem == ELEMENTS[2] and any_earthly_branch == ZODIAC[6]:
        literacy_star = True # yang water, monkey
    elif day_heavenly_stem == ELEMENTS[3] and any_earthly_branch == ZODIAC[1]:
        literacy_star = True # yin water, rabbit
    return literacy_star

def check_taiji_star (day_heavenly_stem, any_earthly_branch):
    '''
    More known in the brazilian community as "the star of methaphysical interest".
    '''
    taiji_star = False
    if day_heavenly_stem == ELEMENTS[4] and (any_earthly_branch in [ZODIAC[10], ZODIAC[4]]):
        taiji_star = True # yang wood, rat or horse
    elif day_heavenly_stem == ELEMENTS[5] and (any_earthly_branch in [ZODIAC[10], ZODIAC[4]]):
        taiji_star = True # yin wood, rat or horse
    elif day_heavenly_stem == ELEMENTS[6] and (any_earthly_branch in [ZODIAC[1], ZODIAC[7]]):
        taiji_star = True # yang fire, rabbit or rooster
    elif day_heavenly_stem == ELEMENTS[7] and (any_earthly_branch in [ZODIAC[1], ZODIAC[7]]):
        taiji_star = True # yin fire, rabbit or rooster
    elif day_heavenly_stem == ELEMENTS[8] and (any_earthly_branch in [ZODIAC[11], ZODIAC[2], ZODIAC[5], ZODIAC[8]]):
        taiji_star = True # yang earth, ox or dragon or goat or dog
    elif day_heavenly_stem == ELEMENTS[9] and (any_earthly_branch in [ZODIAC[11], ZODIAC[2], ZODIAC[5], ZODIAC[8]]):
        taiji_star = True # yin earth, ox or dragon or goat or dog
    elif day_heavenly_stem == ELEMENTS[0] and (any_earthly_branch in [ZODIAC[0], ZODIAC[9]]):
        taiji_star = True # yang metal, tiger or pig
    elif day_heavenly_stem == ELEMENTS[1] and (any_earthly_branch in [ZODIAC[0], ZODIAC[9]]):
        taiji_star = True # yin metal, tiger or pig
    elif day_heavenly_stem == ELEMENTS[2] and (any_earthly_branch in [ZODIAC[3], ZODIAC[6]]):
        taiji_star = True # yang water, snake or monkey
    elif day_heavenly_stem == ELEMENTS[3] and (any_earthly_branch in [ZODIAC[0], ZODIAC[9]]):
        taiji_star = True # yin water, tiger or pig
    return taiji_star

def check_liuhegui_star (day_heavenly_stem, any_heavenly_stem, any_earthly_branch):
    '''
    The Liu He Gui star, according to professor Leonardo Bartel, can be called "mentor of the six harmonies star".
    '''
    liuhegui_star = False
    any_pillar = f'{any_heavenly_stem}{any_earthly_branch}'
    if day_heavenly_stem == ELEMENTS[4] and (any_pillar in ['甲子', '甲午']):
        liuhegui_star = True # yang wood, wood rat or wood horse
    elif day_heavenly_stem == ELEMENTS[5] and (any_pillar in ['乙巳', '乙丑']):
        liuhegui_star = True # yin wood, wood snake or wood ox
    elif day_heavenly_stem == ELEMENTS[6] and (any_pillar in [ZODIAC['丙寅', '丙辰']]):
        liuhegui_star = True # yang fire, fire tiger or fire dragon
    # charts with yin fire DM don't have this star
    elif day_heavenly_stem == ELEMENTS[8] and (any_pillar in ['戊子', '戊午']):
        liuhegui_star = True # yang earth, earth rat or earth horse
    elif day_heavenly_stem == ELEMENTS[9] and (any_pillar in ['己巳', '己丑']):
        liuhegui_star = True # yin earth, earth snake or earth ox
    elif day_heavenly_stem == ELEMENTS[0] and (any_pillar in ['庚子', '庚午']):
        liuhegui_star = True # yang metal, metal rat or metal horse
    elif day_heavenly_stem == ELEMENTS[1] and (any_pillar in ['辛亥', '辛未']):
        liuhegui_star = True # yin metal, metal pig or metal goat
    elif day_heavenly_stem == ELEMENTS[2] and (any_pillar in ['壬申', '壬戌']):
        liuhegui_star = True # yang water, water monkey or water dog
    # charts with yin water DM don't have this star
    return liuhegui_star

def check_guishi_star (day_heavenly_stem, any_heavenly_stem, any_earthly_branch):
    '''
    The Gui Shi star, according to professor Leonardo Bartel, can be called "noble righteous output".
    '''
    guishi_star = False
    any_pillar = f'{any_heavenly_stem}{any_earthly_branch}'
    if day_heavenly_stem == ELEMENTS[4] and (any_pillar in ['丙辰', '丙寅']):
        guishi_star = True # yang wood, fire dragon or fire tiger
    elif day_heavenly_stem == ELEMENTS[5] and (any_pillar in ['丁亥', '丁酉']):
        guishi_star = True # yin wood, fire pig or fire rooster
    elif day_heavenly_stem == ELEMENTS[6] and (any_pillar in ['戊子', '戊午']):
        guishi_star = True # yang fire, earth rat or earth horse
    elif day_heavenly_stem == ELEMENTS[7] and (any_pillar in ['己巳', '己丑']):
        guishi_star = True # yin fire, earth snake or earth ox
    elif day_heavenly_stem == ELEMENTS[8] and (any_pillar in ['庚子', '庚午']):
        guishi_star = True # yang earth, metal rat or metal horse
    elif day_heavenly_stem == ELEMENTS[9] and (any_pillar in ['辛亥', '辛未']):
        guishi_star = True # yin earth, metal pig or metal goat
    elif day_heavenly_stem == ELEMENTS[0] and (any_pillar in ['壬戌', '壬申']):
        guishi_star = True # yang metal, water dog or water monkey
    elif day_heavenly_stem == ELEMENTS[1] and (any_pillar in ['癸巳', '癸卯']):
        guishi_star = True # yin metal, water snake or water rabbit
    elif day_heavenly_stem == ELEMENTS[2] and (any_pillar in ['甲子', '甲午']):
        guishi_star = True # yang water, wood rat or wood horse
    elif day_heavenly_stem == ELEMENTS[3] and (any_pillar in ['乙丑', '乙巳']):
        guishi_star = True # yin water, wood ox or wood snake
    return guishi_star

def check_guihe_star (day_heavenly_stem, any_heavenly_stem, any_earthly_branch):
    '''
    The Gui He, according to professor Leonardo Bartel, can be called "noble harmony".
    '''
    guihe_star = False
    any_pillar = f'{any_heavenly_stem}{any_earthly_branch}'
    if day_heavenly_stem == ELEMENTS[4] and (any_pillar in ['己丑', '己未']):
        guihe_star = True # yang wood, earth ox or earth goat 
    elif day_heavenly_stem == ELEMENTS[5] and (any_pillar in ['庚子', '庚申']):
        guihe_star = True # yin wood, metal rat or metal monkey
    elif day_heavenly_stem == ELEMENTS[6] and (any_pillar in ['辛酉', '辛亥']):
        guihe_star = True # yang fire, metal rooster or metal pig
    # charts with yin fire DM don't have this star
    elif day_heavenly_stem == ELEMENTS[8] and (any_pillar in ['癸丑', '癸未']):
        guihe_star = True # yang earth, water ox or water goat
    elif day_heavenly_stem == ELEMENTS[9] and (any_pillar in ['甲子', '甲申']):
        guihe_star = True # yin earth, wood rat or wood monkey
    elif day_heavenly_stem == ELEMENTS[0] and (any_pillar in ['乙丑', '乙未']):
        guihe_star = True # yang metal, wood ox or wood goat
    elif day_heavenly_stem == ELEMENTS[1] and (any_pillar in ['丙午', '丙寅']):
        guihe_star = True # yin metal, fire horse or fire tiger
    elif day_heavenly_stem == ELEMENTS[2] and (any_pillar in ['丁卯', '丁巳']):
        guihe_star = True # yang water, fire rabbit or fire snake
    # charts with yin water DM don't have this star
    return guihe_star

def check_general_star (day_earthly_branch, other_earthly_branch):
    general_star = False
    if (day_earthly_branch in [ZODIAC[10], ZODIAC[2], ZODIAC[6]]) and (other_earthly_branch == ZODIAC[10]):
        general_star = True # water triad, rat
    elif (day_earthly_branch in [ZODIAC[11], ZODIAC[3], ZODIAC[7]]) and (other_earthly_branch == ZODIAC[7]):
        general_star = True # metal triad, rooster
    elif (day_earthly_branch in [ZODIAC[1], ZODIAC[5], ZODIAC[9]]) and (other_earthly_branch == ZODIAC[1]):
        general_star = True # wood triad, rabbit
    elif (day_earthly_branch in [ZODIAC[0], ZODIAC[4], ZODIAC[8]]) and (other_earthly_branch == ZODIAC[4]):
        general_star = True # fire triad, horse
    return general_star

def check_travelling_horse_star (year_earthly_branch, day_earthly_branch, other_earthly_branch):
    # chekcing day branch
    if (day_earthly_branch in [ZODIAC[10], ZODIAC[2], ZODIAC[6]]) and (other_earthly_branch == ZODIAC[0]):
        return True # water triad, tiger
    if (day_earthly_branch in [ZODIAC[11], ZODIAC[3], ZODIAC[7]]) and (other_earthly_branch == ZODIAC[9]):
        return True # metal triad, pig
    if (day_earthly_branch in [ZODIAC[1], ZODIAC[5], ZODIAC[9]]) and (other_earthly_branch == ZODIAC[3]):
        return True # wood triad, snake
    if (day_earthly_branch in [ZODIAC[0], ZODIAC[4], ZODIAC[8]]) and (other_earthly_branch == ZODIAC[6]):
        return True # fire triad, monkey
    # chekcing year branch
    if year_earthly_branch == ZODIAC[10] and other_earthly_branch == ZODIAC[0]: # rat month
        return True
    if year_earthly_branch == ZODIAC[11] and other_earthly_branch == ZODIAC[9]: # ox month
        return True
    if year_earthly_branch == ZODIAC[0] and other_earthly_branch == ZODIAC[6]: # tiger month
        return True
    if year_earthly_branch == ZODIAC[1] and other_earthly_branch == ZODIAC[3]: # rabbit month
        return True
    if year_earthly_branch == ZODIAC[2] and other_earthly_branch == ZODIAC[0]: # dragon month
        return True
    if year_earthly_branch == ZODIAC[3] and other_earthly_branch == ZODIAC[9]: # snake month
        return True
    if year_earthly_branch == ZODIAC[4] and other_earthly_branch == ZODIAC[6]: # horse month
        return True
    if year_earthly_branch == ZODIAC[5] and other_earthly_branch == ZODIAC[3]: # goat month
        return True
    if year_earthly_branch == ZODIAC[6] and other_earthly_branch == ZODIAC[0]: # monkey month
        return True
    if year_earthly_branch == ZODIAC[7] and other_earthly_branch == ZODIAC[9]: # rooster month
        return True
    if year_earthly_branch == ZODIAC[8] and other_earthly_branch == ZODIAC[6]: # dog month
        return True
    if year_earthly_branch == ZODIAC[9] and other_earthly_branch == ZODIAC[3]: # pig month
        return True
    else:
        return False

def check_peach_blossoms_star (year_earthly_branch, day_earthly_branch, other_earthly_branch):
    # checking day branch
    if (day_earthly_branch in [ZODIAC[10], ZODIAC[2], ZODIAC[6]]) and (other_earthly_branch == ZODIAC[7]):
        return True # water triad, rooster
    elif (day_earthly_branch in [ZODIAC[11], ZODIAC[3], ZODIAC[7]]) and (other_earthly_branch == ZODIAC[4]):
        return True # metal triad, horse
    elif (day_earthly_branch in [ZODIAC[1], ZODIAC[5], ZODIAC[9]]) and (other_earthly_branch == ZODIAC[10]):
        return True # wood triad, rat
    elif (day_earthly_branch in [ZODIAC[0], ZODIAC[4], ZODIAC[8]]) and (other_earthly_branch == ZODIAC[1]):
        return True # fire triad, rabbit
    # chekcing year branch
    if year_earthly_branch == ZODIAC[10] and other_earthly_branch == ZODIAC[7]: # rat month
        return True
    if year_earthly_branch == ZODIAC[11] and other_earthly_branch == ZODIAC[4]: # ox month
        return True
    if year_earthly_branch == ZODIAC[0] and other_earthly_branch == ZODIAC[1]: # tiger month
        return True
    if year_earthly_branch == ZODIAC[1] and other_earthly_branch == ZODIAC[10]: # rabbit month
        return True
    if year_earthly_branch == ZODIAC[2] and other_earthly_branch == ZODIAC[7]: # dragon month
        return True
    if year_earthly_branch == ZODIAC[3] and other_earthly_branch == ZODIAC[4]: # snake month
        return True
    if year_earthly_branch == ZODIAC[4] and other_earthly_branch == ZODIAC[1]: # horse month
        return True
    if year_earthly_branch == ZODIAC[5] and other_earthly_branch == ZODIAC[10]: # goat month
        return True
    if year_earthly_branch == ZODIAC[6] and other_earthly_branch == ZODIAC[7]: # monkey month
        return True
    if year_earthly_branch == ZODIAC[7] and other_earthly_branch == ZODIAC[4]: # rooster month
        return True
    if year_earthly_branch == ZODIAC[8] and other_earthly_branch == ZODIAC[1]: # dog month
        return True
    if year_earthly_branch == ZODIAC[9] and other_earthly_branch == ZODIAC[10]: # pig month
        return True
    else:
        return False

def check_robbing_star (day_earthly_branch, other_earthly_branch):
    robbing_star = False
    if (day_earthly_branch in [ZODIAC[10], ZODIAC[2], ZODIAC[6]]) and (other_earthly_branch == ZODIAC[3]):
        robbing_star = True # water triad, snake
    elif (day_earthly_branch in [ZODIAC[11], ZODIAC[3], ZODIAC[7]]) and (other_earthly_branch == ZODIAC[0]):
        robbing_star = True # metal triad, tiger
    elif (day_earthly_branch in [ZODIAC[1], ZODIAC[5], ZODIAC[9]]) and (other_earthly_branch == ZODIAC[6]):
        robbing_star = True # wood triad, monkey
    elif (day_earthly_branch in [ZODIAC[0], ZODIAC[4], ZODIAC[8]]) and (other_earthly_branch == ZODIAC[9]):
        robbing_star = True # fire triad, pig
    return robbing_star

def check_death_star (day_earthly_branch, other_earthly_branch):
    death_star = False
    if (day_earthly_branch in [ZODIAC[10], ZODIAC[2], ZODIAC[6]]) and (other_earthly_branch == ZODIAC[9]):
        death_star = True # water triad, pig
    elif (day_earthly_branch in [ZODIAC[11], ZODIAC[3], ZODIAC[7]]) and (other_earthly_branch == ZODIAC[6]):
        death_star = True # metal triad, monkey
    elif (day_earthly_branch in [ZODIAC[1], ZODIAC[5], ZODIAC[9]]) and (other_earthly_branch == ZODIAC[0]):
        death_star = True # wood triad, tiger
    elif (day_earthly_branch in [ZODIAC[0], ZODIAC[4], ZODIAC[8]]) and (other_earthly_branch == ZODIAC[3]):
        death_star = True # fire triad, snake
    return death_star

def check_solitary_star (day_earthly_branch, other_earthly_branch):
    solitary_star = False
    if (day_earthly_branch in [ZODIAC[9], ZODIAC[10], ZODIAC[11]]) and (other_earthly_branch == ZODIAC[0]):
        solitary_star == True # pig-rat-ox, tiger
    elif (day_earthly_branch in [ZODIAC[0], ZODIAC[1], ZODIAC[2]]) and (other_earthly_branch == ZODIAC[3]):
        solitary_star == True # tiger-rabbit-dragon, snake
    elif (day_earthly_branch in [ZODIAC[3], ZODIAC[4], ZODIAC[5]]) and (other_earthly_branch == ZODIAC[6]):
        solitary_star == True # snake-horse-goat, monkey
    elif (day_earthly_branch in [ZODIAC[6], ZODIAC[7], ZODIAC[8]]) and (other_earthly_branch == ZODIAC[9]):
        solitary_star == True # monkey-rooster-dog, pig
    return solitary_star

def check_forlorn_star (day_earthly_branch, other_earthly_branch):
    forlorn_star = False
    if (day_earthly_branch in [ZODIAC[9], ZODIAC[10], ZODIAC[11]]) and (other_earthly_branch == ZODIAC[8]):
        forlorn_star == True # pig-rat-ox, dog
    elif (day_earthly_branch in [ZODIAC[0], ZODIAC[1], ZODIAC[2]]) and (other_earthly_branch == ZODIAC[11]):
        forlorn_star == True # tiger-rabbit-dragon, ox
    elif (day_earthly_branch in [ZODIAC[3], ZODIAC[4], ZODIAC[5]]) and (other_earthly_branch == ZODIAC[2]):
        forlorn_star == True # snake-horse-goat, dragon
    elif (day_earthly_branch in [ZODIAC[6], ZODIAC[7], ZODIAC[8]]) and (other_earthly_branch == ZODIAC[5]):
        forlorn_star == True # monkey-rooster-dog, goat
    return forlorn_star

# the legendary point where I started adding new detectors
def check_intelectual_pillar (any_heavenly_stem, any_earthly_branch):
    '''
    Pilares intelectuais:
    Pessoas altamente inteligentes, com mentes aguçadas que sobressaem academicamente.
    '''
    pillar = any_heavenly_stem + any_earthly_branch
    pillars = [
        '戊⼦',
        '⼰丑',
        '⾟⺒',
        '丁未',
        '丙午',
        '⼰未'
    ]
    if pillar in pillars:
        return True
    else:
        return False

def check_clever_pillar  (any_heavenly_stem, any_earthly_branch):
    '''
    Pilar da astúcia e do metodismo:
    Indivíduos altamente inteligentes que planeiam metodicamente.
    '''
    pillar = any_heavenly_stem + any_earthly_branch
    pillars = [
        '戊子',
        '⾟巳'
    ]
    if pillar in pillars:
        return True
    else:
        return False

def check_canniness_pillar (any_heavenly_stem, any_earthly_branch):
    '''
    Pilar de esperteza:
    Peritos, inteligentes e perceptivos.
    '''
    pillar = any_heavenly_stem + any_earthly_branch
    pillars = [
        '丙⾠',
        '戊午',
        '甲⾠',
        '庚戌',
        '⾟亥',
        '丁酉',
        '壬寅',
        '庚寅',
        '⼄亥',
        '癸未'
    ]
    if pillar in pillars:
        return True
    else:
        return False

def check_redlight_pillar (any_heavenly_stem, any_earthly_branch):
    '''
    Pilar da Luz Vermelha:
    (apelidei de pilar da putaria, mas a tradução oficial é a acima)
    (entendeu? luz vermelha? putaria? eu achei engraçado)
    Este sete pilares representam problemas no romance, relacionamentos e amor.
    '''
    pillar = any_heavenly_stem + any_earthly_branch
    pillars = [
        '丁未',
        '庚戌',
        '甲戌',
        '⼄亥',
        '癸未',
        '丙寅',
        '⾟未'
    ]
    if pillar in pillars:
        return True
    else:
        return False

def check_yinyang_mismatch_pillar (any_heavenly_stem, any_earthly_branch):
    '''
    Pilares do desenocntro de Yin e Yang:
    Pessoas que experienciam problemas de relacionamento afectivo ou familiar (cônjuge ou sogros).
    '''
    pillar = any_heavenly_stem + any_earthly_branch
    pillars = [
        '⾟⾣',
        '壬戌',
        '癸亥',
        '丙午',
        '丁未',
        '戊申',
        '⾟卯',
        '壬⾠',
        '癸巳',
        '丙子',
        '丁丑',
        '戊寅'
    ]
    if pillar in pillars:
        return True
    else:
        return False

def check_domination_pillar (any_heavenly_stem, any_earthly_branch):
    '''
    Pilares dominantes:
    Pessoas altamente capazes, ambiciosas e motivadas. Sucesso e reconhecimento. Teimosia e espiritualidade.
    '''
    pillar = any_heavenly_stem + any_earthly_branch
    pillars = [
        '壬戌',
        '庚戌',
        '戊戌',
        '壬辰',
        '庚辰',
        '戊辰'
    ]
    if pillar in pillars:
        return True
    else:
        return False
    
def check_heavenly_mitigation_star (month_earthly_branch, any_heavenly_stem, any_earthly_branch):
    '''
    Estrela do alívio celestial: quando este pilar está presente na carta base, em qualquer pilar,
    confere um alto grau de proteção, normalmente usado para aliviar questões legais.
    '''
    pillar = any_heavenly_stem + any_earthly_branch
    if month_earthly_branch == ZODIAC[10] and pillar == f'{ELEMENTS[4]}{ZODIAC[10]}': # rat month
        return True
    if month_earthly_branch == ZODIAC[11] and pillar == f'{ELEMENTS[4]}{ZODIAC[10]}': # ox month
        return True
    if month_earthly_branch == ZODIAC[0] and pillar == f'{ELEMENTS[8]}{ZODIAC[0]}': # tiger month
        return True
    if month_earthly_branch == ZODIAC[1] and pillar == f'{ELEMENTS[8]}{ZODIAC[0]}': # rabbit month
        return True
    if month_earthly_branch == ZODIAC[2] and pillar == f'{ELEMENTS[8]}{ZODIAC[0]}': # dragon month
        return True
    if month_earthly_branch == ZODIAC[3] and pillar == f'{ELEMENTS[4]}{ZODIAC[4]}': # snake month
        return True
    if month_earthly_branch == ZODIAC[4] and pillar == f'{ELEMENTS[4]}{ZODIAC[4]}': # horse month
        return True
    if month_earthly_branch == ZODIAC[5] and pillar == f'{ELEMENTS[4]}{ZODIAC[4]}': # goat month
        return True
    if month_earthly_branch == ZODIAC[6] and pillar == f'{ELEMENTS[8]}{ZODIAC[6]}': # monkey month
        return True
    if month_earthly_branch == ZODIAC[7] and pillar == f'{ELEMENTS[8]}{ZODIAC[6]}': # rooster month
        return True
    if month_earthly_branch == ZODIAC[8] and pillar == f'{ELEMENTS[8]}{ZODIAC[6]}': # dog month
        return True
    if month_earthly_branch == ZODIAC[9] and pillar == f'{ELEMENTS[4]}{ZODIAC[10]}': # pig month
        return True
    else:
        return False

def check_heavenly_happiness_star (month_earthly_branch, any_earthly_branch):
    '''
    Estrela da felicidade celestial: est aestrela torna a pessoa optimista, altamente satisfeita
    com a sua vida e  generosa. Não se envolve em disputas ou detalhes supérfluos. Quando encontra
    obstáculos e desafios trabalhará para os resolver. É responsável não pregando ou culpabilizando
    terceiros. Quando uma carta tem a estrela do alívio celestial e a felicidade celestial diz-se
    que a pessoa é abençoada.
    '''
    if month_earthly_branch == ZODIAC[10] and any_earthly_branch == ZODIAC[5]: # rat month
        return True
    if month_earthly_branch == ZODIAC[11] and any_earthly_branch == ZODIAC[5]: # ox month
        return True
    if month_earthly_branch == ZODIAC[0] and any_earthly_branch == ZODIAC[8]: # tiger month
        return True
    if month_earthly_branch == ZODIAC[1] and any_earthly_branch == ZODIAC[8]: # rabbit month
        return True
    if month_earthly_branch == ZODIAC[2] and any_earthly_branch == ZODIAC[8]: # dragon month
        return True
    if month_earthly_branch == ZODIAC[3] and any_earthly_branch == ZODIAC[11]: # snake month
        return True
    if month_earthly_branch == ZODIAC[4] and any_earthly_branch == ZODIAC[11]: # horse month
        return True
    if month_earthly_branch == ZODIAC[5] and any_earthly_branch == ZODIAC[11]: # goat month
        return True
    if month_earthly_branch == ZODIAC[6] and any_earthly_branch == ZODIAC[2]: # monkey month
        return True
    if month_earthly_branch == ZODIAC[7] and any_earthly_branch == ZODIAC[2]: # rooster month
        return True
    if month_earthly_branch == ZODIAC[8] and any_earthly_branch == ZODIAC[2]: # dog month
        return True
    if month_earthly_branch == ZODIAC[9] and any_earthly_branch == ZODIAC[5]: # pig month
        return True
    else:
        return False

def check_heavenly_virtue_star(month_earthly_branch, any_heavenly_stem, any_earthly_branch):
    '''
    Estrelas da virtude celestial e virtude mensal:
    Ambas estas estrelas potencial o mesmo efeito, sendo que a virtude celestial representa
    o lado yang, tendo uma consequênica mais forte e fiável. A estrela da virtude mensal, como
    é yin representa uma protecção mais gentil e suave.
    
    Estas estrelas aliviam influências negativas. Quando estão presentes na carta base potenciam
    uma personalidade bondosa, benevolente, generosa e que recebe assistência do universo.
    
    Claro que se não estiverem presentes na carta base ainda se poderão sentir os seus efeitos
    nos períodos do destino ou anos.
    
    A assistência do universo toma diversas formas, diferentes para cada um de nós. Se houver a
    oportunidade de passar por um ano ou período do destino que active estas estrelas na nossa
    carta, é importante registrar e anotar os benefícios recebidos.
    '''
    # first we will check the heavenly virtue star, and on the next function we check the monthly virtue star
    if month_earthly_branch == ZODIAC[10] and (any_earthly_branch == ZODIAC[3]): # rat month
        return True
    if month_earthly_branch == ZODIAC[11] and (any_earthly_branch == ZODIAC[0]): # ox month
        return True
    if month_earthly_branch == ZODIAC[0] and (any_heavenly_stem == ELEMENTS[7]): # tiger month
        return True
    if month_earthly_branch == ZODIAC[1] and (any_earthly_branch == ZODIAC[6]): # rabbit month
        return True
    if month_earthly_branch == ZODIAC[2] and (any_heavenly_stem == ELEMENTS[2]): # dragon month
        return True
    if month_earthly_branch == ZODIAC[3] and (any_heavenly_stem == ELEMENTS[1]): # snake month
        return True
    if month_earthly_branch == ZODIAC[4] and (any_earthly_branch == ZODIAC[9]): # horse month
        return True
    if month_earthly_branch == ZODIAC[5] and (any_heavenly_stem == ELEMENTS[4]): # goat month
        return True
    if month_earthly_branch == ZODIAC[6] and (any_heavenly_stem == ELEMENTS[3]): # monkey month
        return True
    if month_earthly_branch == ZODIAC[7] and (any_earthly_branch == ZODIAC[0]): # rooster month
        return True
    if month_earthly_branch == ZODIAC[8] and (any_heavenly_stem == ELEMENTS[6]): # dog month
        return True
    if month_earthly_branch == ZODIAC[9] and (any_heavenly_stem == ELEMENTS[5]): # pig month
        return True
    else:
        return False

def check_monthly_virtue_star(month_earthly_branch, any_heavenly_stem, any_earthly_branch):
    '''
    Estrelas da virtude celestial e virtude mensal:
    Ambas estas estrelas potencial o mesmo efeito, sendo que a virtude celestial representa
    o lado yang, tendo uma consequênica mais forte e fiável. A estrela da virtude mensal, como
    é yin representa uma protecção mais gentil e suave.
    
    Estas estrelas aliviam influências negativas. Quando estão presentes na carta base potenciam
    uma personalidade bondosa, benevolente, generosa e que recebe assistência do universo.
    
    Claro que se não estiverem presentes na carta base ainda se poderão sentir os seus efeitos
    nos períodos do destino ou anos.
    
    A assistência do universo toma diversas formas, diferentes para cada um de nós. Se houver a
    oportunidade de passar por um ano ou período do destino que active estas estrelas na nossa
    carta, é importante registrar e anotar os benefícios recebidos.
    '''
    if month_earthly_branch == ZODIAC[10] and (any_heavenly_stem == ELEMENTS[2]): # rat month
        return True
    if month_earthly_branch == ZODIAC[11] and (any_heavenly_stem == ELEMENTS[0]): # ox month
        return True
    if month_earthly_branch == ZODIAC[0] and (any_heavenly_stem == ELEMENTS[6]): # tiger month
        return True
    if month_earthly_branch == ZODIAC[1] and (any_heavenly_stem == ELEMENTS[4]): # rabbit month
        return True
    if month_earthly_branch == ZODIAC[2] and (any_heavenly_stem == ELEMENTS[2]): # dragon month
        return True
    if month_earthly_branch == ZODIAC[3] and (any_heavenly_stem == ELEMENTS[0]): # snake month
        return True
    if month_earthly_branch == ZODIAC[4] and (any_heavenly_stem == ELEMENTS[6]): # horse month
        return True
    if month_earthly_branch == ZODIAC[5] and (any_heavenly_stem == ELEMENTS[4]): # goat month
        return True
    if month_earthly_branch == ZODIAC[6] and (any_heavenly_stem == ELEMENTS[2]): # monkey month
        return True
    if month_earthly_branch == ZODIAC[7] and (any_heavenly_stem == ELEMENTS[0]): # rooster month
        return True
    if month_earthly_branch == ZODIAC[8] and (any_heavenly_stem == ELEMENTS[6]): # dog month
        return True
    if month_earthly_branch == ZODIAC[9] and (any_heavenly_stem == ELEMENTS[4]): # pig month
        return True
    else:
        return False

# copypaste for code-use

'''
def check_name_pillar (any_heavenly_stem, any_earthly_branch):
    pillar = any_heavenly_stem + any_earthly_branch
    pillars = [
    ]
    if pillar in pillars:
        return True
    else:
        return False
'''

'''
def check_NAME_star (day_heavenly_stem, any_earthly_branch):
    NAME_star = False
    if day_heavenly_stem == ELEMENTS[4] and (any_earthly_branch in [ZODIAC[]]):
        NAME_star = True # yang wood, 
    elif day_heavenly_stem == ELEMENTS[5] and (any_earthly_branch in [ZODIAC[]]):
        NAME_star = True # yin wood, 
    elif day_heavenly_stem == ELEMENTS[6] and (any_earthly_branch in [ZODIAC[]]):
        NAME_star = True # yang fire, 
    elif day_heavenly_stem == ELEMENTS[7] and (any_earthly_branch in [ZODIAC[]]):
        NAME_star = True # yin fire, 
    elif day_heavenly_stem == ELEMENTS[8] and (any_earthly_branch in [ZODIAC[]]):
        NAME_star = True # yang earth,
    elif day_heavenly_stem == ELEMENTS[9] and (any_earthly_branch in [ZODIAC[]]):
        NAME_star = True # yin earth, 
    elif day_heavenly_stem == ELEMENTS[0] and (any_earthly_branch in [ZODIAC[]]):
        NAME_star = True # yang metal, 
    elif day_heavenly_stem == ELEMENTS[1] and (any_earthly_branch in [ZODIAC[]]):
        NAME_star = True # yin metal,
    elif day_heavenly_stem == ELEMENTS[2] and (any_earthly_branch in [ZODIAC[]]):
        NAME_star = True # yang water,
    elif day_heavenly_stem == ELEMENTS[3] and (any_earthly_branch in [ZODIAC[]]):
        NAME_star = True # yin water,
    return NAME_star
'''

    
def check_all(year_heavenly_stem, year_earthly_branch, month_earthly_branch, day_heavenly_stem, day_earthly_branch, any_heavenly_stem, any_earthly_branch):
    stars = []
    hasStars = False
    if check_monthly_virtue_star(month_earthly_branch, any_heavenly_stem, any_earthly_branch):
        print('- Monthly Virtue Star')
        stars.append('Monthly Virtue Star')
        hasStars = True
    if check_heavenly_virtue_star(month_earthly_branch, any_heavenly_stem, any_earthly_branch):
        print('- Heavenly Virtue Star')
        stars.append('Heavenly Virtue Star')
        hasStars = True
    if check_heavenly_happiness_star(month_earthly_branch, any_earthly_branch):
        print('- Heavenly Happiness Star')
        stars.append('Heavenly Happiness Star')
        hasStars = True
    if check_heavenly_mitigation_star(month_earthly_branch, any_heavenly_stem, any_earthly_branch):
        print('- Heavenly Mitigation Star')
        stars.append('Heavenly Mitigation Star')
        hasStars = True
    if check_domination_pillar(any_heavenly_stem, any_earthly_branch):
        print('- Pillar of Domination')
        stars.append('Pillar of Domination')
        hasStars = True
    if check_yinyang_mismatch_pillar(any_heavenly_stem, any_earthly_branch):
        print('- Pillar of Yin and Yang Mismatch')
        stars.append('Pillar of Yin and Yang Mismatch')
        hasStars = True
    if check_redlight_pillar(any_heavenly_stem, any_earthly_branch):
        print('- Red-light Pillar')
        stars.append('Red-light Pillar')
        hasStars = True
    if check_canniness_pillar(any_heavenly_stem, any_earthly_branch):
        print('- Pillar of Canniness')
        stars.append('Pillar of Canniness')
        hasStars = True
    if check_clever_pillar(any_heavenly_stem, any_earthly_branch):
        print('- Pillar of Cleverness and Methodism')
        stars.append('Pillar of Cleverness and Methodism')
        hasStars = True
    if check_intelectual_pillar(any_heavenly_stem, any_earthly_branch):
        print('- Intelectual Pillar')
        stars.append('Intelectual Pillar')
        hasStars = True
    if check_nobleman_star(day_heavenly_stem, any_earthly_branch):
        print('- Nobleman Star')
        stars.append('Nobleman Star')
        hasStars = True
    if check_success_star(day_heavenly_stem, any_earthly_branch):
        print('- Success Star')
        stars.append('Success Star')
        hasStars = True
    if check_yang_heavenly_noble_star(day_heavenly_stem, any_earthly_branch):
        print('- Yang Heavenly Noble Star')
        stars.append('Yang Heavenly Noble Star')
        hasStars = True
    if check_yin_heavenly_noble_star(day_heavenly_stem, any_earthly_branch):
        print('- Yin Heavenly Noble Star')
        stars.append('Yin Heavenly Noble Star')
        hasStars = True
    if check_prosperity_star(day_heavenly_stem, any_earthly_branch):
        print('- Prosperity Star')
        stars.append('Prosperity Star')
        hasStars = True
    if check_sword_star(day_heavenly_stem, any_earthly_branch):
        print('- Sword Star')
        stars.append('Sword Star')
        hasStars = True
    if check_golden_carriage_star(day_heavenly_stem, any_earthly_branch):
        print('- Golden Carriage Star')
        stars.append('Golden Carriage Star')
        hasStars = True
    if check_red_peach_blossom_star(day_heavenly_stem, any_earthly_branch):
        print('- Red Peach Blossom Star or Erotic Star')
        stars.append('Red Peach Blossom Star or Erotic Star')
        hasStars = True
    if check_academic_star(day_heavenly_stem, any_earthly_branch):
        print('- Academic Star')
        stars.append('Academic Star')
        hasStars = True
    if check_literacy_star(day_heavenly_stem, any_earthly_branch):
        print('- Literacy Star of Learning Hall Star')
        stars.append('Literacy Star of Learning Hall Star')
        hasStars = True
    if check_taiji_star(day_heavenly_stem, any_earthly_branch):
        print('- Methaphysical Interest Star or Tai Ji Star')
        stars.append('Methaphysical Interest Star or Tai Ji Star')
        hasStars = True
    if check_liuhegui_star(day_heavenly_stem, any_heavenly_stem, any_earthly_branch):
        print('- Mentor of the Six Harmonies Star or Liu He Gui Star')
        stars.append('Mentor of the Six Harmonies Star or Liu He Gui Star')
        hasStars = True
    if check_guishi_star(day_heavenly_stem, any_heavenly_stem, any_earthly_branch):
        print('- Noble Righteous Output Star')
        stars.append('Noble Righteous Output Star')
        hasStars = True
    if check_guihe_star(day_heavenly_stem, any_heavenly_stem, any_earthly_branch):
        print('- Noble Harmony Star')
        stars.append('Noble Harmony Star')
        hasStars = True
    if check_general_star(day_heavenly_stem, any_earthly_branch):
        print('- General star of Gold Safe Star')
        stars.append('General star of Gold Safe Star')
        hasStars = True
    if check_travelling_horse_star(year_earthly_branch, day_heavenly_stem, any_earthly_branch):
        print('- Travelling Horse Star')
        stars.append('Travelling Horse Star')
        hasStars = True
    if check_peach_blossoms_star(year_earthly_branch, day_earthly_branch, any_earthly_branch):
        print('- Star of Romance or Peach Blossoms Star')
        stars.append('Star of Romance or Peach Blossoms Star')
        hasStars = True
    if check_robbing_star(day_earthly_branch, any_earthly_branch):
        print('- Robbing Star')
        stars.append('Robbing Star')
        hasStars = True
    if check_death_star(day_earthly_branch, any_earthly_branch):
        print('- Death Star')
        stars.append('Death Star')
        hasStars = True
    if check_solitary_star(day_earthly_branch, any_earthly_branch):
        print('- Solitary Star or Star of Seclusion')
        stars.append('Solitary Star or Star of Seclusion')
        hasStars = True
    if check_forlorn_star(day_earthly_branch, any_earthly_branch):
        print('- Forlorn Star or Abandoment Star')
        stars.append('Forlorn Star or Abandoment Star')
        hasStars = True
    if not hasStars:
        print('Don\'t have stars')
    return stars

def check_all_full_chart(year_heavenly_stem, year_earthly_branch, month_heavenly_stem, month_earthly_branch, day_heavenly_stem, day_earthly_branch, hour_heavenly_stem, hour_earthly_branch):
    # year pillar
    print(f'\nYear pillar ({year_heavenly_stem}{year_earthly_branch}):')
    year_pillar_stars = check_all(year_heavenly_stem, year_earthly_branch, month_earthly_branch, day_heavenly_stem, day_earthly_branch, year_heavenly_stem, year_earthly_branch)

    # month pillar
    print(f'\nMonth pillar ({month_heavenly_stem}{month_earthly_branch}):')
    month_pillar_stars = check_all(year_heavenly_stem, year_earthly_branch, month_earthly_branch, day_heavenly_stem, day_earthly_branch, month_heavenly_stem, month_earthly_branch)

    # day pillar
    print(f'\nDay pillar ({day_heavenly_stem}{day_earthly_branch}):')
    day_pillar_stars = check_all(year_heavenly_stem, year_earthly_branch, month_earthly_branch, day_heavenly_stem, day_earthly_branch, day_heavenly_stem, day_earthly_branch)

    # hour pillar
    print(f'\nHour pillar ({hour_heavenly_stem}{hour_earthly_branch}):')
    hour_pillar_stars = check_all(year_heavenly_stem, year_earthly_branch, month_earthly_branch, day_heavenly_stem, day_earthly_branch, hour_heavenly_stem, hour_earthly_branch)
    
    all_stars = {
        'year': year_pillar_stars,
        'month': month_pillar_stars,
        'day': day_pillar_stars,
        'hour': hour_pillar_stars
    }
    
    return all_stars
    

def check_all_no_hour_chart(year_heavenly_stem, year_earthly_branch, month_heavenly_stem, month_earthly_branch, day_heavenly_stem, day_earthly_branch):
    # year pillar
    print(f'\nYear pillar ({year_heavenly_stem}{year_earthly_branch}):')
    year_pillar_stars = check_all(year_heavenly_stem, year_earthly_branch, month_earthly_branch, day_heavenly_stem, day_earthly_branch, year_heavenly_stem, year_earthly_branch)

    # month pillar
    print(f'\nMonth pillar ({month_heavenly_stem}{month_earthly_branch}):')
    month_pillar_stars = check_all(year_heavenly_stem, year_earthly_branch, month_earthly_branch, day_heavenly_stem, day_earthly_branch, month_heavenly_stem, month_earthly_branch)

    # day pillar
    print(f'\nDay pillar ({day_heavenly_stem}{day_earthly_branch}):')
    day_pillar_stars = check_all(year_heavenly_stem, year_earthly_branch, month_earthly_branch, day_heavenly_stem, day_earthly_branch, day_heavenly_stem, day_earthly_branch)
    
    all_stars = {
        'year': year_pillar_stars,
        'month': month_pillar_stars,
        'day': day_pillar_stars
    }
    
    return all_stars



