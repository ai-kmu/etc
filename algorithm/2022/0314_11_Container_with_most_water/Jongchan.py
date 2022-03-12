class Solution:
    def maxArea(self, height: List[int]) -> int:
        a=0
        
        # 처음과 마지막 막대로 부터 시작해 범위를 좁혀가며 막대를 찾는다.
        # a에 넓이의 max값을 저장하고, 현재의 넓이와 a 값을 비교해 더 큰값을 다시 a에 대입한다.
        # 이때 left와 right 중 작은 막대를 이동시킨다.
        # 넓이는 길이와 높이 두가지 요소를 고려해야하는데, 최대 길이로 시작하기 때문에 높이만 고려하면 되게된다.
        
        left=0 # 처음막대
        right=len(height)-1 # 마지막 막대
        
        for i in range(len(height)-1):
            tmp_a=abs(right-left)*min(height[left],height[right]) # 현재 선택된 left, right 막대로 구한 넓이
            if tmp_a>a:
                a=tmp_a # 이전 값보다 크면 업데이트
                
            if height[left]>height[right]: # 작은 막대쪽을 이동
                right-=1
            else:
                left+=1

        return a
