#  Código con errores
# # def contar_pares(lista):
#     if len(lista)==0:
#         return 0
#     if lista [0] % 2 == 0:
#         return 1
#     else:
#         return contar_pares(lista[1:])
    
# array = [3,4,5,7,8,9,4,2,6,7,8,9,4]
# print (contar_pares(array))  

def contar_pares(lista):
    # Caso base: lista vacía
    if len(lista)== 0:
        return 0
    
    # Caso recursivo
    if lista[0] % 2 == 0:
        # Sumo 1 si el primer elemento es par y sigo con el resto
        return 1 + contar_pares(lista[1:])
    else:
        # Si no es par, no sumo y sigo con el resto
        return contar_pares(lista[1:])

# Prueba
array = [2,4,5,7,8,9,11,12,14,15,17,20]
print(contar_pares(array))
