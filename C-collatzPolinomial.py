def collatz_polinomial():
    
    N = int( input() )
    a = list( map( int, input().split() ) )
    inteiro = 0
    var = 0
    cont = 0
    
    for i in range( N + 1 ):
        if( a[i] == 1 ):
            inteiro += pow( 2, N-i )
    
    while( inteiro != 1 ):
        
        if( inteiro%2 == 0 ):
            inteiro >>= 1
            cont += 1
        else:
            var = inteiro 
            inteiro <<= 1
            inteiro ^= var
            inteiro ^= 1
            cont += 1
        
    
    print( cont )

collatz_polinomial()