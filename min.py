def min_num_list(my_list):
    """Entra una lista, 
    Retorna:valor mínimo de la lista
    """

    min_number = my_list[0]
    for i in my_list:
        if i < min_number:
            min_number = i
    return(min_number)
