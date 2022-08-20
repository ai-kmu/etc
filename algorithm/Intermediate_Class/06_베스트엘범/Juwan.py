from collections import defaultdict
def solution(genres, plays):
    
    
    triple = []
    
    nums = defaultdict(lambda : 0)
    count = defaultdict(lambda : 0)
    
    for idx, (i, j) in enumerate(zip(genres, plays)):
        triple.append([idx, i, j])
        
    # [[0, 'classic', 800], [1, 'pop', 600], [2, 'classic', 500], [3, 'classic', 500], [4, 'pop', 2500]]
    # 각 원래의 Index와 장르, 횟수를 한번에 담는 triple 리스트
        
    for i in triple:
        idx, g, p = i
        nums[g] += p
    
    nums = dict(sorted(nums.items(), key = lambda item: item[1], reverse = True))
    # {'pop': 3100, 'classic': 1800}
    # 각 장르당 얼만큼 총 실행되었는 지를 담고 있는 nums
    
    triple.sort(key = lambda x: x[2], reverse = True)
    # 먼저 Triple 리스트에서 횟수를 기준으로 정렬
    # [[4, 'pop', 2500], [0, 'classic', 800], [1, 'pop', 600], [2, 'classic', 500], [3, 'classic', 500]]
    triple.sort(key = lambda x: nums[x[1]], reverse = True)
    # 그 다음 재생된 횟수를 기준으로 정렬
    # [[4, 'pop', 2500], [1, 'pop', 600], [0, 'classic', 800], [2, 'classic', 500], [3, 'classic', 500]]

    ans = []
    for i in triple:
        a, b, c = i
        if count[b] < 2:
            count[b] += 1
            ans.append(a)
    # [[4, 'pop', 2500], [1, 'pop', 600], [0, 'classic', 800], [2, 'classic', 500], [3, 'classic', 500]]
    # 에서 각 장르별로 최대 2번씩 뽑음.
    return ans
