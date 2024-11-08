class Solution:
    def isHappy(self, n: int) -> bool:
        # 무한반복이라는 건 기존에 나왔던 숫자가 다시 나온다는 것
        # 따라서 visited로 나왔던 숫자들을 set으로 저장해둠
        visited = set([n])
        
        # happy number인지 확인하기 위해 제곱의 합을 구함
        is_happy = sum(int(i) ** 2 for i in str(n))
        
        # 1이 될 때까지 무한루프
        while is_happy != 1:
            # 만약 기존 숫자가 다시 나오면 실패
            if is_happy in visited:
                return False
            
            # set에 새로운 숫자 추가하고 다시 계산
            visited.add(is_happy)
            is_happy = sum(int(i) ** 2 for i in str(is_happy))
        
        # 1이 돼서 while을 빠져 나오면 햅삐
        return True
