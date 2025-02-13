def calc_element_percentage_fullchart(year_element, year_zodiac, month_element, month_zodiac, day_element, day_zodiac, hour_element, hour_zodiac):
    # elemental score
    wood = 0
    fire = 0
    earth = 0
    metal = 0
    water = 0
    
    '''
    Valores dos Troncos Celestes:
    甲 - Madeira Yang = 50 pontos de madeira
    乙 - Madeira Yin = 50 pontos de madeira
    丙 - Fogo Yang = 50 pontos de fogo
    丁 - Fogo Yin = 50 pontos de fogo
    戊 - Terra Yang = 50 pontos de terra
    己 - Terra Yin = 50 pontos de terra
    庚 - Metal Yang = 50 pontos de metal
    辛 - Metal Yin = 50 pontos de metal
    壬 - Água Yang = 50 pontos de água
    癸 - Água Yin = 50 pontos de água
    '''
    # Year Heavenly Stem
    option = year_element
    if option == '甲':
        wood += 50
    elif option == '乙':
        wood += 50
    elif option == '丙':
        fire += 50
    elif option == '丁':
        fire += 50
    elif option == '戊':
        earth += 50
    elif option == '己':
        earth += 50
    elif option == '庚':
        metal += 50
    elif option == '辛':
        metal += 50
    elif option == '壬':
        water += 50
    elif option == '癸':
        water += 50
        
    # Month Heavenly Stem
    option = month_element
    if option == '甲':
        wood += 50
    elif option == '乙':
        wood += 50
    elif option == '丙':
        fire += 50
    elif option == '丁':
        fire += 50
    elif option == '戊':
        earth += 50
    elif option == '己':
        earth += 50
    elif option == '庚':
        metal += 50
    elif option == '辛':
        metal += 50
    elif option == '壬':
        water += 50
    elif option == '癸':
        water += 50
        
    # Day Heavenly Stem
    option = day_element
    if option == '甲':
        wood += 50
    elif option == '乙':
        wood += 50
    elif option == '丙':
        fire += 50
    elif option == '丁':
        fire += 50
    elif option == '戊':
        earth += 50
    elif option == '己':
        earth += 50
    elif option == '庚':
        metal += 50
    elif option == '辛':
        metal += 50
    elif option == '壬':
        water += 50
    elif option == '癸':
        water += 50
        
    # Hour Heavenly Stem
    option = hour_element
    if option == '甲':
        wood += 50
    elif option == '乙':
        wood += 50
    elif option == '丙':
        fire += 50
    elif option == '丁':
        fire += 50
    elif option == '戊':
        earth += 50
    elif option == '己':
        earth += 50
    elif option == '庚':
        metal += 50
    elif option == '辛':
        metal += 50
    elif option == '壬':
        water += 50
    elif option == '癸':
        water += 50
        
    '''
    Valores dos Ramos Terrestres (Animais do Zodíaco):
    子 - Rato = 50 pontos de água
    丑 - Boi = 30 pontos de terra, 12 pontos de metal, 8 pontos de água
    寅 - Tigre = 30 pontos de madeira, 15 pontos de fogo, 5 pontos de terra
    卯 - Coelho = 50 pontos de madeira
    辰 - Dragão = 30 pontos de terra, 12 de água, 8 de madeira
    巳 - Serpente = 30 pontos de fogo, 15 de metal, 5 de terra
    午 - Cavalo = 30 pontos de fogo, 20 pontos de madeira
    未 - Cabra = 30 pontos de terra, 12 pontos de fogo, 8 pontos de madeira
    申 - Macaco = 30 pontos de metal, 15 pontos de água, 5 pontos de terra
    酉 - Galo = 50 pontos de metal
    戌 - Cachorro = 30 pontos de terra, 8 pontos de fogo, 12 pontos de metal
    亥 - Porco = 30 pontos de água, 20 pontos de madeira
    '''
    # Year Earthly Branch
    option = year_zodiac
    if option == '子':
        water += 50
    elif option == '丑':
        earth += 30
        metal += 12
        water += 8
    elif option == '寅':
        wood += 30
        fire += 15
        earth += 5
    elif option == '卯':
        wood += 50
    elif option == '辰':
        earth += 30
        water += 12
        wood += 8
    elif option == '巳':
        fire += 30
        metal += 15
        earth += 5
    elif option == '午':
        fire += 30
        wood += 20
    elif option == '未':
        earth += 30
        fire += 12
        wood += 8
    elif option == '申':
        metal += 30
        water += 15
        earth += 5
    elif option == '酉':
        metal += 50
    elif option == '戌':
        earth += 30
        fire += 8
        metal += 12
    elif option == '亥':
        water += 30
        wood += 20
        
    # Month Earthly Branch
    option = month_zodiac
    if option == '子':
        water += 50
    elif option == '丑':
        earth += 30
        metal += 12
        water += 8
    elif option == '寅':
        wood += 30
        fire += 15
        earth += 5
    elif option == '卯':
        wood += 50
    elif option == '辰':
        earth += 30
        water += 12
        wood += 8
    elif option == '巳':
        fire += 30
        metal += 15
        earth += 5
    elif option == '午':
        fire += 30
        wood += 20
    elif option == '未':
        earth += 30
        fire += 12
        wood += 8
    elif option == '申':
        metal += 30
        water += 15
        earth += 5
    elif option == '酉':
        metal += 50
    elif option == '戌':
        earth += 30
        fire += 8
        metal += 12
    elif option == '亥':
        water += 30
        wood += 20
        
    # Day Earthly Branch
    option = day_zodiac
    if option == '子':
        water += 50
    elif option == '丑':
        earth += 30
        metal += 12
        water += 8
    elif option == '寅':
        wood += 30
        fire += 15
        earth += 5
    elif option == '卯':
        wood += 50
    elif option == '辰':
        earth += 30
        water += 12
        wood += 8
    elif option == '巳':
        fire += 30
        metal += 15
        earth += 5
    elif option == '午':
        fire += 30
        wood += 20
    elif option == '未':
        earth += 30
        fire += 12
        wood += 8
    elif option == '申':
        metal += 30
        water += 15
        earth += 5
    elif option == '酉':
        metal += 50
    elif option == '戌':
        earth += 30
        fire += 8
        metal += 12
    elif option == '亥':
        water += 30
        wood += 20
        
    # Hour Earthly Branch
    option = hour_zodiac
    if option == '子':
        water += 50
    elif option == '丑':
        earth += 30
        metal += 12
        water += 8
    elif option == '寅':
        wood += 30
        fire += 15
        earth += 5
    elif option == '卯':
        wood += 50
    elif option == '辰':
        earth += 30
        water += 12
        wood += 8
    elif option == '巳':
        fire += 30
        metal += 15
        earth += 5
    elif option == '午':
        fire += 30
        wood += 20
    elif option == '未':
        earth += 30
        fire += 12
        wood += 8
    elif option == '申':
        metal += 30
        water += 15
        earth += 5
    elif option == '酉':
        metal += 50
    elif option == '戌':
        earth += 30
        fire += 8
        metal += 12
    elif option == '亥':
        water += 30
        wood += 20
    
    # Calculate triad bonuses
    earhtly_branches_in_chart = [year_zodiac, month_zodiac, day_zodiac, hour_zodiac]
    # how many times each animal appears in chart
    rat = 0
    ox = 0
    tiger = 0
    rabbit = 0
    dragon = 0
    snake = 0
    horse = 0
    goat = 0
    monkey = 0
    rooster = 0
    dog = 0
    pig = 0
    for animal in earhtly_branches_in_chart:
        if animal == '子':
            rat += 1
        elif animal == '丑':
            ox += 1
        elif animal == '寅':
            tiger += 1
        elif animal == '卯':
            rabbit += 1
        elif animal == '辰':
            dragon += 1
        elif animal == '巳':
            snake += 1
        elif animal == '午':
            horse += 1
        elif animal == '未':
            goat += 1
        elif animal == '申':
            monkey += 1
        elif animal == '酉':
            rooster += 1
        elif animal == '戌':
            dog += 1
        elif animal == '亥':
            pig += 1
    
    # fire triad bonuses
    if tiger >= 1 and horse >= 1 and dog >= 1:
        fire += 100
    if tiger >= 2 and horse == 0 and dog == 0:
        fire += 50
    if tiger >= 1 and horse == 0 and dog >= 1:
        fire += 50
    if tiger >= 1 and horse >= 1 and dog == 0:
        fire += 50
    if tiger == 0 and horse >= 2 and dog == 0:
        fire += 50
    if tiger == 0 and horse >= 1 and dog >= 1:
        fire += 50
    
    # metal triad bonuses
    if ox >= 1 and snake >= 1 and rooster >= 1:
        metal += 100
    if ox == 0 and snake >= 2 and rooster == 0:
        metal += 50
    if ox >= 1 and snake >= 1 and rooster == 0:
        metal += 50
    if ox == 0 and snake >= 1 and rooster >= 1:
        metal += 50
    if ox == 0 and snake == 0 and rooster >= 2:
        metal += 50
    if ox >= 1 and snake == 0 and rooster >= 1:
        metal += 50
    
    # water triad bonuses
    if rat >= 1 and dragon >= 1 and monkey >= 1:
        water += 100
    if rat >= 2 and dragon == 0 and monkey == 0:
        water += 50
    if rat >= 1 and dragon >= 1 and monkey == 0:
        water += 50
    if rat >= 1 and dragon == 0 and monkey >= 1:
        water += 50
    if rat == 0 and dragon == 0 and monkey >= 2:
        water += 50
    if rat == 0 and dragon >= 1 and monkey >= 1:
        water += 50
    
    # wood triad bonuses
    if rabbit >= 1 and goat >= 1 and pig >= 1:
        wood += 100
    if rabbit >= 2 and goat == 0 and pig == 0:
        wood += 50
    if rabbit >= 1 and goat >= 1 and pig == 0:
        wood += 50
    if rabbit >= 1 and goat == 0 and pig >= 1:
        wood += 50
    if rabbit == 0 and goat == 0 and pig >= 2:
        wood += 50
    if rabbit == 0 and goat >= 1 and pig >= 1:
        wood += 50
    
    # Calculate bonus from month earthly branch
    '''
    # Bônus de zodíaco do mês
    子 - Rato: Multiplique o valor final da água por 2x
    丑 - Boi: Multiplique o valor final da terra por 2x, o metal por 1,5x, e a água por 1,5x
    寅 - Tigre: Multiplique o fogo por 1,5x, a madeira por 2x, e a terra por 1,5x
    卯 - Coelho: Multiplique a madeira por 2x
    辰 - Dragão: Multiplique a terra por 2x, a madeira por 1,5x, e a água por 1,5x
    巳 - Serpente: Multiplique o fogo por 2x, o metal por 1,5x, e a terra por 1,5x
    午 - Cavalo: Multiplique o fogo por 2x e a terra por 1,5x
    未 - Cabra: Multiplique a terra por 2x, a madeira por 1,5x, e o fogo por 1,5x
    申 - Macaco: Multiplique o metal por 2x, a água por 1,5x, e a terra por 1,5x
    酉 - Galo: Multiplique o metal por 2x
    戌 - Cachorro: Multiplique a terra por 2x, o fogo por 1,5x, e o metal por 1,5x
    亥 - Porco: Multiplique a água por 2x e a madeira por 1,5x
    '''
    if month_zodiac == '子': # Rat
        water *= 2
    elif month_zodiac == '丑': # Ox
        earth *= 2
        metal *= 1.5
        water *= 1.5
    elif month_zodiac == '寅': # Tiger
        fire *= 1.5
        wood *= 2
        earth *= 1.5
    elif month_zodiac == '卯': # Rabbit
        wood *= 2
    elif month_zodiac == '辰': # Dragon
        earth *= 2
        wood *= 1.5
        water *= 1.5
    elif month_zodiac == '巳': # Snake
        fire *= 2
        metal *= 1.5
        earth *= 1.5
    elif month_zodiac == '午': # Horse
        fire *= 2
        earth *= 1.5
    elif month_zodiac == '未': # Goat
        earth *= 2
        wood *= 1.5
        fire *= 1.5
    elif month_zodiac == '申': # Monkey
        metal *= 2
        water *= 1.5
        earth *= 1.5
    elif month_zodiac == '酉': # Rooster
        metal *= 2
    elif month_zodiac == '戌': # Dog
        earth *= 2
        fire *= 1.5
        metal *= 1.5
    elif month_zodiac == '亥': # Pig
        water *= 2
        wood *= 1.5
    
    total = wood + fire + earth + metal + water
    
    return {'wood': (wood/total)*100, 'fire': (fire/total)*100, 'earth': (earth/total)*100, 'metal': (metal/total)*100, 'water': (water/total)*100}

