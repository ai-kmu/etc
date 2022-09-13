from itertools import permutations 

def solution(numbers):
    answer = 0
    nums = []
    
    # numbers 숫자의 개수 만큼 for문을 돌며 permutation을 개수별로 구해준다 
    for i in range(1, len(numbers)+1):
        for each in list(permutations(numbers, i)):
            # 첫번째 자리가 0이 아니고 
            if each[0] != '0':
                # 한자리의 permutation에서 1이 아닌 수를 구해준다
                if not (len(each) == 1 and each[0] == '1'):
                    # 조건에 만족하는 수들을 int로 만들어서 배열에 중복되지 않는 수만 가지고 있는다 
                    num = int(''.join(each))
                    if num not in nums:
                        nums.append(num)
    
    # 중복되지 않는 수로만 이루어진 배열에서 소수를 찾는다 
    for each in nums:
        for i in range(2, each):
            if each % i == 0:
                break
        # for문을 break없이 잘 돌았다면 소수이므로 답에 +1 해준다
        else:  
            answer += 1
            
        
    return answer
