arrangement="()(((()())(())()))(())"

def solution(arrangement):

    answer = 0
    # "(" count : 처음에 쇠막대기 나눌 때 2개로 나눠지고
    #             그 다음부터는 1개씩 나눠진 개수가 늘어나니까 각 쇠막대기의 처음 1개 개수만 따로 계산
    leftCount=0
    #구분하기 쉽게  레이저()를 *로 바꿔줌
    arrangement=arrangement.replace("()","*")

    #"("를 저장할 stack
    stack=[]
    for char in arrangement:
        if char=="(":
            stack.append(char)
            #아까 위에서 말한, 처음 쇠막대기 나눠진 개수 count
            leftCount+=1
        elif char==")":
            stack.pop(0)
        elif char=="*":
            #레이저가 있는 거니까 지금 이어지는 쇠막대기 개수만큼 나눠진 부분을 더해줌(각 쇠막대기 개수당 +1)
            answer+=len(stack)

    #마지막에 각 쇠막대기의 처음 1개 개수 한번에 더해줌
    answer+=leftCount

    return answer
if __name__ == '__main__':
 solution(arrangement)