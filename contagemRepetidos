def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l


linhas, colunas = [int(x) for x in input().split()]

matriz = []

for i in range(linhas):
    linha = []
    linha = [int(x) for x in input().split()]
    matriz.append(linha)

num_repetidos = []

for i in range(linhas):
    for j in range(colunas):
        contador = 0
        for k in range(linhas):
            for l in range(colunas):
                if matriz[i][j] == matriz[k][l]:
                    contador = contador + 1
        if contador > 1:
            num_repetidos.append(matriz[i][j])


lista = remove_repetidos(num_repetidos)

print(len(lista))
