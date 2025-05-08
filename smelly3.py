# Inconsistent indentation
def find_max(numbers):
  max_value = numbers[0]
  for i in range(1, len(numbers))
    if numbers[i] > max_value:
      max_value = numbers[i] 
  return max_value

print(find_max([1,8,5,3,7]))


# Missing whitespace
def list_even_numbers(n):
  for number in range(1, n + 1):
    if number % 2 == 0:
      print(number)

# Single-letter variables 
def multiply_matrices(matrix1,matrix2):
  result=[]
  for i in range(len(matrix1)):
    result.append([])
    for j in range(len(matrix2[0])):
      result[i].append(0)
      for k in range(len(matrix1[0])):
        result[i][j]+=matrix1[i][k]*matrix2[k][j]
  return result

