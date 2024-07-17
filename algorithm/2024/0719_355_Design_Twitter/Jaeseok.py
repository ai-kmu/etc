from collections import defaultdict, deque

class Twitter:

    def __init__(self):
        # user_list : 각 유저와 팔로우 상태를 체크하는 set을 value로 갖는 defaultdict
        # twit_list : 유저의 트윗을 최신 순서가 앞에 위치하도록 트래킹하는 deque
        self.user_list = defaultdict(set)
        self.twit_list = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 최신 트윗이 왼쪽에 위치하도록 appendleft 사용
        self.twit_list.appendleft([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        newsfeed = []
        idx = 0
        # 뉴스피드가 10개가 되거나 혹은 twit_list를 전부 돌 때까지 순회
        while len(newsfeed) < 10 and idx < len(self.twit_list):
            # user 자기 자신의 트윗이거나 user가 팔로우하는 Id인지 체크하고 해당하면 tweetId를 뉴스피드에 추가
            if self.twit_list[idx][0] == userId or self.twit_list[idx][0] in self.user_list[userId]:
                newsfeed.append(self.twit_list[idx][1])
            idx += 1
        
        return newsfeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # 팔로우 상태가 아닌데 언팔로우하는 테스트케이스가 존재하므로 체크하는 if문 추가
        if followeeId in self.user_list[followerId]:
            self.user_list[followerId].remove(followeeId)
