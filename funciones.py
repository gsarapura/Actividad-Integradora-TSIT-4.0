
lista = []
# descomentar está linea si se quiere decidir la cantidad de números a ingresar
#cant = int(input('¿Cuántos números quiere ingresar? '))
#en caso de quere decidir la cantidad de número a agregar en el array, cambiar el parámetro del range por "cant".

for w in  range(5): #el range le dira al for cuantas veces ejecutar el código según el valor que se le indique
    w = int(input('Ingrese un número: '))
    lista.append(w)
    print(lista)

    
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
    largest_number = my_list[0] #Aquí dejar el commit, zero tambien es válido, pero no esta en la lista
    for i in my_list[1:]:
        if i > largest_number:
            largest_number = i
    return(largest_number)