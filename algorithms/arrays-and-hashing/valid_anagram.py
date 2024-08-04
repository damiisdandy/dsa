from collections import defaultdict


def isAnagram(s: str, t: str) -> bool:
    # edgecase for values of unequal length (e.g ana & anagram)
    if len(s) != len(t):
        return False
    # build hashmap for comparism
    s_hashmap = defaultdict(int)
    for c in s:
        s_hashmap[c] += 1
    # ensure all values exists
    for c in t:
        c_exists = s_hashmap.get(c)
        # check for falsy value (e.g 0 or None)
        if not c_exists:
            return False
        # decrement the occurance of seen character
        s_hashmap[c] -= 1
    return True
