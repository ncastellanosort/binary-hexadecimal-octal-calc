print('Hexadecimal a Binario')
num = input('Dime el numero: ')
numcar = []
numbin = []
dec_let = {
    'A': '10',
    'B': '11',
    'C': '12',
    'D': '13',
    'E': '14',
    'F': '15',
}

# agregar cada caracter numerico a la lista
for c in num:
    c = numcar.append(c)  # ['3', 'B', '9']

# ennumerate para agregar un contador iterable,donde genera par de indices mientras se recorre con el bucle for,seguimientos
for key, value in dec_let.items():
    for i, n in enumerate(numcar):
        if n == key:  # si n es igual a la llave, entonces el indice va a ser igual al valor
            numcar[i] = value

# convertir a int toda la lista
lis_int = [int(n) for n in numcar]

# convertir cada indice a binario, con 3 caracteres binarios con el metodo zfill() y agregarlos a la lista numbin
for n in lis_int:
    n = bin(n)[2:].zfill(4)
    n = numbin.append(n)

# en el string vacio usar el metodo join para unir la lista entera
unida = ''.join(numbin)

print('El numero en binario es: ', unida)
