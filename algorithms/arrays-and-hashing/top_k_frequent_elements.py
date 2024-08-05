from collections import defaultdict
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    result = []
    hash_map = defaultdict(int)
    for num in nums:
        hash_map[num] += 1
    bucket = [[] for _ in range(len(nums) + 1)]
    # fill up bucket
    for key, value in hash_map.items():
        bucket[value].append(key)
    print(bucket)
    # loop through bucket backwards
    for i in range(len(bucket) - 1, -1 , -1):
        for item in bucket[i]:
            result.append(item)
            if len(result) == k:
                return result
    return []

print(topKFrequent([3,0,1,0], 1))
