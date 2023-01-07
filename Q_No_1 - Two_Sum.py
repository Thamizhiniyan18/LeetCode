# Link to the Problem :  https://leetcode.com/problems/two-sum/

import time

def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        remaining = target - nums[i]
        if remaining in hashmap:
            return [hashmap[remaining], i]

        hashmap[num] = i


def main():
    start = time.perf_counter()
    numbers_string = input("Enter the numbers separated by a space :\n")
    numbers_list = (numbers_string.split(' '))

    target = int(input("Enter the target : "))

    print(twoSum(numbers_list, target))

    end = time.perf_counter()
    print(f"Total time taken : {end - start}")

if __name__ == "__main__":
    main()