def calc_element_percentage_unknown_hour(year_element, year_zodiac, month_element, month_zodiac, day_element, day_zodiac):
    # elemental score
    wood = 0
    fire = 0
    earth = 0
    metal = 0
    water = 0
    
    '''
    Valores dos Troncos Celestes:
    甲 - Madeira Yang = 50 pontos de madeira
    乙 - Madeira Yin = 50 pontos de madeira
    丙 - Fogo Yang = 50 pontos de fogo
    丁 - Fogo Yin = 50 pontos de fogo
    戊 - Terra Yang = 50 pontos de terra
    己 - Terra Yin = 50 pontos de terra
    庚 - Metal Yang = 50 pontos de metal
    辛 - Metal Yin = 50 pontos de metal
    壬 - Água Yang = 50 pontos de água
    癸 - Água Yin = 50 pontos de água
    '''
    # Year Heavenly Stem
    option = year_element
    if option == '甲':
        wood += 50
    elif option == '乙':
        wood += 50
    elif option == '丙':
        fire += 50
    elif option == '丁':
        fire += 50
    elif option == '戊':
        earth += 50
    elif option == '己':
        earth += 50
    elif option == '庚':
        metal += 50
    elif option == '辛':
        metal += 50
    elif option == '壬':
        water += 50
    elif option == '癸':
        water += 50
        
    # Month Heavenly Stem
    option = month_element
    if option == '甲':
        wood += 50
    elif option == '乙':
        wood += 50
    elif option == '丙':
        fire += 50
    elif option == '丁':
        fire += 50
    elif option == '戊':
        earth += 50
    elif option == '己':
        earth += 50
    elif option == '庚':
        metal += 50
    elif option == '辛':
        metal += 50
    elif option == '壬':
        water += 50
    elif option == '癸':
        water += 50
        
    # Day Heavenly Stem
    option = day_element
    if option == '甲':
        wood += 50
    elif option == '乙':
        wood += 50
    elif option == '丙':
        fire += 50
    elif option == '丁':
        fire += 50
    elif option == '戊':
        earth += 50
    elif option == '己':
        earth += 50
    elif option == '庚':
        metal += 50
    elif option == '辛':
        metal += 50
    elif option == '壬':
        water += 50
    elif option == '癸':
        water += 50
        
    '''
    Valores dos Ramos Terrestres (Animais do Zodíaco):
    子 - Rato = 50 pontos de água
    丑 - Boi = 30 pontos de terra, 12 pontos de metal, 8 pontos de água
    寅 - Tigre = 30 pontos de madeira, 15 pontos de fogo, 5 pontos de terra
    卯 - Coelho = 50 pontos de madeira
    辰 - Dragão = 30 pontos de terra, 12 de água, 8 de madeira
    巳 - Serpente = 30 pontos de fogo, 15 de metal, 5 de terra
    午 - Cavalo = 30 pontos de fogo, 20 pontos de madeira
    未 - Cabra = 30 pontos de terra, 12 pontos de fogo, 8 pontos de madeira
    申 - Macaco = 30 pontos de metal, 15 pontos de água, 5 pontos de terra
    酉 - Galo = 50 pontos de metal
    戌 - Cachorro = 30 pontos de terra, 8 pontos de fogo, 12 pontos de metal
    亥 - Porco = 30 pontos de água, 20 pontos de madeira
    '''
    # Year Earthly Branch
    option = year_zodiac
    if option == '子':
        water += 50
    elif option == '丑':
        earth += 30
        metal += 12
        water += 8
    elif option == '寅':
        wood += 30
        fire += 15
        earth += 5
    elif option == '卯':
        wood += 50
    elif option == '辰':
        earth += 30
        water += 12
        wood += 8
    elif option == '巳':
        fire += 30
        metal += 15
        earth += 5
    elif option == '午':
        fire += 30
        wood += 20
    elif option == '未':
        earth += 30
        fire += 12
        wood += 8
    elif option == '申':
        metal += 30
        water += 15
        earth += 5
    elif option == '酉':
        metal += 50
    elif option == '戌':
        earth += 30
        fire += 8
        metal += 12
    elif option == '亥':
        water += 30
        wood += 20
        
    # Month Earthly Branch
    option = month_zodiac
    if option == '子':
        water += 50
    elif option == '丑':
        earth += 30
        metal += 12
        water += 8
    elif option == '寅':
        wood += 30
        fire += 15
        earth += 5
    elif option == '卯':
        wood += 50
    elif option == '辰':
        earth += 30
        water += 12
        wood += 8
    elif option == '巳':
        fire += 30
        metal += 15
        earth += 5
    elif option == '午':
        fire += 30
        wood += 20
    elif option == '未':
        earth += 30
        fire += 12
        wood += 8
    elif option == '申':
        metal += 30
        water += 15
        earth += 5
    elif option == '酉':
        metal += 50
    elif option == '戌':
        earth += 30
        fire += 8
        metal += 12
    elif option == '亥':
        water += 30
        wood += 20
        
    # Day Earthly Branch
    option = day_zodiac
    if option == '子':
        water += 50
    elif option == '丑':
        earth += 30
        metal += 12
        water += 8
    elif option == '寅':
        wood += 30
        fire += 15
        earth += 5
    elif option == '卯':
        wood += 50
    elif option == '辰':
        earth += 30
        water += 12
        wood += 8
    elif option == '巳':
        fire += 30
        metal += 15
        earth += 5
    elif option == '午':
        fire += 30
        wood += 20
    elif option == '未':
        earth += 30
        fire += 12
        wood += 8
    elif option == '申':
        metal += 30
        water += 15
        earth += 5
    elif option == '酉':
        metal += 50
    elif option == '戌':
        earth += 30
        fire += 8
        metal += 12
    elif option == '亥':
        water += 30
        wood += 20
    
    # Calculate triad bonuses
    earhtly_branches_in_chart = [year_zodiac, month_zodiac, day_zodiac]
    # how many times each animal appears in chart
    rat = 0
    ox = 0
    tiger = 0
    rabbit = 0
    dragon = 0
    snake = 0
    horse = 0
    goat = 0
    monkey = 0
    rooster = 0
    dog = 0
    pig = 0
    for animal in earhtly_branches_in_chart:
        if animal == '子':
            rat += 1
        elif animal == '丑':
            ox += 1
        elif animal == '寅':
            tiger += 1
        elif animal == '卯':
            rabbit += 1
        elif animal == '辰':
            dragon += 1
        elif animal == '巳':
            snake += 1
        elif animal == '午':
            horse += 1
        elif animal == '未':
            goat += 1
        elif animal == '申':
            monkey += 1
        elif animal == '酉':
            rooster += 1
        elif animal == '戌':
            dog += 1
        elif animal == '亥':
            pig += 1
    
    # fire triad bonuses
    if tiger >= 1 and horse >= 1 and dog >= 1:
        fire += 100
    if tiger >= 2 and horse == 0 and dog == 0:
        fire += 50
    if tiger >= 1 and horse == 0 and dog >= 1:
        fire += 50
    if tiger >= 1 and horse >= 1 and dog == 0:
        fire += 50
    if tiger == 0 and horse >= 2 and dog == 0:
        fire += 50
    if tiger == 0 and horse >= 1 and dog >= 1:
        fire += 50
    
    # metal triad bonuses
    if ox >= 1 and snake >= 1 and rooster >= 1:
        metal += 100
    if ox == 0 and snake >= 2 and rooster == 0:
        metal += 50
    if ox >= 1 and snake >= 1 and rooster == 0:
        metal += 50
    if ox == 0 and snake >= 1 and rooster >= 1:
        metal += 50
    if ox == 0 and snake == 0 and rooster >= 2:
        metal += 50
    if ox >= 1 and snake == 0 and rooster >= 1:
        metal += 50
    
    # water triad bonuses
    if rat >= 1 and dragon >= 1 and monkey >= 1:
        water += 100
    if rat >= 2 and dragon == 0 and monkey == 0:
        water += 50
    if rat >= 1 and dragon >= 1 and monkey == 0:
        water += 50
    if rat >= 1 and dragon == 0 and monkey >= 1:
        water += 50
    if rat == 0 and dragon == 0 and monkey >= 2:
        water += 50
    if rat == 0 and dragon >= 1 and monkey >= 1:
        water += 50
    
    # wood triad bonuses
    if rabbit >= 1 and goat >= 1 and pig >= 1:
        wood += 100
    if rabbit >= 2 and goat == 0 and pig == 0:
        wood += 50
    if rabbit >= 1 and goat >= 1 and pig == 0:
        wood += 50
    if rabbit >= 1 and goat == 0 and pig >= 1:
        wood += 50
    if rabbit == 0 and goat == 0 and pig >= 2:
        wood += 50
    if rabbit == 0 and goat >= 1 and pig >= 1:
        wood += 50
    
    # Calculate bonus from month earthly branch
    '''
    # Bônus de zodíaco do mês
    子 - Rato: Multiplique o valor final da água por 2x
    丑 - Boi: Multiplique o valor final da terra por 2x, o metal por 1,5x, e a água por 1,5x
    寅 - Tigre: Multiplique o fogo por 1,5x, a madeira por 2x, e a terra por 1,5x
    卯 - Coelho: Multiplique a madeira por 2x
    辰 - Dragão: Multiplique a terra por 2x, a madeira por 1,5x, e a água por 1,5x
    巳 - Serpente: Multiplique o fogo por 2x, o metal por 1,5x, e a terra por 1,5x
    午 - Cavalo: Multiplique o fogo por 2x e a terra por 1,5x
    未 - Cabra: Multiplique a terra por 2x, a madeira por 1,5x, e o fogo por 1,5x
    申 - Macaco: Multiplique o metal por 2x, a água por 1,5x, e a terra por 1,5x
    酉 - Galo: Multiplique o metal por 2x
    戌 - Cachorro: Multiplique a terra por 2x, o fogo por 1,5x, e o metal por 1,5x
    亥 - Porco: Multiplique a água por 2x e a madeira por 1,5x
    '''
    if month_zodiac == '子': # Rat
        water *= 2
    elif month_zodiac == '丑': # Ox
        earth *= 2
        metal *= 1.5
        water *= 1.5
    elif month_zodiac == '寅': # Tiger
        fire *= 1.5
        wood *= 2
        earth *= 1.5
    elif month_zodiac == '卯': # Rabbit
        wood *= 2
    elif month_zodiac == '辰': # Dragon
        earth *= 2
        wood *= 1.5
        water *= 1.5
    elif month_zodiac == '巳': # Snake
        fire *= 2
        metal *= 1.5
        earth *= 1.5
    elif month_zodiac == '午': # Horse
        fire *= 2
        earth *= 1.5
    elif month_zodiac == '未': # Goat
        earth *= 2
        wood *= 1.5
        fire *= 1.5
    elif month_zodiac == '申': # Monkey
        metal *= 2
        water *= 1.5
        earth *= 1.5
    elif month_zodiac == '酉': # Rooster
        metal *= 2
    elif month_zodiac == '戌': # Dog
        earth *= 2
        fire *= 1.5
        metal *= 1.5
    elif month_zodiac == '亥': # Pig
        water *= 2
        wood *= 1.5
    
    total = wood + fire + earth + metal + water
    
    return {'wood': (wood/total)*100, 'fire': (fire/total)*100, 'earth': (earth/total)*100, 'metal': (metal/total)*100, 'water': (water/total)*100}

def get_element_status(element_percentage):
    if element_percentage <= 15:
        return 'deficient'
    elif element_percentage >= 40:
        return 'excessive'
    else: 
        return 'normal'
