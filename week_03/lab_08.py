#!/usr/bin/python3

def fib_opt(n, F):
	if  n <= 2: return 1
	else:
		if F[n-1] == 0:
			F[n-1] = fib_opt(n-1, F)
		if F[n-2] == 0:
			F[n-2] = fib_opt(n-2, F)
	return F[n-1] + F[n-2]

F1 = [0 for i in range(5)]
print(fib_opt(5, F1))
F2 = [0 for i in range(10)]
print(fib_opt(10, F2))
F3 = [0 for i in range(35)]
print(fib_opt(35, F3))
