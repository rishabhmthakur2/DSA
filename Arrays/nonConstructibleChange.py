"""
Question:

Given an array of positive integers representing the values of coins in your possession, 
write a function that returns the minimum amount of change (the minimum sum of money) 
that you cannot create. The given coins can have any positive integer value
and aren't necessarily unique (i.e., you can have multiple coins of the same value).

For example, if you're given coins = [1, 2, 5], the minimumamount of change that you 
can't create is 4. If you're given nocoins, the minimum amount of change that you can't create is 1
"""

"""
Sample I/O:

Input:
coins = [5, 7, 1, 1, 2, 3, 22]

Output:
20
"""

def nonConstructibleChange(coins):
    # Write your code here.
    numberOfCoins = len(coins)
    if numberOfCoins == 0:
        return 1
    currentSum = 0
    coins.sort()
    for i in range(0, numberOfCoins):
        currentCoin = coins[i]
        if currentCoin > currentSum + 1:
            return currentSum + 1
        currentSum += currentCoin
    return currentSum + 1

"""
TC: O(nlogn)| SC: O(1)

Explanation:
- First we need to sort the array into its ascending order.
- Now we store a running sum for all the elements within the array.
- For each element, if its greater than the current running sum + 1, that means we cannot create
a sum of current sum + 1
    - For example: If we have [1,2,5] as input - we can have 1,2,3 but not 4.
    - This is because 5 > running sum (1 + 2) + 1 and hence we don't have change to make 4.
- Else, just add the current element to the running sum
"""