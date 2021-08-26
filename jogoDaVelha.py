tamanho = int(input())

if tamanho%2 == 0:
    max_jogadas = int((tamanho**2)/2)
else:
    max_jogadas = int(((tamanho**2)/2) + 1)

entrada = []

for i in range(tamanho):
    str = input()
    entrada.append(str)

if tamanho == 1:
    print(f'Vencedor: {entrada[0]}')

else:
    matriz = []
    matriz = [list(jogadas) for jogadas in entrada]

    contador_O = 0
    contador_X = 0

    for linhas in matriz:
        for jogada in linhas:
            if jogada == 'O':
                contador_O = contador_O + 1
            else:
                contador_X = contador_X + 1

    if contador_O > max_jogadas or contador_X > max_jogadas:
        print('UM DOS JOGADORES JOGOU MAIS DO QUE DEVERIA')

    else:
        vencedor = []
        contador = 0
        for i in range(tamanho):
            for j in range(tamanho):
                if matriz[i][j] == matriz[i][0]:
                    contador = contador + 1
                    if contador == tamanho:
                        vencedor.append(matriz[i][j])
                else:
                    break
            contador = 0


        for i in range(tamanho):
            for j in range(tamanho):
                if matriz[j][i] == matriz[0][i]:
                    contador = contador + 1
                    if contador == tamanho:
                        vencedor.append(matriz[j][i])
                else:
                    break
            contador = 0

        for i in range(tamanho):
            if matriz[i][i] == matriz[0][0]:
                contador = contador + 1
                if contador == tamanho:
                    vencedor.append(matriz[i][i])
        contador = 0

        j = 0
        for i in range(tamanho-1, -1, -1):
            if matriz[j][i] == matriz[0][tamanho - 1]:
                contador = contador + 1
                if contador == tamanho:
                    vencedor.append(matriz[j][i])
            j = j + 1

        if 'X' in vencedor and 'O' in vencedor:
            print('Vencedor: INDETERMINADO')
        elif 'X' in vencedor or 'O' in vencedor:
            print(f'Vencedor: {vencedor[0]}')
        else:
            print('Vencedor: EMPATE')
