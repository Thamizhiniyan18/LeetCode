# Link to the Problem : https://leetcode.com/problems/valid-parentheses/

import time

def isValid(s: str) -> bool:
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')

    return True if len(s) == 0 else False

    # Another Method

    # for _ in range(len(s)):
    #     if len(s) > 0:
    #         s = s.replace('()', '').replace('[]', '').replace('{}', '')
    # return True if len(s) == 0 else False

def main():
    start = time.perf_counter()

    print(isValid("()"))

    end = time.perf_counter()
    print(f"Total time taken : {end - start}")

if __name__ == "__main__":
    main()