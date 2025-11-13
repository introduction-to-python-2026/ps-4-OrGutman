def split_before_each_uppercases(formula):
    pass # Replace the `pass` with your code


def split_at_first_digit(formula):
    list = []
    letters = ""
    numbers = ""

    for i in formula:
        is_letter = i.isdigit()
        if not is_letter:
            letters += i
        else:
            numbers += i
    list.append(letters)

    if numbers != "":
        list.append(int(numbers))
    else:
        list.append(1)

    return list
