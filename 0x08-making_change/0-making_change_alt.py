#!/usr/bin/python3
"""
Least Change Coins
"""


def makeChange(coins, total):
    """ Generate changes needed to reach total

    Args:
        coins ([List]): [List of Coins available]
        total ([int]): [total amount needed]
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    tot_coins = 0
    # print(coins)
    for coin in coins:
        while total >= coin:
            tot_coins += 1
            total -= coin
    return tot_coins if total == 0 else - 1
