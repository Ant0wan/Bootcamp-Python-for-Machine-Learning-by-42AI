"""
Bank Account
"""


# pylint: disable=too-few-public-methods
class Account:
    """Account class"""

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        # pylint: disable=invalid-name
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    # pylint: disable=no-member
    def transfer(self, amount):
        """Add amount to object.value"""
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
        """Add a bank account"""
        self.account.append(account)

    @staticmethod
    def _isrightobject(bank, account):
        """Check account passed as arg is an existing
        bank account (the right object)
        """
        found_account = next(filter(
            lambda x: x.name == account.name, bank.account))
        if found_account.ID_COUNT != account.ID_COUNT:
            return False
        return True

    @staticmethod
    def _storesenough(account, amount):
        """Check an account stores enough money to complete the transfer
            . invalid is amount < 0
        """
        if 0 <= account.value < amount:
            return False
        return True

    @staticmethod
    def _getaccount(bank, acc):
        """Get account etheir by name or by id"""
        if isinstance(acc, str):
            return next(filter(lambda x: x.name == acc, bank.account))
        if isinstance(acc, int):
            return next(filter(lambda x: x.ID_COUNT == acc, bank.account))
        raise ValueError("Not a valid account identifier")

    def transfer(self, origin, dest, amount):
        """
        @origin: int(id) or str(name) of the first account
        @dest: int(id) or str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if not isinstance(amount, float):
            raise ValueError("Amount must be float")
        origin_acc = self._getaccount(self, origin)
        if not self._isrightobject(self, origin_acc):
            raise ValueError("Origin account is not valid")
        dest_acc = self._getaccount(self, dest)
        if not self._isrightobject(self, dest_acc):
            raise ValueError("Destination account is not valid")
        self.fix_account(origin_acc)
        self.fix_account(dest_acc)
        if self._storesenough(origin_acc, amount):
            origin_acc.transfer(amount * -1)
            dest_acc.transfer(amount)
            return True
        return False

    def fix_account(self, account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occured

        Check whether an Account class object is corrupted
          Corrupted if:
            . an even number of attributes
            . an attribute starting with b
            . no attribute starting with zip or addr
            . no attribute name, id and value
        """
        if not isinstance(account, Account):
            acc = self._getaccount(self, account)
        else:
            acc = account
        if len(list(filter(
                lambda attr: attr.startswith('b'),
                account.__dict__.keys()))) == 0:
            acc.__dict__['b'] = ''
        if not len(list(filter(
                lambda attr: attr.startswith('zip'),
                account.__dict__.keys()))) == 0:
            acc.__dict__['zip'] = ''
        if len(list(filter(
                lambda attr: attr.startswith('addr'),
                account.__dict__.keys()))) == 0:
            acc.__dict__['addr'] = ''
        if 'name' not in account.__dict__.keys():
            acc.__dict__['name'] = ''
        if 'id' not in account.__dict__.keys():
            acc.__dict__['id'] = Account.ID_COUNT
            Account.ID_COUNT += 1
        if 'value' not in account.__dict__.keys():
            acc.__dict__['value'] = 0
        if not len(account.__dict__.keys()) % 2:
            acc.__dict__[''] = ''
