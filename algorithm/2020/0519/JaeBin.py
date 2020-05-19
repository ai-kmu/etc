# 20. 프로그래머스 - 모의고사

def solution(answers):
    answer = []

    # 1, 2, 3번 수포자들의 규칙을 저장하는 list
    people = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    # 문제 맞힌 수 저장하는 list
    results = []

    # 반복문 돌면서 results list 갱신
    for person in people:
        results.append(sum([cost == person[idx % len(person)] for idx, cost in enumerate(answers)]))

    # 가장 높은 점수 받은 사람 오름차순으로 정렬
    answer = [i for i, res in enumerate(results, 1) if max(results) == res]
    return answer

answers_1 = [1, 2, 3, 4, 5]
answers_2 = [1, 3, 2, 4, 2]

print(solution(answers_1))
print()
print(solution(answers_2))