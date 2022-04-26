# Google challenge lvl 1 re-id 
# Submission: SUCCESSFUL. Completed in: 2 days, 7 hrs, 1 min, 11 secs.
def get_long_prime_string(i):
    # starting with empty string and first natural number > 1
    p = ""
    n = 2
    while len(p) < (i+5):
        # divisor is natural number > 1
        d = 2
        while d <= n:
            r = n % d
            if r == 0 and d < n:
                break
            if d == n:
                p += str(n)
                break
            d += 1
        n += 1
    return p
    
def solution(i):
    # check input i >= 0
    if i < 0:
        detail = "Input {} is not a positive integer.".format(i)
        raise IndexError(detail)
    # get Lambda's string of prime numbers p
    p = get_long_prime_string(i)
    return p[i:i+5]