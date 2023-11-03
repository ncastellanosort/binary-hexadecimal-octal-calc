print('Hexadecimal a Decimal')
num = input('Dime el numero: ')
ptc = []  # lista donde van a ir las potencias de 16
nums = []  # lista donde va a ir cada numero
mults = []  # lista donde van a ir los resultados de las multiplicaciones
dic_hex = {
    'A': '10',
    'B': '11',
    'C': '12',
    'D': '13',
    'E': '14',
    'F': '15',
}

# llenar la lista con cada numero ingresado
for i in num:
    nums.append(i)

# ennumerate para agregar un contador iterable,donde genera par de indices mientras se recorre con el bucle for,
# seguimientos
for key, value in dic_hex.items():
    for i, n in enumerate(nums):
        if n == key:  # si n es igual a la llave, entonces el indice va a ser igual al valor
            nums[i] = value

# llenar la lista con las potencias de 16
for i in range(0, len(num), 1):
    expo = 16 ** i
    ptc.append(expo)
    ptc.sort(reverse=True)

# hacer la multiplicacion de cada numero por su indice y agregarlo a la lista del total de las multiplicaciones
for i in range(0, len(nums), 1):
    # convertirla a solo enteros
    lis_int = [int(n) for n in nums]

    total_mult = ptc[i] * lis_int[i]
    mults.append(total_mult)

print('El numero en decimal es: ', sum(mults))
