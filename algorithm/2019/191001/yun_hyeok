from collections import deque

# deque는 이 용도가 아니지만...
def solution(operations):
    dq = deque()
    for operation in operations:
        command, operand = operation.split()
        if command == "I":
            dq.append(int(operand))
        elif command == "D":
            if operand == "1":
                if dq:
                    dq.remove(max(dq))
            elif operand == "-1":
                if dq:
                    dq.remove(min(dq))
        else:
            raise ValueError
    if dq:
        return [max(dq), min(dq)]
    else:
        return [0, 0]
