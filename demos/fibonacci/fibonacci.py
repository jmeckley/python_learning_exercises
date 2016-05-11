def fibonacci(limit):
	#F_n = F_{n-1} + F_{n-2},

	if limit < 1:
		return 0

	if limit == 1:
		return 1

	while limit > 0:
		return fibonacci(limit - 1) + fibonacci(limit - 2)

def fibonacci_sequence(limit):
	result = []

	while(limit >= 0):
		result.append(fibonacci(limit))
		limit = limit - 1

	result.reverse()

	return result