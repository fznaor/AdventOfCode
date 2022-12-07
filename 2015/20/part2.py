def get_divisors(n):
    if n <= 0:
        return []
    divisors = [1, n]
    for div in range(1, int(n ** 0.5 + 1)):
        if n % div == 0:
            divisors.extend([n // div, div])
    return list(set(divisors))

i = 1
while True:
    divisors = get_divisors(i)
    if sum([x for x in divisors if i/x <= 50])*11 > 29000000:
        print(i)
        break
    i += 1