import math
def solution(distance, rocks, n):
    
    rocks.sort()
    rocks.append(distance)
    
    min_, max_ = 0, distance
    
    answer = 0
    while min_ <= max_:

        prev = 0
        mins = distance

        count = 0

        criterion = (min_ + max_) // 2
        
        for rock in rocks:
            if rock - prev < criterion:
                count += 1
            else:
                mins = min(mins, rock -  prev)
                prev = rock
  
        if count > n:
            max_ = criterion -1   
            

        else:
            answer = mins 
            min_ = criterion + 1     
    return answer

distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(solution(distance, rocks, n))
