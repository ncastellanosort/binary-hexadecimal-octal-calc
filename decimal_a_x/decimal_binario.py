print('Decimal a Binario')
num = int(input('Dime el numero: '))
binario = ''

if num == 0:
    binario = '0'
else:
    while num > 0:
        resto = num % 2
        binario = str(resto) + binario
        num = num // 2

print('El numero es: '+ binario +' en binario')
