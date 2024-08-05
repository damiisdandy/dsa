from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    # set to store previously seen elements
    nums_set = set()
    for num in nums:
        # if we've come across this value return
        if num in nums_set:
            return True
        # else add it to the set
        nums_set.add(num)
    # if we've gone through the list and see nothing, return `False`
    return False
