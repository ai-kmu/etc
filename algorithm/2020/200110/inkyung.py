#시간초과 발생함
num = int(input())
lst = list()

for i in range(num):
    num1, num2 = map(int, input().split())
    lst.append(sorted([num1, num2]))
lst.sort()

answer = 0
print(lst)

#f1 = 첫행렬의 첫번재 숫자, f2 = 첫 행렬의 두번째 숫자
f1, f2 = lst[0][0], lst[0][1]
for i in range(1, num):
    s1, s2 = lst[i][0], lst[i][1]
    #첫 번째와 두번째가 겹치지 않을 경우
    if f2 < s1:
        continue
    answer += s2 - s1
    #첫번째와 두번째가 겹치면서 첫번째가 두번째보다 절대적으로 큰 경우
    if f1 >= s1 and f2 >= s2:
        continue
    #첫 번째와 두 번째가 부분적으로 겹치는 경우
    else:
        f1, f2 = f1, s2
        continue
    answer += f2 - f1

print(answer)

