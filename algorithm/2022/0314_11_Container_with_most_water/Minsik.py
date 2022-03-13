# 풀이 방식
# 왼쪽과 오른쪽의 막대의 길이를 비교하면서 작은 쪽을 움직이면서 면적을 계산해 최대값을 구함
# 왜 작은 쪽을 옮겨야 하나=> 결국 면적의 넓이를 결정하는 높이는 작은 쪽의 높이만큼이기에 이를 움직이면서 계산하면 최대글 구할 수 있음

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        ## 필요 변수 정의
        answer = 0                       # 넓이 초기화
        start, end = 0, len(height) - 1  # 시작점 끝점 설정(-1인 이유는 컴퓨터 index 맞추기 위함)

        ## 종료 조건
        while (start <= end):
            # 직사각형의 넓이 정의 = (start, end의 막대의 높이 중 최소점) * (밑변)
            area = min(height[start], height[end]) * (end-start)
            answer = max(answer, area) # 

            ## 이동조건: 막대의 높이를 결정하는 것 => 왼쪽 오른쪽 중에 막대의 길이가 짧은 것을 기준
            if height[start] > height[end]:  # 막대의 길이가 왼쪽이 크면
                end = end - 1                # 오른쪽의 막대를 이동하면서 크기를 비교
            else:                            # 막대의 길이가 오른쪽이 크면
                start = start + 1            # 왼쪽 막대를 이동하면서 크기를 비교
        return answer 
