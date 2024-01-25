def mergesort(lista):
    if len(lista) <=1:
        return lista
    meio = len(lista)//2 
    lista_esquerda = lista[:meio]
    lista_direita = lista[meio:]

    lista_esquerda = mergesort(lista_esquerda)
    lista_direita = mergesort(lista_direita)
    return merge(lista_direita,lista_esquerda)

def merge(lista_esquerda,lista_direita):
    resultado = []
    i = j = 0

    while i <len(lista_esquerda) and j < len(lista_direita):
        if lista_esquerda[i]<lista_direita[j]:
            resultado.append(lista_esquerda[i])
            i += 1
        else :
            resultado.append(lista_direita[j])
            j+=1

    resultado.extend(lista_esquerda[i:])
    resultado.extend(lista_direita[j:])
    
    return resultado 

lista_numeros = [10,23,45,65,2,1,9,0]
lista_ordenada = mergesort(lista_numeros)

print(f"lista original :{lista_numeros}")
print("lista ordenada:",lista_ordenada)
