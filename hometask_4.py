import re

from plates_No import plates_list

user_input = input("Please type your desired plate number: ").upper()


def plates(value):
    if len(value) != 8:
        print("You have to type 8 symbols!")
        return False
    else:
        if value in plates_list:
            value = value[:2], value[2], value[3], value[4], value[5], value[6:]
            print("Current plate number is in plates list:")
            return value
        else:
            print("Current plate number is not in plates list:")
            value = value[:2], value[2], value[3], value[4], value[5], value[6:]
            return value


print(plates(user_input))

input("Please press any bottom to continue:")


def summary(calc):
    if bool(re.fullmatch(r'^\w{2}\d{4}\w{2}$', user_input)):
        calc = sum(list(map(int, calc[2:6])))
        print(f"The summary of numbers entered is:")
        return calc
    else:
        return "Oops. You have typed the wrong format. Please follow the example: BH1605HD "


print(summary(user_input))
