def solution(number, k):
    # 처음에 number의 첫 숫자를 넣는다.
    stack = [number[0]]
    # 그 뒤에 for문을 돌면서 greedy하게 찾는다.
    for num in number[1:]:
        # stack이 존재하고, stack의 마지막 숫자가 num보다 크고, k 이상일 때
        # 마지막 원소를 뺀다.
        while len(stack)>0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        # 모든 원소는 무조건 append한다. 
        stack.append(num)
    
    # k가 0이 아니라면 stack에서 앞에서부터 k개를 뽑는다.
    if k!=0:
        stack = stack[:-k]
    return "".join(stack)
