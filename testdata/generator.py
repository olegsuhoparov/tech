import random


def random_num(min_value: int = 0, max_value: int = 999):
    return random.randint(min_value, max_value)


def generate_string(set_str: str, min_len=0, max_len=1):
    return ''.join([random.choice(set_str) for _ in range(random.randrange(min_len, max_len))])


def generate_letter(set_str: str):
    return random.choice(set_str)


def alphanum_str(min, max, ru=False):
    russian_symbols = "ЯЧСМИТЬБЮФЫВАПРОЛДЖЭЙЦУКЕНГШЩячсмитьбюфывапролджэйцукенгшщзхъ     <>{}[]?№!-_+1234567890=`~$%^@,./\\"
    english_symbols = "ZXCVBNMASDFGHJKLQWERTYUIOPpoiuytrewqlkjhgfdsazxcvbnm     <>{}[]?№!-_+1234567890=`~$%^@,./\\"
    if not ru:
        return generate_string(english_symbols, min, max)
    return generate_string(russian_symbols, min, max)
