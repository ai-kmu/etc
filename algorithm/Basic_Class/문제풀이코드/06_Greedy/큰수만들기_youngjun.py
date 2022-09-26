def solution(number, k):
    stack = []
    
    # 숫자들을 순회하면서
    for i, n in enumerate(number):
        # 숫자를 제거하는 부분, 이전 숫자보다 앞으로 들어올 숫자가 크면 이전 숫자 제거하여 앞쪽에 큰 숫자가 오게 함.
        # 숫자 제거는 k만큼 시행한다.
        # 스택 길이가 0보다 크고, 스택의 마지막 원소가 새로 들어오는 수보다 작고, k가 0보다 크면
        while stack and stack[-1] < n and k > 0:
            # 스택의 마지막 원소를 없애주고
            stack.pop()
            # k에서 1을 빼준다
            k -= 1
        
        # 숫자 제거가 전부 끝나면
        # k가 0이면
        if k == 0:
            # i번째보다 뒤의 숫자들을 전부 stack에 추가하고 break.
            stack += list(number[i:])
            break
        
        # 이런 과정을 거친 후 숫자들을 하나하나 추가한다.
        stack.append(n)
    
    # for문에서 숫자 제거가 전부 안끝난 경우, k개만큼 뒤에서 숫자를 제거한다.
    stack = stack[:-k] if k > 0 else stack
    
    # stack에 있는 원소들을 join하여 정답을 반환한다.
    answer = ''.join(stack)
    
    return answer
