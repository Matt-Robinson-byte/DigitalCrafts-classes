vector_one = [1,2,3]
vector_two = [4,5,6]
mult_vector = []
i = 0
while i < len(vector_two):
    mult_vector.append(vector_one[i]*vector_two[i])
    i += 1
print(mult_vector)
