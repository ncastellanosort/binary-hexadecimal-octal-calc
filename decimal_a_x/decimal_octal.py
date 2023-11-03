print('Decimal a Octal')
num = int(input('Dime el numero: '))
octal = ''

if num == 0:
    octal = '0'
else:
    while num > 0:
        resto = num % 8
        octal = str(resto) + octal
        num = num // 8

print('El numero es: ' + octal + ' en octal')
