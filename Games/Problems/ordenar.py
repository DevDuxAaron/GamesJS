# import numpy as np
# def camino(cup,n):
#     print(cup)
#     aux = np.zeros([n,n], dtype = int)
#     for f in range(n):
#         for c in range(n):
#             for k in range(n):
#                 if cup[k][c] == 1:
#                     aux[f][c] = 1
#                     break
#             aux[f][c] = 0
#             print("\nAUX\n",aux)
#     cup = aux
#     return aux

# n,m = map(int,input().split())
# copa = np.zeros([n,n], dtype = int)

# for e in range(m):
#     a,b = map(int,input().split())
#     copa[a][b] = 1
# i,j = map(int,input().split())
# if copa[i][j] == 1:
#     res ='SI'
# else:
#     #print('Locura')
#     #print(copa)
#     copa = camino(copa,n)
#     if copa[i][j] == 1:
#         res = 'SI'
#     else:
#         res = 'NO'
# #print("\nMatrix a : \n", copa)
# print(res)


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

# import numpy as np

# n = int(input())
# x1,y1,x2,y2 = map(int,input().split())
# mat = []
# for i in range(n):
#     mat.append(input())

# roads = np.zeros([n,n], dtype = int)

# for i in range(0,n):
#     for j in range(0,n):
#         if mat[i][j] == 'L':
#             roads[i][j] = 1


# conected = True
# while conected:
#     pila = []

# print(mat)
# print()
# print(roads)

d = [0,3,2,3,2,3,4,5]
d_aux = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
dd = [0,2,4,2,4,4,4,6]

brutacio = [
    [6,5,4,5,4,5,4,5,4,5,4,5,4,5,6],
    [5,4,5,4,3,4,3,4,3,4,3,4,5,4,5],
    [4,5,4,3,4,3,4,3,4,3,4,3,4,5,4],
    [5,4,3,4,3,2,3,2,3,2,3,4,3,4,5],
    [4,3,4,3,2,3,2,3,2,3,2,3,4,3,4],
    [5,4,3,2,3,4,1,2,1,4,3,2,3,4,5],
    [4,3,4,3,2,1,2,3,2,1,2,3,4,3,4],
    [5,4,3,2,3,2,3,0,3,2,3,2,3,4,5],
    [4,3,4,3,2,1,2,3,2,1,2,3,4,3,4],
    [5,4,3,2,3,4,1,2,1,4,3,2,3,4,5],
    [4,3,4,3,2,3,2,3,2,3,2,3,4,3,4],
    [5,4,3,4,3,2,3,2,3,2,3,4,3,4,5],
    [4,5,4,3,4,3,4,3,4,3,4,3,4,5,4],
    [5,4,5,4,3,4,3,4,3,4,3,4,5,4,5],
    [6,5,4,5,4,5,4,5,4,5,4,5,4,5,6]
    ]
brutilda = {-7:0,-6:1,-5:2,-4:3,-3:4,-2:5,-1:6,0:7,1:8,2:9,3:10,4:11,5:12,6:13,7:14}
while True:
    try:
        c1,c2 = input().split()
        l1,n1 = c1[0],int(c1[1])
        l2,n2 = c2[0],int(c2[1])
        if l1 == l2 and n1 == n2:
            resp = 0
        elif l1 == l2:
            resp = d[abs(n1-n2)] 
        elif n1 == n2:
            resp = d[abs(d_aux[l1]-d_aux[l2])]
        elif abs(n1-n2) == abs(d_aux[l1]-d_aux[l2]):
            if (l1 == 'a' or l1 == 'h' or l2 == 'a' or l2 == 'h') and (abs(n1-n2) == 1):
                resp = 4
            else:
                resp = dd[abs(n1-n2)]
        else:
            x = brutilda[d_aux[l2]-d_aux[l1]]
            y = brutilda[n2-n1]
            resp = brutacio[x][y]
        print("To get from {} to {} takes {} knight moves.".format(c1,c2,resp)) 
    except EOFError:
        break


