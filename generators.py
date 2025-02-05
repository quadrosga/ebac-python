# Uma função generator simples

def my_gen():
    n = 1
    print('First print, n is {}'.format(n))
    yield n # yield armazena n

    n += 1
    print('Second print, n is {}'.format(n))
    yield n

    n += 1
    print('Third and last print, n is {}'.format(n))
    yield n

# Armazenando a função generator em uma variável
test = my_gen()
next(test)
next(test)
next(test)