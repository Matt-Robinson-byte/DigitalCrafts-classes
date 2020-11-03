nums = [1,2,3,4,5,6]
target = 9
def twoSum():
    for i in nums:
            for j in nums:
                if i+j == target:
                    return nums.index(i), nums.index(j)
                    return i, j

print(twoSum())      
