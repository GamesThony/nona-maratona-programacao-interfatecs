N = int(input())

TME = 0
TMT = 0

inicio = 0
fim = 0

for n in range(0, N):
    entrada = input().split(' ')
    CHEGADA = int(entrada[0])
    DURACAO = int(entrada[1])
    
    TME = TME + (inicio - CHEGADA)
    inicio = inicio + DURACAO

    fim = fim + DURACAO
    TMT = TMT + (fim - CHEGADA)
   

TME = TME / N
TMT = TMT / N
print("TME:%.1f" % TME)
print("TMT:%.1f" % TMT)
