nomes = []
while True:
    try:
        nome = input()
        nomes.append(nome)
    except EOFError: break
    except: break

result = []
for i in range(0, len(nomes)):
    nome_ = nomes[i].split(' ')
    nome = []
    tamanho = len(nome_)
    for i in range(0, tamanho):
        if i == 0 or i + 1 == tamanho:
            nome.append(nome_[i])
        else:
            nome.append(nome_[i][0] + ".")
    result.append(" ".join(nome)) 
result.sort()
for res in result: print(res)
