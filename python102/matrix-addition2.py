
matrix = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
i = 0
j = 0
result = []
if len(matrix[0]) == len(matrix[1]):
    for number in matrix[i]: 
        result.append(number + matrix[i+1][j])
        j += 1
    print(result)