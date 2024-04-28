# 2의 거듭제곱을 찾는 문제?
# n을 한자리수로 쪼갠다음 정렬, 이후 2**0부터 2**29를 쪼개서 정렬한 것과 비교
class Solution(object):
    # 4321 -> [1,2,3,4]와 같은 형식으로 리턴
    def get_split_list(self, n):
        split_list = []

        for i in str(n):
            split_list.append(int(i))

        return sorted(split_list)

    def reorderedPowerOf2(self, n):
        n_split = self.get_split_list(n)
        # 2**30 > 10**9이므로 29까지만 진행해도 ok
        for i in range(30):
            if self.get_split_list(2**i) == n_split:
                return True
            
        return False
