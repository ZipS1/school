def amount(n): 
	""" n - amount of Fibonacci numbers
	"""
	flist = []
	if n < 3:
		raise FibError("Parameter cannot be less than 3")
	n -= 2
	a = 1
	b = 1
	flist.extend((a, b))
	for i in range(n):
		a, b = b, a + b
		flist.append(b)
	return flist

def upto(n): 
	""" n - border number
	"""
	flist = []
	if n < 3:
		raise FibError("Parameter cannot be less than 3")
	n -= 2
	a = 1
	b = 1
	flist.extend((a, b))
	for i in range(n):
		a, b = b, a + b
		if b > n:
			break
		flist.append(b)
	return flist

if __name__ == '__main__':
	print("\nFirst 10 Fibonacci numbers:")
	fib = amount(100)
	print(*fib)

	print("-"*100)

	print("Fibonacci numbers up to 10:")
	fib = upto(1000)
	print(*fib)
