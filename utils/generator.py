def max():
    i = 0
    while i < 100:
        yield i
        i +=1
g = max()
print(next(g))
print(list(g))#list function can turn a generator in to list.

my_range= range(100)
print(my_range)      
