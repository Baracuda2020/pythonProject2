#"Функции в Python. Функция с параметром"

def get_matrix (n, m, value):
   matrix = []
   for row in range(n):
      matrix.append([])
      for column in range(m):
        matrix[row].append(value)
   print(matrix)

result_1 = get_matrix(2,2,10)
result_1 = get_matrix(3,5,42)
result_1 = get_matrix(4,2,13)







