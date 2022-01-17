

def input_array():
    cantidad = int(input("Ingrese cantidad de numeros que desea ingresar:"))
    print(f"Voy a solicitarte ", cantidad, " números:")
    numeros = []
    for i in range(cantidad):
        # Recuerda que range comenzará desde 0, así que imprimimos el número solicitado pero + 1
        numero = input(f"Ingresa el número {i + 1}: ")
        # Convertir a entero, pues input regresa una cadena
        numero = int(numero)
        # Lo agregamos al arreglo con append
        numeros.append(numero)
    return numeros