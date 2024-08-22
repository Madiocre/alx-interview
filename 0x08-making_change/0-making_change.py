#!/usr/bin/python3
"""
Least Change Coins
"""


def makeChange(coins, total):
    """ Function to Calculate coins """
    coins.sort(reverse=True)
    tot_coins = 0
    # print(coins)
    for coin in coins:
        while total >= coin:
            tot_coins += 1
            total -= coin
    return tot_coins if total == 0 else - 1
