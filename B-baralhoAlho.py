def verifica( A, B, N ):
    for i in range( N ):
        if A[i] != B[i]:
            return False
    return True

def baralho_alho():

    N = int( input() )
    
    k = 0

    A = list( map( int, input().split() ) ) 
    B = list( map( int, input().split() ) ) 
    P = list( map( int, input().split() ) ) 
    V = list( range( N ) )
    anteriores = list()
    imp = False
    somaA = 0
    somaB = 0
    
    for i in range( N ):
        somaA += A[i]
        somaB += B[i]
    
    if( somaA != somaB ):
        print("IMPOSSIVEL")
        return
    
    while True:
        
        for i  in range( N ):
            V[ P[i]-1 ] = A[i]
            
        for number in anteriores:
            if( number == V ):
                imp = True
                
        A = list( V )
        anteriores.append( list( V ) )
        k += 1
        
        if( k > 1000000000 ):
            print("DEMAIS")
            break
        if( imp == True ):
            print("IMPOSSIVEL")
            break
        if( verifica( A, B, N ) == True ):
            print( k ) 
            break   
        

baralho_alho()
