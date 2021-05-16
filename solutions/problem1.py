""" If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""

def mul_sum(a: int=3, b: int=5):
    max_num = 1000

    all_nums = [x for x in range(1, max_num) if (x % 3 == 0) | (x % 5 == 0)]
    return sum(all_nums)


if __name__ == "__main__":
    result = mul_sum()
    print(result)