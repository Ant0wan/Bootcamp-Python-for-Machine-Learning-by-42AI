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
            define if a bank account is corrupted
            . an even number of attributes
            . an attribute starting with b
            . no attribute starting with zip or addr
            . no attribute name, id and value
         - and stores enough money to complete the transfer
            . invalid is amount < 0

        -> dir built-in function
    """

    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    @staticmethod
    def _corrupted(account):
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

    def transfer(self, origin, dest, amount):
        """
        @origin: int(id) or str(name) of the first account
        @dest: int(id) or str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        pass

    def fix_account(self, account):
        """
        fix the corrupted account
        @account: int(id) or str(name) of the account
        @return True if success, False if an error occured
        """
        pass
