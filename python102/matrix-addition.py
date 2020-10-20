matrix = [[1,2,3],
[4,5,6]]
i = 0
j = 0
result = []
for number in matrix[i]: 
    result.append(number + matrix[i+1][j])
    j += 1
print(result)
        

