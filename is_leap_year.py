def is_leap_year(year: int) -> bool:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False


year_1 = is_leap_year(2400)
year_2 = is_leap_year(1700)

print(year_1)
print(year_2)
