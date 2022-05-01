class Solution:
    def getPermutation(self, n, k):

        # 1부터 n까지 사용할 것
        # str을 return할 거니까 str으로 설정, str엔 pop이 없어서 list 사용
        remain = [str(i) for i in range(1, n+1)]

        # 0!부터 n!까지 memoization
        fact_list = [0 for _ in range(n+1)] # 0! to n!, n+1개
        def factorial(n):
            if n == 0:
                return 1
            elif fact_list[n]:
                return fact_list[n]
            else:
                temp = factorial(n-1) * n
                fact_list[n] = temp
                return temp
        factorial(n)
        fact_list[0] = 1
        print(fact_list)

        # k가 n!이면 남은 n개 거꾸로 return (1)
        if fact_list[-1] == k:
            return ''.join(remain[::-1])
        
        ans = ''    # ans를 위한 빈 str 설정
        k -= 1      # divmod와 list indexing 특징 활용

        # 쓸 게 남아있는 동안 반복
        while remain:
            '''
            (1)이 아니면 최소 하나는 고정시키고
            n-1 개 가지고 반복해야한다.
            즉, (n-1)!으로 나눈 몫(ind)만큼 반복하고
            나머지(k) 만큼 더 진행하면 된다.
            '''

            # 반복할 때, n에 해당하는 건 remain의 길이
            ind, k = divmod(k, fact_list[len(remain)-1])

            # ind만큼 반복했다는 건 ind+1을 고정시키고 k만큼 더 갈 거란 얘기.
            # remain의 0번째 요소가 1이니까 ind번째 요소를 pop하면 ind+1이 나옴
            ans += remain.pop(ind)

        '''
        divmod와 list indexing의 특징
        divmod의 피제수로 -1를 입력하면
        몫은 -1이고 나머지는 (제수-1)이 나온다.
        k -= 1을 안해주면
        k = 0, 즉 "반복하고 끝내기" = "남은 거 거꾸로 return하기"
        를 처리하기가 곤란해지는데
        k -= 1 해주면 "list[-1] = 마지막요소"란 특징을 통해
        끝부터 return = 남은 거 거꾸로 return이 구현된다.
        '''

        return ans
