# 앞 단어와 뒤의 단어 중 같은 문자열의 개수를 구하는 함수
def compare(left, right, min_len):
    ans = []
    for idx in range(min_len):
        if left[idx] == right[idx]:
            ans.append(left[idx])
        else:
        # 이거 안해주면 시간초과...
            break
    return len(ans)

def solution(words):
    answer = [0]*len(words)
    sorted_words = sorted(words)
    # 앞 뒤 단어 비교 시작
    for idx in range(0,len(sorted_words)-1):
        left = list(sorted_words[idx])
        right = list(sorted_words[idx+1])
        min_len = min(len(left), len(right))
        cmp = compare(left, right, min_len)
        
        # 같은 문자열의 개수가 단어의 길이와 같을 때
        if cmp == min_len:
            answer[idx] = cmp
            answer[idx+1] = cmp + 1
        else:
            answer[idx] = max(answer[idx], cmp + 1)
            answer[idx+1] = cmp + 1
    
    real_answer = 0
    for _ in answer:
        real_answer += _
            
    return real_answer
