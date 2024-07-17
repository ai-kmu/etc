from collections import defaultdict as ddict, deque as deq

class Twitter:

    def __init__(self):
        # 빠른 탐색을 위해 set 형식의 dictionary로 follower 관리
        self.following = ddict(set)

        # 최신 거부터 가져오기 위해서 왼쪽에 넣기 위해 deque 사용
        self.posts = deq([])  # (userId, tweetId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 최신 걸 왼쪽에 넣기
        self.posts.appendleft((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # follow하고 있는 애들 가져오고
        target = self.following[userId]
        # 자기자신 추가
        target.add(userId)
        
        feeds = []
        num_feeds = 0
        for u, t in self.posts:
            # post 탐색하면서 userId가 target에 있으면 추가
            if u in target:
                feeds.append(t)
                num_feeds += 1
            # 10개 다 모이면 break
            if num_feeds == 10:
                break
        return feeds

    def follow(self, followerId: int, followeeId: int) -> None:
        # set이니까 add로 팔로워 추가
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # 없는 애를 왜 언팔하는진 모르겠는데 그런 경우도 있더라구요
        # 그래서 일단 있는지 탐색하고나서 remove로 제거
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
