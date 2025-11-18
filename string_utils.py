def split_before_each_uppercases(formula):
    if formula == "":
        return []

    parts = []
    start = 0

    for i in range(1, len(formula)):
        if formula[i].isupper():  
            parts.append(formula[start:i])
            start = i

    parts.append(formula[start:])

    return parts



def split_at_first_digit(formula):
    prefix = ""
    index = 0
    while index < len(formula):
        char = formula[index]
        if char.isdigit():
            number = int(formula[index:])
            return prefix, number

        prefix += char
        index += 1

    return formula, 1

