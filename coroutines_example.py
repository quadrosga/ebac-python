def func():
    print('Function starts')

    #Pause
    yield

    print('End of function')

try:
    y = func()
    print(type(y))
    next(y)
    next(y)

except StopIteration as e:
    pass