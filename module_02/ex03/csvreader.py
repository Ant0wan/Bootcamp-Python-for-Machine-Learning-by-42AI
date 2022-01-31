"""
ex03
"""


class CsvReader():
    """CsvReader Class context manager"""

	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

	def __enter__(self):
        self.file = open(self.filename, 'rt')
        lines = self.file.read().split('\n')
        if self.header:
            self.header = lines.[0].split(self.sep)
            self.data = [line.split(self.sep) for line in lines[1 + self.skip_top:self.skip_bottom]]
            self.len = len(self.header)
        else:
            self.header = None
            self.data = [line.split(self.sep) for line in lines[self.skip_top:self.skip_bottom]]
            self.len = len(self.data[0])
        if list(filter(lambda x: len(x) != self.len, self.data)):
            raise AssertionError("Invalid csv file")
        return self.file

	def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file
            self.file.close()

	def getdata(self):
	    """ Retrieves the data/records from skip_top to skip bottom.
	    Return:
	    -------
	    	nested list (list(list, list, ...)) representing the data.
	    """
		return self.data

	def getheader(self):
	    """ Retrieves the header from csv file.
	    Return:
	    -------
	    	list: representing the data (when self.header is True).
            None: (when self.header is False).
	    """
        return self.header
