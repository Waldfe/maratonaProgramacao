def joao_joao():
    
    D = list( map( int, input().split() ) )
    verifica = [0]*4
    cont = 0
    
    for i in range( len( D ) ):
        if( D[i] == 1 ):
            verifica[0] =+ 1
        if( D[i] == 2 ):
            verifica[1] =+ 1
        if( D[i] == 3 ):
            verifica[2] =+ 1
        if( D[i] == 4 ):
            verifica[3] =+ 1
    for i in range( 4 ):
        if( verifica[i] == 0 ):
            cont += 1
            
    print( cont )
    
joao_joao()