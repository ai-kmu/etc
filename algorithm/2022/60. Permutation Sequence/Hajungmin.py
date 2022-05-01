import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        # 숫자들을 리스트로 선언
        nums = [i for i in range(1,n+1)]
        ans = ''
        
        # 1에서부터 추가할 수 있는 숫자들을 모두 루프를 통해 돔
        for i in range(1, n+1):
            index = 0
            # 현재 시점에서 만들 수 있는 경우의 수를 저장하는 cnt 선언
            # cnt는 현재까지 사용한 숫자를 제외한 숫자들의 팩토리얼 값과 같음
            cnt = math.factorial(n-i)
            
            # 예를 들어 n=3, k=3인 경우를 생각하면
            # k가 cnt보다 크다는 뜻은 [1,x,x] 인 총 경우의 수가 2가지인데
            # cnt는 2이고 k는 3이기 때문에 [1,x,x]인 경우는 아니라는 뜻
            # 즉, [2,x,x]에서 다시 찾아야해서 index를 1 늘린다.
            # 이렇게 k가 cnt보다 클 때의 index값을 찾아서 ans에 추가시켜주고 
            # 해당 index의 숫자는 사용했기 때문에 del을 사용하여 리스트에서 없애준다.
            while k > cnt:
                index += 1
                k -= cnt
                
            ans += str(nums[index])
            del nums[index]
            
        return ans
