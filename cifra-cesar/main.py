import sys
sys.path.append(sys.path[0] + "/..")

from operator import mod
from functools import partial
from string import ascii_lowercase as alphabet
from argparse import ArgumentParser
from utils.validation import validate_type


def index(char: str, task: str='encrypt') -> int:
    alpha_len = len(alphabet)
    if task == 'encrypt':
        position = alphabet.index(char) + 3
    else:
        position = alphabet.index(char) - 3
    return alphabet[mod(position, alpha_len)]

pdecrypt = partial(index, task='decrypt')

@validate_type(str)
def encrypt(phrase: str) -> str:
    return ''.join(map(index, phrase))

@validate_type(str)
def decrypt(phrase: str) -> str:
    return ''.join(map(pdecrypt, phrase))

def get_args():
    parser = ArgumentParser()
    parser.add_argument('-e', '--encrypt')
    parser.add_argument('-d', '--decrypt')
    return vars(parser.parse_args())

def output():
    args = get_args()

    if args['encrypt']:
        return encrypt(args['encrypt'])
    return decrypt(args['decrypt'])

if __name__ == '__main__':
    print(output())
