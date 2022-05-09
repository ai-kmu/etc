class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = copy.deepcopy(triangle) # 합친 결과를 저장할 ans는 triangle을 deepcopy
        if len(triangle) == 1: # triangle이 요소 하나이면은 그 값 그대로 출력
            return triangle[0][0]
        
        for i, row in enumerate(triangle):
            for j, v in enumerate(row):
                if i == 0: # triangle에서 첫번째 줄은 값 하나이므로 ans에 그대로 저장
                    ans[i][j] = triangle[i][j]
                    continue  
                if j == 0: # 첫번째 요소는 전 줄의 첫 요소와 합한 결과를 ans에 저장
                    ans[i][j] = ans[i-1][0] + triangle[i][j]
                elif j == (len(row)-1): # 마지막 요소는 전 줄의 마지막 요소와 합한 결과를 ans에 저장
                    ans[i][j] = ans[i-1][-1] + triangle[i][j]
                else: # 그 외 인덱스를 갖는 요소는 전 줄의 인접한 인덱스의 값과 합한 두개의 값 중 작은 것을 선택하여 ans에 저장
                    ans[i][j] = min(ans[i-1][j-1] + triangle[i][j], ans[i-1][j] + triangle[i][j])     
        return min(ans[-1]) # 결국 ans의 마지막 줄의 값들 중 최소값을 정하면 된다.
