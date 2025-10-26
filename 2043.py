from typing import List


class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.length = len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 - 1 < 0 or account1 - 1 >= self.length or account2 - 1 < 0 or account2 - 1 >= self.length:
            return False
        if self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account - 1 < 0 or account - 1 >= self.length:
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account - 1 < 0 or account - 1 >= self.length:
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True
