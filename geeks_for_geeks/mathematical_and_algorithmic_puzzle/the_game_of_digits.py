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


def generate_smallest(factors):
    
    if len(factors) == 0:
        return 0
    
    if max(factors) > 9:
        return -1
    
    digit_map = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    
    for d in factors:
        digit_map[d] = digit_map[d] + 1
    
    while digit_map[3] >= 2:
        digit_map[9] = digit_map[9] + 1
        digit_map[3] = digit_map[3] - 2
    
    while digit_map[2] >= 1 and digit_map[4] >= 1:
        digit_map[8] = digit_map[8] + 1
        digit_map[4] = digit_map[4] - 1
        digit_map[2] = digit_map[2] - 1
        
    while digit_map[2] >= 3:
        digit_map[8] = digit_map[8] + 1
        digit_map[2] = digit_map[2] - 3
        
    while digit_map[2] >= 1 and digit_map[3] >= 1:
        digit_map[6] = digit_map[6] + 1
        digit_map[3] = digit_map[3] - 1
        digit_map[2] = digit_map[2] - 1
        
    while digit_map[2] >= 2:
        digit_map[4] = digit_map[4] + 1
        digit_map[2] = digit_map[2] - 2    
    
    digits = ['0']
    
    for key, val in digit_map.items():
        digits_to_add = [str(key)] * val
        digits.extend(digits_to_add)
        
    digits.sort()
    return int(''.join(digits))


if __name__ == '__main__':
    
    test_cases = int(input())
    
    for i in range(test_cases):
        n = int(input())
        factors = prime_factors(n)
        print(generate_smallest(factors))
