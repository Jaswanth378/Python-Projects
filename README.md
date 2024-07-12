# Cache Management Algorithms

This Python script implements two cache management algorithms: First-In-First-Out (FIFO) and Least Frequently Used (LFU).

## Author

- Name: Jaswanth Kattubavi Sreenivasulu
- File: cache.py

## Algorithms

### FIFO (First-In-First-Out)

The FIFO algorithm manages the cache by removing the oldest item when the cache is full. It follows the principle of "first in, first out."

### LFU (Least Frequently Used)

The LFU algorithm manages the cache by removing the least frequently used item when the cache is full. It keeps track of the frequency of each item in the cache and removes the item with the lowest frequency.

## Usage

1. Run the script using Python.
2. Enter a series of integers representing the requests, one per line. Press Enter without entering a value to finish the input.
3. Enter the preference for the cache management algorithm:
   - Enter "1" for FIFO algorithm.
   - Enter "2" for LFU algorithm.
   - Enter "Q" to quit the program.
4. The script will simulate the cache management algorithm based on the provided requests and cache size.
5. The final state of the cache will be displayed.


# Voting Rules and Preference Aggregation

This Python script implements various voting rules and preference aggregation methods.

## Author

- Name: Jaswanth Kattubavi Sreenivasulu
- File: voting.py

## Methods

### `generate_preferences`

This method generates a preference profile based on the given sheet. It takes a `Workbook` object as input and returns a dictionary representing agent preferences.

### `apply_tie_break`

This method applies tie-breaking rules to determine the winner among tied alternatives. It takes the list of winners, the preferences dictionary, and the tie-breaking rule as input. The tie-breaking rule can be either a string ("max" or "min") or an integer representing the agent ID for dictatorship.

### `dictatorship`

This method determines the winner according to the Dictatorship rule. It takes the preference profile and the agent ID as input and returns the winner.

### `plurality`

This method determines the winner according to the Plurality rule. It takes the preferences dictionary and the tie-breaking rule as input and returns the winner.

### `veto`

This method determines the winner according to the Veto rule. It takes the preferences dictionary and the tie-breaking rule as input and returns the winner.

### `borda`

This method determines the winner according to the Borda rule. It takes the preferences dictionary and the tie-breaking rule as input and returns the winner.

### `harmonic`

This method determines the winner according to the Harmonic rule. It takes the preferences dictionary and the tie-breaking rule as input and returns the winner.

### `calculate_harmonic_scores`

This method calculates the Harmonic scores for each alternative. It takes the preferences dictionary as input and returns a defaultdict containing the scores.

### `scoring_rule`

This method determines the winner using the Scoring Rule. It takes the preferences dictionary, the score vector, and the tie-breaking rule as input and returns the winner.

### `range_voting`

This method determines the winner using Range Voting. It takes a `Workbook` object and the tie-breaking rule as input and returns the winner.

### `STV`

This method determines the winner using Single Transferable Vote (STV). It takes the preferences dictionary and the tie-breaking rule as input and returns the winner.

# Bank Account Management System

This Python script provides a basic implementation of a bank account management system with two account types: Basic Account and Premium Account.

## Author

- Name: Jaswanth Kattubavi Sreenivasulu
- File: accounts.py

## Classes

### `BasicAccount`

The `BasicAccount` class represents a basic bank account with the following attributes and methods:

- Attributes:
  - `total_no_of_accounts` (int): Class variable to keep track of the total number of BasicAccount instances.
  - `name` (str): The name of the account holder.
  - `ac_num` (int): The account number.
  - `balance` (float): The current balance of the account.
  - `card_num` (str): The card number associated with the account.
  - `card_exp` (tuple): The expiration month and year of the card.

- Methods:
  - `__init__(self, account_name: str, opening_balance: float) -> None`: Initialize a basic account.
  - `__str__(self) -> str`: Return a string representation of the basic account.
  - `deposit(self, amount: float) -> None`: Deposit the specified amount into the account.
  - `withdraw(self, amount: float) -> None`: Withdraw the specified amount from the account.
  - `_get_updated_balance(self) -> float`: Get the updated account balance, ensuring it is not negative.
  - `get_available_balance(self) -> float`: Get the available balance in the account.
  - `get_balance(self) -> float`: Get the current balance of the account.
  - `print_balance(self) -> None`: Print the remaining balance of the account.
  - `get_name(self) -> str`: Get the name of the account holder.
  - `get_ac_num(self) -> str`: Get the account number as a string.
  - `issue_new_card(self) -> None`: Issue a new card for the account.
  - `close_account(self) -> bool`: Close the account if it is not overdrawn.

### `PremiumAccount`

The `PremiumAccount` class is a child class of `BasicAccount` and represents a premium bank account with additional features such as an overdraft limit. It inherits all the attributes and methods from the `BasicAccount` class and adds the following:

- Attributes:
  - `overdraft_limit` (float): The overdraft limit for the account.
  - `overdraft` (bool): Indicates whether the account has an overdraft facility.

- Methods:
  - `__init__(self, account_name: str, opening_balance: float, overdraft_limit: float) -> None`: Initialize a premium account.
  - `__str__(self) -> str`: Return a string representation of the premium account.
  - `withdraw(self, amount: float) -> None`: Withdraw the specified amount from the premium account, considering the overdraft limit.
  - `set_overdraft_limit(self, new_limit: float) -> None`: Set a new overdraft limit for the premium account.
  - `get_available_balance(self) -> float`: Get the available balance in the premium account, considering the overdraft limit.
  - `print_balance(self) -> None`: Print the remaining balance and overdraft of the premium account.
  - `close_account(self) -> bool`: Close the premium account, considering the overdraft if applicable.

