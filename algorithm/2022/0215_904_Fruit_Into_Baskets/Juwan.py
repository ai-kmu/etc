class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) < 3:
            return len(fruits)

        max_val = 0

        low = 0

        high = 0

        bucket = set()
        temp = []
        for idx, fruit in enumerate(fruits):
            temp.append(fruit)

            # print("=============idx iteration : ", idx, "==============")
            # print("process : ", temp)
            high = idx
            bucket.add(fruit)
            # print("bucket : ", bucket)

            if len(bucket) == 3:
    #             print("======== In if =======")
                bucket.remove(fruits[low])
                # print("removed bucket : ", bucket)
                low = low+1
                # print("final high low : ", high, ", ", low)
                max_val = max(max_val, high - low+1)            
                # print("max_val : ", max_val)
    #             print("======== out if =======")
                continue
            else:

                # print("final high low : ", high, ", ", low)
                max_val = max(max_val, high+1 - low)
                # print("out if max_val : ", max_val)

        return max_val
