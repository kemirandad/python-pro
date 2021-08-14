
def is_palindrome(text: str):
    try:
        if text.isalpha():
            return 'Es palindromo' if text == text[::-1] else 'No es palindromo'
        else:
            print('Oops! Hubo un error')
            raise TypeError('Tu entrada contiene uno o más números...')
    except TypeError as te:
        print(te)

def main():
    entry = input('Ingresa tu palabra...\n')
    print(is_palindrome(entry))

if __name__ == '__main__':
    main()