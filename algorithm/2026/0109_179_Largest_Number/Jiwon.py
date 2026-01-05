from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 사전식 정렬로는 큰 수 만들기 불가
        # nums.sort(key=lambda x: str(x), reverse=True)
        # return ''.join(map(str, nums))

        # 별도의 비교함수 생성
        def compare(a, b):
            a, b = str(a), str(b)
            ab = a + b
            ba = b + a
            return -1 if ab > ba else 1 if ab < ba else 0
          
        # sort key를 아까 생성해둔 비교함수로 사용
        nums.sort(key=cmp_to_key(compare))
        # 0으로만 구성된 경우 (ex: tc 232 "00")는 0으로 바꿔서 반환
        if set(nums) == {0}:
            return "0"
        return ''.join(map(str, nums))  # int 말고 str로 반환
