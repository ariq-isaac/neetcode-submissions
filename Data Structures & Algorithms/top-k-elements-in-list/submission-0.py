class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        sort_items = dict(sorted(count.items(), key = lambda item: item[1], reverse = True))
        return list(sort_items)[:k]