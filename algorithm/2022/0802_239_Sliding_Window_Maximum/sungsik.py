import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 첫 k개를 heap으로 만듦
        heap = [(-num, i) for i, num in enumerate(nums[:k])]
        heapq.heapify(heap)
        
        # heappop을 통해 answer의 첫번째에 저장
        n = len(nums)
        answer = [None] * (n-k+1)
        max_neg_num, max_idx = heapq.heappop(heap)
        answer[0] = -max_neg_num
        
        # window를 이동
        # window는 start부터 end까지
        for end in range(k, n):
            start = end - k + 1
            # end 위치가 최댓값일 경우
            # max_neg_num을 변경
            # 꼭 '>'가 아니라 '>='을 사용해야 max_idx가 변경됨
            '''
                (추가)
                '>'를 써도 정답이 나오는데
                밑에 else에서 처리가 되기 때문
                다만, 최대한 index가 큰 값으로 유지하는 것이 더 효율적이라고 생각
            '''
            if nums[end] >= -max_neg_num:
                max_idx = end
                max_neg_num = -nums[end]
            # end 위치가 최댓값이 아닐 경우
            else:
                # 현재 위치를 heap에 저장
                heapq.heappush(heap, (-nums[end], end))
                # 만약 최댓값이 window에 벗어날 경우
                # window에 벗어나지 않은 값들 중 최댓값을 찾음
                while max_idx < start:
                    max_neg_num, max_idx = heapq.heappop(heap)
            answer[start] = -max_neg_num
            
        return answer
