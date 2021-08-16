import time
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

class FiboIter():

    def __init__(self, max = None):
        logger.info('Creaste el objeto Fibonacci con un número máximo de {}'.format(max))
        self.__max = max


    def __iter__(self):
        logger.info('Definiste que el objeto es un iterador')
        self.__n1 = 0
        self.__n2 = 1
        self.__counter = 0
        return self


    def __next__(self):
        logger.info('Imprimes la secuencia de Fibonacci')
        try:
            if self.__max == None or self.__max < 0:
                raise ValueError('ValueError ::::::::: Debes ingresar un número natural...')

            elif self.__max >= self.__n1 + self.__n2:
                if self.__counter == 0:
                    self.__counter += 1
                    return self.__n1
                elif self.__counter == 1:
                    self.__counter += 1
                    return self.__n2
                else:
                    self.__aux = self.__n1 + self.__n2
                    self.__n1, self.__n2 = self.__n2, self.__aux
                    self.__counter += 1
                    return self.__aux
            
            else:
                raise StopIteration('StopIteration ::::::::: Se detuvo tu iteracíon...')

        except ValueError as e:
            print(e)
            return None
        except StopIteration as e:
            print(e)
            return None


if __name__ == '__main__':
    fibonacci = FiboIter(0)
    fibonacci.__iter__()
    while True:
        result = fibonacci.__next__()
        if result != None:
            print(result)
            time.sleep(0.5)
        else:
            break
