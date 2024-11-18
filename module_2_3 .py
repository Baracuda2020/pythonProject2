#Нули ничто, отрицание недопустимо!
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_elem = 0

while index_elem < len(my_list):
   element = my_list[index_elem]
   index_elem += 1
   if element == 0:
      continue
   elif element < 0:
      break
   else:
      print(element)





