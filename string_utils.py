def split_before_each_uppercases(formula):
    index = 0
    mylist = []
    upper_index = 0

    while index < len(formula):
        char = formula[index]
        if char.isupper():
            if index != 0:
                mylist.append(formula[upper_index:index])
            upper_index = index
            
        index += 1
        
    mylist.append(formula[upper_index:index])

    return mylist


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

