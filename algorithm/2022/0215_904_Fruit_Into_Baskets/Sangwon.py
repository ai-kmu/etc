class Solution:
    
            
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        l = 0
        ans = 0
        cnt = Counter()
        for r, t in enumerate(fruits):
            cnt[t] += 1 #딕셔너리에 하나씩 추가
            while len(cnt) > 2: #과일 종류가 3가지인 경우
                cnt[fruits[l]] -= 1 #왼쪽 과일의 카운트가 0이 될때까지 -1을 한다.
                if cnt[fruits[l]] == 0: #왼쪽과일 카운트가 0이 될때 pop을 이용하여 왼쪽과일 제거 
                    cnt.pop(fruits[l])
                l += 1 #왼쪽 인덱스를 오른쪽으로 한칸 옮기기 
            ans = max(ans, r - l + 1) #왼쪽과 오른쪽 길이가 제일 크게 차이나야 하므로 max()이용 
        return ans
    
#이문제는 sliding window알고리즘이다. 
#왼쪽 인덱스와 오른쪽 인덱스를 가장 크게 차이나는 것 이 목표이다.
#과일을 2가지만 담을 수 있으며, 한 번 시작하면 fruits가 끝나거나 제3의 과일이 나올 때까지 멈출 수 없다. 
'''
예시)
fruits = [1,2,3,2,2]인 경우

cnt = Counter{1:1, 2:1}이 되다가
cnt = Counter{1:1, 2:1, 3:1}이 되는 순간

{1:1-1, 2:1, 3:1}을 하여 1을 pop()하고 
{2:1, 3:1}로 만든다.
l은 +1을 하여 2를 가리키고 있다. 
'''
