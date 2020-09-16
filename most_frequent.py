def most_frequent():
	freqs = {}
	str = input("Enter a string: ")
	for ch in str.lower():
		if ch in freqs:
			freqs[ch] = freqs[ch] + 1
		else:
			freqs[ch] = 1
	sorted_f = sorted(freqs.items(), key = lambda x: x[1], reverse = True)
	
	for k,v in sorted_f:
		print(k +" : {}".format(v))

most_frequent()

