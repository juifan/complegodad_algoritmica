import random

def busqueda_binaria(lista,comienzo,final,objetivo,count=0):
    print(f'buscando{objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    count +=1
    if comienzo > final:
        return False,count
    
    medio = (comienzo+final ) // 2

    if lista[medio] == objetivo:
        return True,count
    elif lista[medio] < objetivo:
        return busqueda_binaria (lista, medio + 1, final, objetivo,count=count)
    else:
        return busqueda_binaria(lista,comienzo,medio-1,objetivo,count=count)

    

if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño sera la lista?'))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0,100) for i in range(tamano_lista)])

    encontrado,count = busqueda_binaria(lista,0, len(lista),objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Iteraciones {count}')


