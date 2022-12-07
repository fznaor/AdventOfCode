def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

counter = 1
while True:
    pf = prime_factors(counter)
    product = 1
    inarow = 0
    for i,f in enumerate(pf):
        inarow += 1
        if i < len(pf) - 1:
            if pf[i+1] == pf[i]:
                continue
            else:
                product *= (f**(inarow+1)-1)//(f-1)
                inarow = 0  
        else:
            product *= (f**(inarow+1)-1)//(f-1)
            inarow = 0   
    if product*10 > 29000000:
        print(counter)
        break
    counter += 1