class Twitter:

    def __init__(self):
        self.time = 0  # check time of tweet object
        self.tweet = defaultdict(list)
        self.followlist = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([tweetId, self.time])  # record the time of tweet upload
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        # collecting tweets for the user's feed
        feed.extend(self.tweet[userId])
        for followee in self.followlist[userId]:
            feed.extend(self.tweet[followee])

        newsfeed = [tweetId for tweetId, _ in heapq.nsmallest(10, feed, key=lambda x: x[1])]

        return newsfeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followlist[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followlist[followerId].discard(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
