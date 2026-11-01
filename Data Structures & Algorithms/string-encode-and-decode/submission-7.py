class Solution:

    def encode(self, strs: List[str]) -> str:
        len_str = []
        for el in strs:
            len_str.append(f"{len(el)}#{el}")
        return "".join(len_str)

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while(i!=len(s)):
            idx_next_delimiter = s.find("#", i)
            word_len = int(s[i:idx_next_delimiter])
            result.append(s[idx_next_delimiter+1:idx_next_delimiter+word_len+1])
            i = idx_next_delimiter+word_len+1

        return result