from collections import deque
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.post_idx = 0
        self.post_dict = defaultdict(list) # key : userId, vlaues : [(tweetId_1, post_idx), ... , (tweetId_n, post_idx)]
        self.follow_dict = defaultdict(set) # key : userId, vlaues : (userId_1, ... ,userId_2)

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        # 버그 방지
        self.follow_dict[userId].add(userId)

        # 최대 10개 까지만 저장, post_idx로 sorting이 가능하도록 설계
        if userId not in self.post_dict.keys():
            self.post_dict[userId] = deque([])  
        self.post_dict[userId].append([tweetId, self.post_idx])
        self.post_idx += 1
        if len(self.post_dict[userId]) > 10:
            self.post_dict[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:

        # 버그방지
        self.follow_dict[userId].add(userId)

        # followee_post_list를 모아 post_idx로 sorting후 return
        followee_post_list = [] # max len : len(num of followee) * 10

        if userId not in self.follow_dict.keys():
            return []
        
        self.follow_dict[userId].add(userId)
        followee_id_list = self.follow_dict[userId]

        for followee_id in followee_id_list:
            followee_post_list.extend(list(self.post_dict[followee_id]))
        followee_post_list.sort(key = lambda x : -x[1])

        n = min(10, len(followee_post_list))

        return [followee_post_list[i][0] for i in range(n)]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        # 버그방지
        self.follow_dict[followerId].add(followerId)
        self.follow_dict[followerId].add(followeeId)

        # follow
        self.follow_dict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        # 버그 방지
        self.follow_dict[followerId].add(followerId)

        # unfollow
        self.follow_dict[followerId].discard(followeeId)

