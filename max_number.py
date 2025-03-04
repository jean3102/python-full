score = [150, 140, 95, 600, 160, 115]


def max_number(numbers):
    """Return the maximum number from a list. Returns None if the list is empty."""
    max_num = numbers[0]
    for element in numbers[1:]:
        if element > max_num:
            max_num = element
    return max_num


VALUE = max_number(score)
print(f'''{VALUE=}''')
