"""
    baseline을 설정해놓고 이 baseline을 올리며 이 위로 몇개의 음식이 있는지를 셈
"""

def solution(food_times, k):
    base_line = 0   # 초기 base_line
    food_length = len(food_times) # 배열 길이
    initial_food_length = food_length # 배열 길이(변하지 않음)
    arr= sorted(food_times)

    idx = 0
    while True:
        minus = food_length * (arr[idx] - base_line) # 몇을 빼줄 것인지
        
        if k < minus: # 마지막 부분
            base_line += k//food_length
            k %=food_length
            
            for i in range(initial_food_length):
                if food_times[i] > base_line:
                    k-=1
                if k <0:
                    return i + 1

        base_line = arr[idx]
        while True:
            idx+=1
            if idx == initial_food_length:
                return -1
            if arr[idx] != arr[idx - 1]:
                break
        food_length = (initial_food_length-idx)
        k-=minus

for i in range(40,60):
    print( i , ": " ,solution([7, 7, 10,10,10,10], i))
