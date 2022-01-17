from input_array import input_array
def main():
    array = input_array()
    suma = int(input("Ingresa el resultado de la suma : "))
    array.sort()
    position_sumando_A=0
    while array[position_sumando_A] <= suma:
        position_sumando_B = position_sumando_A+1
        while array[position_sumando_B] <= suma:
            if (array[position_sumando_A] + array[position_sumando_B]) == suma:
                print("El primer subconjunto de 2 numeros que de resultado", suma, "son el", array[position_sumando_A], "y", array[position_sumando_B])
                exit()
            else:
                position_sumando_B+=1
        position_sumando_A+=1
    print("No existe subconjunto de 2 numeros que su suma den ", suma)

if __name__ == "__main__":
    main()