'''
#seperate integers and strings
def list_filter(the_list):
	int_list = []
	str_list = []
	other_int_list = []
	other_str_list = []
	other_items = []
	for item in the_list:
		if isinstance(item, int) or isinstance(item, float):
			int_list.append(item)
		elif isinstance(item, str):
			str_list.append(item)
		elif isinstance(item, list):
			other_items.append(item)
	for item in other_items:
		if isinstance(item, list):
			for subitem in item:
				if isinstance(subitem, int) or isinstance(subitem, float):
					other_int_list.append(subitem)
				elif isinstance(subitem, str):
					other_str_list.append(subitem)
				elif isinstance(item, list):
					other_items.append(item)

	return int_list, str_list, other_int_list, other_str_list
'''
def list_filter(the_list):
	'''seperate integers and strings'''
	int_list = []
	str_list = []
	other_list = []
	for item in the_list:
		if isinstance(item, int) or isinstance(item, float):
			int_list.append(item)
		elif isinstance(item, str):
			str_list.append(item)
		elif isinstance(item, list):
			other_list.append(item)
	return int_list, str_list, other_list

def totalof(the_list):
	total = 0
	for item in the_list:
		if isinstance(item, int) or isinstance(item, float):
			total += item
		elif isinstance(item, list):
			for subitem in item:
				if isinstance(subitem, int):
					total+=subitem
	return total

def average(the_list, integer=False, details=False):
	total, n = 0, 0
	other_items = []
	if isinstance(the_list, list):
		for item in the_list:
			if isinstance(item, int) or isinstance(item, float):
				total += item
				n += 1
			else:
				other_items.append(item)
	for item in other_items:
		if isinstance(item, list):
			for subitem in item:
				if isinstance(subitem, int):
					total+=subitem
					n+=1


	if details:
		return other_items , "Removed item/s"
	if integer:
		return int(total/(n*1.0))
	elif not integer:
		return total/(n*1.0)

list_a = ["arafat", "mohamed",["look","back",[23,55,'ar',"en"],23,44,"back"], 23,34.5,3465,1.4345,"aly"]