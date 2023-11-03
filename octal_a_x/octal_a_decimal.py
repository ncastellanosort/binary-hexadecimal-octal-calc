print('Octal a Decimal')
num = input('Dime el numero: ')
ptc = []  # lista donde van a ir las potencias de 16
nums = []  # lista donde va a ir cada numero
mults = []  # lista donde van a ir los resultados de las multiplicaciones


# llenar la lista con las potencias de 16
for i in range(0, len(num), 1):
    expo = 8 ** i
    ptc.append(expo)
    ptc.sort(reverse=True)

# llenar la lista con cada numero ingresado
for i in num:
    i = int(i)
    nums.append(i)

# hacer la multiplicacion de cada numero por su indice y agregarlo a la lista del total de las multiplicaciones
for i in range(0, len(nums), 1):
    total_mult = ptc[i] * nums[i]
    mults.append(total_mult)

# la funcion sum() suma todos los elementos de la lista
print('El numero en octal es: ', sum(mults))
