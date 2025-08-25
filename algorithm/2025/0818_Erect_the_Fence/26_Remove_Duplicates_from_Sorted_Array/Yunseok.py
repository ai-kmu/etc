class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = Counter()
        for elem in nums:
            counter[elem] += 1

        # print(counter.items())
        total_sum = 0
        items = []
        removing_idx = []
        for dict_item in counter.items():
            # print(dict_item[0], dict_item[1] - 1)
            items.append(dict_item[0])
            cnt_left = dict_item[1] - 1
            # print(f"cnt_left: {cnt_left}")
            # total_sum += 
            removing_idx.append(cnt_left if cnt_left > 0 else 0)
            # print(dict_item[0], total_sum)

        print(removing_idx)
        # nums.remove(1)
        for idx, item in enumerate(items):
            # print(idx, item, removing_idx[idx])
            for i in range(removing_idx[idx]):
                nums.remove(item)
            # nums.remove(removing_idx)

        return len(items)
