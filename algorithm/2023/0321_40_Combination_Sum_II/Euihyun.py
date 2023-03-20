class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        answer = []
        n = len(candidates)
        
        def back(idx, lst, nums):
            # 들어온 값이 같으면 list를 추가하고 return
            if nums == target:
                answer.append(lst)
                return
            
            for i in range(idx,n):
                # 한번만 사용 가능하기 때문에 중복방지
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                
                # 타겟값을 넘으면 탈출
                if nums + candidates[i] > target:
                    break
                
                # 정답용 list 채우고 새로운 숫자 넣어서 target 값과 비교
                back(i+1, lst+[candidates[i]], nums+candidates[i])
        
        back(0,[],0)
        
        return answer
