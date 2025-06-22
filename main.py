def has_digit(password):
    return any(char.isdigit() for char in password)


def is_very_long(length_of_password):
    return length_of_password > 12


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return not all(char.isalpha() or char.isdigit() for char in password)


def main():
    print("Введите пароль:")
    password = input()
    length_of_password = len(password)

    test_digit = has_digit(password)
    test_length = is_very_long(length_of_password)
    test_upper_letters = has_upper_letters(password)
    test_lower_letters = has_lower_letters(password)
    test_symbols = has_symbols(password)

    test_list = [
        test_digit,
        test_length,
        test_upper_letters,
        test_lower_letters,
        test_symbols,
    ]

    score = 0

    for test in test_list:
        if test:
            score += 2

    print("Рейтинг пароля:", score)


if __name__ == "__main__":
    main()
