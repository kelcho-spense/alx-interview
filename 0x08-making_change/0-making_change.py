#!/usr/bin/python3
""" A function that determines the fewest number of coins
neededto meet a given amount total
"""


def makeChange(coins, total):
    """Determines the fewest number of coins
    Args:
        coins (list[int]) : list of different values of changes
        total (int): The given amount

    Return:
        change (int): the fewest number of coin
    """

    if total < 1:
        return 0

    change = -1

    if len(coins):
        coins = sorted(coins, reverse=True)
        noOfCoins = len(coins)
        change = 0

        for i in range(noOfCoins):
            while total:
                # if total >= 1:
                if total - coins[i] >= 0:
                    change += 1
                    total -= coins[i]
                else:
                    break

        if total != 0:
            change = -1

    return change
