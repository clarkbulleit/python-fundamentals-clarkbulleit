def main():
	p = add_three(1,2,3)
	average_three(p)
	
def add_three(v1,v2,v3):
	""" add three numbers
	
	:param v1: number one
	:param v2: number two
	:param v3: number three
	"""
	p = v1+v2+v3
	
	return p

def average_three(w1):
	""" divide sum by three

	:param w1: sum of numbers one to three
	"""

	q = w1/3
	
	print(q)

if __name__ == "__main__":
	main()

