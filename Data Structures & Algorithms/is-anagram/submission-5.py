import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letter_dict = {letter: 0 for letter in string.ascii_lowercase}
        for s_letter, t_letter in zip(s,t):
            letter_dict[s_letter] +=1
            letter_dict[t_letter] -=1
        return not any(letter_dict.values())
