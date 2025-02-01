def convertYearToIndexOfZodiac(year):
    while year < 2010:
        year += 12
    while year > 2021:
        year -= 12
    return year-2010

# yes, i choose 2020 because it was more easy to calculate in my head