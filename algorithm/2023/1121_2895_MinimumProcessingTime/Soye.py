class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        # 내림차순으로 정렬하여 더 큰 작업을 우선 처리
        tasks.sort(reverse=True)
        
        # 오름차순으로 정렬하여 처리 시간이 적은 프로세서에 작업을 할당
        processorTime.sort()
        
        ans, ind = 0, 0
        
        for i in range(len(processorTime)):
            # 현재 프로세서의 처리 시간을 계산하여 작업 시간을 더함
            current_processing_time = processorTime[i] + tasks[ind]
            
            # 현재 처리 시간이 더 크다면 전체 최소 처리 시간을 업데이트
            ans = max(ans, current_processing_time)
            
            # 정렬된 작업 목록에서 다음 작업으로 이동
            ind += 4
        
        return ans
