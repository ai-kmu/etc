def solution(numbers, target):
    # 깊이 우선으로 도는 재귀들 호출
    def dfs(numbers, num, target):
        # 종료 조건. 길이가 1일 때
        if not numbers:
            if num == target:
                return 1
            return 0
        # 나머지
        sum = 0
        sum += dfs(numbers[1:], num + numbers[0], target)
        sum += dfs(numbers[1:], num - numbers[0], target)
        return sum
    answer = dfs(numbers, 0, target)
    return answer
