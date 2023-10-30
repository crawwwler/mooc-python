import random
def lottery_numbers(amount: int, lower: int, upper: int):
    x = list(range(lower,upper+1))
    xx = random.sample(x, amount)
    return sorted(xx)