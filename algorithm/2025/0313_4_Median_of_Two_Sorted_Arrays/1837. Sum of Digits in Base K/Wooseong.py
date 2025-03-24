class Solution:
    def sumBase(self, n: int, k: int) -> int:
        # 이미 10이면 그냥 그대로
        if k == 10:
            base = str(n)
        # 아니라면 바꾸기
        else:
            base = ''
            # divmod 써서 나머지를 앞에 붙이는 방식으로 변경 가능
            while n:
                n, res = divmod(n, k)
                base = str(res) + base
        # 자리수 합 return
        return sum(int(i) for i in base)
