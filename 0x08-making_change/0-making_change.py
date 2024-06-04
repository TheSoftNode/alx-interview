#!/usr/bin/python3
"""
Change comes from within
"""

def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.

    Return: fewest number of coins needed to meet total
        - If total is 0 or less, return 0
        - If total cannot be met by any number of coins you have, return -1

        - Coins is a list of the values of the coins in your possession
        - The value of a coin will always be an integer greater than 0
        - You can assume you have an infinite number of each denomination of
        coin in the list
    """
    if total <= 0:
        return 0

    # Initialize the memo array to a large value
    memo = [total + 1] * (total + 1)
    memo[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                memo[i] = min(memo[i], memo[i - coin] + 1)

    return memo[total] if memo[total] != total + 1 else -1

