from collections import defaultdict
from typing import List

class Twitter:
    def __init__(self):
        self.user_follows = defaultdict(set)
        self.user_tweets = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 트윗 ID와 타임스탬프를 사용자의 트윗 목록에 추가
        self.user_tweets[userId].add((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # 사용자가 자신의 트윗을 볼 수 있도록 자신을 팔로우하게 설정
        if userId not in self.user_follows[userId]:
            self.user_follows[userId].add(userId)

        # 사용자가 팔로우하는 모든 사용자의 트윗을 수집
        result = []
        for followeeId in self.user_follows[userId]:
            for tweet, time in self.user_tweets[followeeId]:
                result.append((tweet, time))

        # 수집한 트윗을 타임스탬프를 기준으로 정렬 (최신순)
        result.sort(key=lambda data: data[1], reverse=True)

        # 가장 최근의 10개의 트윗 ID를 반환
        return [tweet for tweet, _ in result][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        # 팔로워가 팔로우하는 사용자 목록에 팔로이를 추가
        self.user_follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # 팔로워가 팔로우하는 사용자 목록에서 팔로이를 제거
        if followeeId in self.user_follows[followerId]:
            self.user_follows[followerId].remove(followeeId)
