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

    def cash_withrawal(self, amount):
        """
        the function withrawal money from the account
        :param amount: the amount of money that is taken
                       from the account
        :return: True if the cash withrawal succeed 
                 False if it failed
        """
        # Check the bank account has enough money
        if amount > self.account_money:
            return False
        # Take the money from the account
        self.account_money -= amount
        return True

    def set_secret_code(self, secret_code):
        """
        the function change the secret code
        :param secret_code: the new secret code
        """
        self.secret_code = secret_code

    def authenticate_account(self, secret_code):
        """
        the function authenticate the account  
        :param secret_code: the secret code of the account
        :return: if the secret code is correct return true
                 else return false
        """
        return self.secret_code == secret_code

def main():
    # Create a bank account object
    bank_account = BankAccount(1234, 150)

if __name__ == '__main__':
    main()