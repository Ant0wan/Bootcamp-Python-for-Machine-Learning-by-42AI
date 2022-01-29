"""
Bank Account
"""


class Account:
    """Account class"""

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank:
    """The Bank Class
        Checks Account:
         - the right object
         - not corrupted
         - and stores enough money to complete the transfer
            . invalid is amount < 0
        A member can only own one bank account.
    """

    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    @staticmethod
    def _isrightobject(self, account):
        """Check account passed as arg is an existing bank account (the right object)"""
        found_account = next(filter(lambda x: x.name == account.name, self.account))
        if found_account.ID_COUNT != account.ID_COUNT:
            return False
        return True

    @staticmethod
    def _iscorrupted(account):
        """Check whether an Account class object is corrupted
          Corrupted if:
            . an even number of attributes
            . an attribute starting with b
            . no attribute starting with zip or addr
            . no attribute name, id and value
        """
        if (
                not len(account.__dict__.keys()) % 2
                or len(list(filter(lambda attr: attr.startswith('b'), account.__dict__.keys())))
                or not len(list(filter(lambda attr: attr.startswith('zip'), account.__dict__.keys())))
                or not len(list(filter(lambda attr: attr.startswith('addr'), account.__dict__.keys())))
                or name in account.__dict__.keys()
                or id in account.__dict__.keys()
                or value in account.__dict__.keys()
            ):
            return True
        return False

    @staticmethod
    def _storesenough(account, amount):
        """Check an account stores enough money to complete the transfer
            . invalid is amount < 0
        """
        if 0 <= account.value < amount:
            return False
        return True

    @staticmethod
    def _getaccount(self, acc):
        """Get account etheir by name or by id"""
        if isinstance(acc, str):
            return next(filter(lambda x: x.name == acc, self.account))
        if isinstance(acc, int):
            return next(filter(lambda x: x.ID_COUNT == acc, self.account))
        raise ValueError("Not a valid account identifier")

    def transfer(self, origin, dest, amount):
        """
        @origin: int(id) or str(name) of the first account
        @dest: int(id) or str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        origin_acc = self._getaccount(self, origin)
        if not self._isrightobject(self, origin_acc):
            raise ValueError("Origin account is not valid")
        dest_acc = self._getaccount(self, dest)
        if not self._isrightobject(self, dest_acc):
            raise ValueError("Destination account is not valid")
        if self._iscorrupted(origin_acc):
            raise ValueError("Origin account is corrupted")
        if self._iscorrupted(dest_acc):
            raise ValueError("Destination account is corrupted")

        pass

    def fix_account(self, account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occured
        """
        pass
