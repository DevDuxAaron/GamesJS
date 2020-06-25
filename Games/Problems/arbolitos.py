# def insertion(arr):
#     n = len(arr)
#     for i in range(1,n):
#         currentVal = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > currentVal:
#             arr[j+1] = arr[j]
#             j = j - 1
#         arr[j+1] = currentVal
# arr = [6,4,3,11,10]
# insertion(arr)
# print(arr)


#Suma de subconjuntos
# def procesarSolucion(conjunto):
#     global s,r
#     if s != m:
#         return
#     r += 1
# def esSolucion(conjunto,pos):
#     return len(conjunto) == pos
# def imprime(conjunto,pos):
#     global s,r
#     if esSolucion(conjunto,pos):
#         procesarSolucion(conjunto)
#     else:
#         s += a[pos]
#         conjunto[pos] = True
#         if s <= m:
#             imprime(conjunto,pos+1)
#         conjunto[pos] = False
#         s -= a[pos]
#         imprime(conjunto,pos+1)
# while True:
#     try:
#         m,aux = map(int,list(input().split(" ")))
#         a = list(map(int,list(input().split(" "))))
#         a.sort()
#         s = 0
#         r = 0
#         conjuntos = [False]*(len(a))
#         imprime(conjuntos,0)
#         print(r)
#     except EOFError:
#         break

#Operaciones con conjuntos
# def completar(n1,n2):
#     if len(n1) == len(n2):
#         return n1,n2
#     me = min(n1,n2)
#     dif = abs(len(n1)-len(n2))
#     res = me[:2] + ("0"*dif) + me[2:]
#     if me == n1:
#         return res,n2 
#     return n1,res
# def union(n1,n2):
#     res = ["0","b"]
#     for i in range(2,len(n1)):
#         if n1[i] == "1" or n2[i] == "1":
#             res.append("1")
#         else:
#             res.append("0")
#     aux = "".join(res)
#     return int(aux,base=2)
# def interseccion(n1,n2):
#     res = ["0","b"]
#     for j in range(2,len(n1)):
#         if n1[j] == "1" and n2[j] == "1":
#             res.append("1")
#         else:
#             res.append("0")
#     aux = "".join(res)
#     return int(aux,base=2)

# def diferencia(n1,n2):
#     res = ["0","b"]
#     for k in range(2,len(n1)):
#         if n1[k] == "1" and n2[k] == "0":
#             res.append("1")
#         else:
#             res.append("0")
#     aux = "".join(res)
#     return int(aux,base=2)
# while True:
#     try:
#         x,y = map(int,list(input().split()))
#         bx,by = bin(x),bin(y)
#         bx,by = completar(bx,by)
#         print(union(bx,by),interseccion(bx,by),diferencia(bx,by))
#     except EOFError:
#         break

#

