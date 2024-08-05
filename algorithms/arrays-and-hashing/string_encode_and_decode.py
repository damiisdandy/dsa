from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            # encode each word into the format: boat -> 4#boat
            result += f"{len(word)}#{word}"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        # place both pointers at the start of the string
        l = r = 0
        while r < len(s):
            # loop through each character
            r += 1
            if s[r] == '#':
                # get the number -> 4 <- #boat
                count = int(s[l:r])
                # get the word 4# ->boat<-
                word = s[r + 1:r + count + 1]
                result.append(word)
                # place left and right pointer to start of nect encode word e.g  -> 5#dance
                r += count + 1
                l = r
        return result
