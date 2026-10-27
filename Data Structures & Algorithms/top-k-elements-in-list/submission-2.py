class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq as hq
        #tmp = defaultdict(list)
        counter = Counter(nums)
        res = []
        h = []
        for key, value in counter.items():
            hq.heappush_max(h, (value, key))
        
        
        for i in range(k):
            res.append(hq.heappop_max(h)[1])
        return res