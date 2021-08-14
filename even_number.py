def is_even_number(n: int) -> bool:
    try:
        if not n.isdigit():
            raise ValueError('La cadena ingresada no es un número')
        else:
            n = int(n.strip())
            for i in range(2, n+1):
                if i != n and n%i == 0:
                    return False
            return True

    except ValueError as ve:
        print(ve)
        
def main():
    number = input('Ingresa un numero: ')
    print(is_even_number(number))
    
if __name__ == '__main__':
    main()