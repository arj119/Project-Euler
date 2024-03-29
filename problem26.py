def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def f(N):
    if N < 8: return 3
    for d in prime_sieve(N)[::-1]:
        period = 1
        while pow(10, period) % d != 1: period += 1
        if d-1 == period: return d

answer = 'Y'

while answer != 'n' or answer != 'N':
      
    N = int(input('The longest recurring cycle for 1/d where d <'))
    if len(str(N)) <= 7:
        print("is d =", f(N))
        answer = str(input('Would you like to enter another number? Y/N: '))
    else:
        print('number was too long')
        N = int(input('The longest recurring cycle for 1/d where d <'))
