# 어질어질 구현 실패
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.userId = defaultdict(int)
        self.tweetId = defaultdict(list)
        self.relat = defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetId[userId].append(tweetId)
        print(self.tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        print("관계:", self.relat[userId])
        a = []
        a.append(self.tweetId[userId])
        for i in list(self.relat.keys()):
            if i == userId:
                
                a.append(self.tweetId[self.relat[int(i)][0]])
        return a

    def follow(self, followerId: int, followeeId: int) -> None:
        self.relat[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.relat[followerId].pop()



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
