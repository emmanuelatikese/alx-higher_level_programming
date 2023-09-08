#!/usr/bin/python3
def print_list_integer(my_list=[]):
	if my_list is None:
		return
	else:
		for x in my_list:
			if (x, isinstance(x, int)):
				print("{}".format(x))
	return
