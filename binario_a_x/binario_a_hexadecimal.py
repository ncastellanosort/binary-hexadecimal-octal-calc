print('Binario a Hexadecimal')
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

# recorrer la lista que esta separada en cantidades de 4 y convertir cada indice en binario con la funcion int(,base 2)
for n in partes:
    n = int(n, 2)
    n = lista.append(n)
# hacer otra compresion de la lista normal para convertir los datos de int a string para despues unirla
lista_st = [str(num) for num in lista]


# unirla con el metodo join en el string de al lado
unida = ''.join(lista_st)

#un for para recorrer el diccionario y para reemplazar por cada key y value
for key, value in dic_hex.items():
    unida = unida.replace(key,value)

print('El numero en hexadecimal es: ', unida)
