# Link to the Problem : https://leetcode.com/problems/longest-common-prefix/

import time
from itertools import takewhile


def longestCommonPrefix(strs: list[str]) -> str:
    res = ''.join(c[0] for c in takewhile(lambda x: all(x[0] == y for y in x), zip(*strs)))

    return res

def main():
    start = time.perf_counter()

    print(longestCommonPrefix(["dog","racecar","car"]))

    end = time.perf_counter()
    print(f"Total time taken : {end - start}")

if __name__ == "__main__":
    main()