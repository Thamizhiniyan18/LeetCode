# Link to the Problem : https://leetcode.com/problems/maximum-ice-cream-bars/

def maxIceCream(costs, coins) -> int:
    count = 0
    for cost in sorted(costs):
        if int(cost) <= coins:
            count += 1
            coins -= int(cost)
    return count


def main():
    costs_string = input("Enter the costs separated by a space :\n")
    costs_list = (costs_string.split(' '))

    coins = int(input("Enter the initial amount of coins : "))

    print(maxIceCream(costs_list, coins))

if __name__ == "__main__":
    main()