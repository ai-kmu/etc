def solution(arr):
    # This stack is stored the index if we meet '('
    start_stack = []
    answer = 0
    
    for i in range(len(arr)):
        if arr[i] == '(':
            start_stack.append(i)
            
        # if we meet ')'
        else:
            diff = i - start_stack.pop()
            # Laser shot
            if diff == 1:
                answer += len(start_stack)
            # the rest pip    
            else:
                answer += 1
                
    return answer
