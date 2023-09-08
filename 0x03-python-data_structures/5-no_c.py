#!/usr/bin/python3
def no_c(my_string):
	if my_string == '':
		return
	result = ''
	for x in my_string:
		if x == 'c' or x == "C":
			x = ''
		result += x
	return result
