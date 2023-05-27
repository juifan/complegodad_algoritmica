#Ley de suma

def f(n):
    for i in range(n):
        print(1)

    for i in range(n):
        print(i)


# O(n) + O(n) = O(n + n) = O(2n) = O(n)

    for i in range(n):
        print(1)

    for i in range(n * n):
        print(i)

# O(n) + O(n * n) = O(n + n²) = O(n²)