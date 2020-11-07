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

Alda Gusmao Antonia Naves
Ismael Novais Silveira Da Silva De Melo Santos
Prince Uria Noite
Ismael Castelo Gorjao
Jeferson Vargas Capistrano
Layra Bogado
Kyara Ramalho Cavaco
Telmo Lagos Ourique
Ariele Lousa
Nicolae Chaves Fitas
Tania Nascimento Montenegro
Aayush Areosa Sintra
Gastao Saraiva Guilheiro
Ariane
Lina Madureira Saloio
