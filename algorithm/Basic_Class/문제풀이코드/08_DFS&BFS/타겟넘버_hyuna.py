def solution(numbers, target):
    answer = 0
    
    def dfs(num, idx):
        # 인덱스가 넘버스 수와 같고 합한 값이 타겟과 같다면 답 1 증가
        # 처음 값을 넘겨줄 때 0,0으로 시작하기 때문에 인덱스는 len(numbers)-1이 아니라 len(numbers)까지 해줘야함 
        if idx == len(numbers):
            if num == target:
                nonlocal answer
                answer += 1
            return
        
        # 해당 인덱스의 값을 구해서 다음으로 넘겨줌 
        # 더하고 빼는 두가지의 옵션이 있기때문에 구분해줌 
        temp = numbers[idx]
        dfs(num+temp, idx+1)
        dfs(num-temp, idx+1)
    
    dfs(0, 0)
        
    return answer
