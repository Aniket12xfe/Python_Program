from decimal import Decimal
from typing import Union
from datetime import datetime

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

class Account:
    """A class representing a bank account with basic banking operations.
    
    This class provides functionality for managing a bank account including
    deposits, withdrawals, and balance inquiries.
    """
    
    def __init__(self, initial_balance: Union[int, float, Decimal], account_no: str):
        """Initialize a new bank account.
        
        Args:
            initial_balance: Initial deposit amount
            account_no: Unique account number
        
        Raises:
            ValueError: If initial balance is negative or account number is invalid
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        if not account_no or not isinstance(account_no, str):
            raise ValueError("Invalid account number")
            
        self._balance = Decimal(str(initial_balance))
        self._account_no = account_no
        self._transactions = []
        
    @property
    def balance(self) -> Decimal:
        """Get current account balance."""
        return self._balance
        
    @property
    def account_no(self) -> str:
        """Get account number."""
        return self._account_no
        
    def debit(self, amount: Union[int, float, Decimal]) -> None:
        """Withdraw money from the account.
        
        Args:
            amount: Amount to withdraw
            
        Raises:
            ValueError: If amount is negative
            InsufficientFundsError: If withdrawal amount exceeds balance
        """
        if amount <= 0:
            raise ValueError("Debit amount must be positive")
            
        amount = Decimal(str(amount))
        if amount > self._balance:
            raise InsufficientFundsError(f"Insufficient funds. Available balance: ₹{self._balance:,.2f}")
            
        self._balance -= amount
        self._record_transaction("DEBIT", amount)
        print(f"₹{amount:,.2f} debited from account {self._account_no}")
        print(f"Current balance: ₹{self._balance:,.2f}")
        
    def credit(self, amount: Union[int, float, Decimal]) -> None:
        """Deposit money into the account.
        
        Args:
            amount: Amount to deposit
            
        Raises:
            ValueError: If amount is negative
        """
        if amount <= 0:
            raise ValueError("Credit amount must be positive")
            
        amount = Decimal(str(amount))
        self._balance += amount
        self._record_transaction("CREDIT", amount)
        print(f"₹{amount:,.2f} credited to account {self._account_no}")
        print(f"Current balance: ₹{self._balance:,.2f}")
        
    def get_statement(self) -> None:
        """Print account statement showing recent transactions."""
        print("\nAccount Statement")
        print("-" * 50)
        print(f"Account Number: {self._account_no}")
        print(f"Current Balance: ₹{self._balance:,.2f}")
        print("\nRecent Transactions:")
        print("Date                 Type    Amount")
        print("-" * 50)
        for date, type_, amount in self._transactions:
            print(f"{date}  {type_:<7} ₹{amount:>10,.2f}")
            
    def _record_transaction(self, type_: str, amount: Decimal) -> None:
        """Record a transaction in the account history.
        
        Args:
            type_: Transaction type (DEBIT/CREDIT)
            amount: Transaction amount
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._transactions.append((timestamp, type_, amount))

# Example usage
if __name__ == "__main__":
    try:
        # Create account with initial balance
        account = Account(12000, "UBI12344567")
        
        # Perform some transactions
        account.debit(1000)
        account.credit(21050)
        account.debit(1000)
        
        # Print account statement
        account.get_statement()
        
    except (ValueError, InsufficientFundsError) as e:
        print(f"Error: {e}")