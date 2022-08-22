from collections import defaultdict

def solution(genres, plays):
    answer = []
    hap = []
    
    # genres와 plays를 합친다. 합치지 않으면 정신이 나가버림..
    for index, (i, j) in enumerate(zip(genres, plays)):
        hap.append([index, i, j])
    
    hash = defaultdict(int)
    
    # hap[] = [idx, genre, play]
    for h in hap:
        # 장르별 총 플레이 횟수 구하기
        hash[h[1]] += h[2] 
    
    # 총 플레이 횟수가 큰 장르 내림차순으로 정렬
    sorting_hash = sorted(hash.items(), key = lambda item : -item[1])
    
    # 장르별 2곡 카운트용 cnt
    cnt = 0
    
    # for문으로 순차대로 탐색하기 위해 장르별로 play 내림차순 정렬
    hap.sort(key = lambda x : -x[2])
    
    # 장르별 play 많은 순으로 추가, 2번 추가되면 cnt < 2 조건에 의해 다음 장르로 넘어감.
    for sh in sorting_hash:
        for h in hap: # h[1] = genre
            if h[1] == sh[0]: # hap list genre == (play 많은 순)genre 
                if cnt < 2: 
                    cnt += 1
                    answer.append(h[0])
        # sorting_hash 장르 하나 탐색 끝냈다면, 다음 sorting_hash 장르 탐색을 위한 초기화        
        cnt = 0 

    return answer
                
