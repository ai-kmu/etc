class Solution:
    def countArrangement(self, n: int) -> int:
        """
        <고려 조건>
        1. n으로 구성된 permutation
            - 생성해놓고 검사 불가능 (TLE, MLE)
            - 백트래킹 구현
        2. 아래의 조건을 만족하는 permutation인지
            1) i % perm[i] == 0
            2) perm[i] % i == 0
        """
        if n < 3:
            return n

        used = [False] * (n + 1)
        self.cnt = 0

        def back(idx):
            # 조건을 만족하는 순열 생성 완료
            if idx > n:
                self.cnt += 1
                return

            # 사용하지 않은 숫자 중 조건 2를 만족하는 숫자로만 순열 생성 시도
            for x in range(1, n+1):
                if not used[x] and (idx % x == 0 or x % idx == 0):
                    used[x] = True
                    back(idx + 1)
                    used[x] = False  # 백트래킹 조건 복원

        back(1)
        return self.cnt
