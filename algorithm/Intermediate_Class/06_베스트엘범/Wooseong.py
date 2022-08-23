import heapq as hq
from collections import defaultdict

def solution(genres, plays):
    # genre_play: 장르 별 총 플레이 수를 계산
    # genre_song: 각 장르에 해당하는 노래의 (플레이 수, 인덱스) 저장
    genre_play = defaultdict(int)
    genre_song = defaultdict(list)
    n = len(genres)
    
    # genre_play와 song 갱신
    for i in range(n):
        genre_play[genres[i]] += plays[i]
        genre_song[genres[i]].append((plays[i], i))
    
    # genre_song의 리스트들을
    # 1. 플레이 적은 순
    # 2. 인덱스 큰 순
    # 으로 정렬함 -> 끝에서부터 pop할 거임
    for song in genre_song:
        genre_song[song].sort(key=lambda x: (x[0], -x[1]))
    
    # genre_play를 총 플레이 수 많은 순으로 정렬함
    genre_play = sorted(genre_play.items(), key=lambda x: -x[1])
    
    answer = []
    # 플레이 수 많은 순으로 불러와서
    for item in genre_play:
        # 장르 받고
        genre = item[0]
        # 해당 장르에 해당하는 곡의 (플레이 수, 인덱스) 리스트 받아서
        songs = genre_song[genre]
        
        cnt = 0
        # 최대 두 개까지만 answer에 추가
        # pop을 이용해서 한 개밖에 없는 경우도 처리
        while (cnt < 2) and songs:
            # 인덱스로 넣음
            answer.append(songs.pop()[1])
            cnt += 1
    
    return answer
