# Funcion que recibe por parametro dos lista y devuelve una ordenada
def merge (arr1,arr2):
  result = [] #Lista donde se almacena el resultado de la fusion
  i, j = 0, 0 # Valores inciales para los indices de cada una de las listas

  # Se ejecuta un bucle mientras haya elementos en ambas listas (arr1 y arr2).
  # Compara los elementos actuales de ambas listas y agrega el elemento más pequeño al resultado. Luego, incrementa el índice correspondiente.
  while i < len (arr1) and j < len (arr2):
    if arr1[i] < arr2[j]:
      result.append(arr1[i])
      i += 1
    else:
      result.append(arr2[j])
      j += 1
  
  #Después de salir del bucle, verifica si alguna de las listas aún tiene elementos sin procesar.
  #Si hay elementos restantes en arr1, agrégales al resultado.
  #Si hay elementos restantes en arr2, agrégales al resultado
  if i == len(arr1):
    for k in range(j, len(arr2)):
      result.append(arr2[k])

  if j == len(arr2):
    for k in range(i, len(arr1)):
      result.append(arr1[k])

  return result       

# Funcion que divide recursivamente una lista en mas sublistas y realiza el ordenamiento a medida que se llama al a funcion merge y ordena dos listas
def merge_sort (arr):

  # Si la longitud de la lista es menor de dos elementos, quiere decir que ya esta ordenada
  if len(arr) < 2:
    return arr
  # En caso contrario, si la lista posee mas de dos elementos se la divide recursivamente
  else:
    #
    middle = len(arr)//2
    #Llama recursivamente a merge_sort para ordenar la primera mitad de la lista original.
    arr1 = merge_sort(arr[:middle])
    #Llama recursivamente a merge_sort para ordenar la segunda mitad de la lista original.
    arr2 = merge_sort(arr[middle:])
    #Toma las sublistas ordenadas arr1 y arr2 y devuelve la lista resultante de la fusión de ambas sublistas en orden.
    return merge(arr1,arr2)
  

unsorted_list = [24, 4, 2, 7, 1, 9, 5, 2, 10, 22, 12, 8]
sorted_list = merge_sort(unsorted_list)


print("Lista Desordenada")
print(unsorted_list)
print("Lista Ordenada")
print(sorted_list)
  