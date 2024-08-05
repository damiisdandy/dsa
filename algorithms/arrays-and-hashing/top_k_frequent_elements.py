from collections import defaultdict
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    result = []
    hash_map = defaultdict(int)
    for num in nums:
        hash_map[num] += 1
    # we do not use [[]] * len(nums) + 1
    # because each list within the parent list is a point to the one list
    # we've end up updating all inner lists simultanously
    bucket = [[] for _ in range(len(nums) + 1)]
    # fill up bucket (we're index is occurance count and value is the element)
    for key, value in hash_map.items():
        bucket[value].append(key)
    # loop through bucket backwards (highest to lower based on index)
    for i in range(len(bucket) - 1, -1 , -1):
        # each list item is a smaller list since some elements can occur more than once
        for item in bucket[i]:
            result.append(item)
            # return `k` number of items
            if len(result) == k:
                return result
    return []
