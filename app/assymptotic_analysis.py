import time
from random import randrange
from prime_numbers import generate_prime
# Measure the running time of the function
for listsize in range(1000, 10001, 1000):
    alist = [ randrange(20000, 100001, 3) for x in range(listsize) ]

    start = time.time()
    print(generate_prime(alist))
    end = time.time()

    print("Size: %d ... Time: %10.7f" % (listsize, end-start))