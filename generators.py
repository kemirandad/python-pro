import time
from typing import Counter

def fibo_gen(max = None):
    try:
        if max == None:
            raise ValueError('ValueError ::: Oops! parece que no has ingresado un número')
        elif max >= 0:
            n1 = 0
            n2 = 1
            counter = 0
            while True and max >= n1 + n2:
                if counter == 0:
                    counter += 1
                    yield n1
                elif counter == 1:
                    counter += 1
                    yield n2
                else:
                    counter += 1
                    aux = n1 + n2
                    n1, n2 = n2, aux
                    yield aux
        else:
            raise StopIteration('StopIteration ::: Tu iteración ha terminado... ')
    except ValueError as ve:
        yield ve

    except StopIteration as si:
        yield si

    

if __name__ == '__main__':
    fibonacci = fibo_gen(10)
    if fibonacci != None:
        for element in fibonacci:
            print(element)
            time.sleep(1)