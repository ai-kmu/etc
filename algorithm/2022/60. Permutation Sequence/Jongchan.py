'''
  ex) n=3, k=4 -> 2!x2 -> 231 -> n자리 1개 올라감, 나머지 거꾸로
'''
class Solution:
    def fct(self, i): # 펙토리얼 계산 함수
        n = 1
        for k in range(1, i + 1):
            n *= k
        
        return n
    
    def getPermutation(self, n: int, k: int) -> str:
        factorials = {}
        
        if k == self.fct(n): # 만약 k가 n! 이면 -> 예외처리
            s = ""
            for j in range(0,n):
                s += str(n-j)
            return s
        
        i = n-1
        while k : # 팩토리얼의 개수를 세어줌
            ft = self.fct(i)
            while k - ft >= 0:
                k -= ft
                if i in factorials:
                    factorials[i] += 1
                else:
                    factorials[i] = 1
                
            i -= 1
        
        nums=[x for x in range(1,n+1)] # 1 ~ n 까지 숫자 리스트
        
        s = ""
        
        i = n-1
        while i: # 팩토리얼의 개수를 바탕으로 추론
            if i in factorials:
                if len(factorials) > 1:
                    s += str(nums[factorials[next(iter(factorials))]])

                    del nums[factorials[next(iter(factorials))]]
                    del factorials[next(iter(factorials))]
                else:
                    if next(iter(factorials)) == 1:
                        for x in nums:
                            s += str(x)
                        del factorials[next(iter(factorials))]
                        break;
                    else:
                        s += str(nums[factorials[next(iter(factorials))]-1])
                        del nums[factorials[next(iter(factorials))]-1]
                        for x in nums[::-1]:
                            s += str(x)
                        break;
            else:
                s += str(nums[0])
                del nums[0]
            i-=1
            
        return s
