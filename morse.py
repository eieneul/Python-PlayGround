import pprint
import re


chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
codes = """.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-..
-- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..
.---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"""

dd = dict(zip(chars.lower(), codes.split()))
DD = dict(zip(codes.split(), chars.lower()))

# pprint.pprint(dd)


def chars2morse(char):
    return dd.get(char.lower(), ' ')


def morse2chars(morse):
    return DD.get(morse, ' ')


while True:
    str = input()
    x = str.split(' ')
    ccc = ''.join(x)
    if re.match('^[0-9a-zA-Z]+$', ccc):
        print(' '.join(chars2morse(c) for c in ccc))
    else:
        cc = str.split()
        print(' '.join(morse2chars(c) for c in cc))
