class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # 배열의 모든 요소의 합을 계산
        total = sum(nums)
        # 합을 3으로 나눈 몫(q)과 나머지(r)를 구함
        q, r = divmod(total, 3)
        
        # 나머지가 0이면 전체 합이 3으로 나누어 떨어지므로 반환
        if r == 0:
            return total
        
        # 나머지가 1인 요소를 저장할 리스트
        r1 = []
        # 나머지가 2인 요소를 저장할 리스트
        r2 = []
        
        # 각 요소의 나머지에 따라 리스트에 추가
        for val in nums:
            if val % 3 == 1:
                r1.append(val)
            elif val % 3 == 2:
                r2.append(val)
        
        # 나머지 리스트를 오름차순으로 정렬
        r1.sort()
        r2.sort()
        
        # 나머지가 1인 경우 처리
        if r == 1:
            # r1이 비어있으면 r2에서 두 개의 최소 값을 사용
            if not r1:
                return total - (r2[0] + r2[1])
            # r2가 두 개 이하일 경우 r1에서 최소 값을 사용
            elif len(r2) <= 1:
                return total - (r1[0])
            else:
                # r1과 r2의 최소 값을 비교하여 최소 값을 반환
                pos1 = r1[0]
                pos2 = r2[0] + r2[1]
                return total - min(pos1, pos2)
            
        # 나머지가 2인 경우 처리
        elif r == 2:
            # r2가 비어있으면 r1에서 두 개의 최소 값을 사용
            if not r2:
                return total - (r1[0] + r1[1])
            # r1이 두 개 이하일 경우 r2에서 최소 값을 사용
            elif len(r1) <= 1:
                return total - (r2[0])
            else:
                # r2와 r1의 최소 값을 비교하여 최소 값을 반환
                pos1 = r2[0]
                pos2 = r1[0] + r1[1]
                return total - min(pos1, pos2)
