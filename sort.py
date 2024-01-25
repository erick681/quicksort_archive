def quicksort(lista, inicio = 0,fim=None):
    if fim is None :
        fim = len(lista)-1
    if inicio < fim :
        p = partition(lista,inicio,fim)
        quicksort(lista,inicio,p-1)
        quicksort(lista,p+1,fim)
        print(lista)

def partition(lista,inicio,fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio,fim):
        if lista[j] <= pivot:
            lista[j],lista[i] = lista[i],lista[j]
            i = i+1
    lista[i], lista[fim] = lista[fim],lista[i]
    return i 
quicksort([7,3,5,4,1,8,7,9,9])


