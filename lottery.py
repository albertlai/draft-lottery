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
    6: 43,
    7: 28,
    8: 17,
    9: 11,
    10: 8,
    11: 7,
    12: 6,
    13: 5,
    14: 4,
    15: 3,
}

# Remove unnecessary lotto slots (we support up to 16)
for r in range(len(team_names),16):
    del LOTTO_BALLS[r]

# Run the drawing, removing selected teams
order = []
while LOTTO_BALLS:
    N = float(np.sum(LOTTO_BALLS.values()))
    draw = choice(LOTTO_BALLS.keys(), 1, p=[LOTTO_BALLS[c] / N for c in LOTTO_BALLS])[0]
    order.append(team_names[draw])
    del LOTTO_BALLS[draw]

# Print some gibberish to make it look like the program is thinking really hard
def print_gibberish(time_to_run, str_len=50):
    start = time()
    while True:
        sys.stdout.write('\r')
        if time()-start > time_to_run:
            sys.stdout.write(' '*str_len)
            return
        else:
            sys.stdout.write(''.join(random.choice(string.uppercase) for x in range(str_len)))

# Output the final draft results
gibberish_time = 1
for i, result in enumerate(reversed(order)):
    print_gibberish(gibberish_time)
    sys.stdout.write('\r')
    sys.stdout.flush()
    print('#%d:\t%s' % (len(order)-i, result))
    gibberish_time += 0.1
