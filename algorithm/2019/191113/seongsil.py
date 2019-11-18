from collections import defaultdict

def numSubmatrix(matrix, target):
    res = 0
    row, col = len(matrix), len(matrix[0])
    for k in range(row):
        nums = [0 for _ in range(col)]
        for i in range(k, row):
            for j in range(col):
                nums[j] += matrix[i][j]
            # nums: [0,1,0], [1,2,1], [1,3,1], [1,1,1], [1,2,1], [0,1,0] 
            res += check(nums, target)
    return res
        
def check(nums, target):
    counter, res = defaultdict(int), 0  # defaultdict(<class 'int'>, {})
    counter[0], cum_sum = 1,0  # counter에 {0:1} 추가
    #print("start")
    #print("nums", nums)
    for num in nums:  # cum_sum -> 1,4,5,3,4,1
        cum_sum += num
        res += counter[cum_sum - target]  #앞이랑 똑같으면 합이 0이라는뜻
        #print("cum_sum:", cum_sum)
        counter[cum_sum] += 1
        #print("counter2:" ,counter)
        #print("res:", res)
    return res
    #res : 2 -> 0 -> 0 -> 0 -> 0 -> 2
    
    
    
    
matrix1 = [[0,1,0],[1,1,1],[0,1,0]] 
matrix2 = [[1,-1],[-1,1]]
target = 0

print(numSubmatrix(matrix1,target))
