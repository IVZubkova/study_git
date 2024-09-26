
def check_pattern():
    import re

    pattern = r'^[ -~А-Яа-яЁё№«»]*$'
    text = 'Клиент: Константин Иваноа (ID: 7569)\nE-mail: gsdfgsdfgsf@mail.ru\nТелефон: 9000001011'

    match = re.match(pattern, text)

    if match:
        print("Содержимое соответствует регулярному выражению.")
    else:
        for i in range(len(text)):
            if not re.match(pattern, text[:i + 1]):
                print(f"Несоответствие найдено на позиции {i}: '{text[i]}'")
                break

if __name__ == '__main__':
    check_pattern()