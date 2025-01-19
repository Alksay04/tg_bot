def read_aggressive_lines():
    f = open('pon.txt', encoding='utf=8')
    lines = f.readlines()
    f.close()
    return lines

def get_random_aggressive_line():
    from random import choice
    lines = read_aggressive_lines()
    line = choice(lines)
    line = line.strip('\n')
    return line
def generate_random_ip():
    from random import randint
    return f"{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}"