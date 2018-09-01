import sys
import string
from numpy.random import choice
from time import time
import random
import numpy as np

input_file = sys.argv[1]

with open(input_file, 'r') as f:
    team_names = [line.strip() for line in f]
    
LOTTO_BALLS = {
    0: 250,
    1: 199,
    2: 156,
    3: 119,
    4: 88,
    5: 63,
    6: 45,
    7: 30,
    8: 20,
    9: 13,
    10: 10,
    11: 7,
}

order = []
while LOTTO_BALLS:
    N = float(np.sum(LOTTO_BALLS.values()))
    draw = choice(LOTTO_BALLS.keys(), 1, p=[LOTTO_BALLS[c] / N for c in LOTTO_BALLS])[0]
    order.append(team_names[draw])
    del LOTTO_BALLS[draw]

def print_gibberish(time_to_run, str_len=50):
    start = time()
    while True:
        sys.stdout.write('\r')
        if time()-start > time_to_run:
            sys.stdout.write(' '*str_len)
            return
        else:
            sys.stdout.write(''.join(random.choice(string.uppercase) for x in range(str_len)))

gibberish_time = 1
for i, result in enumerate(reversed(order)):
    print_gibberish(gibberish_time)
    sys.stdout.write('\r')
    sys.stdout.flush()
    print('#%d:\t%s' % (len(order)-i, result))
