#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from itertools import permutations
import math
def solution(numbers):
    answer = 0
    num_list = []
    # i로 나누어 떨어지는 경우에 대한 함수를 만듭니다.
    # i로 나누어 떨어지면 소수가 아니므로 False 리턴
    def is_prime_num(n):
        for i in range(2, n):
            if n % i == 0:
                return False 

        return True
    
    # numbers의 숫자를 문자열로 받아와 조합해줄 준비를 합니다.
    len_check = len(numbers)
    numbers = list(map(str,numbers))
    num_list = list(map(str,numbers))
    ans_list = []
    
    # ans_list에 numlist가 없는 경우 추가해줍니다.
    for i in range(len(num_list)):
        if num_list[i] not in ans_list:
            ans_list.append(num_list[i])
        
    sum = ''
    
    # permutations를 통해 모든 조합을 넣어주었습니다.
    for length in range(2,len(num_list)+1):
        for perm in list(permutations(numbers,length)):
            for j in range(len(perm)):
                sum = sum + str(perm[j])
            if sum not in ans_list:
                ans_list.append(sum)
            sum = ''
    
    ans_list = list(map(int,ans_list))
    ans_list = list(set(ans_list))
    
    # 마지막으로 소수의 갯수를 구해주었습니다.
    # 모든 조합에 대한 숫자이면서 is_prime_num 을 통과하는지 확인해주었습니다.
    for i in range(len(ans_list)):
        if ans_list[i] >= 2 and is_prime_num(int(ans_list[i])) == True:
            answer = answer + 1
    
    
    return answer

