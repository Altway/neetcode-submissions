class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "0"
        len_str = []
        for el in strs:
            len_str.append(f"{len(el)}#{el}")
        return "".join(len_str)

    def decode(self, s: str) -> List[str]:
        if s == "0":
            return []
        i = 0
        word_len = []
        result = []
        while(i!=len(s)):
            #print(f"word_len: {word_len}")
            if s[i] == '#':
                word_len = int(''.join(word_len))
                #print(word_len)
                result.append(s[i+1:i+1+word_len])
                i = i+1+word_len
                word_len = []
            else:
                word_len.append(f"{s[i]}")
                i+=1

        return result