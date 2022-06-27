
def sumar(list_num):
    suma = 0
    for i in list_num:
        suma += i
        return suma
#aca hago el edit mío para el pull




list_num = []
# descomentar está linea si se quiere decidir la cantidad de números a ingresar
#cant = int(input('¿Cuántos números quiere ingresar? '))
#en caso de quere decidir la cantidad de número a agregar en el array, cambiar el parámetro del range por "cant".

print('Bienvenido a la Supercalculadora, por favor ingrese 5 números enteros ')

for w in  range(5): #el range le dira al for cuantas veces ejecutar el código según el valor que se le indique
    w = int(input('Ingrese un número: '))
    list_num.append(w)
    
print('Los números ingresados son los siguientes: ',list_num)


#código función suma







def min_num_list(my_list):
    """
    Entra una lista, 
    Retorna: valor mínimo de la lista
    """
    min_number = my_list[0]
    for i in my_list:
        if i < min_number:
            min_number = i
    return(min_number)

# Maximo pasado a funcion
def largest_num_list(my_list):
    """
    Entra una lista, 
    Retorna: valor máximo de la lista
    """
    largest_number = my_list[0] #Aquí dejar el commit, zero tambien es válido, pero no esta en la lista
    for i in my_list[1:]:
        if i > largest_number:
            largest_number = i
    return(largest_number)


# Promedio
def promedio(lista):
    """
    Recibe una lista como argumento y retorna el promedio de todos sus elementos.
    """
    acumulador = 0
    for i in lista:
        acumulador += i
    promedio = acumulador // len(lista)
    return promedio

#Éste es el código del menu. Utiliza una cadena de elif para ejecutar el código de la opcion elegida

option = int(input('Elija el número de las Siguentes opciones: \n '
 """
------------------------------ MENU ------------------------------
    1. Función Suma
    2. Función Promedio
    3. Función Máximo
    4. Función Mínimo
-------------------------------------------------------------------
    """))


if option == 1:    #Suma
    #ejecuto la funcion suma ásandole de parámetro la lista de números
    print('La Suma de todos los números que ingresaste es: ' ,'Aquí va el ejecutable de la Suma')

elif option == 2:  #Promedio
    #ejecuto la funcion promedio ásandole de parámetro la lista de números
    print('El Promedio de los números que ingresaste es: ', promedio(list_num))

elif option == 3:  #Máximo
    print('El Máximo valor de la lista es: ', largest_num_list(list_num))
    
elif option == 4:  #Mínimo
    print('El Mínimo valor de la lista es: ',min_num_list(list_num))

else:
    print('Has elegido incorrectamente. Por favor vuelva a intentarlo. ')

