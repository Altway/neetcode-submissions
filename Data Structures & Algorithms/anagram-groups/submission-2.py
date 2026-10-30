class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_key = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for letter in word:
                key[ord(letter) - ord('a')] += 1 
            word_key[tuple(key)].append(word)
        return list(word_key.values())