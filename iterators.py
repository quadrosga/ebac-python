my_list = [1,2,3,4,5]

print(my_list)

# Usando for loop tradicional

for num in my_list:
    print(num)

# Usando iterators

iter_exemplo = iter(my_list)

print(iter_exemplo)

print(next(iter_exemplo)) # next acessa o primeiro elemento do iterator

print(next(iter_exemplo)) # next acessa o segundo elemento do iterator

print(next(iter_exemplo)) # next acessa o terceiro elemento do iterator

print(next(iter_exemplo)) # next acessa o quarto elemento do iterator

print(next(iter_exemplo)) # next acessa o quinto elemento do iterator

print(next(iter_exemplo)) # StopIteration (não há sexto elemento)

# Loop for tradicional
x = [1, 2, 3, 4, 5]

for i in x:
    print(i)

# Iterator com for loop

x = [1, 2, 3, 4, 5]
y = iter(x)
try:
    while True:
        print(next(y))
except StopIteration as e:
    pass