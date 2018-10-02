#!/usr/bin/python3
import sys
sys.path.append('../common/')
from common import lcm
out = lcm.lcm(list(range(1, 21)))
print('lcm of natural numbers 1 to 20 is ', out)
