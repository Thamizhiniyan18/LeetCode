# Link to the Problem : https://leetcode.com/problems/palindrome-number/

import time

def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

def main():
    start = time.perf_counter()

    print(isPalindrome(121))

    end = time.perf_counter()
    print(f"Total time taken : {end - start}")

if __name__ == "__main__":
    main()