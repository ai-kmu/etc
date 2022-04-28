# from itertools import permutations
from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # n!개의 permutation
        # 순서대로 sorting하고 k번째 가져오기
        
        # itertool 이용해서 하는 방법 : 엄청 오래 걸림 
        # permu = list(permutations(range(1, n+1)))
        # permu.sort()
        # return ''.join([str(i) for i in permu[k-1]])
    
        # 각 자리당 뒤로 오는 것들이 몇개의 종류로 만들어지는지??
        # 1-n까지 (n-1)!개 -> 첫번째자리에서 생성할 수 있는 수들의 덩어리로 순서를 뽑음
        # 두번째자리에서는 (n-2)!개 -> 반복적으로 수행
        # 나머지로 나눠주면서 남아있는 번호를 계속해서 뽑음
        
        answer = ''
        num_arr = [str(i) for i in range(1, n+1)]
        divide = factorial(n-1)
        for i in range(n-1, 0, -1):
            select = k // divide
            if k % divide == 0: # 0으로 나뉘어지는거면 첫째자리의 마지막 순서이므로 select-1 해줌
                select -= 1
                k = divide
            else:
                k %= divide
            answer += num_arr[select]
            num_arr.pop(select)
            divide //= i
        
        return answer + num_arr[-1] # 마지막에 남은거 더해주기
