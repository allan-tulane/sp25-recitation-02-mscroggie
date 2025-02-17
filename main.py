"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
	#base case
	if n <= 1:
		return 1
	#recursive step
	else:
		return a * simple_work_calc(n//b,a,b) + n




def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	#base case
	if n <= 1:
		return 1
	else:
		return a * work_calc(n//b,a,b,f) + f(n)



def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	if n <= 1:
		return 1
	else:
		return f(n) + a * span_calc(n//b, a, b, f)+f(n)






def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))



def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			span_fn1,
			span_fn2
			))
	return result
	

def curried_work_calc(n):
    def step_a(a):
        def step_b(b):
            def step_f(f):
                def work_calc_inner(n):
                    if n <= 1.0:
                        return 1.0
                    else:
                        return a * work_calc_inner(n // b) + f(n)
                return work_calc_inner
            return step_f
        return step_b
    return step_a
def curried_simple_work_calc(n):
    def step_a(a):
        def step_b(b):
            def step_f(f):
                def work_calc_inner(n):
                    if n <= 1.0:
                        return 1.0
                    else:
                        return a * work_calc_inner(n // b) + n
                return work_calc_inner
            return step_f
        return step_b
    return step_a