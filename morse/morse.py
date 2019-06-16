from os import system
from string import ascii_lowercase, whitespace


alpha = list(ascii_lowercase + whitespace)
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
         '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
         '..-', '...-', '.--', '-..-', '-.--', '--..', '/']
morse_alphabet = {key:value for key, value in zip(alpha, morse)}
morse_dict = {key:value for key, value in zip(morse, alpha)}


def clear_screen(message=''):
    system('clear')
    print('=' * 80)
    print('''
    Escolha o que quer fazer:
    1 - Codificar texto para morse.
    2 - Decodificar texto em morse.
    (você pode sair a qualquer momento digitando "sair")
    ''')
    print('=' * 80)
    print(message)


def encrypt(phrase: str) -> str:
    new_phrase = ''.join([morse_alphabet[char] + ' ' for char in phrase])
    return new_phrase


def decrypt(phrase: str) -> str:
    new_phrase = ''.join([morse_dict[char] + ' ' for char in phrase])
    return new_phrase


def main():
    word = ''
    clear_screen()
    while True:
        choice = input('>>> ')
        print('=' * 80)

        if 'sair' in choice.lower():
            break
        elif choice == '1':
            clear_screen('Digite o texto a ser codificado: ')
            word = input('>>> ')
            print(encrypt(word))
        elif choice == '2':
            clear_screen('Digite o texto a ser decodificado: ')
            word = input('>>> ')
            print(decrypt(word))
        else:
            continue


if __name__ == '__main__':
    main()
