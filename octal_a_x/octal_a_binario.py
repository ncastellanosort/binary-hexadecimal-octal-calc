print('Octal a Binario')
num = input('Dime el numero: ')
numcar = []
numbin = []

# agregar cada caracter numerico a la lista
for c in num:
    c = int(c)
    c = numcar.append(c)

# convertir cada indice a binario, con 3 caracteres binarios con el metodo zfill() y agregarlos a la lista numbin
for n in numcar:
    n = bin(n)[2:].zfill(3)
    n = numbin.append(n)

# en el string vacio usar el metodo join para unir la lista entera
unida = ''.join(numbin)

print('El numero en binario es: ', unida)
