from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += f"{len(word)}#{word}"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        l = r = 0
        while r < len(s):
            r += 1
            if s[r] == '#':
                count = int(s[l:r])
                word = s[r + 1:r + count + 1]
                result.append(word)
                r += count + 1
                l = r
        return result
