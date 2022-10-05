# 스택 풀이 - dfs인가?
def solution(numbers, target):
    # 수식을 시작하기 위한 초깃값 0
    # G에는 numbers에서 하나 씩 빼서 만든 중간 수식들의 결괏값
    G = [0]
    
    # numbers에서 하나 씩 빼서
    for n in numbers:
        # 걔를 G의 모든 숫자와 더하거나 빼서 수식을 늘려감
        G = [g + n for g in G] + [g - n for g in G]
    
    # 그 중 target을 셈
    answer = G.count(target)
    return answer


# 그래서 DFS로도 풀었어요
def solution(numbers, target):
    # global 어려워서 편법: list 활용하기
    count = [0]
    n = len(numbers)
    
    def dfs(ind, accum):
        # 종료 조건: 끝까지 탐색했을 때
        if ind == n:
            # 만약 계산 결과가 target과 같다면 count += 1
            if accum == target:
                count[0] += 1
            return
        
        # 더한 거
        dfs(ind + 1, accum + numbers[ind])
        # 뺀 거
        dfs(ind + 1, accum - numbers[ind])
        
    dfs(0, 0)
    return count[0]
        
