def count(config, nums):
    
    # Base cases
    
    """
    If config is empty, then there cannot be any numbers in nums
    If there is numbers in nums, it is not a valid config
    """
    if config == "":
        return 1 if nums == () else 0

    """
    If nums is empty, then there cannot be any # signs in config
    as this would mean there needs to be more numbers
    If there are are ? signs and nums is empty, it means there is 
    exacly one config, which is all dots
    """
    if nums == ():
        return 0 if "#" in config else 1

    result = 0
    if config[0] in ".?":
        result += count(config[1:], nums)

    """
    We are doinf if's because if the statement is indeed a ? it will then go into
    the second if statement to check it as a #
    """
    if config[0] in "#?":
        if nums[0] <= len(config) and "." not in config[:nums[0]] and (nums[0] == len(config) or config[nums[0]] != "#"):
            # +1 is for the gap that must exist
            result += count(config[nums[0]+1:], nums[1:])
    
    return result


with open("day12\input12.txt") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    config, nums = line.split()
    nums = tuple(map(int, nums.split(',')))
    total += count(config, nums)
print(total)