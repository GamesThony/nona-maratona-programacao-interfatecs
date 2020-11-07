def indexOf(arr, val):
    try: return arr.index(val)
    except: return -1

while True:
    try:
        N = int(input())
        valores = []
        for n in range(0, N):
            valores.append(int(input()))

        valores.sort()

        qnt = len(valores)

        media = sum(valores) / qnt
        mediana = 0

        if qnt % 2 == 0: mediana = (valores[qnt // 2] + valores[(qnt // 2) - 1]) / 2
        else: mediana = valores[qnt // 2]

        NUMS = []
        QNTS = []

        for valor in valores:
            index = indexOf(NUMS, valor)
            if index == -1:
                NUMS.append(valor)
                QNTS.append(1)
            else: QNTS[index] = QNTS[index] + 1

        maior = max(QNTS)
        modas = [str(NUMS[i]) for i in range(0, len(NUMS)) if QNTS[i] == maior]

        print("MODA=" + ",".join(modas))
        print("MEDIA=%.2f" % media)
        print("MEDIANA=%.2f" % mediana)
    except: break
