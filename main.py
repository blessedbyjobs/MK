import numpy as np


def dummy(input_str):
    last_symbol = ''

    try:
        if input_str == "":
            raise ValueError
        else:
            for i in range(0, input_str.__len__(), 1):
                if last_symbol != '':
                    if input_str[i] == '1' and (last_symbol == '1' or last_symbol == '2'):
                        last_symbol = '1'
                    elif input_str[i] == '2' and (last_symbol == '1' or last_symbol == '2' or last_symbol == '3'):
                        last_symbol = '2'
                    elif input_str[i] == '3' and (last_symbol == '3' or last_symbol == '2'):
                        last_symbol = '3'
                    else:
                        raise ValueError
                elif i == 0 and input_str[i] != '1':
                    raise ValueError
                else:
                    last_symbol = input_str[i]

                if i == input_str.__len__() - 1 and last_symbol != '1':
                    raise ValueError

            print("Строка составлена правильно")

    except ValueError:
        print("Строка составлена неправильно")


if __name__ == '__main__':
    current_state = 0

    input_str = "11111222223333332221111"

    codes = np.array([[1, 99, 99, 99], [1, 2, 99, 99], [1, 2, 3, 99], [99, 2, 3, 99], [99, 99, 99, 99]])

    for i in range(0, input_str.__len__(), 1):
        if current_state != 99:
            if input_str[i] == '1' or input_str[i] == '2' or input_str[i] == '3':
                current_state = codes[current_state][int(input_str[i]) - 1]
            else:
                current_state = codes[current_state][3]

            if i == input_str.__len__() - 1 and current_state != 1:
                current_state = 99
        else:
            break

    print("Строка правильная" if current_state != 99 else "Строка не правильная")
