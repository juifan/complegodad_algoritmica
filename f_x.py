
def f(x):
    respuesta = 0

    for i in range(1000):
        respuesta +=1

    for i in range(x):
        respuesta += x

    for i in range(x):
        print(i)
        for j in range(x):
            print(j)
            respuesta +=1
            respuesta +=1
    print(respuesta)
    return respuesta