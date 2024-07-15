class Twitter:
    def __init__(self):
        self.user = [list() for _ in range(501)]  # Each dict: list([tweetId, time], []...)
        self.following = [list() for _ in range(501)]  # ex) user 1 follows user 2,3: self.following[1]=[2,3]
        self.time = 0  # current time for Twitter objecct

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user[userId].append([tweetId, self.time])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        from copy import deepcopy
        feed_list = deepcopy(self.user[userId])
        for followeeId in self.following[userId]:
            feed_list.extend(self.user[followeeId])
        feed_list.sort(key = lambda x: -x[1])  # sort by time 
        only_feed = list()
        for i in feed_list[:10]:
            only_feed.append(i[0])
        return only_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
