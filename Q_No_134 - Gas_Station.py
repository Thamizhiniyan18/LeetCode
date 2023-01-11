# Link to the Problem : https://leetcode.com/problems/gas-station/

import time

def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    # Another method - Not optimized
    #
    # if sum(gas) >= sum(cost):
    #     difference = []
    #     for i in range(len(gas)):
    #         difference.append(gas[i] - cost[i])
    #
    #     for index, each in enumerate(difference):
    #         i = index
    #         total = 0
    #         if each >= 0:
    #             starting_station = index
    #             for _ in range(len(gas)):
    #                 if total >= 0:
    #                     total += difference[i]
    #                     i = 0 if i >= len(gas) - 1 else i + 1
    #                 else:
    #                     break
    #             if starting_station == i:
    #                 return starting_station
    #
    # else:
    #     return -1

    if sum(gas) < sum(cost):
        return -1


    starting_station = 0
    total = 0
    for i in range(len(gas)):
        total += (gas[i] - cost[i])

        if total < 0:
            total = 0
            starting_station = i + 1

    return starting_station


def main():
    start = time.perf_counter()

    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

    print(canCompleteCircuit(gas, cost))

    end = time.perf_counter()
    print(f"Total time taken : {end - start}")

if __name__ == "__main__":
    main()