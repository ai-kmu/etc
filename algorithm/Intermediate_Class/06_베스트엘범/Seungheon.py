from collections import defaultdict
def solution(genres, plays):
    
    # 장르마다 재생된 
    gen_count_dict = defaultdict(int)
    # album에 담긴 수 count
    alubm_genre_count = defaultdict(int)
    
    # 재생횟수 세기
    for i, genre in enumerate(genres):
        gen_count_dict[genre] += plays[i]
    
    # 엘범 list 만들기
    album_list = []
    for i, play in enumerate(plays):
        g_idx = gen_count_dict[genres[i]]
        album_list.append([g_idx, play, i])
    
    # 정렬하고, 2개이하씩 answer에 담기
    answer = []
    for genre, play, idx in sorted(album_list, key = lambda x : (-x[0], -x[1], x[2])):
        if alubm_genre_count[genre] < 2:
            alubm_genre_count[genre] += 1
            answer.append(idx)
    
    return answer
