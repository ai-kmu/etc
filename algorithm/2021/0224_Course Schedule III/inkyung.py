class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        힙 = 트리 구조로 수의 집합에서 가장 작은 수나 가장 큰 수만을 자주 꺼내올때 유용한 자료 구조
        """
        if courses == None or len(courses) == 0:
            return 0
        
        courses.sort(key = lambda x: x[1])
        print(courses)
        curr_time = count = 0
        max_heap = []
        heapify(max_heap)
		
        for i in range(len(courses)):
            heappush(max_heap, -1 * courses[i][0])
            curr_time += courses[i][0]
            count += 1
            
            if  curr_time > courses[i][1] :
                curr_time += heappop(max_heap)
                count -= 1
            print(curr_time)
        return count
        
