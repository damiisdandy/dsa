from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # store previously seen elements
    # future element's difference should match past element
    prev_hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in prev_hashmap:
            return [prev_hashmap[diff], i]
        # store elements seen (should be the last thing to do, so we do not repeat values)
        prev_hashmap[num] = i
    return [-1, -1]
