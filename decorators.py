from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron {} segundos".format(time_elapsed.total_seconds()))
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 100000000):
        ...
        
random_func()

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

suma(5, 5)


@execution_time
def saludo(nombre='Cesar'):
    print("Hola " + nombre)
    
saludo("Kenny")



