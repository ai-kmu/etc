# 솔루션 참고 했습니다.
class Twitter:

    def __init__(self):
        # 사용자의 팔로우 관계를 저장할 딕셔너리. 각 사용자는 여러 사용자 팔로우 가능
        self.follows = collections.defaultdict(set)
        # 트윗을 저장할 힙 (최소 힙)
        self.heap = []
        heapq.heapify(self.heap)
        # 트윗의 타임스탬프를 기록할 변수
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # 사용자가 아직 팔로우 관계에 없으면 자기 자신을 팔로우하도록 추가
        if userId not in self.follows:
            self.follows[userId].add(userId)

        # 트윗을 게시할 때마다 타임스탬프 증가
        self.time += 1
        # 힙에 트윗을 추가. 타임스탬프를 음수로 저장하여 최신 트윗이 먼저 나오도록
        heapq.heappush(self.heap, [-1 * self.time, userId, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # 사용자가 팔로우하는 사용자의 집합을 가져옴
        feed = self.follows[userId]

        # 타임스탬프 증가
        self.time += 1

        count = 0  # 가져올 트윗 수를 카운트하는 변수
        res = []  # 결과로 반환할 트윗 ID 리스트
        q = deque()  # 힙에서 잠시 꺼낸 트윗을 저장할 큐

        while count < 10 and self.heap:
            timer, userId, tweetId = heapq.heappop(self.heap)

            # 팔로우하는 사용자의 트윗인지 확인
            if userId in feed:
                count += 1
                res.append(tweetId)

            q.append([timer, userId, tweetId])

        # 큐에 있는 트윗을 다시 힙에 넣음
        while q:
            heapq.heappush(self.heap, q.popleft())

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # 팔로우 관계 추가
        self.follows[followerId].add(followeeId)
        # 팔로우하는 사용자가 팔로우 관계에 없으면 자기 자신을 팔로우하도록 추가
        if followeeId not in self.follows:
            self.follows[followeeId].add(followeeId)
        # 타임스탬프 증가
        self.time += 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # 타임스탬프 증가
        self.time += 1

        # 언팔로우하는 사용자가 팔로우 관계에 있으면 제거
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
