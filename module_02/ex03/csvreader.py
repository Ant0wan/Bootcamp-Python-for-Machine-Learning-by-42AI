"""
ex03
"""


class CsvReader:
    """CsvReader Class context manager"""

    # pylint: disable=too-many-instance-attributes,too-many-arguments
    def __init__(
            self, filename=None, sep=',', header=False,
            skip_top=0, skip_bottom=0
    ):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.top = skip_top
        self.bottom = skip_bottom
        self.file = None
        self.data = None

    def __enter__(self):
        self.file = open(self.filename, 'rt')
        lines = self.file.read().split('\n')
        if self.header:
            self.header = lines[0].split(self.sep)
            if self.bottom > 0:
                self.data = [line.split(
                    self.sep) for line in lines[1 + self.top:-self.bottom - 1]]
            else:
                self.data = [line.split(self.sep)
                             for line in lines[1 + self.top:-1]]
            len_ = len(self.header)
        else:
            self.header = None
            if self.bottom > 0:
                self.data = [line.split(self.sep)
                             for line in lines[self.top:-self.bottom - 1]]
            else:
                self.data = [line.split(self.sep)
                             for line in lines[self.top:-1]]
            len_ = len(self.data[0])
        for line in self.data:
            if len(line) != len_ or any(not field for field in line):
                return None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
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
