def split_before_each_uppercases(formula):
    pass # Replace the `pass` with your code


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
