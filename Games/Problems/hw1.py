#Ejercicio 1
#Factorial
def facto(n, a = 1):
    if (n == 0):
        return a
    return facto(n - 1, n * a)

#Ejercicio 2
#Fibonacci
def fibo(n):
    global caching
    if caching[n] == 0 and n > 0:
        caching[n] = fibo(n-1) + fibo(n-2)
    return caching[n]
    
caching = [0,1]
entrada = 8
for i in range(entrada):
    caching.append(0)
print(fibo(entrada))



#Ejercicio 3
