class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        '''
        팩토리얼 계산을 통해 숫자 하나마다의 인덱스를 구해서 맞는 순서의 리스트를 만든다.
        n = 4, k = 9 일때, 4! = 24인데 맨 앞자리수에 따라 4개로 나눌 수 있다.
        즉, 맨 앞자리수를 기준으로 1~6 / 7~12 / 13~18 / 19~24의 순서로 나눌 수 있다.
        k = 9이기 때문에 맨 앞자리수는 2로 시작함을 알 수 있고, 해당 수를 num1에 넣고 num2에서 제거한다.
        n = 3이되고, k = 3이 되는데 k = 1일때 까지 위의 과정을 반복한다.
        k = 1 -> num2의 순서를 변경할 필요가 없다.
        즉, k = 1일때 num1 = [2, 3] / num2 = [1, 4]가 되는데 이 둘을 합친 배열이 정답.
        '''
        # n이 주어졌을때 -> (n-1)!을 구하는 함수
        def get_factorial(x):
            ret = 1
            x -= 1
            while x > 1:
                ret *= x
                x -= 1 
            return ret

        result =''
        # num2에서 num1으로 수들을 옮길것이다.
        num1 = list()
        num2 = [i+1 for i in range(n)]
        
        while k > 1:
            # window size와 r, l의 범위 설정
            size = get_factorial(n)
            r = get_factorial(n)
            l = 1
            cnt = 0
            # k의 값이 r과 l사이에 있을때까지 cnt를 증사
            while True:
                if k <= r and k >= l:
                    break
                else:
                    cnt += 1
                    r += size
                    l += size
            # num1에 값을 넣고 num2에서 해당하는 값을 제거
            num1.append(num2[cnt])
            num2.remove(num2[cnt])
            # n과 k 업데이트
            n -= 1
            k -= (cnt*size)
            
        for i in num1 + num2:
            result += str(i)
            
        return result
