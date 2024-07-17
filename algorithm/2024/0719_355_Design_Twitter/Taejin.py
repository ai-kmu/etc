from collections import defaultdict, deque


class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followees = defaultdict(list)
        self.cnt = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.cnt, tweetId])
        self.cnt += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        newsfeed = self.tweets[userId][::]

        for followee in self.followees[userId]:
            newsfeed += self.tweets[followee]
        
        newsfeed.sort(key = lambda x: -x[0])
        
        return [x[1] for x in newsfeed[:10]]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followees[followerId]:
            self.followees[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
