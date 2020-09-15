n  = input("Enter the number of terms of Fibonacci series to be displayed: ")
n = int(n)

def fib(num):
	lst = []
	lst.append(0)
	lst.append(1)
	for i in range(num-2):
		lst.append(lst[i]+lst[i+1])
	return lst

print(fib(n))
	
