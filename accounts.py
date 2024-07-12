# Jaswanth Kattubavi Sreenivasulu
# 201760526

import random
from datetime import datetime, timedelta

class BasicAccount:
    """
    A basic bank account class .
    Attribute :
        total_no_of_accounts (int): This is a Class variable to keep track of the total number of BasicAccount instances.
    """
    total_no_of_accounts: int = 0

    def __init__(self, account_name: str, opening_balance: float) -> None:
        """
        Initialize a basic account.
            account_name (str): The name of the account holder.
            opening_balance (float): The initial balance of the account.
        """
        # Increment the total number of accounts
        BasicAccount.total_no_of_accounts += 1

        # Assign account details
        self.name = account_name
        self.ac_num = BasicAccount.total_no_of_accounts
        self.balance = opening_balance
        self.card_num = ''
        self.card_exp = None, None
        # Issue a new card with an expiration date
        self.issue_new_card()

    def __str__(self) -> str:
        """
        It returns a string representation of the  basic account.
        """
        return f"account holder name : {self.name}, available balance: £{self.balance}, account number: {self.ac_num}"

    def deposit(self, amount: float) -> None:
        """
        Deposit the specified amount into the account.
        amount (float): The amount to be deposited.
        """
        # Ensure the deposited amount is positive
        if amount <= 0:
            print(f"Error: Amount should be a positive number, {amount=}")
            return
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraw the specified amount from the account.
        amount (float): The amount to be withdrawn.
        """
        # Check if the withdrawal amount is valid
        if (amount > self.balance) or (amount <= 0):
            print(f"Can not withdraw £{amount}")
        else:
            # Process the withdrawal and display the updated balance
            self.balance -= amount
            print(f"{self.name} has withdrawn £{amount}. New balance is £{self._get_updated_balance()}")

    def _get_updated_balance(self) -> float:
        """
        Get the updated account balance, ensuring it is not negative.
        This returns float: The updated account balance.
        """
        return max(0, self.balance)

    def get_available_balance(self) -> float:
        """
        Get the available balance in the account.
        This returns float: The available balance.
        """
        return self._get_updated_balance()

    def get_balance(self) -> float:
        """
        Get the current balance of the account.
        This returns float: The current balance.
        """
        return self._get_updated_balance()

    def print_balance(self) -> None:
        """Print the remaining balance of the account."""
        print(f"Remaining Balance: £{self._get_updated_balance()}")

    def get_name(self) -> str:
        """
        Get the name of the account holder.
        This returns str: The name of the account holder.
        """
        return self.name

    def get_ac_num(self) -> str:
        """
        Get the account number as a string.
        This returns str: The account number.
        """
        return str(self.ac_num)

    def issue_new_card(self) -> None:
        """
        Issues a new card for the account.
        """
        today_date = datetime.now()
        # It Generates a new random card number
        card_digits = [str(random.randint(0, 9)) for _ in range(16)]
        self.card_num = "".join(card_digits)

        # The expiry date is set as 3 years to the month from now
        exp_date = today_date + timedelta(days=365 * 3)
        self.card_exp = exp_date.month, exp_date.year % 100


    def close_account(self) -> bool:
        """
        Close the account if it is not overdrawn.
        Returns:
            bool: True if the account is closed, False otherwise.
        """
        if self.balance >= 0:
            self.withdraw(self.balance)
            return True
        print(f"Can not close account due to customer being overdrawn by £{abs(self.balance)}")




class PremiumAccount(BasicAccount):
    """
    A premium bank account class.
    Inherits from BasicAccount as it is a child class.
    """

    def __init__(
        self, account_name: str, opening_balance: float, overdraft_limit: float
    ) -> None:
        """
        Initialize a premium account.
            account_name (str): The name of the account holder.
            opening_balance (float): The initial balance of the account.
            overdraft_limit (float): The overdraft limit for the account.
        """
        # Initialize the premium account with additional overdraft details
        super().__init__(account_name=account_name, opening_balance=opening_balance)
        self.overdraft_limit = overdraft_limit
        self.overdraft = bool(self.overdraft_limit)

    def __str__(self) -> str:
        """
        Returns a string representation of the PremiumAccount.
        """
        return f"account holder name: {self.name}, available balance: £{self.balance}, account number: {self.ac_num}, Overdraft Limit: £{self.overdraft_limit if self.overdraft else 'Not Applicable'}"

    def withdraw(self, amount: float) -> None:
        """
        Withdraw the specified amount from the premium account.
           amount (float): The amount to be withdrawn.
        """
        # Calculate the remaining balance considering the overdraft
        remaining_bal = self.balance + self.overdraft_limit

        # Check if the withdrawal amount is valid
        if (amount > remaining_bal) or (amount <= 0):
            print(f"Can not withdraw £{amount}")
        else:
            # Process the withdrawal and display the updated balance
            self.balance -= amount
            print(f"{self.name} has withdrawn £{amount}. New balance is £{self._get_updated_balance()}")

    def set_overdraft_limit(self, new_limit: float) -> None:
        """
        Set a new overdraft limit for the premium account.
        new_limit (float): The new overdraft limit.
        """
        self.overdraft_limit = new_limit

    def get_available_balance(self) -> float:
        """
        Get the available balance in the premium account, considering overdraft.
        Returns:
            float: The available balance.
        """
        final_balance = super().get_available_balance()

        if self.overdraft and final_balance < 0:
            final_balance = self.overdraft_limit - abs(final_balance)
        return final_balance

    def print_balance(self) -> None:
        """Print the remaining balance and overdraft of the premium account."""
        super().print_balance()
        overdraft_balance = (
            self.overdraft_limit - abs(self.balance)
            if self.balance < 0
            else self.overdraft_limit
        )
        print(f"Remaining Overdraft: £{overdraft_balance}")

    def close_account(self) -> bool:
        """
        Close the premium account, considering overdraft if applicable.
        Returns:
            bool: True if the account is closed, False otherwise.
        """
        if self.overdraft and self.balance < 0:
            print(f"Can not close account due to customer being overdrawn by £{abs(self.balance)}")
            return False
        return super().close_account()