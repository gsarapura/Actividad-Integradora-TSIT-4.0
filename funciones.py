
def min_num_list(my_list):
    """Entra una lista, 
    Retorna:valor mínimo de la lista
    """

    min_number = my_list[0]
    for i in my_list:
        if i < min_number:
            min_number = i
    return(min_number)

#Inicio prueba, limpiar commits "TAREA UNO_LIStA"
#Cambiar, valor a "LARGEST_NUMBER" segun branch_input
#num1 = int(input("Ingrese primer digito: "))
#num2 = int(input("Ingrese segundo digito: "))
#num3 = int(input("Ingrese tercero digito: "))
#num4 = int(input("Ingrese cuarto digito: "))
#num5 = int(input("Ingrese quinto digito: "))
#my_list = [num1, num2, num3, num4, num5]
largest_number = num1 #Aquí dejar el commit, zero tambien es válido, pero no esta en la lista
for i in my_list[1:]:
    if i > largest_number:
        largest_number = i
print(largest_number)

