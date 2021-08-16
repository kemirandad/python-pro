class EvenNumbers:
    
    def __init__(self, max=None):
        self.__max = max
    
    def __iter__(self):
        self.__num = 0
        return self
    
    def __next__(self):
        if not self.__max or self.__num <= self.__max:
            result = self.__num
            self.__num += 2
            return result
        else:
            raise StopIteration
        
    
if __name__ == '__main__':
    even_number = EvenNumbers(5)
    even_number.__iter__()
    while True:
        try:         
            print(even_number.__next__())
        except StopIteration:
            break
            