from collections import defaultdict
from typing import List, DefaultDict


def groupAnagrams(strs:List[str]) -> List[List[str]]:
    # create hashmap, where each key are values unique to group of anagrams
    hash_map = defaultdict(list)
    for s in strs:
        # all anagrams sorted look the same (eat, tea, ate) -> aet
        sorted_s = "".join(sorted(s))
        # append matching anagram
        hash_map[sorted_s].append(s)
        # convert hashmap to list of its values
    return [value for _, value in hash_map.items()]

def groupAnagramsV2(strs:List[str]) -> List[List[str]]:
    hash_map = defaultdict(list)
    for s in strs:
        s_hash = [0]*26
        for c in s:
            s_hash[ord(c.lower()) - ord('a')] += 1
        hash_map[tuple(s_hash)].append(s)
    return [value for _, value in hash_map.items()]
