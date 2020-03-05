def solution(p):
    stack = []
    answer = [i for i in p]

    print(answer)

    for i in range(len(p)):

        if p[i] == "(":
            stack.append("(")

        else:
            if len(stack) == 0:
                answer[i] = "("
            else:
                stack.pop()

    if len(stack) != 0:

        stackSize = len(stack) // 2 + 1

        while (stackSize):

            for i in range(len(answer)):
                if answer[len(answer) - i - 1] == "(":
                    answer[len(answer) - i - 1] = ")"
                    stackSize -= 1
                    if stackSize == 0:
                        break


    return ''.join(answer)



