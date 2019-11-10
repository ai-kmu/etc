# 시간 초과. 문제가 굉장히 안좋음. 조건 불분명.

#앞에서부터 시작
def front_start(start_str, correct_str, C):
    curr_str = start_str
    # reverse할 string의 시작 인덱스
    i = 0
    # reverse할 string의 끝 인덱스
    j = i+1
    # 몇번 바꿨는지.
    count = 0
    # 총 cost가 얼마나 들었는지
    cost = 0
    # reverse한 index의 시작과 끝이 들어있는 list
    answer_list = []
    while j < len(curr_str):

        count += 1
        # i와 j의 숫자가 같을 경우 바꿀 필요가 없다.
        if curr_str[i] == curr_str[j]:
            j += 1
            if j == len(curr_str):
                return count-1, cost, answer_list
            # i, i+1, j가 같을 경우 바꿀 필요가 없다.
            elif curr_str[i] == curr_str[j]:
                i += 1
                j += 1
        # curr가 122, correct가 221 일때
        elif curr_str[i:j+2][::-1] == correct_str[i:j+2] and j < len(curr_str)-1:
            j += 1
        # i,j구간만 reverse하기
        curr_str = curr_str[0:i] + curr_str[i:j+1][::-1] + curr_str[j+1:]
        # i와 j의 인덱스 append
        answer_list.append((i+1, j+1))
        # cost 더하기
        for char in curr_str[i:j+1]:
            cost += int(char)
        cost += C
        # 다음 i로 업데이트 하기
        if curr_str[:i+1] != correct_str[:i+1]: # 3개 들어서 바꿨는데 i가 back해야할 경우.
            i = i - 1
            j = i + 1
        else:
            i = j
            j = i + 1
        # 현재까지 바꾼 string이 정답인 string과 같다면 i를 굳이 포함시킬 필요가 없음.
        # '11221' '11212' i=2일때 굳이 2를 같이 바꿀 필요가 없음.
        if curr_str[:i+1] == correct_str[:i+1]:
            i += 1
            j += 1
        # 정답과 같으면 멈춤.
        if curr_str == correct_str:
            # print(True)
            break

    return count, cost, answer_list

#뒤에서부터 시작 앞에서 시작한 것과 코드는 같음.
def back_start(start_str, correct_str, C):
    curr_str = start_str
    i = len(start_str) - 1
    j = i-1
    count = 0
    cost = 0
    answer_list = []
    while j >= 0:

        count += 1
        if curr_str[i] == curr_str[j]:
            j -= 1
            if j < 0:
                return count-1, cost, answer_list
            elif curr_str[i] == curr_str[j]:
                i -= 1
                j = i - 1
        elif curr_str[j-1:i+1][::-1] == correct_str[j-1:i+1] and j > 0:
            j -= 1

        curr_str = curr_str[:j] + (curr_str[j:i+1])[::-1] + curr_str[i+1:]
        answer_list.append((j+1, i+1))
        for char in curr_str[j:i+1]:
            cost += int(char)
        cost += C

        if curr_str[i+1:] != correct_str[i+1:]:
            i = i + 1
            j = i - 1
        else:
            i = j
            j = i - 1
        if curr_str[i:] == correct_str[i:]:
            i -=1
            j -=1
        if curr_str == correct_str:
            # print(True)
            break

    return count, cost, answer_list


N, Cost = map(int, input().split())

# 처음 컨테이너
start_str = input()
# 출고할 컨테이너
correct_str = input()

count, cost, candidate_list = front_start(start_str, correct_str, Cost)
count2, cost2, candidate_list2 = back_start(start_str, correct_str, Cost)
if cost > cost2:
    # print('1')
    answer_count = count2
    answer_list = candidate_list2
else:
    # print('2')
    answer_count = count
    answer_list = candidate_list
print(answer_count)
for ele in answer_list:
    print(ele[0], ele[1])


