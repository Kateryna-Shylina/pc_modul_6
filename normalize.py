import re

UKRAINIAN = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "je", "zh", "z", "y", "i", "ji", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "ju", "ja")

TRANS_DICT = {}

for key, value in zip(UKRAINIAN, TRANSLATION):
    TRANS_DICT[ord(key)] = value
    TRANS_DICT[ord(key.upper())] = value.upper()

def normalize(name: str) -> str:
    name, *extension = name.split('.')
    new_name = name.translate(TRANS_DICT)
    new_name = re.sub(r'\W', '_', new_name)
    return f"{new_name}.{'.'.join(extension)}"





#if __name__ == '__main__':
#    print(normalize('прВАН)пр?.tar.gz'))