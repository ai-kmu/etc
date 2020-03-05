#괄호 변환(프로그래머스)
#10:50~11:10
#11:10~12:36

input="()))((()"

def check_balancing(str):

    left_parenthesis_count=0
    right_parenthesis_count=0
    u=""
    v=""

    for i in range(0, len(str)):
        if str[i]=="(":
            left_parenthesis_count+=1
        elif str[i]==")":
            right_parenthesis_count+=1

        u+=str[i]

        if left_parenthesis_count==right_parenthesis_count:
            for j in range(i+1,len(str)):
                v+=str[j]
            break

    return u,v

def check_correct(str):
    left_parenthesis_count=0
    right_parenthesis_count=0

    for char in str:
        if char=="(":
            left_parenthesis_count+=1
        elif char==")":
            right_parenthesis_count+=1

        if left_parenthesis_count<right_parenthesis_count:

            return False

    return True


def solution(p):
    answer = ''
    empty=""

    if p=="":
        return ""
    else:
        u,v=check_balancing(p)


        #3
        if check_correct(u):

            new_v=solution(v)
            answer=u+new_v

        #4
        else:

            empty="("
            empty+=solution(v)
            empty+=")"

            #첫번째 문자 제거
            u=u[1:]
            #마지막 문자 제거
            u=u[:-1]



            for char in u:
                if char=="(":
                    empty+=")"
                elif char==")":
                    empty+="("




            answer=empty

    return answer


if __name__ == '__main__':
   print(solution(input))