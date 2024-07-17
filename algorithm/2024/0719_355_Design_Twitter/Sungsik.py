class Twitter:

    def __init__(self):
        self.user_ids = dict()
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # tweet을 역순으로 순회하며 post한 사람이 follow했으면 news_feed에 추가
        news_feed = []
        followers = self.user_ids.get(userId, set([userId]))
        for tweet, post_id in self.tweets[::-1]:
            if post_id in followers:
                news_feed.append(tweet)
            if len(news_feed) >= 10:
                return news_feed
        return news_feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_ids[followerId] = self.user_ids.get(followerId, set([followerId]))
        self.user_ids[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_ids[followerId] = self.user_ids.get(followerId, set([followerId]))
        if followeeId in self.user_ids[followerId]:
            self.user_ids[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
