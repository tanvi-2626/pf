if __name__ == "__main__":
    N = 23
    G = 37

    print('The Value of N is: %d' % N)
    print('The Value of G is: %d' % G)

    a = 4
    print('Secret Number for Priya is: %d' % a)
    x = pow(G, a, N)

    b = 5
    print('Secret Number for Preet: %d' % b)
    y = pow(G, b, N)

    ka = pow(y, a, N)
    kb = pow(x, b, N)

    print('Secret Key for Priya is: %d' % ka)
    print('Secret Key for Preet is: %d' % kb)
