while True:
    entrada = input().split(' ')
    H = float(entrada[0])
    C = float(entrada[1])
    L = float(entrada[2])
    if H + C + L == 0: break
    
    i = H * 100 / C
    if i <= 8.334 and L >= 0.8: print("PROJETO SIMPLES")
    else: print("PROJETO ESPECIAL")
