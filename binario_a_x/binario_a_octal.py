print('Binario a Octal')
num = input('Escribe el numero binario: ')
lista = []

# hacer una compresion para separar el input en cantidades de 3
partes = [num[i:i + 3] for i in range(0, len(num), 3)]

# recorrer la lista que esta separada en cantidades de 3 y convertir cada indice en binario con la funcion int(,base 2)
for n in partes:
    n = int(n, 2)
    n = lista.append(n)

# hacer otra compresion de la lista normal para convertir los datos de int a string para despues unirla
lista_st = [str(num) for num in lista]

# unirla con el metodo join en el string de al lado
unida = ''.join(lista_st)

print('El numero en octal es: ', unida)
