from pathlib import Path
from random import randint
import base64



letters_lowercase = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]

letters_uppercase = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z'
]



def rlen(input): return range(len(input))

def lsrlen(input): return list(range(len(input)))


def numls(): return list(range(0, 9))

def numlsstr(): return str(list(range(0, 9))).removeprefix('(').removesuffix(')').split(', ')


def choosefromlist(choosefrom: list, default: str = '', message: str = None, cursor: str = ''):
    choosefrom = list(choosefrom)
    if message == None: message = 'Please type a number or the option to select one'
    print(message)
    for i in rlen(choosefrom):
        c = choosefrom[i]
        print(str(i + 1) + ': ' + c)
    choosing = True
    while choosing:
        reply = input(cursor)
        if reply.isdigit():
            if int(reply) - 1 in lsrlen(choosefrom):
                return choosefrom[int(reply) - 1]
            else: print('not an option')
        else:
            try:
                chosen = choosefrom.index(reply)
                return chosen
            except ValueError: print('not an option')
    return default

def confirm(message: str, confirms: list[str] = ['y', 'yes'], cancels: list[str] = ['n', 'no'], cursor: str = ''):
    if len(confirms) < 1 or len(cancels) < 1: return False
    print(message + f'({confirms[0]}/{cancels[0]})')
    confirming = True
    while confirming:
        reply = input(cursor)
        if reply in confirms: return True
        elif reply in cancels: return False
    return False

def even(number: int): return not number % 2


def multiin(check: list, against: list | str):
    for c in check:
        if c in against: return True
    return False


def getfile(path: str, unsafe = False):
    if not Path(path).exists() and not unsafe: print(f'file "{path}" does not exist'); return ''
    with open(path, 'rt') as file: return file.read()

def setfile(path: str, content: str = '', unsafe = False):
    if not Path(path).exists() and not unsafe: print(f'file "{path}" does not exist'); return
    with open(path, 'wt') as file: return file.write(str(content))
    
def appfile(path: str, content: str = '', unsafe = False):
    if not Path(path).exists() and not unsafe: print(f'file "{path}" does not exist'); return
    with open(path, 'at') as file: return file.write(str(content) + '\n')


def removeitems(list: list, items: list | tuple):
    out = []
    for i in list:
        if i not in items: out.append(i)
    return out


def b64e(s):
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')

def b64d(s):
    return base64.b64decode(s).decode('utf-8')


def encapsulatedby(input: str, startandend: str | tuple[str]):
    return input.startswith(startandend) and input.endswith(startandend)

def sstrip(input: str, toremove: str): return input.removeprefix(toremove).removesuffix(toremove)


def randomchoice(list): return list[randint(0, len(list) - 1)]


def default(input, default):
    '''
    if the input is None, return given default, otherwise return the input
    '''
    if input == None:
        return default
    else:
        return input

def clamp(value: int | float, min: int | float, max: int | float):
    '''
    Clamps an int or float between the given minimum and maximum
    '''
    if value > max:
        return max
    elif value < min:
        return min
    else:
        return value


def numgen(length: int = 10):
    '''
    Generates number the length of the given int
    '''
    result = ''
    for _ in range(length):
        result += str(randint(0, 9))
    return result




class ncpath:
    def __init___(self, path: str):
        self.path = path.removeprefix('/') + '/'
    
    def add(self, path: str):
        self.path += path.removeprefix('/') + '/'
    
    def __str__(self):
        return self.path
