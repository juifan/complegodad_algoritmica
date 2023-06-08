import time
import sys
import f_x
import suma
import multiplicacion

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *=n
        n -= 1

    return respuesta

def factorial_recursivo(n):

    if n == 1:
        return 1
    
    return n*factorial_recursivo(n-1)

def run():
    #f_x.f(5)
    #suma.f()
    multiplicacion.f(5)

if __name__ == '__main__':
   # n = 10000
    #sys.setrecursionlimit(100000000)
    #comienzo = time.time()
    #factorial(n)
    #final = time.time()
    #print(final - comienzo)

    #comienzo = time.time()
    #factorial_recursivo(n)
    #final = time.time()
    #print(final - comienzo)    
    run()
