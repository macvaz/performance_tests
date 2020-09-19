import random
import timeit
from datetime import datetime

N = 20000000
L = [i for i in range(0, N)]

def run_random_access(times):
	start = datetime.now()
	for i in range(times):
		r=L[random.randint(0, N-1)]
	print(datetime.now() - start)

def run_predictable_access(times):
	start = datetime.now()
	for i in range(times):
		r=L[20]
	print(datetime.now() - start)
