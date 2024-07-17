from collections import defaultdict

class Twitter(object):
    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = []
        
    def postTweet(self, userId, tweetId):
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId):
        aws = []
        # 최근 트윗부터 확인
        for user, tweetId in reversed(self.tweets):
            #  트윗의 작성자가 본인이거나 팔로우 사람인 경우
            if user == userId or user in self.users[userId]:
                # 트윗 ID를 결과 리스트에 추가
                aws.append(tweetId)
        # 최근 10개만 반환
        return aws[:10]

    def follow(self, followerId, followeeId):
        if followeeId not in self.users[followerId]:
            self.users[followerId].add(followeeId)
        
    def unfollow(self, followerId, followeeId):
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
