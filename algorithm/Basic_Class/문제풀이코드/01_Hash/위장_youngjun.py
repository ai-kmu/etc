from itertools import combinations

def solution(clothes):
    answer = 0
    store = {c:0 for _, c in clothes}

    for _, c in clothes:
        store[c] += 1
    
    clothes_len = list(store.values())

    for i in range(len(clothes_len)):
        if i == 0:
            for j in range(len(clothes_len)):
                answer += clothes_len[j]
        else:
            combs = list(combinations(clothes_len,i+1))
            for k in range(len(combs)):
                num = 1
                for l in range(i+1):
                    num *= combs[k][l]
                answer += num
                
    return answer
