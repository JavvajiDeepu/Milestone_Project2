def prime_generator(bound):
    prime_list =[]
    for i in range(2, bound):
        for x in range(2,n):
            if i % x ==0:
                print('{} equals {} * {}.'.format(n,x,n//x))
                break
        else:
            print('{} is aprime numner.'.format(n))
            yield n