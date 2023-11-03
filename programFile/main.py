def lineas():
    print('---------------------------------------------')


lineas()
print('Programa de conversiones')
lineas()
print('Que deseas convertir?')
print('Selecciona el indice para la conversion que quieras hacer:')
lineas()
print('1. Decimales')
print('2. Binarios')
print('3. Hexadecimales')
print('4. Octales')
lineas()
dec1 = input('Selecciona el numero de la conversion que deseas realizar: ')

match dec1:
    case '1':
        lineas()
        print('1. Decimal a Binario')
        print('2. Decimal a Hexadecimal')
        print('3. Decimal a Octal')
        lineas()
        dec2 = input('Selecciona el numero de la conversion que deseas realizar: ')
        lineas()
        match dec2:
            case '1':
                print('Decimal a Binario')
                lineas()
                num = int(input('Dime el numero: '))
                binario = ''
                if num == 0:
                    binario = '0'
                else:
                    while num > 0:
                        resto = num % 2
                        binario = str(resto) + binario
                        num = num // 2
                lineas()
                print('El numero es: ' + binario + ' en binario')

            case '2':
                print('Decimal a Hexadecimal')
                lineas()
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
                lineas()
                print('Numero en hexadecimal:', hxdc)

            case '3':
                print('Decimal a Octal')
                lineas()
                num = int(input('Dime el numero: '))
                octal = ''

                if num == 0:
                    octal = '0'
                else:
                    while num > 0:
                        resto = num % 8
                        octal = str(resto) + octal
                        num = num // 8
                lineas()
                print('El numero es: ' + octal + ' en octal')

    case '2':
        lineas()
        print('1. Binario a Decimal')
        print('2. Binario a Hexadecimal')
        print('3. Binario a Octal')
        lineas()
        dec2 = input('Selecciona el numero de la conversion que deseas realizar: ')
        lineas()
        match dec2:
            case '1':
                print('Binario a Decimal')
                lineas()
                num = input('Ingresa el numero: ')
                ptc = []  # lista donde van a ir las potencias de 16
                nums = []  # lista donde va a ir cada numero
                mults = []  # lista donde van a ir los resultados de las multiplicaciones

                # llenar la lista con las potencias de 16
                for i in range(0, len(num), 1):
                    expo = 2 ** i
                    ptc.append(expo)
                    ptc.sort(reverse=True)

                # llenar la lista con cada numero ingresado
                for i in num:
                    i = int(i)
                    nums.append(i)

                # realizar la multiplicacion de cada digito por su respectiva potencia y agregarlo a la lista total_mult
                for i in range(0, len(nums), 1):
                    total_mult = ptc[i] * nums[i]
                    mults.append(total_mult)

                # la funcion sum() suma todos los elementos de la lista
                lineas()
                print('El numero en decimal es: ', sum(mults))

            case '2':
                print('Binario a Hexadecimal')
                lineas()
                num = input('Escribe el numero binario: ')
                lista = []
                dic_hex = {
                    '10': 'A',
                    '11': 'B',
                    '12': 'C',
                    '13': 'D',
                    '14': 'E',
                    '15': 'F',
                }

                # hacer una compresion para separar el input en cantidades de 3
                partes = [num[i:i + 4] for i in range(0, len(num), 4)]

                # recorrer la lista que esta separada en cantidades de 4 y convertir cada indice en binario con la
                # funcion int(,base 2)
                for n in partes:
                    n = int(n, 2)
                    n = lista.append(n)
                # hacer otra compresion de la lista normal para convertir los datos de int a string para despues unirla
                lista_st = [str(num) for num in lista]

                # unirla con el metodo join en el string de al lado
                unida = ''.join(lista_st)

                # un for para recorrer el diccionario y para reemplazar por cada key y value
                for key, value in dic_hex.items():
                    unida = unida.replace(key, value)

                lineas()
                print('El numero en hexadecimal es: ', unida)

            case '3':
                print('Binario a Octal')
                lineas()
                num = input('Escribe el numero binario: ')
                lista = []

                # hacer una compresion para separar el input en cantidades de 3
                partes = [num[i:i + 3] for i in range(0, len(num), 3)]

                # recorrer la lista que esta separada en cantidades de 3 y convertir cada indice en binario con la
                # funcion int(,base 2)
                for n in partes:
                    n = int(n, 2)
                    n = lista.append(n)

                # hacer otra compresion de la lista normal para convertir los datos de int a string para despues unirla
                lista_st = [str(num) for num in lista]

                # unirla con el metodo join en el string de al lado
                unida = ''.join(lista_st)

                lineas()
                print('El numero en octal es: ', unida)

    case '3':
        lineas()
        print('1. Hexadecimal a Binario')
        print('2. Hexadecimal a Decimal')
        lineas()
        dec2 = input('Selecciona el numero de la conversion que deseas realizar: ')
        lineas()
        match dec2:
            case '1':
                print('Hexadecimal a Binario')
                lineas()
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

                # ennumerate para agregar un contador iterable,donde genera par de indices mientras se recorre con el
                # bucle for,seguimientos
                for key, value in dec_let.items():
                    for i, n in enumerate(numcar):
                        if n == key:  # si n es igual a la llave, entonces el indice va a ser igual al valor
                            numcar[i] = value

                # convertir a int toda la lista
                lis_int = [int(n) for n in numcar]

                # convertir cada indice a binario, con 3 caracteres binarios con el metodo zfill() y agregarlos a la
                # lista numbin
                for n in lis_int:
                    n = bin(n)[2:].zfill(4)
                    n = numbin.append(n)

                # en el string vacio usar el metodo join para unir la lista entera
                unida = ''.join(numbin)

                lineas()
                print('El numero en binario es: ', unida)

            case '2':
                print('Hexadecimal a Decimal')
                lineas()
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

                # ennumerate para agregar un contador iterable,donde genera par de indices mientras se recorre con el
                # bucle for, seguimientos
                for key, value in dic_hex.items():
                    for i, n in enumerate(nums):
                        if n == key:  # si n es igual a la llave, entonces el indice va a ser igual al valor
                            nums[i] = value

                # llenar la lista con las potencias de 16
                for i in range(0, len(num), 1):
                    expo = 16 ** i
                    ptc.append(expo)
                    ptc.sort(reverse=True)

                # hacer la multiplicacion de cada numero por su indice y agregarlo a la lista del total de las
                # multiplicaciones
                for i in range(0, len(nums), 1):
                    # convertirla a solo enteros
                    lis_int = [int(n) for n in nums]

                    total_mult = ptc[i] * lis_int[i]
                    mults.append(total_mult)

                lineas()
                print('El numero en decimal es: ', sum(mults))

    case '4':
        lineas()
        print('1. Octal a Binario')
        print('2. Octal a Decimal')
        lineas()
        dec2 = input('Selecciona el numero de la conversion que deseas realizar: ')
        lineas()
        match dec2:
            case '1':
                print('Octal a Binario')
                lineas()
                num = input('Dime el numero: ')
                numcar = []
                numbin = []

                # agregar cada caracter numerico a la lista
                for c in num:
                    c = int(c)
                    c = numcar.append(c)

                # convertir cada indice a binario, con 3 caracteres binarios con el metodo zfill() y agregarlos a la
                # lista numbin
                for n in numcar:
                    n = bin(n)[2:].zfill(3)
                    n = numbin.append(n)

                # en el string vacio usar el metodo join para unir la lista entera
                unida = ''.join(numbin)

                lineas()
                print('El numero en binario es: ', unida)

            case '2':
                print('Octal a Decimal')
                lineas()
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

                # hacer la multiplicacion de cada numero por su indice y agregarlo a la lista del total de las
                # multiplicaciones
                for i in range(0, len(nums), 1):
                    total_mult = ptc[i] * nums[i]
                    mults.append(total_mult)

                # la funcion sum() suma todos los elementos de la lista
                lineas()
                print('El numero en octal es: ', sum(mults))
