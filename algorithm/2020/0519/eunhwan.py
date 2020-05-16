__author__ = 'JudePark'
__email__ = 'judepark@kookmin.ac.kr'


def solution(answers):
    # pattern 초기화
    p1 = ([1, 2, 3, 4, 5] * (int(len(answers) / 5) + 1))
    p2 = ([2, 1, 2, 3, 2, 4, 2, 5] * (int(len(answers) / 8) + 1))
    p3 = ([3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (int(len(answers) / 10) + 1))

    # 정답 확인 lambda function
    calc = lambda x, y: sum(list(map(lambda x, y: x == y, x, y)))

    # 수포자 1-3 까지의 맞춘 수
    result_list = [calc(p1, answers), calc(p2, answers), calc(p3, answers)]
    
    # 정답 제출 포맷으로 변경
    return [i + 1 for i, result in enumerate(result_list) if max(result_list) == result]
