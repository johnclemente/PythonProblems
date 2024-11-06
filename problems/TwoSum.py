# input
nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in hash_map:
            print([hash_map[compliment], i])
            return [hash_map[compliment], i]
        hash_map[num] = i
    print([])
    return []

twoSum(nums, target)
    