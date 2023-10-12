from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # 예외처리: nums 길이를 k로 나눈 나머지가 존재하면 불가능
        if len(nums) % k:
            return False

        # nums 개수 세기 (defaultdict랑 비슷한 형태)
        count = Counter(nums)

        # nums 길이를 k로 나눈 몫만큼 반복해야됨
        for _ in range(len(nums) // k):
            # 현재 갖고 있는 nums 세고
            unique = count.keys()
            # 가장 작은 값을 새로운 consecutive의 시작점으로 삼음
            start = min(unique)
            
            # consecutive는 k만큼 반복되어야 함
            for i in range(k):
                # start + i가 현재 num 값임
                curr = start + i
                # 근데 그게 count에 없으면 안 되는 거임
                if count[curr] <= 0:
                    return False
                # 하나 썼으니까 빼주고
                count[curr] -= 1
                # 만약 다 썼으면 key 삭제
                if count[curr] == 0:
                    del count[curr]
        
        # return False를 마주치지 않고 for문이 다 돌았으면 된 거임
        return True
