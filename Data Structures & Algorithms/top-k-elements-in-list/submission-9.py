class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurence = []
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            if len(occurence) < counter[num]:
                occurence.append([num])
            else:
                occurence[counter[num]-1].append(num)
        resultat = set()

        while(len(resultat) < k):
            candidate = occurence.pop()
            resultat = resultat.union(candidate)

        return list(resultat)