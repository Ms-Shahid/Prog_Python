import psutil

def check_cpu_usage(percent):
	"""
		TO check the bug in the cpu_analysis file
	"""
	usage = psutil.cpu_percent()
	usage = psutil.cpu_percent(1)
	print("DEBUG: usage: {}".format(usage))
	return usage < percent

"""
if not check_cpu_usage(75):
	print('Not Fine!!')
"""