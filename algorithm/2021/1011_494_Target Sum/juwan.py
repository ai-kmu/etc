import collections
def findTargetSumWays(nums, target):
    main_dict = collections.defaultdict(lambda: 0) 
    main_dict[nums[0]] = 1
    main_dict[-nums[0]] += 1
    # 맨 처음 요소값에 +- 값을 counter라는 dict에 저장.
        
    for num in nums[1:]: # 처음 요소를 제외하고 나머지 nums에 있는 요소들에 대해서 for loop를 돌면서 모든 경우의 수를 저장한다.
        new_dict = collections.defaultdict(lambda: 0)
        for value, count in main_dict.items():
            print("value : ", value)
            print("count : ", count)
            print("-------")
            new_dict[value + num] += count # value +, - num은 여러 요소들의 조합으로 이루어지며 중복된 것은 dict 특성상
            new_dict[value - num] += count # 같은 곳을 가르키기 때문에 해당 target에 대한 경우의 수는 통합이 된다.
        print("inner loops ended")
        print("new_dict : ", new_dict)
        print("--------")
        main_dict = new_dict  # 메인 dict를 업데이트하여 이제까지 나온 경우의 수를 저장해준다.
#     print(new)
    return main_dict[target]




