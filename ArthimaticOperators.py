if __name__ == '__main__':
    a = int(input())
    b = int(input())
    '''
           ( a>0 & a<(10 * 10) ) & ( b > 0 & b < (10 * 10) )
    '''
    if ( a>0 and a<(10**10) and b>0 and b<(10**10) ):
        print (a+b);
        print (a-b);
        print (a*b);