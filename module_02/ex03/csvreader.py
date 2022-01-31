"""
ex03
"""


class CsvReader():
    """CsvReader Class"""

	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		... Your code ...

	def __enter__(...):
		... Your code ...

	def __exit__(...):
		... Your code ...

	def getdata(self):
	""" Retrieves the data/records from skip_top to skip bottom.
	Return:
	-------
		nested list (list(list, list, ...)) representing the data.
	"""
		... Your code ...

	def getheader(self):
	""" Retrieves the header from csv file.
	Return:
	-------
		list: representing the data (when self.header is True).
        None: (when self.header is False).
	"""
		... Your code ...
