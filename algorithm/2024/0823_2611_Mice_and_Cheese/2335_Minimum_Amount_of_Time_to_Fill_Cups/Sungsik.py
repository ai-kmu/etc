class Solution:
    def fillCups(self, amount: List[int]) -> int:
        small, mid, large = sorted(amount)
        answer = 0
        while small + mid + large > 0:
            # 만약 mid가 0일경우
            if mid == 0:
                # large만 남아있으므로 이를 다 더한다
                answer += large
                break
            # 그렇지 않을 경우 mid와 large에서 각각 컵을 채운다
            else:
                answer += 1
                mid -= 1
                large -= 1
            small, mid, large = sorted((small, mid, large))
        return answer
