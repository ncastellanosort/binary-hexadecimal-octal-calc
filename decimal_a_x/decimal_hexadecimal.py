print('Decimal a Hexadecimal')
num = int(input('Dime el numero: '))
hxdc = ''
dic_hex = {
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F',
}

if num == 0:
    hxdc = '0'

while num > 0:
    resto = num % 16
    hxdc = str(resto) + hxdc
    num = num // 16

    for key, value in dic_hex.items():
        if str(resto) == key:
            hxdc = hxdc.replace(key, value)
            break

print('Numero en hexadecimal:', hxdc)
