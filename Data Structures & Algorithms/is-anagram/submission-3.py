import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_dict = {}
        for letter in string.ascii_lowercase:
            letter_dict[letter] = 0
        for letter in s:
            letter_dict[letter] +=1
        for letter in t:
            letter_dict[letter] -=1
        if any(letter_dict.values()):
            return False

        return True