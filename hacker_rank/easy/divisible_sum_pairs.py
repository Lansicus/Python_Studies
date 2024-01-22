# TODO -
# You have an array of numbers and a target number (k). The goal is to count
# the pairs of numbers in the array such that when you add any two numbers
# from a pair,the result is divisible evenly by the target number (k).

# STDIN           Function
# -----           --------
# 6 3             n = 6, k = 3
# 1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]
def divisibleSumPairs(n, k, ar):
    count = 0
    remainder_count = {}

    for num in ar:
        remainder = num % k
        complement = (k - remainder) % k

        count += remainder_count.get(complement, 0)
        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

    return count
