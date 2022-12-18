from collections import defaultdict
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:

        # dictionary를 이용하여 graph를 만들고 탐색
        
        # graph 만들기 part
        # num -> 약수 -> num -> 약수 순으로 탐색 할 수 있게끔 dictionary를 이요앟여 graph를만든다

        # num의 약수
        divisors_dict = defaultdict(set)

        # 해당숫자를 약수로 갖는 num
        num_dict = defaultdict(set)

        # 방문처리를 위한 dict
        visited_dict = defaultdict(int)

        # O(num.length)
        # 모든 nums의 약수찾기 
        for n in nums:
            for i in range(1, int(n**(1/2)) + 1):
                if (n % i == 0):
                    divisors_dict[n].add(i)
                    num_dict[i].add(n)
                    if ( (i**2) != n) : 
                        divisors_dict[n].add(n // i)
                        num_dict[n // i].add(n)
        
        # 탐색 part
        
        answer  = 0
        tmp_answer = 0
        
        # 봣던 num과 봤던 divisors는 탐색하지 않기 위함
        seen_num = set()
        seen_divisors = set()
        
        # 모든 num을 돌아가면서 탐색
        for num in nums:
            
            # 봤던 num은 탐색하지않음
            if num in seen_num:
                continue
            
            tmp_answer = 0
            Q = set([num])
            while Q:
                tmp_num = Q.pop()
                
                # 봤던 num은 탐색하지않음
                if tmp_num in seen_num :
                    continue

                seen_num.add(tmp_num)
                
                # 탐색할때마다 tmp_answer + 1 (연결된곳이 하나 늘은것을 의미)
                tmp_answer += 1

                for i in divisors_dict[tmp_num]:
                    if i == 1:
                        continue
                    if i in seen_divisors:
                        continue
                    # 약수를 갖고있는 num
                    for j in num_dict[i]:
 
                        Q.add(j)
    
                    seen_divisors.add(i)

            # 정답값 갱신
            answer = max(tmp_answer, answer)
        
        return answer
