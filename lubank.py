TECLAS = [[], [], [], [], [], [], [], [], [], [], [], []]
for n in range(0, 12):
    entrada = input().split(';')
    index = int(entrada[0]) - 1
    del entrada[0]
    TECLAS[index] = entrada

NOME = []
SENHA = []
TENTATIVAS = []

while True:
    entrada = input().split(';')
    nome = entrada[0]
    senha = entrada[1]
    if nome == senha and nome == "fim": break
    else:
        NOME.append(nome)
        SENHA.append(senha)
        TENTATIVAS.append(0)

while True:
    try:
        entrada = input().split(';')
        user = entrada[0]
        if user not in NOME: print(user + ": usuario inexistente")
        else:
            del entrada[0]
            index = NOME.index(user)
            senha = SENHA[index]

            if len(entrada) != len(senha):
                TENTATIVAS[index] = TENTATIVAS[index] + 1
                if TENTATIVAS[index] >= 3: print(user + ": usuario bloqueado")
                else: print(user + ": acesso negado")
            else:
                ok = True
                for i in range(0, len(senha)):
                    indexTecla = int(entrada[i]) - 1
                    if senha[i] not in TECLAS[indexTecla]:
                        ok = False
                        break
                    
                if ok == True:
                    if TENTATIVAS[index] >= 3: print(user + ": usuario bloqueado")
                    else:
                        print(user + ": acesso concedido")
                        TENTATIVAS[index] = 0
                else:
                    TENTATIVAS[index] = TENTATIVAS[index] + 1
                    if TENTATIVAS[index] >= 3: print(user + ": usuario bloqueado")
                    else: print(user + ": acesso negado")
    except EOFError: break
    except: break
