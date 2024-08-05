from collections import defaultdict
from typing import List, DefaultDict


# O(n * mlon(m))
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

# O(n * m) BEST
def groupAnagramsV2(strs:List[str]) -> List[List[str]]:
    hash_map = defaultdict(list)
    for s in strs:
        # create unique hash based on number of occurance of each letter indexed by
        # its unicode value
        s_hash = [0]*26
        for c in s:
            # ord('a') -> 97, ord('b') -> 98 : ord('b') - ord('a') = 1
            s_hash[ord(c) - ord('a')] += 1
        # convert list to tuple inorder to use it as a dictionary key
        hash_map[tuple(s_hash)].append(s)
    return [value for _, value in hash_map.items()]
