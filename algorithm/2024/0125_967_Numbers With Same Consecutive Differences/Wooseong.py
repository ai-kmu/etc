class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # 예외 케이스
        # k == 0이면 11..1부터 99..9 (n자리수)까지 return
        if k == 0:
            return [int("".join([str(i)] * n)) for i in range(1, 10)]

        # list는 call-by-ref니까 알아서 쭉쭉 업데이트 될 것.
        answer = []
        def recursive(remain_digit, number):
            # 더 이상 남은 digit이 없으면 잘 온 거니까 append하고 함수 종료
            if remain_digit == 0:
                answer.append(number)
                return
            
            # 마지막 자리수 받아서
            curr_int = number % 10
            
            # 1. 뒷 자리수가 더 커지는 경우
            if curr_int + k <= 9:
                recursive(remain_digit - 1, number * 10 + curr_int + k)
            
            # 2. 뒷 자리수가 더 작아지는 경우
            if curr_int - k >= 0:
                recursive(remain_digit - 1, number * 10 + curr_int - k)

        # 맨 앞자리수는 1부터 9까지 가능
        # `start`로 이미 한 자리 채웠으니까 remain_digit은 1빼고 시작
        for start in range(1, 10):
            recursive(n - 1, start)

        return answer
