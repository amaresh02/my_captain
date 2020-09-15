# This is a program which takes a file name as input and returns its extention as output

exts = {'py': 'python', 'c': 'C', 'cpp': 'C++', 'js': 'Java Script', 'html': 'HTML', 'java': 'Java'}
file_name = input("Enter the file name: ")
if '.' in file_name:
	if file_name[file_name.find('.')+1:] in exts:
		print("The extention of the file is : '{}'".format(exts[file_name[file_name.find('.')+1:]]))

	else:
		print('Unknown file extention.')
	

else:
	print("Invalid file name!")
