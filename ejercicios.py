#Taller Acondicionamiento - Sabrina Sagasti

#Ejercicio 1

def sumar_digitos():
    numero = input("Digite un número entero: ")
    total = sum(int(digito) for digito in numero)
    print(f"Resultado de la suma de dígitos: {total}")

sumar_digitos()

#Ejercicio 2
def contar_vocales():
    suma = 0
    texto = input("Ingrese un texto: ").lower()

    for letra in texto:
        if letra in "aeiou":
            suma += 1
    
    print(f"Cantidad de vocales encontradas: {suma}")

contar_vocales()

#Ejercicio 3

def es_palindromo():
    entrada = input("Ingrese una frase: ").lower()
    limpio = []

    for letra in entrada:
        if letra != " ":
            limpio.append(letra)

    invertido = limpio[::-1]

    if limpio == invertido:
        print("Sí es un palíndromo")
    else:
        print("No es un palíndromo")

es_palindromo()

#Ejercicio 4

def invertir_lista():
    numeros = input("Introduce números separados por espacios: ")
    lista_numeros = numeros.split()

    lista_numeros.reverse()

    print(" ".join(lista_numeros))

invertir_lista()

#Ejercicio 5

def contar_palabras_en_texto():
    cadena = input("Por favor ingrese una frase: ")  # Captura la entrada del usuario
    palabras = cadena.split()  # Divide la cadena en palabras, considerando cualquier cantidad de espacios
    print(f"Cantidad de palabras: {len(palabras)}")  # Muestra el número de palabras

contar_palabras_en_texto()

#Ejercicio 6

def encontrar_max_y_min():
    entrada = input("Introduce números separados por espacios: ")
    lista_numeros = entrada.split()

    for i in range(len(lista_numeros)):
        lista_numeros[i] = int(lista_numeros[i])

    mayor = lista_numeros[0]
    menor = lista_numeros[0]

    for numero in lista_numeros:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero

    print(f"Mayor: {mayor}  Menor: {menor}")

encontrar_max_y_min()

