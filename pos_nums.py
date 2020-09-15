# Program which takes a list of integers as input and returns all the positive integers

lst = []
n = int(input("Enter the number of elements : "))

print("Enter the elements:")
for i in range(n):
	elem = int(input())
	lst.append(elem)

pos_lst = []

for num in lst:
	if num > 0:
		pos_lst.append(num)

print(pos_lst)