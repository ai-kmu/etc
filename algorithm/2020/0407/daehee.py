import numpy as np

class KeyLock:                          # class 선언
    def __init__(self, k, l):           # Key,Lock을 ndarray형태로 저장
        self.key = np.array(k)
        self.lock = np.array(l)
        self.M, m = self.key.shape
        self.N, n = self.lock.shape
        pad = self.M-1
        npad = ((pad, pad),(pad, pad))
        self.lock = np.pad(self.lock, npad,'constant', constant_values=(0))
                                        # M-1만큼 패딩해줌

        
    def rotate(self):                   # Key 회전
        self.key = np.rot90(self.key)
        
    def is_unlocked(self):              # 매칭
        ones = np.ones((self.N,self.N)) # lock 사이즈만큼 1로 가득채워진 ndarray 선언(기준 선언)
        locks = self.lock.copy()
        
        end = self.M + self.N - 1

        for _ in range(4):              # 회전수 만큼
            for i in range(end):        # 컨볼루션처럼 돌면서 매칭함
                for j in range(end):
                    locks = self.lock.copy()
                    locks[i:i+self.M, j:j+self.M] += self.key        #lock의 복사본에 key값을 더함
                    summ = locks[self.M-1:end, self.M-1:end].copy()  #padding을 제외한 lock만큼만 떼옴
                    comp = np.array_equal(summ, ones)                #일치하는지 확인
                    if comp == True:
                        return True
            self.rotate()
        return False
        
def solution(key, lock):
    answer = False
    kl = KeyLock(key,lock)
    answer = kl.is_unlocked()
    
    return answer
