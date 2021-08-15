import random


dicc = {
    'letters' : 'abcdefghijklmnopqrstuvxyz',
    'numbers' : '1234567890',
    'special' : '#/$%*-+'
}


my_keys = dict()


def encritador(func):
    def wrapper(text):
        my_keys[text] = random.sample(dicc['letters']+dicc['numbers']+dicc['special']+dicc['letters'].upper(), k=20)
        for k,v in my_keys.items():
            print("{} --> {}".format(k, ''.join(v)))
        func(text)
    return wrapper


if __name__ == '__main__':
    entry = input('...\n\n')
    
    @encritador
    def word(text):
        print('Process finished!')
        
    word(entry)