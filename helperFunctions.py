#helper functions


def monthToNum(shortMonth):
	if(shortMonth == 'Jan' or shortMonth == 'January'):
		return '1'
	elif(shortMonth =='Feb' or shortMonth == 'February'):
		return '2'
	elif(shortMonth == 'Mar' or shortMonth == 'March'):
		return '3'
	elif(shortMonth == 'Apr' or shortMonth == 'April'):
		return '4'
	elif(shortMonth == 'May' or shortMonth == 'May'):
		return '5'
	elif(shortMonth == 'Jun' or shortMonth == 'June'):
		return '6'
	elif(shortMonth == 'Jul' or shortMonth == 'July'):
		return '7'
	elif(shortMonth == 'Aug' or shortMonth == 'August'):
		return '8'
	elif(shortMonth == 'Sep' or shortMonth == 'September'):
		return '9'
	elif(shortMonth == 'Oct' or shortMonth == 'October'):
		return '10'
	elif(shortMonth == 'Nov' or shortMonth == 'November'):
		return '11'
	elif(shortMonth == 'Dec' or shortMonth == 'December'):
		return '12'
	else:
		return shortMonth
