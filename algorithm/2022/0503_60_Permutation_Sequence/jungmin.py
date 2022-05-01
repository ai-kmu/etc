class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [0] * (n+1)
        factorial[0] = 1
        numset = [0] * n
        ans = ""
        
        for i in range(1,n+1):
            factorial[i] = factorial[i-1] * i # 0 ~ n까지의 factorial 배열 생성
            numset[i-1] = i # n까지의 자연수 배열 생성
        
        '''
        예) n=3, k=3
        1. 각각 수열이 갖는 첫번째 수가 같은 것으로 그룹을 묶으면,
        그룹마다 첫번째 수가 같은 것은 두 가지(fact = (3-1)!)가 있다(123,132/213,231/312,321).
        2. 여기서 k=3이므로 첫번째 숫자는 2이다.
        (--> k-1을 fact로 나눈 몫을 이용해서 어느 숫자가 나와야 하는지 정한다.
        몫이 0이면 k는 첫번째 그룹, 몫이 1이면 k는 두번째 그룹에 속한다는 것이다.)
        3. 그 이후 numset에서 숫자 2를 제거하고 
        그 다음 숫자가 무엇이 나올지 정하기 위해
        첫번째 숫자가 2인 그룹 내에서의 새로운 k를 선언해야 한다.
        (--> k = k % fact)
        4. 그 이후 남은 numset(=[1,3]) 중에서 숫자 무엇을 사용해야 하는지는 
        while을 통해서 다시 1부터 반복적으로 정한다.
        '''
        while(n):
            print("-------------------------")
            fact = factorial[n-1]
            ind = (k-1) // fact # 인덱스이므로 k에서 1을 뺀것을 fact로 나눈 몫이어야 한다.
            ans += str(numset[ind])
            numset.remove(numset[ind])
            n -= 1
            k %= fact 
        return ans
