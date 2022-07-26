from collections import defaultdict
def solution(clothes):
    dict = {}
    dict = defaultdict(int)
    for _, srt in clothes:
        dict[srt] += 1
    answer = 1
    for key in dict.keys():
        answer *= (dict[key]+1)
    answer -= 1
    return answer
