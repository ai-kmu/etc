class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        smaller = [] # rating의 인덱스 i보다 작은 요소의 개수
        bigger = [] # rating의 인덱스 i보다 큰 요소의 개수
        for i in range(len(rating)):
            bg = 0
            sm = 0
            for j in range(i+1, len(rating)):
                if rating[i] > rating[j]:
                    sm += 1
                if rating[i] < rating[j]:
                    bg += 1
            smaller.append(sm)
            bigger.append(bg)

        ans = 0
        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                if rating[i] > rating[j]:
                    ans += smaller[j]       # i > j > k인 경우가 몇개인지 더해주는 것
                if rating[i] < rating[j]:
                    ans += bigger[j]        # i < j < k인 경우가 몇개인지 더해주는 것
        return ans

