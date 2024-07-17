import heapq

class Twitter:
    def __init__(self):
        # 현재 타임스탬프를 0으로 초기화
        self.time = 0
        # 각 사용자의 트윗을 저장하는 딕셔너리. 
        # key -> 사용자 ID
        # value -> (타임스탬프, 트윗 ID)의 리스트
        self.user_tweets = {}
        # 팔로우 관계를 저장하는 딕셔너리. 
        # key -> 팔로워 ID 
        # value -> 팔로이 ID의 리스트
        self.followees = {}
    
    def postTweet(self, userId, tweetId):
        # 새로운 트윗을 게시할 때마다 타임스탬프를 증가
        self.time += 1
        # 해당 사용자가 처음 트윗하는 경우, 빈 리스트를 줘서 리스트를 만들어줌
        if userId not in self.user_tweets:
            self.user_tweets[userId] = []
        # (타임스탬프, 트윗 ID)를 리스트에 추가
        self.user_tweets[userId].append((self.time, tweetId))
    
    def getNewsFeed(self, userId):
        # 최근 트윗을 저장하기 위한 힙 리스트 구성
        heap = []
        
        # 현재 사용자와 팔로우한 사용자의 트윗을 가져옴
        users = set()
        users.add(userId)
        if userId in self.followees:
            for followee in self.followees[userId]:
                users.add(followee)
        
        # 각 사용자의 최근 10개 트윗을 가져와서 힙에 추가
        for user in users:
            if user in self.user_tweets:
                for tweet in self.user_tweets[user][-10:]:
                    heapq.heappush(heap, tweet)
                    if len(heap) > 10:
                        heapq.heappop(heap)
        
        # 힙에서 트윗 ID를 시간 역순으로 정렬하여 최신 순서로 맞춰서 순서를 반환
        heap.sort(reverse=True)
        result = []
        for time, tweetId in heap:
            result.append(tweetId)
        return result
    
    def follow(self, followerId, followeeId):
        # 팔로워가 팔로우할 때, 팔로우 관계가 존재하지 않으면 초기화 시켜줌
        if followerId not in self.followees:
            self.followees[followerId] = set()
        # 팔로이 ID를 팔로워의 팔로우 집합에 추가
        self.followees[followerId].add(followeeId)
    
    def unfollow(self, followerId, followeeId):
        # 만약 팔로우 관계가 존재하면 언팔
        if followerId in self.followees:
            if followeeId in self.followees[followerId]:
                self.followees[followerId].remove(followeeId)
