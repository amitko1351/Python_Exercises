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


def input_operation():
    """
    the function prints the menu and gets 
    operation that the user want to do
    :return: the number represent the operation 
             that the user want to do
    """
    while True:
        print("Enter the operation that you want to do:")
        print("1 for printing the balance")
        print("2 for taking money from the bank account")
        print("3 for changing the secret code of the bank account")
        print("4 for exit the system")
        choice = int(input())
        if 0 < choice < 5:
            return choice


def check_the_secret_code(bank_account):
    """
    the function gets the secret code from the user 
    and check if the code is correct
    :param bank_account: the bank account object

    """
    while True:
        secret_code = input("Enter your secret code \n")
        if bank_account.authenticate_account(secret_code):
            break


def take_money_from_account(bank_account):
    """
    the function gets from the user the amount
    of money that he would like to take from the 
    account (if he doesnt have enough money the function
     prints a message)
    :param bank_account: the user bank account object
    """
    print("How much money do you want to take?")
    print("50 or 20 or other")
    print("please enter the amount of the money")
    amount = int(input())
    if not bank_account.cash_withrawal(amount):
        print("the cash withrawal failed you dont have enough money")


def operate(operation, bank_account):
    """
    the function operate according to the user decisions
    :param operation: the number represent the operation 
                      that the user want to do
    :param bank_account: the user bank account object
    """
    if operation == 1:
        bank_account.print_balance()
    elif operation == 2:
        take_money_from_account(bank_account)
    elif operation == 3:
        secret_code = input("Enter you new code:")
        bank_account.set_secret_code(secret_code)
    else:
        exit(0)


def operate_bank_account(bank_account):
    """
    Operate on the bank account
    :param bank_account: the user bank account object
    """
    # Operate on the bank account
    while True:
        # Check the secret code
        check_the_secret_code(bank_account)
        # Print the menu and gets the number of
        # the operation
        operation = input_operation()
        # Operate According to the number entered
        operate(operation, bank_account)


def main():
    # Create a bank account object
    bank_account = BankAccount("1234", 150)
    operate_bank_account(bank_account)

if __name__ == '__main__':
    main()
