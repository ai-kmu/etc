import heapq
from typing import List

class Twitter:
    def __init__(self):
        self.user_twits_dict = {}  # {user_id: heap}
        self.following_dict = {}  # {user_id: follower_list}
        self.heap_priority = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_twits_dict:
            self.user_twits_dict[userId] = []

        if len(self.user_twits_dict[userId]) >= 10:
            heapq.heappop(self.user_twits_dict[userId])

        heapq.heappush(self.user_twits_dict[userId], (self.heap_priority, tweetId))
        self.heap_priority += 1

        return None

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = []
        if userId in self.following_dict:
            followers = list(self.following_dict[userId])

        followers.append(userId)

        merged_heap = []
        for following_id in followers:
            if following_id in self.user_twits_dict:
                merged_heap = list(heapq.merge(merged_heap, self.user_twits_dict[following_id]))

        # 작은 순서로 정렬된 결과를 리스트로 변환
        sorted_list = sorted(merged_heap)

        # 리스트를 뒤집어 큰 순서로 정렬
        sorted_list.reverse()

        # 리스트를 10개로 자르기
        sorted_heap_10 = sorted_list[:10]

        # 각 원소의 1번째 element 출력
        result = [elem[1] for elem in sorted_heap_10]

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following_dict:
            self.following_dict[followerId] = set()

        self.following_dict[followerId].add(followeeId)
        return None

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following_dict:
            return None

        self.following_dict[followerId].discard(followeeId)
        return None
