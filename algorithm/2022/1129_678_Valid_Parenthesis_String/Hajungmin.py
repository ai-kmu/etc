class Solution:
    def checkValidString(self, s: str) -> bool:
        # *을 처리할 때 (로 처리하는 left max, )로 처리하는 left min
        # 각 변수는 (의 개수를 나타냄
        left_min = 0
        left_max = 0
        
        for char in s:
            # 만약 (라면 left min과 max 둘 다 1 더해주고 
            # ) 라면 둘 다 1씩 빼줌
            if char == "(":
                left_min += 1
                left_max += 1
                
            elif char == ")":
                left_min -= 1
                left_max -= 1
                
            # *은 (,),공백으로 대체될 수 있어서 여기서 min과 max를 다르게 계산
            else:
                left_min -= 1
                left_max += 1
            
            # max는 (를 최대한으로 계산하는 것(*을 전부 (로 취급)이기 때문에 0 이하가 나오면 pair가 안맞는 것
            # 따라서 False 반환
            if left_max < 0:
                return False
            
            # )의 개수가 (보다 많은 경우는 위에서 예외 처리를 해주었기 때문에
            # 여기서 left min이 0보다 작게 나오는 경우는 *을 )로 처리해준 경우 쌍이 안 맞을 때이다
            # 그런데 *은 공백 처리가 가능하기 때문에 max()를 사용해서 *을 모두 공백으로 처리한다
            left_min = max(left_min, 0)
        
        return left_min == 0
