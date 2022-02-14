class Solution:
    '''
    sliding window  방식
    comment 상관 없는 코드 제거
    '''
    def totalFruit(self, fruits: List[int]) -> int:
        
        # if len(fruits) < 3: 속도에 영향 x
        #     return len(fruits)

        max_val = 0

        low = 0

        high = 0


        bucket = set()


        for idx, fruit in enumerate(fruits):

            high = idx


            bucket.add(fruit)



            if len(bucket) == 3:


                max_val = max(max_val, high - low)            


                low = idx - 1

                while fruits[low-1] == fruits[low]:
                    low -= 1

                bucket = set()
                bucket.add(fruits[low])
                bucket.add(fruits[high])




            else:
                continue
        max_val = max(max_val, high - low+1)
        return max_val
