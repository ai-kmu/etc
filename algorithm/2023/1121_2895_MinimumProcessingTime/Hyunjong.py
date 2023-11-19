class Solution:
    def minProcessingTime(self, processor_times: List[int], tasks: List[int]) -> int:
        task_index = 0
        processing_times = []
        processor_times.sort()
        tasks.sort(reverse=True)
        for processor_time in processor_times:
            processing_times.append(processor_time + tasks[task_index])
            task_index += 4
        return max(processing_times)
