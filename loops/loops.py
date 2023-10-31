#normal
for i in range(6):
    x = "* "
    x = x*i
    print(f'{x: ^10}')

#downwards
for i in range(6):
    x = "* "
    x = x*(6-i)
    print(f'{x: ^10}')

#left
for i in range(6):
    x = "* "
    x = x*i
    print(f'{x: <10}')

#right
for i in range(6):
    x = "* "
    x = x*i
    print(f'{x: >10}')


