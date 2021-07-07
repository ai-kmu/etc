class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        done = set()  ## 가본 적 있는 곳
        ans = 0 ## 반복 횟수(정답값)
        for i in forbidden: ## 방해물도 가본 적 있는 곳으로 취급
            done.add((i, True)) ## true는 앞으로 가서 위치한 곳
            done.add((i, False)) ## false는 뒤로 가서 위치한 곳
        
        done.add((0,True)) ## 초기 시작위치
        q = set() ##  현재 위치할수 있는 곳
        q.add((0, True)) ## 초기 시작위치
        max_done = max(x, max(forbidden))+ a + b ## bug가 갈 수 있는 최대 값 (설정안하면 무한대로 발산할 수도 있음)
        while(q): ## 현재 위치 할 수 있는 모든 정보
            new_q = set() ## 1차례 미래에서 위치할 수 있는 모든 정보
            for pos, can_back in q: ## pos는 위치값, can_back은 뒤로 갈수 있는지 판단용
                if pos == x: ## 현재 위치가 목표 값이면 정답
                    return ans
                if pos+a <= max_done and (pos+a, True) not in done: ##앞으로 갈 수 있을 때
                    done.add((pos+a, True)) ## 가본 적 있다고 저장
                    new_q.add((pos+a, True)) ## 미래에 위치할 수 있다고 저장
                if not can_back: ## 뒤로 갈 수 없는 상황에서는 continue
                    continue
                if pos-b >=0 and (pos-b, False) not in done: ## 뒤로 갈 수 있을 때
                    done.add((pos-b, False)) ## 가본 적 있다고 저장
                    new_q.add((pos-b, False)) ## 미래에 위치할 수 있다고 저장
            q = new_q ## 새롭게 현재 위치할수 있는 곳 갱신
            ans += 1 ## 반복횟수 갱신
        return -1 ##모든 곳 다 돌아보았을 때 x로 갈 수 없는 상황 
