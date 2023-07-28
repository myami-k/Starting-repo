

def get_float(prompt: str):
    try:
        return float(input(prompt))
    except ValueError:
        ""


def get_convert():
    while True:
        convert_u = input('\nCONVERT Kg or Lb or Oz\n> ')

        if convert_u == "Kg":
            if unit == "Lb":
                result = first_unit / 2.205
                print(round(result, 2))
            elif unit == "Oz":
                result = first_unit / 35.3
                print(round(result, 2))
        elif convert_u == "Lb":
            if unit == "Kg":
                result = first_unit * 2.205
                print(round(result, 2))
            elif unit == "Oz":
                result = first_unit / 16
                print(round(result, 2))
        elif convert_u == "Oz":
            if unit == "Kg":
                result = first_unit * 35.3
                print(round(result, 2))
            elif unit == "Lb":
                result = first_unit * 16
                print(round(result, 2))
        else:
            continue
        break


while True:
    unit = input('--------------\nKg or Lb or Oz\n> ')
    if unit == "Kg":
        first_unit = get_float('Kg: ')
    elif unit == "Lb":
        first_unit = get_float('Lb: ')
    elif unit == "Oz":
        first_unit = get_float('Oz: ')
    else:
        continue
    get_convert()
