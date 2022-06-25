list_num = []
# descomentar está linea si se quiere decidir la cantidad de números a ingresar
#cant = int(input('¿Cuántos números quiere ingresar? '))
#en caso de quere decidir la cantidad de número a agregar en el array, cambiar el parámetro del range por "cant".

for w in  range(5): #el range le dira al for cuantas veces ejecutar el código según el valor que se le indique
    w = int(input('Ingrese un número: '))
    list_num.append(w)
    
print(list_num)



   
def min_num_list(my_list):
    """Entra una lista, 
    Retorna:valor mínimo de la lista
    """
    min_number = my_list[0]
    for i in my_list:
        if i < min_number:
            min_number = i
    return(min_number)

# Maximo pasado a funcion
def largest_num_list(my_list):
    """Entra una lista, 
    Retorna:valor máximo de la lista
    """
    largest_number = my_list[0] #Aquí dejar el commit, zero tambien es válido, pero no esta en la lista
    for i in my_list[1:]:
        if i > largest_number:
            largest_number = i
    return(largest_number)



#Éste es el código del menu. Utiliza una cadena de elif para ejecutar el código de la opcion elegida


option = int(input('Elija el número de las Siguentes opciones: 1-sumar, 2-mínimo, 3-máximo, 4-promedio '))


if option == 1:    #Suma
    #ejecuto la funcion suma ásandole de parámetro la lista de números
    print('Aquí va el ejecutable de la Suma')
elif option == 2:  #Mínimo
    print(min_num_list(list_num))
elif option == 3:  #Máximo
    print(largest_num_list(list_num))

elif option == 4:  #Promedio
    #ejecuto la funcion promedio ásandole de parámetro la lista de números
    print('Aquí va el ejecutable del Promedio')
else: #Máximo
    print('Has elegido incorrectamente')

# Promedio
def promedio(lista):
    """
    Recibe una lista como argumento y retorna el promedio de sus elementos.
    """
    acumulador = 0
    for i in lista:
        acumulador += i
    promedio = acumulador // len(lista)
    return promedio

print("Primer Programa de Trabajo en Equipo")
print("Materia = Programación Inicial\n")
menu_selection = input("Seleccione la Operación que desea realizar: ")
print("1- Suma de total de la lista")
print("2- Promedio de lista")
print("3- Mínimo Valor en la lista")
print("4- Máximo valor en la lista")

min_num_list(list_num)
largest_num_list(list_num)
print(min_num_list(list_num))
print(largest_num_list(list_num))
