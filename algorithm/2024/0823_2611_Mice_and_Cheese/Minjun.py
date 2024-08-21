class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # 돼지 쥐 2가 죄다 먹었을 떄 가정.
        pig_mouse2 = sum(reward2)
        # 쥐 1이 k개 만큼 뺐어먹을거임 
        yummy_mouse1 = [r1 - r2 for r1, r2 in zip(reward1, reward2)]
        # 똑똑해서 젤 이득 볼 수 있는 것들만 먹음.
        pig_mouse2 += sum(sorted(yummy_mouse1, reverse=True)[:k])
        return pig_mouse2
