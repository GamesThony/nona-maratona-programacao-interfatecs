def indexOf(arr, val):
    try: return arr.index(val)
    except: return -1

N = int(input())

pad = []
E = []
D = []
for n in range(0, N):
    entrada = input().split(' ')
    padE = int(entrada[0])
    padD = int(entrada[1])
    indexE = indexOf(pad, padE)
    if indexE == -1:
        pad.append(padE)
        E.append(1)
        D.append(0)
    else:
        E[indexE] = E[indexE] + 1
        
    indexD = indexOf(pad, padD)
    if indexD == -1:
        pad.append(padD)
        E.append(0)
        D.append(1)
    else:
        D[indexD] = D[indexD] + 1

values = []
for i in range(0, len(pad)):
    values.append([pad[i], E[i], D[i]])

values.sort()

qnt = 0

for value in values:
    padrao = value[0]
    esq_ = value[1] - 1
    dir_ = value[2] - 1
    if esq_ > 0:
        print("%d E %d" % (padrao, esq_))
        qnt = qnt + 1
        
    if dir_ > 0:
        print("%d D %d" % (padrao, dir_))
        qnt = qnt + 1

if qnt == 0: print("SEM TROCAS DESTA VEZ")
