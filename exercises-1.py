class BankAccount:
    def __init__(self, secret_code, initial_money):
        """
        the method initialize the BankAccount object
        :param secret_code: the secret code of the bank account
        :param initial_money: the initial money the bank account has
        """
        self.secret_code = secret_code
        self.account_money = initial_money

    def print_balance(self):
        """
        print the current balance of the bank account
        """
        print("the balance is {}".format(self.account_money))
