class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0 # 무한루프에서 인덱스 
        while True:

            # index별로 숫자를 비교하는데 만약 리스트를 벗어난 index를 비교하려할 때 루프문을 빠져나감            
            if ((len(asteroids) - 1) == i):
                break
            
            #리스트가 비어있을 때에도 루프문을 빠져나감    
            if not asteroids:
                break

            #현재 index의 숫자가 양수일 경우
            if asteroids[i] > 0:

                # 양수의 경우 행성이 오른쪽으로 진행하기 때문에 i+1의 인덱스에 있는 숫자를 비교함
                # 만약 i+1의 숫자가 양수라면 인덱스 i를 1증가시키고 continue를 통해 루프를 다시 돔
                if asteroids[i+1] > 0:
                    i += 1
                    continue

                # i+1이 음수일 경우 
                else:

                    # i와 i+1의 숫자의 절대값의 차가 음수인지, 양수인지, 0인지에 따라 리스트에서 더 작은 숫자를 pop해준다.
                    # 이후 pop해준 리스트를 가지고 다시 비교해야하기 때문에 i=0으로 초기화 시켜주고 continue를 통해 루프문을 다시돈다.
                    if abs(asteroids[i]) - abs(asteroids[i+1]) > 0:
                        asteroids.pop(i+1)
                        i = 0
                        continue

                    if abs(asteroids[i]) - abs(asteroids[i+1]) < 0:
                        asteroids.pop(i)
                        i = 0
                        continue
                    
                    # 만약 두 수의 차가 0일경우 i+1먼저 pop해주고 i를 pop해줘야 우리가 목표한 두 수를 정확히 pop해줄 수 있다.
                    # 순서가 바뀌게 되면 인덱스가 변화되기 때문이다.
                    else: 
                        asteroids.pop(i+1)
                        asteroids.pop(i)
                        i = 0
                        continue

            # 만약 현재 인덱스의 숫자가 음수일 경우는 비교할 필요없이 인덱스 i의 숫자를 1증가시켜주고 continue를 통해 루프문으로 다시 돌아간다.
            if asteroids[i] < 0:
                i += 1
                continue

        # 모든 루프가 끝나고 break를 통해 루프문을 빠져나오면 asteroids 리스트를 반환해준다.
        return asteroids
