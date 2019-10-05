def solution(operations):
    answer = []
    for i in operations:
        oper = i.split(" ")
        if oper[0] == "I" :
            answer.append(int(oper[1]))
        elif oper[0] == "D":
            if len(answer) > 0 :
                if oper[1] == "-1":
                    answer.remove(min(answer))
                elif oper[1] == "1":
                    answer.remove(max(answer))
    if len(answer) == 0 :
        return [0,0]
    else:
        return [max(answer),min(answer)]