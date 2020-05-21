import numpy as np
def camino(cup,n):
    print(cup)
    aux = np.zeros([n,n], dtype = int)
    for f in range(n):
        for c in range(n):
            for k in range(n):
                if cup[k][c] == 1:
                    aux[f][c] = 1
                    break
            aux[f][c] = 0
            print("\nAUX\n",aux)
    cup = aux
    return aux

n,m = map(int,input().split())
copa = np.zeros([n,n], dtype = int)

for e in range(m):
    a,b = map(int,input().split())
    copa[a][b] = 1
i,j = map(int,input().split())
if copa[i][j] == 1:
    res ='SI'
else:
    #print('Locura')
    #print(copa)
    copa = camino(copa,n)
    if copa[i][j] == 1:
        res = 'SI'
    else:
        res = 'NO'
#print("\nMatrix a : \n", copa)
print(res)

# #la = {5:"Hola",15:"Hola",9:"Hola",8:"Hola",3:"Hola",4:"Hola"}
# foo = {}
# while True:
#     try:
#         n = int(input())
#         for i in range(n):
#             v,k = input().split()
#             k = int(k)
#             foo[k] = v
#         res = sorted(foo)
#         for j in res:
#             print(foo[j])
#     except EOFError :
#         break


# pal = {}
# i = 1
# #Para 1
# for j in range(97,123):
#     pal[i] = chr(j)
#     i += 1
# #Para 2
# for j in range(97,123):
#     for k in range(97,123):
#         if k > j:
#             pal[i] = chr(j) + chr(k)
#             i += 1
# #Para 3
# for j in range(27,352):
#     for k in range(97,123):
#         if chr(k) > pal[j][-1]:
#             pal[i] = pal[j] + chr(k)
#             i += 1
# # #Para 4
# for j in range(351,2952):
#     for k in range(97,123):
#         if chr(k) > pal[j][-1]:
#             pal[i] = pal[j] + chr(k)
#             i += 1
# #Para 5
# for j in range(2951,17903):
#     for k in range(97,123):
#         if chr(k) > pal[j][-1]:
#             pal[i] = pal[j] + chr(k)
#             i += 1
# for p in range(82000,84000):
#     print(p,pal[p])
    

# fri = {}
# n = int(input())
# for i in range(n):
#     am1,am2 = input().split()
#     if am1 in fri:
#         fri[am1] += 1
#     else:
#         fri[am1] = 1
#     if am2 in fri:
#         fri[am2] += 1
#     else:
#         fri[am2] = 1
# max = {}
# for k1,v1 in fri.items():
#     if v1 in max:
#         max[v1].append(k1)
#         max[v1].sort()
#     else:
#         max[v1] = [k1]
# egg = sorted(max)
# print(max[egg[-1]][0])