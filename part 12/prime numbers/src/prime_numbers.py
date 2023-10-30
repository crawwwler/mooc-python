# Write your solution here
def prime_numbers():
    n = 2
    while True:
        if n == 2 or n == 3 :
            yield n
            n += 1
        if check_num(n):
            yield n
            n += 1
        else :
            n += 1
            continue

def check_num(n: int):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


