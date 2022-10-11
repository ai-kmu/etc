def solution(numbers, target):
    aws = 0
    
    def dfs(numbers, target, index, calculate):
        nonlocal aws
        
        # 종료 조건
        if index == len(numbers):
            if calculate == target:
                aws += 1
            return
        
        # 탐색, +일때, -일때
        dfs(numbers, target, index+1, calculate+numbers[index])
        dfs(numbers, target, index+1, calculate-numbers[index])
    
    # 탐색 시작
    dfs(numbers, target, 0, 0)
    return aws
