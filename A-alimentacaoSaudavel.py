
def alimentacao_saudavel():
    
    cont = 0
    soma = 0

    N, M = map( int, input().split() )

    matrix = []

    for i in range(N):
        linha = list( map( int, input().split() ) )
        matrix.append(linha)
    

    for j in range(M):
        cont = 0
        for i in range(N):
            if matrix[i][j] > cont:
                cont = matrix[i][j]
        soma += cont
        
    print(soma)

alimentacao_saudavel()