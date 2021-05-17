class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        curr = []
        for asteroid in asteroids:
            # curr가 비어 있거나, 행성이 양수방향이면 curr에 행성 등록
            if not curr or asteroid > 0:
                curr.append(asteroid)
                
            # 아닌 경우, curr[-1] 양수인 경우와 음수인 경우로 분리, 양수인 경우를 기준으로 판단
            else:
                while curr and curr[-1] > 0:
                    # 같으면 두 행성 제거
                    if curr[-1] == -asteroid:
                        curr.pop()
                        break
                    # curr[-1]이 더 작으면 현재 행성 제거
                    elif curr[-1] < -asteroid:
                        curr.pop()
                        continue
                    # curr[-1]이 더 크면 asteroid curr에 추가하지 않도록 하여 제거되도록
                    elif curr[-1] > -asteroid:
                        break
                # while문 실행 안될 경우, 둘다 제거 안되므로 asteroid 등록
                else:
                    curr.append(asteroid)
        return curr
